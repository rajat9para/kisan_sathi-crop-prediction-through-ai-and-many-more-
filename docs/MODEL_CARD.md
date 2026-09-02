# Model Card: Kisaan Sathi ML & Computer Vision Engines

**Document Version**: 1.0  
**Target Submission**: Smart India Hackathon 2026  
**Repository**: `rajat9para/kisan_sathi-crop-prediction-through-ai-and-many-more-`

---

## 1. Model Overview

### 1.1 Crop Recommendation Engine
- **Model Type**: Multi-Class Gradient Boosted Decision Trees (`XGBClassifier`) + Explainable AI (`shap.TreeExplainer`).
- **Input Features (7 continuous variables)**:
  1. `N` (Available Soil Nitrogen, kg/ha): 0 to 140
  2. `P` (Available Soil Phosphorus, kg/ha): 5 to 145
  3. `K` (Available Soil Potassium, kg/ha): 5 to 205
  4. `temperature` (Mean Ambient Temperature, °C): 8 to 44
  5. `humidity` (Relative Humidity, %): 14 to 100
  6. `ph` (Soil pH value): 3.5 to 9.5
  7. `rainfall` (Seasonal Rainfall, mm): 20 to 300
- **Target Classes (22 Indian Crops)**: Rice, Maize, Chickpea, Kidneybeans, Pigeonpeas, Mothbeans, Mungbean, Blackgram, Lentil, Pomegranate, Banana, Mango, Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, Coconut, Cotton, Jute, Coffee.

### 1.2 Plant Doctor Leaf Pathology Engine
- **Model Type**: Deep Convolutional Neural Network (`MobileNetV2` — ImageNet-pretrained frozen backbone + fine-tuned 2-layer Dropout-Dense classification head).
- **Framework**: PyTorch (`torch`, `torchvision`).
- **Training Data**: Genuine **PlantVillage** public dataset (spMohanty/PlantVillage-Dataset, CC-BY-SA) — 4,200 verified leaf images across 7 classes (3,570 train / 630 val).
- **Input Preprocessing**: RGB PIL Image -> Resize (160, 160) -> Tensor -> Normalize (ImageNet mean `[0.485, 0.456, 0.406]`, std `[0.229, 0.224, 0.225]`). Train-time augmentation: RandomResizedCrop, horizontal flip, ±15° rotation, color jitter.
- **CV-Diagnosable Classes (7 — verified public training data exists)**: Apple Scab, Grape Black Rot, Healthy Leaf, Potato Early Blight, Potato Late Blight, Tomato Early Blight, Tomato Late Blight.
- **Honest capability boundary**: Crops with NO verified public leaf-pathology dataset (wheat, rice, cotton, chilli, mustard, sugarcane, soybean-YMV, chickpea) are deliberately **not claimed as CV-diagnosable**. They are served by the ICAR/TNAU/PAU symptom-based knowledge base and API responses carry `diagnosis_method: "symptom_guidelines"` with `confidence_pct: null`. The UI displays "ICAR symptom-based guidance" instead of a fabricated neural score.

### 1.2.1 Vision Model Evaluation (held-out validation set, n=630)
| Metric | Value |
|---|---|
| **Validation Accuracy** | **95.87%** |
| **Macro F1** | **95.88%** |
| **Weighted F1** | **95.88%** |
| Apple Scab F1 | 0.983 |
| Grape Black Rot F1 | 0.994 |
| Healthy Leaf F1 | 0.972 |
| Potato Early Blight F1 | 0.966 |
| Potato Late Blight F1 | 0.941 |
| Tomato Early Blight F1 | 0.930 |
| Tomato Late Blight F1 | 0.924 |

Per-epoch training history and the full confusion matrix are exported to
`backend/ml/artifacts/vision_training_history.json` and
`vision_evaluation_metrics.json`. Confidence scores returned by the API are the
**raw softmax outputs** — never artificially floored or clamped.

### 1.3 Weather-Driven Disease-Risk Early Warning
Rule-based epidemiological risk indices (ICAR/SAU infection thresholds) computed
from the **live Open-Meteo forecast**: temperature trapezoid favourability ×
humidity ramp × rainfall/leaf-wetness proxy for Wheat Yellow Rust, Rice Blast,
Late Blight (potato/tomato) and Grape Downy Mildew. Exposed via
`GET /api/weather` → `disease_risk_early_warning`.

---

## 2. Training Data & Provenance

- **Crop Recommendation Dataset**: 2,200 verified agro-climatic vectors (100 samples per class across 22 crops) sourced from the standard Kaggle & ICAR precision agriculture benchmark dataset.
- **Pathology Diagnostic Standards**: Symptoms and remedies grounded in verified Indian Council of Agricultural Research (ICAR), Tamil Nadu Agricultural University (TNAU), Punjab Agricultural University (PAU), and GBPUAT agronomic extension guidelines.

---

## 3. Evaluation & Validation Metrics

### 3.1 5-Fold Stratified Cross-Validation (Crop Model)
| Metric | Value |
|---|---|
| Fold 1 Accuracy | 99.09% |
| Fold 2 Accuracy | 98.64% |
| Fold 3 Accuracy | 98.41% |
| Fold 4 Accuracy | 98.41% |
| Fold 5 Accuracy | 98.64% |
| **Mean CV Accuracy** | **98.64% (± 0.25%)** |

### 3.2 Held-Out Test Set (80/20 Stratified Split, 440 Test Vectors)
| Metric | Value |
|---|---|
| **Overall Accuracy** | **99.09%** |
| **Weighted Precision** | **99.12%** |
| **Weighted Recall** | **99.09%** |
| **Weighted F1-Score** | **99.08%** |

---

## 4. Multi-Pillar Re-Ranking & Sustainability Formulation

To satisfy the SIH 2026 Problem Statement requirements for **Yield, Profit Margins, and Sustainability Forecasting**, the engine computes:

1. **Soil & Weather Fit ($F_{\text{soil}}, F_{\text{weather}}$)**: Distance penalties against agronomic tolerance bounds.
2. **Crop Rotation Fit ($F_{\text{rotation}}$)**: +15% boost for Legume $\to$ Cereal or Cereal $\to$ Legume rotation; penalty for consecutive monoculture.
3. **Dynamic Net Profit Margin ($\text{Profit} = \text{Yield} \times \text{MandiPrice} - \text{ProductionCost}$)**: Scaled by nutrient fit and farm acreage.
4. **Quantitative Sustainability Score ($S \in [0, 100]$)**:
   $$S = 0.35 \times W_{\text{water}} + 0.35 \times H_{\text{soil}} + 0.20 \times C_{\text{chemical}} + 0.10 \times B_{\text{carbon}}$$
   - Legumes with biological Nitrogen fixation ($40\text{–}80\text{ kg N/ha}$) receive maximum soil conservation scores.

---

## 5. Explainability & Trust (SHAP)

Local explanations are computed in real time using `shap.TreeExplainer`:
- Calculates exact log-odds contribution vector for each of the 7 features.
- Translated into clear bilingual farmer narratives (e.g. *"Optimal Nitrogen level (85 kg/ha) boosts recommendation by +0.24"*).

---

## 6. Limitations & Fallback Protocol

1. **Non-leaf image rejection**: The computer vision model verifies contrast and variance to reject blank or solid-color uploads with clear guidance.
2. **Offline resilience**: In zero-connectivity mode, the Flutter app executes `OfflineInferenceEngine` directly on-device in pure Dart with zero network dependency.
