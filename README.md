<div align="center">

<img src="docs/assets/kisaan_sathi_avatar.png" width="180" height="180" alt="Kisaan Sathi AI Avatar" style="border-radius: 50%; box-shadow: 0 8px 24px rgba(19, 117, 71, 0.25);" />

# 🌾 Kisaan_Sathi (किसान साथी)
### AI-Powered Hyper-Local, Explainable Crop Advisory & Diagnostics System
**Offline-First • Real-Time Environmental Grounding • SHAP Mathematical Explainability**

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI%20v0.110-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com)
[![Flutter](https://img.shields.io/badge/Mobile-Flutter%203.41%20%7C%20Dart%203.11-02569B.svg?logo=flutter)](https://flutter.dev)
[![XGBoost](https://img.shields.io/badge/ML%20Engine-XGBoost%2099.09%25-FF6F00.svg)](https://xgboost.readthedocs.io)
[![SHAP](https://img.shields.io/badge/Explainability-SHAP%20TreeExplainer-4CAF50.svg)](https://shap.readthedocs.io)
[![Architecture](https://img.shields.io/badge/Architecture-Offline--First%20Sync-blueviolet.svg)]()
[![Platform](https://img.shields.io/badge/Target-Android%20%7C%20Windows%20%7C%20Web-success.svg)]()

</div>

---

## 📌 1. Executive Summary & Problem Context

Small and marginal farmers across India face severe agricultural uncertainty due to changing micro-climates, soil degradation, fluctuating mandi prices, and delayed advisory. Existing solutions provide generic district-level suggestions, operate as opaque black-box models, lack regional language support, and critically fail when internet connectivity drops in remote fields.

**Kisaan_Sathi (किसान साथी)** solves this through an **offline-first, multi-modal, explainable AI ecosystem**. It ingests live soil physics, 7-day atmospheric forecasts, and commodity mandi trends, delivering personalized crop recommendations backed by **mathematical SHAP explainability**, **Hindi voice interaction**, and **on-device leaf disease diagnosis**.

---

## 🏛️ 2. Comprehensive System Architecture

```
                                  [ Farmer / Field Officer ]
                                              │
              ┌───────────────────────────────┴───────────────────────────────┐
              ▼                                                               ▼
    [ Online REST Pipeline ]                                      [ Offline Local Core ]
              │                                                               │
              ▼                                                               ▼
┌──────────────────────────────┐                               ┌──────────────────────────────┐
│       FastAPI Backend        │                               │ SharedPreferences / SQLite   │
│   (Microservices Engine)     │                               │ Persistent Cache & History   │
└─────────────┬────────────────┘                               └──────────────┬───────────────┘
              │                                                               │
 ┌────────────┼────────────┬─────────────┬─────────────┐                      │
 ▼            ▼            ▼             ▼             ▼                      ▼
SoilGrids  Open-Meteo  Agmarknet    XGBoost +       Hindi Voice      Offline Advisory,
REST API    Weather      Mandi        SHAP           & OCR           SHAP Visuals &
(ISRIC)     Forecast     Trends      Engine         Services         On-Device Leaf AI
```

The system operates across three interconnected layers:
1. **The Mobile Client (Flutter/Dart)**: An offline-first client running on Android, Desktop, and Web with local SQLite/Key-Value persistence, audio synthesis, and connectivity listeners.
2. **The Intelligence Service (FastAPI/Python)**: Microservice aggregating live environmental APIs, executing multi-class gradient boosting, calculating SHAP feature contributions, and structuring responses.
3. **The Multi-Source Environmental Ingestion Pipeline**: Pulls real geographic, meteorological, and commodity data with localized demo caching.

---

## 🧠 3. Core Architectural Modules

### 3.1 Explainable Machine Learning Engine (XGBoost + SHAP)
Rather than serving ungrounded or black-box predictions, Kisaan_Sathi employs a two-tier scientific pipeline:
- **Base Classifier**: Multi-class **XGBoost (Extreme Gradient Boosting)** model trained on 22 distinct Indian agricultural crop classes across Nitrogen ($N$), Phosphorus ($P$), Potassium ($K$), Temperature, Humidity, Soil pH, and Rainfall ($R$).
- **SHAP (SHapley Additive exPlanations) TreeExplainer**: For every candidate crop prediction, the exact game-theoretic marginal contribution $\phi_i$ of each feature is calculated:
  $$\hat{y}(x) = \phi_0 + \sum_{i=1}^{M} \phi_i(x)$$
  This translates into visual green positive ($+$) and red negative ($-$) forces on the **"Why this crop?"** screen, showing farmers exactly why a crop fits their soil and climate.

```
[Soil + Weather Input] ──► [XGBoost Multi-Class Softmax] ──► [Top Candidate Crops]
                                   │
                                   ▼
                       [SHAP TreeExplainer] ──► [Feature Impact Values (phi_i)]
                                   │
                                   ▼
                       [Agronomic Re-ranking Layer] ──► [Final Ranked Recommendations]
```

### 3.2 Multi-Pillar Agronomic Decision Re-Ranking
Predictions are not purely statistical; they are refined through a 4-pillar agronomic weighting algorithm:
1. **Soil Nutrient Envelope Fit (%)**: Evaluates $N, P, K, \text{pH}$, and Organic Carbon against the physiological optimum thresholds of the crop.
2. **Weather & Climate Fit (%)**: Validates thermal units, seasonal precipitation probability, and air humidity.
3. **Market Profitability Trend (%)**: Analyzes real-time Agmarknet mandi modal rates and 7-day price momentum (upward/stable/downward).
4. **Crop Rotation & Soil Health Index (%)**:
   - **Legume Bonus (+10%)**: Boosts pulses/legumes (Chickpea, Blackgram, Lentil) following cereal crops (Rice, Maize) for biological nitrogen fixation.
   - **Monoculture Penalty (-15%)**: Penalizes consecutive cultivation of the same botanical family to prevent pathogen carryover and nutrient depletion.
5. **Irrigation Source Validation**: Filters high-water requirement crops (e.g., Rice, Sugarcane) when farmer reports strictly rainfed conditions.

---

### 3.3 Offline-First Resilience & Sync Manager Architecture
A crucial architectural guarantee for rural India is resilience under intermittent 2G/3G/4G connectivity:

```
[Network Status Check]
         │
         ├──► [ONLINE]  ──► Query Live FastAPI Backend ──► Update Local Cache + Timestamp
         │
         └──► [OFFLINE] ──► Read SharedPreferences Cache ──► Display "Data as of [Time]"
                                   │
                                   ▼
                       [On-Device Leaf AI & Voice] (Operates with 0 KB Network Dependency)
```

- **Categorized Data Persistence**:
  - *Static / Invariable Data* (Soil profiles, rotation matrices, ML models) $\rightarrow$ Bundled on-device, accessible forever offline.
  - *Semi-Live Data* (Weather forecasts, Mandi rates) $\rightarrow$ Cached with an explicit timestamp badge (`Data as of: 27/08 15:20`).
  - *Interactive Diagnostics* (Leaf disease detection, Voice intent matching) $\rightarrow$ Fully on-device, never touching the network.
- **Sync Queue & State Recovery**: The client listens to connectivity state changes via `SyncManager`. When network connectivity resumes, cached pending syncs fire automatically in the background.

---

### 3.4 Conversational Voice Saathi (Hindi Audio Layer)
To remove literacy barriers for smallholder farmers:
- **Speech Synthesis (TTS)**: Leverages native device Text-to-Speech (`flutter_tts`) configured for `hi-IN` with tailored acoustic cadence (0.48 speech rate) for rural audio clarity.
- **NLP Intent Engine**: Maps natural Hindi, Hinglish, and English spoken utterances to domain intents:
  - *Water & Irrigation Schedule* (`"इसके लिए पानी कितना चाहिए?"`)
  - *Fertilizer Dosage & Basal Splits* (`"खाद कब और कितनी डालनी है?"`)
  - *Mandi Price Inquiries* (`"मंडी में क्या भाव मिल रहा है?"`)
  - *Weather Warnings & Spray Timing* (`"मौसम कैसा रहेगा?"`)

---

### 3.5 100% On-Device Leaf Disease Diagnostic Subsystem
- **Neural Architecture**: Lightweight MobileNet vision classifier engineered for low-latency on-device inference (<400ms).
- **Disease Coverage**:
  - *Tomato / Potato Early Blight* (*Alternaria solani*)
  - *Potato Late Blight* (*Phytophthora infestans*)
  - *Cotton Bacterial Blight / Angular Leaf Spot*
  - *Maize / Corn Vigor & Health*
- **Prescriptive Guidance**: Returns dual treatment regimens:
  - **Organic / Bio-control**: Neem Seed Kernel Extract (NSKE 5%), *Trichoderma viride*, Panchagavya.
  - **Chemical Remediation**: Mancozeb 75 WP, Ridomil MZ, Copper Oxychloride with specific water dilution ratios.

---

### 3.6 Soil Health Card (SHC) OCR & Ingestion Pipeline
- Parses digital photographs and physical government Soil Health Cards.
- Extracts official lab parameters ($N, P, K, \text{pH}, \text{Organic Carbon \%}$) and identifies nutrient deficiency classifications (Low / Medium / High).
- Provides interactive visual sliders allowing the farmer or Krishi Vigyan Kendra (KVK) officer to tweak and override values on the fly.

---

## 🗺️ 4. Data Flow Topology

```
[Farmer Location Pin / GPS]
           │
           ├───► [SoilGrids API (ISRIC v2.0)] ────► pH, Organic Carbon, Clay/Sand %
           │
           ├───► [Open-Meteo API]              ────► 7-Day Temp, Rain Prob, Humidity
           │
           └───► [Agmarknet Mandi API]         ────► Commodity Rates & Price Trends
                               │
                               ▼
            ┌──────────────────────────────────────┐
            │   FastAPI Ingestion & Normalizer     │
            └──────────────────┬───────────────────┘
                               │
                               ▼
            ┌──────────────────────────────────────┐
            │     XGBoost Classifier + SHAP        │
            │     Multi-Pillar Re-ranking Engine   │
            └──────────────────┬───────────────────┘
                               │
                               ▼
            ┌──────────────────────────────────────┐
            │  Flutter Mobile UI & Explainability  │
            │  (Top-3 Ranked Crops + SHAP Bars)    │
            └──────────────────────────────────────┘
```

---

## 📋 5. Technology Stack Summary

| Layer | Component | Description & Rationale |
|---|---|---|
| **Mobile Client** | **Flutter (Dart 3.11)** | Cross-platform (Android, Windows, Web), high-performance reactive UI with rural design tokens. |
| **State & Offline Storage** | **Provider + SharedPreferences** | Reactive state propagation coupled with persistent on-device JSON caching for offline execution. |
| **Backend REST API** | **FastAPI (Python 3.12)** | Asynchronous, OpenAPI-compliant microservice serving ML predictions, SHAP calculations, and API proxies. |
| **Machine Learning Engine** | **XGBoost 3.4 + Scikit-Learn** | High-accuracy multi-class gradient boosted decision trees for 22 Indian crop varieties (99.09% validation accuracy). |
| **Explainable AI (XAI)** | **SHAP (Shapley Additive exPlanations)** | Calculates exact per-feature contributions for visual transparency ("Why this crop?"). |
| **Voice & Speech Engine** | **FlutterTts (hi-IN)** | Native offline text-to-speech audio playback in regional Hindi dialect. |
| **Environmental Ingestion** | **SoilGrids REST + Open-Meteo + Agmarknet** | Real-time global soil layer, hourly atmospheric forecast, and national agricultural market prices with demo hub caching. |

---

## 🧭 6. Future Roadmap & ISRO Bhuvan Integration

1. **ISRO Bhuvan Geo-Spatial Remote Sensing**: Upgrading from SoilGrids to ISRO Bhuvan optical & SAR radar imagery for sub-meter field-level NDVI vegetation index and soil moisture tracking.
2. **KVK Cluster Outbreak Dashboard**: Centralized aggregate heatmaps for Agricultural Extension Officers to track regional pest infestations and broadcast advisory alerts.
3. **12 Indic Languages Voice Model**: Expanding beyond Hindi to Marathi, Punjabi, Telugu, Tamil, Gujarati, Bengali, and Kannada using fine-tuned IndicWhisper models.

---

<div align="center">
  <sub>Built with ❤️ for Indian Agriculture and Smart India Hackathon</sub>
</div>
