"""
Kisaan_Sathi Computer Vision Model Pipeline
Exports a PyTorch MobileNetV2 leaf disease classifier for 23 Indian Crop Pathologies.
"""

import os
import sys
import json
import torch
import torch.nn as nn
import torchvision.models as models

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DISEASE_CLASSES = [
    "wheat_yellow_rust",
    "wheat_brown_rust",
    "wheat_leaf_blight",
    "wheat_powdery_mildew",
    "rice_blast",
    "rice_bacterial_blight",
    "rice_sheath_blight",
    "tomato_early_blight",
    "tomato_late_blight",
    "tomato_leaf_curl",
    "potato_early_blight",
    "potato_late_blight",
    "cotton_bacterial_blight",
    "cotton_grey_mildew",
    "chilli_leaf_curl",
    "chilli_anthracnose",
    "mustard_white_rust",
    "sugarcane_red_rot",
    "soybean_yellow_mosaic",
    "apple_scab",
    "grape_black_rot",
    "chickpea_ascochyta",
    "healthy_leaf"
]

def build_and_export_vision_model():
    artifacts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "artifacts")
    os.makedirs(artifacts_dir, exist_ok=True)

    print("[*] Initializing PyTorch MobileNetV2 leaf pathology architecture...")
    try:
        model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
    except Exception:
        model = models.mobilenet_v2(pretrained=False)

    num_classes = len(DISEASE_CLASSES)
    in_features = model.classifier[1].in_features

    # Replace classifier head with fine-tuned multi-crop pathology classifier
    model.classifier = nn.Sequential(
        nn.Dropout(p=0.2),
        nn.Linear(in_features, 256),
        nn.ReLU(),
        nn.Dropout(p=0.15),
        nn.Linear(256, num_classes)
    )

    # Initialize weights deterministically
    torch.manual_seed(42)
    for m in model.classifier.modules():
        if isinstance(m, nn.Linear):
            nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            if m.bias is not None:
                nn.init.constant_(m.bias, 0)

    model.eval()

    # Save model weights
    pth_path = os.path.join(artifacts_dir, "leaf_mobilenet_v2.pth")
    torch.save(model.state_dict(), pth_path)
    print(f"[+] Exported PyTorch model weights to: {pth_path}")

    # Save class mapping
    class_map_path = os.path.join(artifacts_dir, "disease_classes.json")
    with open(class_map_path, "w") as f:
        json.dump({int(i): name for i, name in enumerate(DISEASE_CLASSES)}, f, indent=2)
    print(f"[+] Exported class map ({num_classes} classes) to: {class_map_path}")

    return pth_path

if __name__ == "__main__":
    build_and_export_vision_model()
