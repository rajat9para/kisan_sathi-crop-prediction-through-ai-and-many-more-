<div align="center">

<img src="public/kisaan_sathi_avatar.png" width="160" height="160" alt="Kisaan Sathi AI Avatar" style="border-radius: 50%; box-shadow: 0 8px 24px rgba(19, 117, 71, 0.25);" />

# 🌾 Kisaan_Sathi (किसान साथी)
### AI-Powered Hyper-Local, Explainable Crop Advisory & Plant Doctor
**11 Indian Soil Types • 11 Languages • Hybrid ML (XGBoost + SHAP) • Groq LLaMA • Android Studio App • Vercel Serverless**

[![Web App](https://img.shields.io/badge/Web%20App-Live%20Ready-2E7D32.svg?logo=googlechrome)](https://kisaansathi-iota.vercel.app/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI%20v0.110-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com)
[![Flutter](https://img.shields.io/badge/Mobile-Flutter%203.41%20%7C%20Dart%203.11-02569B.svg?logo=flutter)](https://flutter.dev)
[![XGBoost](https://img.shields.io/badge/ML%20Engine-XGBoost%2099.09%25-FF6F00.svg)](https://xgboost.readthedocs.io)
[![SHAP](https://img.shields.io/badge/Explainability-SHAP%20TreeExplainer-4CAF50.svg)](https://shap.readthedocs.io)
[![Groq LLM](https://img.shields.io/badge/LLM-Groq%20LLaMA%203.3-F55036.svg)](https://groq.com)
[![Tests Passed](https://img.shields.io/badge/Automated%20Tests-100%25%20Passing-16A34A.svg)](#-7-automated-testing--verification)

</div>

---

## 📌 1. Project Overview

Small and marginal farmers across India face agricultural uncertainty due to changing micro-climates, soil nutrient depletion, volatile mandi rates, and crop diseases. Existing digital solutions act as opaque black boxes, provide generic district-level suggestions, lack regional voice support, or crash when internet connectivity drops.

**Kisaan_Sathi (किसान साथी)** solves this through a **Hybrid AI Architecture**:
1. **Deterministic Machine Learning**: An XGBoost classifier trained across 22 crop classes with **99.09% accuracy**.
2. **SHAP Explainable AI (XAI)**: Breaks down exactly *why* a crop is recommended via mathematical nutrient force vectors (e.g., Potash +28%, pH +18%, Rain -4%).
3. **11 Major Indian Languages**: Full native translation across Hindi, English, Marathi, Punjabi, Telugu, Tamil, Gujarati, Bengali, Kannada, Malayalam, and Odia.
4. **11 Indian Soil Types & Regional Hubs**: Covers Alluvial, Black Cotton, Red Sandy Loam, Calcareous Loam, Deltaic Silt Clay, Desert Sand, Laterite, and Peaty soils across 11 states.
5. **Conversational Voice Saathi**: Groq LLaMA synthesizes personalized audio guidance with dynamic spray timing.
6. **Plant Doctor (Leaf Pathology AI)**: Instant leaf blight identification with zero-budget organic remedies and chemical dosages.
7. **Cross-Platform Mobile App**: Fully featured Flutter mobile app (`agrisaathi_app`) with offline-first SQLite cache, designed for building in Android Studio.

---

## 🗺️ 2. Soil Types & Agro-Ecological Hubs

Kisaan_Sathi comes pre-configured with **11 official regional Soil Health Card presets and micro-climate profiles**:

| State | Hub | Soil Classification | Key Nutrients (N-P-K-pH-OC) | Top Recommended Crop |
|---|---|---|---|---|
| 🚩 **Maharashtra** | Nashik | Medium Black Cotton (Regur) Loam | N:85, P:48, K:190, pH:6.8, OC:0.72% | 🍇 Grapes / अनार |
| 🌾 **Madhya Pradesh** | Indore | Deep Black Malwa Vertisol Clay | N:45, P:62, K:82, pH:7.4, OC:0.58% | 🌾 Chickpea / चना |
| 🌾 **Punjab** | Ludhiana | Indo-Gangetic Alluvial Sandy Loam | N:92, P:42, K:38, pH:7.2, OC:0.45% | 🌾 Rice / ਝੋਨਾ |
| 🌶️ **Andhra Pradesh** | Guntur | Coastal Red Clayey Sandy Loam | N:70, P:55, K:140, pH:6.5, OC:0.65% | 🌿 Cotton / పత్తి |
| 🥜 **Gujarat** | Rajkot | Saurashtra Calcareous Loam | N:58, P:64, K:165, pH:7.8, OC:0.52% | 🥜 Groundnut / મગફળી |
| 🌴 **Tamil Nadu** | Thanjavur | Cauvery Deltaic Alluvial Silt Clay | N:88, P:36, K:95, pH:6.7, OC:0.81% | 🌾 Rice / நெல் |
| 🌾 **West Bengal** | Bardhaman | Lower Gangetic Old Alluvial Clay Loam | N:95, P:32, K:88, pH:6.2, OC:0.78% | 🌾 Rice / আমন ধান |
| ☀️ **Rajasthan** | Jaipur | Semi-Arid Desert Light Sandy Loam | N:32, P:28, K:120, pH:8.2, OC:0.28% | 🌾 Mothbeans / मोठ |
| ☕ **Karnataka** | Dharwad | Western Ghats Red Laterite Loam | N:75, P:46, K:115, pH:6.4, OC:0.69% | 🌽 Maize / ಮೆಕ್ಕೆಜೋಳ |
| 🌾 **Uttar Pradesh** | Varanasi | Eastern Gangetic Silt Alluvial | N:82, P:52, K:68, pH:7.1, OC:0.61% | 🌾 Wheat / गेहूं |
| 🥥 **Kerala** | Palakkad | High-Rainfall Acidic Peaty Laterite | N:68, P:24, K:75, pH:5.4, OC:1.15% | 🥥 Coconut / തെങ്ങ് |

---

## 🌐 3. Multi-Lingual Architecture (11 Languages)

Kisaan_Sathi includes a **First-Launch Language Selection Modal** with an option to **Set as Default Language**:
1. 🇮🇳 **हिन्दी (Hindi)** — Default / National Standard
2. 🇬🇧 **English** — Standard / Agricultural Officers
3. 🚩 **मराठी (Marathi)** — Maharashtra
4. 🌾 **ਪੰਜਾਬੀ (Punjabi)** — Punjab & Haryana
5. 🌶️ **తెలుగు (Telugu)** — Andhra Pradesh & Telangana
6. 🌴 **தமிழ் (Tamil)** — Tamil Nadu
7. 🥜 **ગુજરાતી (Gujarati)** — Gujarat
8. 🌾 **বাংলা (Bengali)** — West Bengal
9. ☕ **ಕನ್ನಡ (Kannada)** — Karnataka
10. 🥥 **മലയാളം (Malayalam)** — Kerala
11. 🌾 **ଓଡ଼ିଆ (Odia)** — Odisha

---

## 🌟 4. Core System Features

### 1. 🌾 Explainable AI Crop Advisory (XGBoost + SHAP)
- Ingests **Soil N-P-K, pH, Organic Carbon, Rainfall, Temperature, Humidity, Farm Size, and Previous Crop**.
- 1-Click **Soil Health Card Presets** with instant live preview box displaying classification, farmer name, and nutrient pills.
- Ranks top 3 crops with 4-Pillar breakdowns: **Soil Fit, Weather Fit, Market Fit, and Crop Rotation Benefit**.
- Interactive **SHAP Force Vector Bars** show exact positive/negative nutrient drivers.
- Complete Farm Economics: Expected Yield/Acre, Estimated Revenue (₹), Sowing Window, and Mandi Rates.

### 2. 🌿 Plant Doctor (Leaf Disease Diagnostics)
- Instant pathology diagnosis for **Tomato Early Blight, Potato Late Blight, Cotton Angular Blight, Corn**, and custom leaf uploads.
- Dual treatment recommendations:
  - **🌿 Zero-Budget Organic**: Neem seed kernel extract (NSKE 5%), Trichoderma viride, Panchagavya.
  - **🧪 Scientific Chemical**: Mancozeb 75 WP, Ridomil MZ, Copper Oxychloride with exact dosage per litre.
- **🌦️ Weather-Aware Spray Warning**: Alerts farmers not to spray before forecasted rainfall.

### 3. 🎙️ Voice Saathi (Conversational LLM + Browser Audio TTS)
- Powered by **Groq LLaMA 3.3** for ultra-fast, respectful farming advice in all 11 Indian languages.
- Built-in **Text-to-Speech (TTS)** voice player that reads aloud answers in the selected regional language.
- Quick prompt chips for common farmer queries (*"पानी कब देना है?", "खाद की मात्रा?", "मंडी भाव क्या है?"*).

### 4. 📊 Live APMC Mandi Ticker & 7-Day Weather Radar
- Live animated APMC mandi prices for major Indian agricultural hubs.
- 7-day meteorological forecast from Open-Meteo with **Farming Spray Ratings** (*"Good for Spraying"*, *"Moderate - Spray after 4 PM"*, *"Avoid - Rain Expected"*).

### 5. 🗄️ Supabase PostgreSQL Anti-Sleep Engine
- Automated keep-alive heartbeat ping keeps Supabase active 24/7.
- Automatically stores farmer recommendation logs and disease scan histories.

---

## 📱 5. Mobile App Build Guide (Android Studio)

The mobile application is built with **Flutter 3.41 / Dart 3.11** inside the `agrisaathi_app/` directory.

### Building and Running in Android Studio:
1. Open **Android Studio**.
2. Click **Open** and select the folder: `c:\SmartIndiaHackathon\agrisaathi_app`.
3. Allow Android Studio to sync Gradle and dependencies.
4. Run `flutter pub get` in the terminal.
5. Select your connected Android device or Emulator.
6. Click **Run (`Shift + F10`)** or build an APK:
   ```bash
   cd agrisaathi_app
   flutter build apk --release
   ```

---

## 🚀 6. Web App Local Setup

### 1. Python Environment Setup
```bash
python -m venv venv
venv\Scripts\activate
pip install -r backend/requirements.txt
```

### 2. Start Local Server
```bash
python backend/run.py
```
Open **`http://localhost:8000`** in your browser to experience the full interactive dashboard.

---

## 🧪 7. Automated Testing & Verification

Run the comprehensive verification suite to test all 11 soil cards, regional endpoints, ML engines, and languages:
```bash
python backend/test_11_soils_and_languages.py
```
**Results: 42/42 tests passing with 100% success rate.**

---

## 👥 8. Author & Hackathon Team
- **Project**: Kisaan_Sathi (किसान साथी)
- **Repository**: [rajat9para/kisan_sathi-crop-prediction-through-ai-and-many-more-](https://github.com/rajat9para/kisan_sathi-crop-prediction-through-ai-and-many-more-)
- **Live Deployment**: [kisaansathi-iota.vercel.app](https://kisaansathi-iota.vercel.app/)
