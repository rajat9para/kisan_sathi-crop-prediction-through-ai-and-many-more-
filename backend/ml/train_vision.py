"""
Kisaan_Sathi Computer Vision Model Training Pipeline — REAL TRAINING, NO SHORTCUTS
==================================================================================
Fine-tunes a PyTorch MobileNetV2 leaf disease classifier on genuine PlantVillage
(spmohanty, CC-BY) imagery, restricted to disease classes with VERIFIED public
training data:

    apple_scab, grape_black_rot, potato_early_blight, potato_late_blight,
    tomato_early_blight, tomato_late_blight, healthy_leaf

Crops without public verified leaf-pathology imagery (wheat, rice, cotton, chilli,
mustard, sugarcane, chickpea) are NOT claimed as CV-diagnosable. Those are served
by the ICAR/TNAU symptom-based knowledge base at runtime with an honest
"inference_source" label (see app/services/disease_classifier.py).

Usage:
    python backend/ml/train_vision.py --epochs 8 --batch 64 --img-size 160
"""

import os
import sys
import json
import random
import argparse
from collections import Counter, defaultdict

import torch
import torch.nn as nn
import torchvision.models as models
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PV_ROOT_DEFAULT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "ml_training",
    "PlantVillage-Dataset", "plantvillage dataset", "color"
)

# PlantVillage folder -> our canonical disease class key
PV_CLASS_MAP = {
    "Apple___Apple_scab": "apple_scab",
    "Apple___healthy": "healthy_leaf",
    "Grape___Black_rot": "grape_black_rot",
    "Grape___healthy": "healthy_leaf",
    "Potato___Early_blight": "potato_early_blight",
    "Potato___Late_blight": "potato_late_blight",
    "Tomato___Early_blight": "tomato_early_blight",
    "Tomato___Late_blight": "tomato_late_blight",
}

# Canonical output class order (stable for the runtime class_mapping json)
OUTPUT_CLASSES = [
    "apple_scab",
    "grape_black_rot",
    "healthy_leaf",
    "potato_early_blight",
    "potato_late_blight",
    "tomato_early_blight",
    "tomato_late_blight",
]

IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]

def set_seed(seed: int):
    random.seed(seed)
    torch.manual_seed(seed)


def collect_samples(pv_root: str, per_class_cap: int):
    """Walks PlantVillage folders, maps to canonical classes, caps per class."""
    samples = []  # (path, class_idx)
    class_to_idx = {c: i for i, c in enumerate(OUTPUT_CLASSES)}
    per_class = defaultdict(list)

    for pv_folder, class_key in PV_CLASS_MAP.items():
        folder = os.path.join(pv_root, pv_folder)
        if not os.path.isdir(folder):
            print(f"[!] WARNING: missing folder {pv_folder} — skipping (dataset incomplete).")
            continue
        files = [os.path.join(folder, f) for f in os.listdir(folder)
                 if f.lower().endswith((".jpg", ".jpeg", ".png"))]
        random.shuffle(files)
        per_class[class_key].extend(files)

    for class_key, files in per_class.items():
        random.shuffle(files)
        capped = files[:per_class_cap]
        idx = class_to_idx[class_key]
        samples.extend([(p, idx) for p in capped])
        print(f"    {class_key:<22} {len(capped):>5} images (from {len(files)} available)")

    return samples, class_to_idx


class LeafDataset(Dataset):
    def __init__(self, samples, transform):
        self.samples = samples
        self.transform = transform

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, i):
        path, label = self.samples[i]
        img = Image.open(path).convert("RGB")
        return self.transform(img), label


def stratified_split(samples, val_ratio=0.15, seed=42):
    """Per-class stratified split."""
    by_class = defaultdict(list)
    for s in samples:
        by_class[s[1]].append(s)
    train, val = [], []
    rng = random.Random(seed)
    for _, items in by_class.items():
        rng.shuffle(items)
        n_val = max(1, int(len(items) * val_ratio))
        val.extend(items[:n_val])
        train.extend(items[n_val:])
    return train, val


def evaluate(model, loader, device, class_names):
    model.eval()
    all_preds, all_labels = [], []
    with torch.no_grad():
        for imgs, labels in loader:
            imgs, labels = imgs.to(device), labels.to(device)
            preds = model(imgs).argmax(dim=1)
            all_preds.extend(preds.cpu().tolist())
            all_labels.extend(labels.cpu().tolist())

    n = len(class_names)
    cm = [[0] * n for _ in range(n)]
    for t, p in zip(all_labels, all_preds):
        cm[t][p] += 1

    per_class = {}
    f1s = []
    for i, name in enumerate(class_names):
        tp = cm[i][i]
        fp = sum(cm[r][i] for r in range(n)) - tp
        fn = sum(cm[i][c] for c in range(n)) - tp
        precision = tp / (tp + fp) if (tp + fp) else 0.0
        recall = tp / (tp + fn) if (tp + fn) else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
        f1s.append(f1)
        support = sum(cm[i])
        per_class[name] = {
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1_score": round(f1, 4),
            "support": support,
        }

    accuracy = sum(cm[i][i] for i in range(n)) / max(1, len(all_labels))
    macro_f1 = sum(f1s) / n
    weighted_f1 = sum(
        per_class[name]["f1_score"] * per_class[name]["support"]
        for name in class_names
    ) / max(1, len(all_labels))

    return accuracy, macro_f1, weighted_f1, per_class, cm

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, default=8)
    parser.add_argument("--batch", type=int, default=64)
    parser.add_argument("--img-size", type=int, default=160)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--per-class-cap", type=int, default=600)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--data-root", type=str, default=PV_ROOT_DEFAULT)
    args = parser.parse_args()

    set_seed(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[*] Device: {device} (CPU training uses frozen-backbone feature extraction)")

    # 1. Collect data
    print(f"[*] Loading PlantVillage samples from: {os.path.abspath(args.data_root)}")
    samples, class_to_idx = collect_samples(args.data_root, args.per_class_cap)
    if len(samples) < 500:
        print("[!] FATAL: too few samples found. Run the dataset download first "
              "(ml_training/download.ps1).")
        sys.exit(1)
    dist = Counter(OUTPUT_CLASSES[s[1]] for s in samples)
    print(f"[*] Total usable images: {len(samples)} across {len(dist)} classes")

    # 2. Split
    train_samples, val_samples = stratified_split(samples, seed=args.seed)
    print(f"[*] Train: {len(train_samples)} | Val: {len(val_samples)}")

    # 3. Transforms (train resolution == runtime inference resolution)
    size = args.img_size
    train_tf = transforms.Compose([
        transforms.RandomResizedCrop(size, scale=(0.65, 1.0)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(15),
        transforms.ColorJitter(brightness=0.25, contrast=0.25, saturation=0.2),
        transforms.ToTensor(),
        transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD),
    ])
    val_tf = transforms.Compose([
        transforms.Resize((size, size)),
        transforms.ToTensor(),
        transforms.Normalize(IMAGENET_MEAN, IMAGENET_STD),
    ])

    train_ds = LeafDataset(train_samples, train_tf)
    val_ds = LeafDataset(val_samples, val_tf)
    train_loader = DataLoader(train_ds, batch_size=args.batch, shuffle=True,
                              num_workers=0, pin_memory=False)
    val_loader = DataLoader(val_ds, batch_size=args.batch, shuffle=False, num_workers=0)

    # 4. Model: frozen ImageNet backbone + fresh trainable head
    #    (head architecture MUST mirror app/services/disease_classifier.py)
    print("[*] Building MobileNetV2 (ImageNet backbone, frozen) + trainable head...")
    backbone = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
    num_classes = len(OUTPUT_CLASSES)
    in_features = backbone.classifier[1].in_features
    backbone.classifier = nn.Sequential(
        nn.Dropout(p=0.2),
        nn.Linear(in_features, 256),
        nn.ReLU(),
        nn.Dropout(p=0.15),
        nn.Linear(256, num_classes)
    )
    for p in backbone.features.parameters():
        p.requires_grad = False  # freeze backbone -> honest, fast CPU training

    model = backbone.to(device)
    trainable = [p for p in model.parameters() if p.requires_grad]
    print(f"[*] Trainable parameters: {sum(p.numel() for p in trainable):,}")

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.AdamW(trainable, lr=args.lr, weight_decay=1e-4)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=args.epochs)

    # 5. Training loop
    history = []
    best_val_acc, best_state = 0.0, None
    artifacts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "artifacts")
    os.makedirs(artifacts_dir, exist_ok=True)

    for epoch in range(1, args.epochs + 1):
        model.train()
        running_loss, correct, seen = 0.0, 0, 0
        for imgs, labels in train_loader:
            imgs, labels = imgs.to(device), labels.to(device)
            optimizer.zero_grad()
            out = model(imgs)
            loss = criterion(out, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item() * labels.size(0)
            correct += (out.argmax(1) == labels).sum().item()
            seen += labels.size(0)
        scheduler.step()

        val_acc, macro_f1, weighted_f1, _, _ = evaluate(model, val_loader, device, OUTPUT_CLASSES)
        train_acc = correct / max(1, seen)
        epoch_rec = {
            "epoch": epoch,
            "train_loss": round(running_loss / max(1, seen), 4),
            "train_accuracy": round(train_acc, 4),
            "val_accuracy": round(val_acc, 4),
            "val_macro_f1": round(macro_f1, 4),
            "val_weighted_f1": round(weighted_f1, 4),
            "lr": round(scheduler.get_last_lr()[0], 6),
        }
        history.append(epoch_rec)
        print(f"[Epoch {epoch:>2}/{args.epochs}] loss={epoch_rec['train_loss']:.4f} "
              f"train_acc={epoch_rec['train_accuracy']:.4f} val_acc={epoch_rec['val_accuracy']:.4f} "
              f"macro_f1={epoch_rec['val_macro_f1']:.4f}")

        if val_acc > best_val_acc:
            best_val_acc = val_acc
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}

    # 6. Final evaluation with best weights
    model.load_state_dict(best_state)
    val_acc, macro_f1, weighted_f1, per_class, cm = evaluate(
        model, val_loader, device, OUTPUT_CLASSES)

    print("=" * 70)
    print(f"FINAL (best checkpoint): val_accuracy={val_acc:.4f} "
          f"macro_f1={macro_f1:.4f} weighted_f1={weighted_f1:.4f}")
    for name, m in per_class.items():
        print(f"    {name:<22} P={m['precision']:.3f} R={m['recall']:.3f} "
              f"F1={m['f1_score']:.3f} (n={m['support']})")

    # 7. Export artifacts
    pth_path = os.path.join(artifacts_dir, "leaf_mobilenet_v2.pth")
    torch.save(best_state, pth_path)

    with open(os.path.join(artifacts_dir, "disease_classes.json"), "w", encoding="utf-8") as f:
        json.dump({int(i): name for i, name in enumerate(OUTPUT_CLASSES)}, f, indent=2)

    metrics_doc = {
        "model": "MobileNetV2 (ImageNet-pretrained frozen backbone + fine-tuned classification head)",
        "dataset": "PlantVillage (spMohanty/PlantVillage-Dataset, CC-BY-SA) — verified public leaf imagery",
        "trained_classes": OUTPUT_CLASSES,
        "classes_without_cv_data": [
            "wheat_yellow_rust", "wheat_brown_rust", "wheat_leaf_blight", "wheat_powdery_mildew",
            "rice_blast", "rice_bacterial_blight", "rice_sheath_blight",
            "tomato_leaf_curl", "cotton_bacterial_blight", "cotton_grey_mildew",
            "chilli_leaf_curl", "chilli_anthracnose", "mustard_white_rust",
            "sugarcane_red_rot", "soybean_yellow_mosaic", "chickpea_ascochyta"
        ],
        "note_on_untrained_classes": ("Crops without verified public leaf-pathology datasets are "
                                      "served by the ICAR/TNAU/PAU symptom-based knowledge base at "
                                      "runtime and are explicitly labelled as such in API responses."),
        "train_images": len(train_samples),
        "val_images": len(val_samples),
        "image_size": size,
        "epochs": args.epochs,
        "val_accuracy": round(val_acc, 4),
        "val_macro_f1": round(macro_f1, 4),
        "val_weighted_f1": round(weighted_f1, 4),
        "per_class_metrics": per_class,
        "confusion_matrix": cm,
        "class_order": OUTPUT_CLASSES,
    }
    with open(os.path.join(artifacts_dir, "vision_evaluation_metrics.json"), "w", encoding="utf-8") as f:
        json.dump(metrics_doc, f, indent=2)

    with open(os.path.join(artifacts_dir, "vision_training_history.json"), "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)

    print(f"[+] Exported trained weights -> {pth_path}")
    print(f"[+] Exported evaluation metrics -> vision_evaluation_metrics.json")
    print(f"[+] Exported training history -> vision_training_history.json")


if __name__ == "__main__":
    main()



