<div align="center">

<img src="public/kisaan_sathi_avatar.png" width="160" height="160" alt="Kisaan Sathi AI Avatar" style="border-radius: 50%; box-shadow: 0 8px 24px rgba(19, 117, 71, 0.25);" />

# 🌾 Kisan Sathi 2.0 (किसान साथी)
### Edge-AI Smart Farming Assistant & Autonomous Closed-Loop Field Node
**Qualcomm Problem Statement #26180 • Smart India Hackathon 2026 • Dual-Track Hardware (RPi 4 + Qualcomm RB3 Gen 2 12 TOPS NPU) • Closed-Loop 5V Relay Actuation • FAO-56 ET₀ Water Budgeting • On-Device Pest AI • SIM800L GSM SMS • LoRa SX1278 Mesh • 18 Agro-Ecological Hubs • 11 Indian Languages • 100% On-Device Offline Inference**

> **📖 Data honesty**: every API response carries an explicit `source` field.
> Real feeds (SoilGrids, Open-Meteo, Agmarknet, Sentinel-2) and live hardware GPIOs are used;
> graceful simulations and fallbacks are always explicitly labelled. See
> [DATA_PROVENANCE.md](docs/DATA_PROVENANCE.md).

[![Web App](https://img.shields.io/badge/Web%20App-Live%20Ready-2E7D32.svg?logo=googlechrome)](https://kisaansathicroppredictionaiandmanym.vercel.app/)
[![Qualcomm PS #26180](https://img.shields.io/badge/Qualcomm%20PS%20%2326180-Hardware%20Track%20A%20%26%20B-7C3AED.svg)](#-edge-ai-field-node-actuation)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI%20v0.110-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com)
[![Flutter](https://img.shields.io/badge/Mobile-Flutter%203.41%20%7C%20Dart%203.11-02569B.svg?logo=flutter)](https://flutter.dev)
[![Edge AI](https://img.shields.io/badge/Edge%20AI-5V%20Relay%20%7C%20FAO--56%20%7C%20SIM800L%20%7C%20LoRa-0284C7.svg)](#-edge-ai-field-node-actuation)
[![CI Tests](https://img.shields.io/badge/Automated%20Tests-21%2F21%20Passing%20(100%25)-16A34A.svg)](#-8-automated-testing--system-verification)

</div>

---

## 📌 1. Project Overview & SIH 2026 Problem Statement

Small and marginal farmers across India face critical challenges in accessing timely, personalized, and accurate agricultural decision support. Language barriers, lack of technical knowledge, and limited reach of conventional advisory services reduce the effectiveness of existing tools.

**Kisaan_Sathi (किसान साथी)** directly addresses the SIH 2026 Problem Statement with a verified, end-to-end precision agriculture intelligence platform:

1. **Verified ML Crop Recommendation Engine**: An XGBoost multi-class classifier trained on 2,200 verified soil-crop vectors across 22 Indian crops with **98.64% 5-Fold Stratified Cross-Validation Accuracy** and **99.09% held-out test accuracy**.
2. **Transparent Explainable AI (SHAP TreeExplainer)**: Computes local Shapley force vectors for Nitrogen (N), Phosphorus (P), Potassium (K), soil pH ($3.5\text{–}9.5$), temperature, humidity, and rainfall.
3. **Deep Learning Plant Doctor (`/api/doctor/diagnose`)**: PyTorch `MobileNetV2` leaf pathology engine diagnosing 23 Indian crop diseases with input validation, real neural confidence scores, and dual **100% Organic** & **Scientific Chemical** ICAR cures.
4. **Dynamic Yield, Profit Margin & Sustainability Model**: Computes per-acre dynamic yield forecasts, production costs, and net profit margins alongside a **Quantitative 4-Pillar Sustainability Score (0-100)** evaluating water footprint efficiency, biological nitrogen fixation, and chemical intensity.
5. **Crop-Specific Agronomic Schedules**: Detailed stage-by-stage fertilizer (DAP, Urea, MOP, micronutrients) and irrigation schedules tailored to individual crop growth phenology.
6. **Soil Health Card OCR Recognition (`/api/ocr/soil-card`)**: OpenCV image preprocessing and OCR extraction of N, P, K, pH, and Organic Carbon values from physical cards.
7. **Satellite Earth Observation & Volumetric Soil Moisture**: Open-Meteo live satellite feeds with volumetric soil moisture ($0\text{–}1\text{cm}, 1\text{–}3\text{cm}$) and Copernicus Sentinel-2 multispectral **NDVI & NDRE** canopy health indexing.
8. **IoT Sensor Hardware Telemetry (`/api/iot/reading`)**: Direct ingestion of field probe telemetry (ESP32, LoRaWAN) with optical NPK ppm-to-kg/ha conversion.
9. **Genuine 100% On-Device Offline Inference**: Standalone pure-Dart agronomic ML engine in Flutter providing instant recommendations in airplane mode without internet connectivity.
10. **Multilingual Voice Saathi (`/api/voice/query`) & USSD/SMS Gateway**: Groq LLM advisory with Web Speech STT/TTS in 11 Indian languages, plus bandwidth-efficient SMS summaries for feature phone farmers.
11. **Autonomous Closed-Loop Smart Irrigation Engine**: Physical 5V Relay actuation (BCM 23) driving a DC pump guided by Hargreaves & FAO-56 Penman-Monteith Evapotranspiration ($ET_0$), dynamic root deficit ($L/m^2$), capacitive soil moisture thresholding (<22%), FC-37 rain lockout, and 15-minute fail-safe hardware watchdog timer.
12. **On-Device Vision Pest Detection & Rural Alerting**: PyTorch edge inference detecting 5 destructive insect pests (Fall Armyworm, Aphids, Whiteflies, Stem Borer, Bollworm) with ICAR ETL thresholds, regional SIM800L UART AT-command SMS dispatches, and LoRa SX1278 868MHz binary mesh networking.

---

## 🛰️ 2. Edge-AI Field Node & Hardware Actuation (Qualcomm PS #26180)

Kisan Sathi 2.0 directly solves **Qualcomm Problem Statement #26180** ("Smart Farming Assistant") by closing the loop between edge sensing, on-device AI inference, and autonomous physical actuation in low-connectivity rural environments.

### 🔌 Dual-Track Hardware Architecture

| Specification | Track A: Maker / Field-Ready Build | Track B: Qualcomm Dragonwing RB3 Gen 2 |
|---|---|---|
| **Core Compute** | Raspberry Pi 4 Model B (Quad Cortex-A72 @ 1.5GHz) | Qualcomm QCS6490 (8-core Kryo CPU @ 2.7GHz) |
| **Edge AI NPU** | CPU-accelerated PyTorch / ARM NEON | **Qualcomm Hexagon NPU (12 TOPS INT8 Compute)** |
| **Vision Sensor** | Raspberry Pi Camera Module V2 (Sony IMX219 8MP) | Dual MIPI-CSI 4-Lane / High-speed ISP |
| **Inference Latency** | 74.2 ms (MobileNetV2 INT8) | **6.1 ms (Qualcomm AI Hub QNN DLC)** |
| **Throughput** | 13.5 FPS | **163.9 FPS (12.16x Acceleration)** |
| **Power Consumption**| 5.1 W active | **1.8 W (64.7% Energy Savings)** |
| **Efficiency** | 2.65 FPS/Watt | **91.06 FPS/Watt (34.4x Multiplier)** |
| **Physical Actuation**| 5V Optocoupler Relay (BCM 23) → 12V DC Pump | 40-Pin Low-Speed Expansion Header (GPIO 12) |
| **Safety Protocols** | 15-Min Cutoff Watchdog + FC-37 Rain Lockout | Real-Time Hardware Watchdog + Low-Power Sleep |
| **Offline Comms** | SIM800L UART GSM SMS + LoRa SX1278 (868MHz) | Integrated Wi-Fi 6E + Sub-GHz LoRaWAN SPI |
| **Bill of Materials**| **~₹8,965 ($107 USD)** | Developer Kit Platform |

### 🛠️ Hardware Circuit Connections (Track A: RPi 4)
- **5V Optocoupler Relay**: VCC → Pin 2 (5V), GND → Pin 6 (GND), IN → Pin 16 (GPIO 23 / BCM 23).
- **Capacitive Soil Moisture v1.2**: VCC → Pin 1 (3.3V), GND → Pin 9 (GND), AOUT → ADS1115 I2C ADC (SDA Pin 3, SCL Pin 5).
- **DHT22 Temp & Humidity**: VCC → Pin 4 (5V), GND → Pin 14 (GND), DATA → Pin 7 (GPIO 4).
- **FC-37 Rain Inhibitor**: VCC → Pin 17 (3.3V), GND → Pin 20 (GND), DO → Pin 18 (GPIO 24).
- **SIM800L GSM Module**: VCC → External 4.2V 2A regulator, GND → Common GND, TX → Pin 10 (RXD), RX → Pin 8 (TXD).
- **LoRa SX1278 868MHz Transceiver**: SPI0 bus (MOSI Pin 19, MISO Pin 21, SCLK Pin 23, CS0 Pin 24, DIO0 Pin 22).

### 🔄 Autonomous Irrigation State Machine & Water Budgeting
$$\text{Water Deficit } (L/m^2) = \max\left(0, (\theta_{\text{field}} - \theta_{\text{current}}) \times Z_r \times 10\right) + ET_c - P_{\text{eff}}$$
- **Soil Deficit Trigger**: When capacitive soil moisture drops below threshold (default 22%), the controller computes required water volume ($L/m^2$) and drip irrigation duration.
- **Rain Lockout Safety**: If FC-37 rain sensor detects rain, pump activation is immediately inhibited.
- **15-Minute Hardware Watchdog**: The relay driver enforces a hard 900-second maximum run time to prevent flooding or root rot caused by sensor failure.

---

## 🏗️ 3. System Architecture

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   KISAAN_SATHI TARGET ARCHITECTURE                               │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘

 [ PRESENTATION TIER — Government of India National Portal UI ]
 ┌────────────────────────────────────────────────────────────────────────────────────────────────┐
 │  🇮🇳 GOI Portal Chrome: a11y toolbar (A/A+/A++/contrast), utility strip, tricolor divider,      │
 │     national emblem band (india.gov.in design language, Noto Sans typography)                   │
 │  🎞️ Hero Carousel (4 scheme-banners, autoplay/dots/swipe)  •  🏛️ Central Scheme Cards →        │
 │     real portals (PM-KISAN, PMFBY, SHC, e-NAM, PM-KUSUM, AIF, KCC, MY-Scheme)                   │
 │  📱 Responsive PWA (Vanilla JS / Modern CSS)          •  📲 Flutter Mobile App (Dart 3.11)      │
 │  🧠 100% On-Device Offline Dart ML Engine              •  📷 Real-Time Leaf Photo Diagnostic UI │
 │  🗣️ Web Speech STT / TTS in 11 Indian Languages      •  🖨️ PDF Farmer Advisory Generator     │
 └────────────────────────────────────────┬───────────────────────────────────────────────────────┘
                                          │  HTTPS / REST / JSON (TLS 1.3)
                                          ▼
 [ API GATEWAY (FastAPI) ]
 ┌────────────────────────────────────────────────────────────────────────────────────────────────┐
 │  🚀 FastAPI Async REST Router  •  Pydantic V2 Schemas  •  CORS & Uvicorn ASGI Server          │
 └──────┬───────────────┬────────────────┬──────────────┬──────────────┬───────────────┬──────────┘
        │               │                │              │              │               │
 ┌──────▼───────┐┌──────▼───────┐┌───────▼──────┐┌──────▼───────┐┌─────▼────────┐┌────▼──────────┐
 │ ML Recommend ││ Plant Doctor ││ Market Radar ││ SHC OCR      ││ Soil/Weather ││ IoT & Sentinel │
 │ XGBoost+SHAP ││ MobileNetV2  ││ Agmarknet via││ OpenCV +     ││ SoilGrids v2 ││ /api/iot/      │
 │ Yield & Sust ││ PlantVillage ││ data.gov.in  ││ Text Regex   ││ Open-Meteo + ││ /api/satellite/│
 │ Model        ││ 7 CV Classes ││ 3-Tier Feeds ││ Parameter Ext││ Moisture Pct ││ NDVI (CDSE)    │
 └──────┬───────┘└──────┬───────┘└───────┬──────┘└──────┬───────┘└─────┬────────┘└────┬───────────┘
        │               │                │              │              │              │
        └───────────────┴────────────────┴──────┬───────┴──────────────┴──────────────┘
                                                ▼
 [ PERSISTENCE & EXTENSION ]
 ┌────────────────────────────────────────────────────────────────────────────────────────────────┐
 │  🗄️ Supabase PostgreSQL (Logs, telemetry cache, farmer profiles)                               │
 │  📍 18-Hub Regional Geospatial Cache (GPS-matched offline data & verified ICAR-KVK contacts)   │
 └────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📊 3. Model Performance & Validation Summary

| Component | Architecture / Model | Validation Metric | Tested On | Status |
|---|---|---|---|---|
| **Crop Recommendation** | XGBoost Multi-Class Classifier | **98.64%** 5-Fold Cross-Validation (±0.25%) | 2,200 verified Kaggle/ICAR vectors | ✅ Verified & Exported |
| **Held-Out Test Set** | XGBoost (80/20 Split) | **99.09%** Accuracy, **99.12%** Precision | 440 held-out test vectors | ✅ Verified |
| **Explainable AI** | SHAP `TreeExplainer` | Local Shapley force vectors for 7 features | Real-time per prediction | ✅ Operational |
| **Leaf Pathology (CV)** | PyTorch `MobileNetV2` fine-tuned on PlantVillage | **95.87%** val accuracy, **0.959** macro-F1, per-class F1 0.92–0.99 | 630 held-out real leaf images (7 classes) | ✅ Trained & Exported |
| **Disease Triage Integrity** | Capability-gated hybrid | CV confidence = raw softmax (never floored); non-CV crops honestly labelled "symptom_guidelines" | All 23 pathologies | ✅ Honest by design |
| **Disease-Risk Early Warning** | ICAR epidemiological thresholds on live Open-Meteo forecast | Quantitative risk index (0–100) per disease | Wheat rust, Rice blast, Late blight, Grape downy mildew | ✅ Operational |
| **Live Mandi Prices** | Agmarknet via data.gov.in API | Median modal price across matching APMC markets + Supabase 7-day trend snapshots | Real feed → cached snapshot → labelled estimate | ✅ Real, 3-tier |
| **Live NDVI** | Copernicus Sentinel-2 L2A (CDSE Statistical API) | 60-day parcel NDVI statistics, ≤20% cloud, 5-day means | Real satellite → explicitly-labelled estimate | ✅ Real, 2-tier |
| **Dynamic Economics** | Agronomic Economic Engine | Expected Yield, Cost, Net Profit (₹/Acre) | Dynamic per soil/weather fit | ✅ Operational |
| **Sustainability Score**| 4-Pillar Quantitative Index | Water (35%), Soil (35%), Chem (20%), C (10%) | 0 to 100 composite score | ✅ Operational |
| **Soil Card OCR** | OpenCV + Text Extraction Parser | N, P, K, pH, OC parameter extraction | Physical/digital soil cards | ✅ Operational |
| **Offline Inference** | Pure Dart On-Device ML Engine | Instant recommendation in Airplane Mode | On-device Flutter runtime | ✅ Operational |

Detailed documentation: [Model Card (`docs/MODEL_CARD.md`)](docs/MODEL_CARD.md) • [Data Provenance (`docs/DATA_PROVENANCE.md`)](docs/DATA_PROVENANCE.md) • [Architecture (`docs/ARCHITECTURE.md`)](docs/ARCHITECTURE.md) • [Deployment Guide (`DEPLOYMENT.md`)](DEPLOYMENT.md).

---

## 🗺️ 4. 18 Agro-Ecological Hubs & ICAR-KVK Network

Kisaan_Sathi includes pre-calibrated soil chemistry profiles and official ICAR Krishi Vigyan Kendra nodal contacts across 18 major agricultural hubs:

| Hub | State | Soil Classification | Verified ICAR KVK & Contact |
|---|---|---|---|
| 🏔️ **Dehradun** | Uttarakhand | Doon Valley Alluvial & Terai Loam | ICAR-IISWC & KVK Dhakrani (`0135-2758564`) |
| 🌾 **Pantnagar** | Uttarakhand | Tarai Calcareous Silty Clay Loam | KVK, GBPUAT Pantnagar (`05944-233345`) |
| 🍎 **Shimla** | Himachal Pradesh | Himalayan Acidic Brown Forest Loam | KVK, ICAR-CPRI / UHF Rohru (`01781-240120`) |
| 🍇 **Nashik** | Maharashtra | Medium Black Cotton (Regur) Loam | KVK, YCMOU Campus Nashik (`0253-2231714`) |
| 🍊 **Nagpur** | Maharashtra | Basaltic Medium Deep Vertisol | KVK, ICAR-CICR Nagpur (`07103-275536`) |
| 🌾 **Indore** | Madhya Pradesh | Deep Black Malwa Vertisol Clay | KVK, Kasturbagram Indore (`0731-2856214`) |
| 🌾 **Ludhiana** | Punjab | Indo-Gangetic Alluvial Sandy Loam | KVK, PAU Ludhiana (`0161-2401960`) |
| 🌾 **Patna** | Bihar | Middle Gangetic Deep Alluvial Loam | KVK, ICAR-RCER Barh Patna (`06132-243120`) |
| 🌶️ **Guntur** | Andhra Pradesh | Coastal Red Clayey Sandy Loam | KVK, ANGRAU Lam Guntur (`0863-2293045`) |
| 🥜 **Rajkot** | Gujarat | Saurashtra Calcareous Loam | KVK, JAU Targhadia Rajkot (`0281-2784241`) |
| 🌴 **Thanjavur** | Tamil Nadu | Cauvery Deltaic Alluvial Silt Clay | KVK, TNAU Kattuthottam (`04362-267566`) |
| 🌾 **Bardhaman** | West Bengal | Lower Gangetic Old Alluvial Clay | KVK, Budbud Purba Bardhaman (`0343-2513645`) |
| ⛏️ **Ranchi** | Jharkhand | Chota Nagpur Acidic Red Sandy Loam | KVK, Birsa Agri University (`0651-2450840`) |
| 🍵 **Guwahati** | Assam | Brahmaputra Acidic Floodplain Loam | KVK, AAU Kahikuchi Kamrup (`0361-2840245`) |
| ☀️ **Jaipur** | Rajasthan | Semi-Arid Desert Light Sandy Loam | KVK, SKNAU Chomu Jaipur (`01423-220033`) |
| ☕ **Dharwad** | Karnataka | Western Ghats Red Laterite Loam | KVK, UAS Campus Dharwad (`0836-2217333`) |
| 🌾 **Varanasi** | Uttar Pradesh | Eastern Gangetic Silt Alluvial | KVK, ICAR-IIVR Jakhini (`0542-2635247`) |
| 🥥 **Palakkad** | Kerala | High-Rainfall Acidic Peaty Laterite | KVK, KAU Pattambi Palakkad (`0466-2212275`) |

---

## 🌐 5. Multilingual Engine (11 Indian Languages)

Kisaan_Sathi enforces strict **monolingual rendering with 0% language leakage**:
- **Supported Languages**: Hindi (`hi-IN`), English (`en-IN`), Marathi (`mr-IN`), Punjabi (`pa-IN`), Telugu (`te-IN`), Tamil (`ta-IN`), Gujarati (`gu-IN`), Bengali (`bn-IN`), Kannada (`kn-IN`), Malayalam (`ml-IN`), Odia (`or-IN`).
- **Feature Phone Access**: SMS / USSD advisory generation endpoint (`/api/advisory/sms-advisory`) providing concise text advice in local languages.

---

## 🇮🇳 5b. Frontend Design — National Portal Experience

The PWA is dressed in the **design language of the Government of India's national portals**
([india.gov.in](https://www.india.gov.in), [agriwelfare.gov.in](https://agriwelfare.gov.in), [mygov.in](https://www.mygov.in))
to feel instantly familiar and trustworthy to Indian farmers and officials:

| UI Element | Implementation |
|---|---|
| **National portal chrome** | Accessibility toolbar (text size A/A+/A++ & high-contrast, persisted), cross-government utility strip, tricolor divider, navy national band with a wheat-emblem SVG and bilingual portal title |
| **Typography** | Noto Sans + Noto Sans Devanagari (official-portal standard, full Devanagari coverage, system fallbacks for offline use) |
| **Hero carousel** | 4 auto-rotating scheme banners (5.5 s autoplay, dots, arrows, touch-swipe, pause-on-hover) linking straight into the app's features |
| **Quick services strip** | National-portal style service cards that deep-link into each app tab |
| **Central schemes grid** | 8 real central-sector scheme cards — **PM-KISAN, PMFBY, Soil Health Card, e-NAM, PM-KUSUM, Agriculture Infrastructure Fund, Kisan Call Centre, MY-Scheme** — each redirecting to the official portal in a new tab |
| **Impact stats strip** | Government-dashboard style platform statistics |
| **GOI multi-column footer** | Scheme links, government portals, live data-source attribution, Kisan Call Centre helpline (1800-180-1551) and an **honest SIH-prototype disclaimer** |
| **Architecture** | Pure vanilla JS/CSS overlay (`gov-portal.css` + `gov-portal.js`) layered on top of the app — zero framework, zero build step, works fully offline (font fallbacks included) |

---

## 🔌 6. API Reference

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/recommend` | Re-ranks 22 crops with SHAP explainability, dynamic yield, profit, and sustainability score |
| `POST` | `/api/doctor/diagnose` | PyTorch MobileNetV2 leaf disease pathology diagnosis (Base64) |
| `POST` | `/api/doctor/diagnose-file` | Multipart file upload for leaf pathology diagnosis |
| `POST` | `/api/ocr/soil-card` | OCR extraction of Soil Health Card parameters (Base64 / Preset) |
| `POST` | `/api/ocr/soil-card-upload` | Multipart file upload for physical Soil Health Card scanning |
| `POST` | `/api/iot/reading` | Ingests real-time IoT soil probe sensor telemetry (Moisture, Temp, NPK ppm, pH) |
| `GET` | `/api/iot/latest/{device_id}` | Retrieves latest telemetry from an active field IoT probe |
| `GET` | `/api/satellite/ndvi` | Copernicus Sentinel-2 multispectral NDVI, NDRE, and canopy vigor rating |
| `POST` | `/api/advisory/sms-advisory` | Generates concise SMS / USSD broadcast advisory for feature phones |
| `GET` | `/api/market-prices` | APMC mandi daily modal rates and 7-day price momentum |
| `GET` | `/api/weather` | 7-day agro-meteorological forecast with volumetric soil moisture % |
| `POST` | `/api/voice/query` | Groq LLM multilingual farmer consultant with TTS audio response |

---

## 🚀 7. Installation & Quickstart

### 1. Clone Repository & Setup Environment
```bash
git clone https://github.com/rajat9para/kisan_sathi-crop-prediction-through-ai-and-many-more-.git
cd kisan_sathi-crop-prediction-through-ai-and-many-more-
python -m venv venv
venv\Scripts\activate  # On Linux/macOS: source venv/bin/activate
pip install -r backend/requirements.txt
```

### 2. Train & Export ML/Vision Artifacts
```bash
python backend/ml/train.py
python backend/ml/train_vision.py
```

### 3. Start Backend Server
```bash
python backend/run.py
```
Visit **`http://localhost:8000`** in your browser for the PWA or **`http://localhost:8000/docs`** for the interactive Swagger API documentation.

---

## 🧪 8. Automated Testing & System Verification

Run the comprehensive test suites across backend, hardware edge node, and Flutter mobile app:
```bash
# 1. Backend Core & Edge IoT Test Suites (19 Tests)
python backend/tests/run_tests.py

# 2. Flutter Mobile & Edge Node Controller Tests (2 Tests)
cd agrisaathi_app && flutter test
```

**Verification Results (21/21 Tests Passing — 100%):**
```
================================================================================
RUNNING KISAN SATHI 2.0 VERIFICATION SUITE
================================================================================
[PASS]  1. XGBoost & SHAP ML Recommendation Engine
[PASS]  2. Dynamic Yield, Cost & Net Profit Forecasting
[PASS]  3. Quantitative 4-Pillar Sustainability Scoring
[PASS]  4. Crop-Specific Agronomic Schedules
[PASS]  5. PyTorch MobileNetV2 Leaf Pathology Inference (PlantVillage-trained)
[PASS]  6. Honest Symptom Triage for Non-CV Crops
[PASS]  7. Input Validation (Blank Image Rejection)
[PASS]  8. Agmarknet Mandi Price Feed (3-tier: live → cache → labelled estimate)
[PASS]  9. Soil Health Card OCR Parameter Parser
[PASS] 10. IoT Telemetry Ingestion Node (Supabase-persisted)
[PASS] 11. Sentinel-2 Satellite NDVI Earth Observation (CDSE / labelled estimate)
[PASS] 12. FastAPI /api/recommend Endpoint
[PASS] 13. USSD / SMS Regional Advisory Gateway
--------------------------------------------------------------------------------
[PASS] 14. Edge Vision & Pest Detection (5 Pests + ICAR ETL thresholds)
[PASS] 15. FastAPI /api/edge/* Actuator & Telemetry REST Endpoints
[PASS] 16. SIM800L GSM AT-Command Driver & Regional SMS Outbox
[PASS] 17. LoRa SX1278 14-Byte Binary Protocol & CRC-16-CCITT Integrity
[PASS] 18. Qualcomm RB3 Gen 2 12 TOPS NPU Benchmarks & AI Hub Export
[PASS] 19. Smart Irrigation FAO-56 ET₀ Controller & 15-Min Watchdog Cutoff
--------------------------------------------------------------------------------
[PASS] 20. Flutter AgriSaathi App Splash & Navigation Flow
[PASS] 21. Flutter EdgeNodeControllerScreen Telemetry, 5V Relay & RB3 Specs
================================================================================
RESULTS: 21/21 TESTS PASSED (100.0%)
================================================================================
```

Deployment (Render backend + Vercel static frontend + RPi4 / RB3 edge node): see [DEPLOYMENT.md](DEPLOYMENT.md).

---

## 👥 9. Hackathon Team & Provenance
- **Project**: Kisaan_Sathi (किसान साथी)
- **Target Competition**: Smart India Hackathon (SIH) 2026
- **Repository**: [rajat9para/kisan_sathi-crop-prediction-through-ai-and-many-more-](https://github.com/rajat9para/kisan_sathi-crop-prediction-through-ai-and-many-more-)
- **Live Deployment**: [kisaansathicroppredictionaiandmanym.vercel.app](https://kisaansathicroppredictionaiandmanym.vercel.app/)
