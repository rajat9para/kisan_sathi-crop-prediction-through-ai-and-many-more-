"""
AgriSaathi ML Engine Training & Evaluation Pipeline
Trains an XGBoost multi-class classifier on verified Crop Recommendation data,
performs 5-fold Stratified Cross-Validation, generates a confusion matrix,
and prepares SHAP TreeExplainer for feature importance explainability.
"""

import os
import sys
import json
import numpy as np
import pandas as pd
import joblib
import xgboost as xgb
import shap
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix, classification_report

# Ensure utf-8 output encoding
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# 22 standard crops in Indian agro-climatic conditions
CROPS = [
    "rice", "maize", "chickpea", "kidneybeans", "pigeonpeas",
    "mothbeans", "mungbean", "blackgram", "lentil", "pomegranate",
    "banana", "mango", "grapes", "watermelon", "muskmelon",
    "apple", "orange", "papaya", "coconut", "cotton", "jute", "coffee"
]

# Agronomic optimal ranges (N, P, K, Temp C, Humidity %, pH, Rainfall mm)
CROP_PROFILES = {
    "rice":        {"N": (60, 100), "P": (35, 60), "K": (35, 45), "temp": (20, 27), "humidity": (80, 85), "ph": (5.0, 7.5), "rain": (180, 300)},
    "maize":       {"N": (60, 100), "P": (35, 60), "K": (15, 25), "temp": (18, 27), "humidity": (55, 75), "ph": (5.5, 7.5), "rain": (60, 110)},
    "chickpea":    {"N": (20, 60),  "P": (55, 80), "K": (75, 85), "temp": (15, 22), "humidity": (14, 20), "ph": (6.0, 8.5), "rain": (65, 95)},
    "kidneybeans": {"N": (10, 40),  "P": (55, 80), "K": (15, 25), "temp": (15, 24), "humidity": (18, 25), "ph": (5.5, 6.0), "rain": (60, 150)},
    "pigeonpeas":  {"N": (10, 40),  "P": (55, 80), "K": (15, 25), "temp": (25, 38), "humidity": (30, 70), "ph": (5.0, 7.5), "rain": (90, 200)},
    "mothbeans":   {"N": (10, 40),  "P": (35, 60), "K": (15, 25), "temp": (24, 32), "humidity": (40, 65), "ph": (3.5, 9.5), "rain": (30, 75)},
    "mungbean":    {"N": (10, 40),  "P": (35, 60), "K": (15, 25), "temp": (27, 30), "humidity": (80, 90), "ph": (6.2, 7.2), "rain": (35, 60)},
    "blackgram":   {"N": (30, 60),  "P": (55, 80), "K": (15, 25), "temp": (25, 35), "humidity": (60, 70), "ph": (6.5, 7.5), "rain": (60, 75)},
    "lentil":      {"N": (10, 40),  "P": (55, 80), "K": (15, 25), "temp": (18, 30), "humidity": (60, 70), "ph": (6.0, 7.5), "rain": (35, 55)},
    "pomegranate": {"N": (15, 40),  "P": (10, 30), "K": (35, 45), "temp": (18, 25), "humidity": (85, 95), "ph": (5.5, 7.2), "rain": (100, 115)},
    "banana":      {"N": (80, 120), "P": (70, 95), "K": (45, 55), "temp": (25, 30), "humidity": (75, 85), "ph": (5.5, 6.5), "rain": (90, 120)},
    "mango":       {"N": (10, 40),  "P": (15, 35), "K": (25, 35), "temp": (27, 36), "humidity": (45, 55), "ph": (4.5, 7.0), "rain": (85, 105)},
    "grapes":      {"N": (15, 40),  "P": (120, 145), "K": (195, 205), "temp": (8, 42), "humidity": (80, 85), "ph": (5.5, 6.5), "rain": (65, 75)},
    "watermelon":  {"N": (80, 120), "P": (5, 30),  "K": (45, 55), "temp": (24, 27), "humidity": (80, 90), "ph": (6.0, 7.0), "rain": (40, 60)},
    "muskmelon":   {"N": (80, 120), "P": (5, 30),  "K": (45, 55), "temp": (27, 30), "humidity": (90, 95), "ph": (6.0, 6.8), "rain": (20, 30)},
    "apple":       {"N": (15, 40),  "P": (120, 145), "K": (195, 205), "temp": (21, 24), "humidity": (90, 95), "ph": (5.5, 6.5), "rain": (100, 125)},
    "orange":      {"N": (10, 40),  "P": (5, 30),   "K": (5, 15),  "temp": (10, 35), "humidity": (90, 95), "ph": (6.0, 8.0), "rain": (100, 120)},
    "papaya":      {"N": (30, 70),  "P": (45, 70),  "K": (45, 55), "temp": (23, 44), "humidity": (90, 95), "ph": (6.5, 7.0), "rain": (40, 250)},
    "coconut":     {"N": (15, 40),  "P": (5, 30),   "K": (25, 35), "temp": (25, 29), "humidity": (90, 100), "ph": (5.5, 6.5), "rain": (130, 230)},
    "cotton":      {"N": (100, 140), "P": (35, 60), "K": (15, 25), "temp": (22, 26), "humidity": (75, 85), "ph": (6.0, 8.0), "rain": (60, 100)},
    "jute":        {"N": (60, 100), "P": (35, 60), "K": (35, 45), "temp": (23, 26), "humidity": (70, 90), "ph": (6.0, 7.5), "rain": (150, 200)},
    "coffee":      {"N": (80, 120), "P": (15, 40), "K": (25, 35), "temp": (23, 28), "humidity": (50, 70), "ph": (6.0, 7.5), "rain": (115, 200)},
}

def load_verified_dataset(csv_path: str) -> pd.DataFrame:
    """Loads and validates the 2,200 sample Kaggle/ICAR Indian Crop Recommendation dataset."""
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Verified dataset not found at: {csv_path}")
    df = pd.read_csv(csv_path)
    required_cols = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall", "label"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column in dataset: {col}")
    print(f"[+] Loaded verified dataset from {csv_path} with {len(df)} samples across {df['label'].nunique()} crop classes.")
    return df

def train_and_export():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    artifacts_dir = os.path.join(base_dir, "artifacts")
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(artifacts_dir, exist_ok=True)

    csv_path = os.path.join(data_dir, "Crop_recommendation.csv")
    df = load_verified_dataset(csv_path)

    # Feature columns
    feature_cols = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
    X = df[feature_cols]
    y_raw = df["label"]

    # Label Encoding
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y_raw)
    
    # Save label mapping
    crop_mapping = {int(i): str(crop) for i, crop in enumerate(label_encoder.classes_)}
    with open(os.path.join(artifacts_dir, "crop_label_encoder.json"), "w", encoding="utf-8") as f:
        json.dump(crop_mapping, f, indent=2)

    # Calculate feature stats (mean, std, min, max) for UI normalization
    feature_stats = {}
    for col in feature_cols:
        feature_stats[col] = {
            "mean": round(float(df[col].mean()), 2),
            "std": round(float(df[col].std()), 2),
            "min": round(float(df[col].min()), 2),
            "max": round(float(df[col].max()), 2)
        }
    with open(os.path.join(artifacts_dir, "feature_stats.json"), "w", encoding="utf-8") as f:
        json.dump(feature_stats, f, indent=2)

    # Save Agronomic profiles for rule-based explanation
    with open(os.path.join(artifacts_dir, "crop_profiles.json"), "w", encoding="utf-8") as f:
        json.dump(CROP_PROFILES, f, indent=2)

    # 1. Rigorous 5-Fold Stratified Cross-Validation
    print("[*] Running 5-Fold Stratified Cross-Validation on verified dataset...")
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_model = xgb.XGBClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        objective="multi:softprob",
        num_class=len(label_encoder.classes_),
        random_state=42,
        eval_metric="mlogloss"
    )
    cv_scores = cross_val_score(cv_model, X, y, cv=cv, scoring="accuracy")
    print(f"[+] 5-Fold Cross-Validation Accuracies: {[round(float(s) * 100, 2) for s in cv_scores]}%")
    print(f"[+] Mean CV Accuracy: {cv_scores.mean() * 100:.2f}% (+/- {cv_scores.std() * 100:.2f}%)")

    # 2. Train / Held-Out Test Split (80% Train, 20% Held-out Test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    print("[*] Training Final XGBoost Multi-Class Production Model...")
    model = xgb.XGBClassifier(
        n_estimators=120,
        max_depth=5,
        learning_rate=0.08,
        objective="multi:softprob",
        num_class=len(label_encoder.classes_),
        random_state=42,
        eval_metric="mlogloss"
    )
    model.fit(X_train, y_train)

    # 3. Evaluate on Held-Out Test Set
    y_pred = model.predict(X_test)
    test_acc = accuracy_score(y_test, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average="weighted")
    cm = confusion_matrix(y_test, y_pred).tolist()

    print(f"[+] Held-Out Test Set Accuracy: {test_acc * 100:.2f}%")
    print(f"[+] Weighted Precision: {precision * 100:.2f}%, Recall: {recall * 100:.2f}%, F1-Score: {f1 * 100:.2f}%")

    # Save comprehensive evaluation metrics & provenance for auditing
    eval_report = {
        "dataset_source": "Kaggle Verified Crop Recommendation Dataset (2,200 samples, 22 Indian crop classes)",
        "dataset_samples_total": len(df),
        "num_classes": len(label_encoder.classes_),
        "features": feature_cols,
        "cross_validation_5fold_scores_pct": [round(float(s) * 100, 2) for s in cv_scores],
        "cross_validation_mean_accuracy_pct": round(float(cv_scores.mean()) * 100, 2),
        "cross_validation_std_pct": round(float(cv_scores.std()) * 100, 2),
        "heldout_test_accuracy_pct": round(float(test_acc) * 100, 2),
        "heldout_weighted_precision_pct": round(float(precision) * 100, 2),
        "heldout_weighted_recall_pct": round(float(recall) * 100, 2),
        "heldout_weighted_f1_score_pct": round(float(f1) * 100, 2),
        "confusion_matrix": cm,
        "classes": list(label_encoder.classes_)
    }
    with open(os.path.join(artifacts_dir, "evaluation_metrics.json"), "w", encoding="utf-8") as f:
        json.dump(eval_report, f, indent=2)
    print(f"[+] Saved evaluation metrics to: {os.path.join(artifacts_dir, 'evaluation_metrics.json')}")

    # 4. Save XGBoost Model
    model_json_path = os.path.join(artifacts_dir, "crop_xgboost_model.json")
    model_pkl_path = os.path.join(artifacts_dir, "crop_xgboost_model.pkl")
    model.save_model(model_json_path)
    joblib.dump(model, model_pkl_path)
    print(f"[+] Exported XGBoost model to: {model_json_path}")

    # 5. Fit SHAP TreeExplainer
    print("[*] Fitting SHAP TreeExplainer on XGBoost model...")
    explainer = shap.TreeExplainer(model)
    joblib.dump(explainer, os.path.join(artifacts_dir, "shap_explainer.pkl"))
    print("[+] SHAP TreeExplainer artifact built successfully.")

    # 6. Verify SHAP output
    sample_input = X_test.iloc[[0]]
    sample_crop_idx = y_pred[0]
    _ = explainer.shap_values(sample_input)
    print(f"[+] SHAP Explanation verified for top predicted crop '{label_encoder.classes_[sample_crop_idx]}'.")
    print("[+] All ML artifacts successfully trained, verified, and exported!")

if __name__ == "__main__":
    train_and_export()
