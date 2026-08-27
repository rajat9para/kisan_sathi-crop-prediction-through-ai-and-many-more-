"""
AgriSaathi ML Engine Training Pipeline
Trains an XGBoost multi-class classifier on Crop Recommendation data
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
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

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

def generate_crop_dataset(samples_per_crop=100, random_seed=42):
    np.random.seed(random_seed)
    data = []
    
    for crop, profile in CROP_PROFILES.items():
        for _ in range(samples_per_crop):
            n = np.clip(np.random.normal((profile["N"][0] + profile["N"][1]) / 2, (profile["N"][1] - profile["N"][0]) / 5), 0, 160)
            p = np.clip(np.random.normal((profile["P"][0] + profile["P"][1]) / 2, (profile["P"][1] - profile["P"][0]) / 5), 0, 160)
            k = np.clip(np.random.normal((profile["K"][0] + profile["K"][1]) / 2, (profile["K"][1] - profile["K"][0]) / 5), 0, 220)
            temp = np.clip(np.random.normal((profile["temp"][0] + profile["temp"][1]) / 2, (profile["temp"][1] - profile["temp"][0]) / 4), 5, 45)
            humidity = np.clip(np.random.normal((profile["humidity"][0] + profile["humidity"][1]) / 2, (profile["humidity"][1] - profile["humidity"][0]) / 5), 10, 100)
            ph = np.clip(np.random.normal((profile["ph"][0] + profile["ph"][1]) / 2, (profile["ph"][1] - profile["ph"][0]) / 5), 3.5, 9.5)
            rainfall = np.clip(np.random.normal((profile["rain"][0] + profile["rain"][1]) / 2, (profile["rain"][1] - profile["rain"][0]) / 4), 15, 350)
            
            data.append({
                "N": round(float(n), 2),
                "P": round(float(p), 2),
                "K": round(float(k), 2),
                "temperature": round(float(temp), 2),
                "humidity": round(float(humidity), 2),
                "ph": round(float(ph), 2),
                "rainfall": round(float(rainfall), 2),
                "label": crop
            })
            
    df = pd.DataFrame(data)
    return df

def train_and_export():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    artifacts_dir = os.path.join(base_dir, "artifacts")
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(artifacts_dir, exist_ok=True)

    print("[*] Generating Kaggle-standard Crop Recommendation Dataset (2,200 samples)...")
    df = generate_crop_dataset(samples_per_crop=100)
    csv_path = os.path.join(data_dir, "Crop_recommendation.csv")
    df.to_csv(csv_path, index=False)
    print(f"[+] Saved dataset to: {csv_path}")

    # Feature columns
    feature_cols = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
    X = df[feature_cols]
    y_raw = df["label"]

    # Label Encoding
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y_raw)
    
    # Save label mapping
    crop_mapping = {int(i): str(crop) for i, crop in enumerate(label_encoder.classes_)}
    with open(os.path.join(artifacts_dir, "crop_label_encoder.json"), "w") as f:
        json.dump(crop_mapping, f, indent=2)

    # Calculate feature stats (mean, std, min, max) for UI normalization
    feature_stats = {}
    for col in feature_cols:
        feature_stats[col] = {
            "mean": float(df[col].mean()),
            "std": float(df[col].std()),
            "min": float(df[col].min()),
            "max": float(df[col].max())
        }
    with open(os.path.join(artifacts_dir, "feature_stats.json"), "w") as f:
        json.dump(feature_stats, f, indent=2)

    # Save Agronomic profiles for rule-based explanation
    with open(os.path.join(artifacts_dir, "crop_profiles.json"), "w") as f:
        json.dump(CROP_PROFILES, f, indent=2)

    # Train / Test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    print("[*] Training XGBoost Multi-Class Classifier...")
    model = xgb.XGBClassifier(
        n_estimators=120,
        max_depth=5,
        learning_rate=0.1,
        objective="multi:softprob",
        num_class=len(label_encoder.classes_),
        random_state=42,
        eval_metric="mlogloss"
    )
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"[+] Model Accuracy on Test Set: {acc * 100:.2f}%")

    # Save XGBoost Model
    model_json_path = os.path.join(artifacts_dir, "crop_xgboost_model.json")
    model.save_model(model_json_path)
    joblib.dump(model, os.path.join(artifacts_dir, "crop_xgboost_model.pkl"))
    print(f"[+] Exported XGBoost model to: {model_json_path}")

    # Build SHAP TreeExplainer & pre-test
    print("[*] Fitting SHAP TreeExplainer...")
    explainer = shap.TreeExplainer(model)
    joblib.dump(explainer, os.path.join(artifacts_dir, "shap_explainer.pkl"))
    
    # Test SHAP on a sample
    sample_input = X_test.iloc[[0]]
    sample_crop_idx = y_pred[0]
    shap_values = explainer.shap_values(sample_input)
    
    print(f"[+] SHAP Explanation ready for top predicted crop '{label_encoder.classes_[sample_crop_idx]}'.")
    print("[+] ML Artifacts successfully built!")

if __name__ == "__main__":
    train_and_export()
