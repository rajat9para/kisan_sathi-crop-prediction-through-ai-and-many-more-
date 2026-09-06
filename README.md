# 🌾 Kisan Sathi 2.0 (किसान साथी)
### Edge-AI Smart Farming Assistant & Autonomous Closed-Loop Field Node
**Target:** Smart India Hackathon (SIH 2026) | **Problem Statement:** #26180  
**Category:** Hardware | **Theme:** Agriculture, FoodTech & Rural Development  
**Hardware Build:** **Field-Deployable Raspberry Pi 4 Model B Maker Prototype (₹9,850 INR / ~$118 USD)**

---

## 📑 Table of Contents
- [1. Hackathon Overview & Problem Statement #26180](#1-hackathon-overview--problem-statement-26180)
- [2. System Architecture & End-to-End Dataflow](#2-system-architecture--end-to-end-dataflow)
- [3. Things Needed to Build the Project (Hardware BOM & Costs)](#3-things-needed-to-build-the-project-hardware-bom--costs)
- [4. Hardware Wiring & Pin Interconnect Guide](#4-hardware-wiring--pin-interconnect-guide)
- [5. How the System Works & Key Features](#5-how-the-system-works--key-features)
  - [5.1 Closed-Loop Smart Irrigation & 15-Minute Watchdog](#51-closed-loop-smart-irrigation--15-minute-watchdog)
  - [5.2 On-Device Vision, Quality Gating & Pest AI](#52-on-device-vision-quality-gating--pest-ai)
  - [5.3 Multi-Factor Environmental Risk & Bilingual Micro-Alerts](#53-multi-factor-environmental-risk--bilingual-micro-alerts)
  - [5.4 Zero-Internet Rural Redundancy (SIM800L SMS & LoRa Mesh)](#54-zero-internet-rural-redundancy-sim800l-sms--lora-mesh)
  - [5.5 Transparent Explainable AI (XGBoost + SHAP)](#55-transparent-explainable-ai-xgboost--shap)
  - [5.6 18-Hub ICAR Krishi Vigyan Kendra (KVK) Network](#56-18-hub-icar-krishi-vigyan-kendra-kvk-network)
- [6. How to Start, Operate, Control & Stop the Project](#6-how-to-start-operate-control--stop-the-project)
  - [6.1 Installation & Setup](#61-installation--setup)
  - [6.2 Starting the Edge Daemon (Autonomous Field Loop)](#62-starting-the-edge-daemon-autonomous-field-loop)
  - [6.3 Starting the Backend & Web Dashboard](#63-starting-the-backend--web-dashboard)
  - [6.4 Operating & Controlling via Web Dashboard](#64-operating--controlling-via-web-dashboard)
  - [6.5 Operating via Flutter Mobile Application](#65-operating-via-flutter-mobile-application)
  - [6.6 How to Safely Stop the Project](#66-how-to-safely-stop-the-project)
- [7. Automated Verification & Testing Suite (18/18 Passing)](#7-automated-verification--testing-suite-1818-passing)
- [8. Repository Structure](#8-repository-structure)
- [9. Deep Architectural Documentation](#9-deep-architectural-documentation)

---

## 1. Hackathon Overview & Problem Statement #26180

**Problem Statement #26180** calls for a **field-deployable smart farming assistant** that improves agricultural productivity, water stewardship, and rural resilience under unpredictable climatic conditions.

Most hackathon solutions present passive software forms that depend on continuous cloud connectivity and provide only generic text tips. **Kisan Sathi 2.0** replaces this with an **autonomous cyber-physical edge station**:
- **Senses** physical soil moisture, microclimate, and precipitation via dedicated hardware buses.
- **Filters & Gates** camera frames using Laplacian blur checks and green chromaticity ratios.
- **Infers** plant pathology and agricultural pest infestations locally using **ONNX MobileNetV2** directly on ARM CPU.
- **Decides** exact volumetric crop water demand via **FAO-56 Hargreaves evapotranspiration math**.
- **Actuates** a physical 12V irrigation pump via an optocoupled relay protected by an autonomous **15-minute fail-safe hardware watchdog**.
- **Alerts** smallholders via **Devanagari Hindi SMS (SIM800L)** and **868MHz LoRa mesh packets** when off the grid.
- **Escalates** severe agricultural anomalies directly to scientists across **18 Regional ICAR Krishi Vigyan Kendras (KVKs)**.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          CYBER-PHYSICAL FEEDBACK CYCLE                                 │
│                                                                                        │
│   ┌────────────────┐      ┌────────────────┐      ┌────────────────┐                   │
│   │ 1. SENSE       │ ───► │ 2. INFER       │ ───► │ 3. DECIDE      │                   │
│   │ Capacitive VWC │      │ ONNX MobileNet │      │ FAO-56 ET₀     │                   │
│   │ DHT22 & Rain   │      │ 5 Pests + 23 Dx│      │ Risk Engines   │                   │
│   └────────────────┘      └────────────────┘      └───────┬────────┘                   │
│                                                           │                            │
│                                                           ▼                            │
│   ┌────────────────┐      ┌────────────────┐      ┌────────────────┐                   │
│   │ 6. ESCALATE    │ ◄─── │ 5. ALERT       │ ◄─── │ 4. ACTUATE     │                   │
│   │ 18 ICAR KVKs   │      │ SMS (SIM800L)  │      │ 5V Relay, Pump │                   │
│   │ WhatsApp / PDF │      │ LoRa 868MHz    │      │ 15-Min Cutoff  │                   │
│   └────────────────┘      └────────────────┘      └────────────────┘                   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. System Architecture & End-to-End Dataflow

```
 ┌───────────────────────────────────────────────────────────────────────────────────────────┐
 │                                   1. PHYSICAL SENSING LAYER                               │
 │                                                                                           │
 │   Capacitive Soil Probe          DHT22 Temp & Humidity          FC-37 Rain Comparator     │
 │   (Analog 1.2V - 3.0V)           (1-Wire Digital GPIO 4)        (Digital Active-LOW Pin)  │
 │            │                               │                               │              │
 │            ▼                               │                               │              │
 │   ADS1115 16-Bit I2C ADC                   │                               │              │
 │            │                               │                               │              │
 └────────────┼───────────────────────────────┼───────────────────────────────┼──────────────┘
              │ I2C Bus (Pins 3 & 5)          │ Single-Bus (Pin 7)            │ GPIO 27 (Pin 13)
              ▼                               ▼                               ▼
 ┌───────────────────────────────────────────────────────────────────────────────────────────┐
 │                   2. EDGE COMPUTING LAYER (Raspberry Pi 4 Model B)                        │
 │                                                                                           │
 │  ┌─────────────────────────────────────────────────────────────────────────────────────┐  │
 │  │                         edge_daemon.py Autonomous Loop                              │  │
 │  │                                                                                     │  │
 │  │   ┌───────────────────────┐   ┌────────────────────────┐   ┌────────────────────┐   │  │
 │  │   │ smart_irrigation.py   │   │ environmental_risk.py  │   │ alert_engine.py    │   │  │
 │  │   │ - FAO-56 Hargreaves   │──►│ - Drought Risk (0-100) │──►│ - Bilingual alerts │   │  │
 │  │   │ - Deficit Calculation │   │ - Flood Risk (0-100)   │   │ - English / Hindi  │   │  │
 │  │   │ - 15-Min Cutoff Guard │   │ - Heat Stress (0-100)  │   │ - Actionable tips  │   │  │
 │  │   └───────────┬───────────┘   │ - Pathogen Favor (0-100│   └──────────┬─────────┘   │  │
 │  │               │               └────────────────────────┘              │             │  │
 │  │               ▼                                                       │             │  │
 │  │   ┌───────────────────────┐                                           │             │  │
 │  │   │ vision_detector.py    │                                           │             │  │
 │  │   │ - Laplacian Blur Gate │                                           │             │  │
 │  │   │ - Green Chroma Gate   │                                           │             │  │
 │  │   │ - ONNX MobileNetV2    │                                           │             │  │
 │  │   │ - 5 Pests + ICAR ETL  │                                           │             │  │
 │  │   └───────────────────────┘                                           │             │  │
 │  └───────────────────────────────────────┬───────────────────────────────┼─────────────┘  │
 └──────────────────────────────────────────┼───────────────────────────────┼────────────────┘
                                            │                               │
                                            ▼                               ▼
 ┌───────────────────────────────────────────────────────┐   ┌───────────────────────────────┐
 │              3. PHYSICAL ACTUATION LAYER              │   │   4. ZERO-INTERNET TELEMETRY  │
 │                                                       │   │                               │
 │   GPIO 17 (Pin 11) Active-LOW                         │   │   SIM800L GSM Module (UART0)  │
 │   5V Optocoupled Relay Module                         │   │   - Devanagari Hindi SMS      │
 │   Switches 12V Rail to R385 Diaphragm Pump            │   │   Reyax LoRa SX1278 (868 MHz) │
 │   Hardware Cutoff enforces <= 15.0 minutes runtime    │   │   - 14-Byte Binary Packets    │
 └───────────────────────────────────────────────────────┘   └───────────────────────────────┘
```

---

## 3. Things Needed to Build the Project (Hardware BOM & Costs)

The physical prototype is constructed from off-the-shelf, cost-effective components readily available in India:

| # | Component Name | Model / Specification | Interface / Pinout | Qty | Price (INR) | Price (USD) |
|---|---|---|---|:---:|:---:|:---:|
| 1 | **Single-Board Computer** | Raspberry Pi 4 Model B (4GB) | 40-Pin GPIO Header | 1 | ₹4,200 | $50.50 |
| 2 | **High-Precision ADC** | ADS1115 16-Bit I2C ADC Module | I2C (Address `0x48`) | 1 | ₹280 | $3.35 |
| 3 | **Corrosion-Proof Soil Probe** | Capacitive Soil Moisture v1.2 | Analog Out (1.2V–3.0V) | 1 | ₹180 | $2.15 |
| 4 | **Ambient Temp & Humidity** | DHT22 (AM2302) Digital Sensor | 1-Wire Digital (GPIO 4) | 1 | ₹320 | $3.85 |
| 5 | **Rain Conduction Sensor** | FC-37 Rain Plate + LM393 | Digital Out (GPIO 27) | 1 | ₹110 | $1.30 |
| 6 | **Actuation Relay** | 5V 1-Channel Optocoupled Relay | Active-LOW (GPIO 17) | 1 | ₹120 | $1.45 |
| 7 | **Irrigation Water Pump** | 12V DC R385 Diaphragm Pump | Switched by Relay | 1 | ₹450 | $5.40 |
| 8 | **Cellular Modem** | SIM800L GSM / GPRS Module | UART0 (GPIO 14/15) | 1 | ₹680 | $8.20 |
| 9 | **Sub-GHz RF Transceiver** | Reyax RYLR896 LoRa (SX1278) | SPI0 / UART (868 MHz) | 1 | ₹1,250 | $15.00 |
| 10 | **Solar PV Panel** | 20W 18V Monocrystalline Panel | Screw Terminals to MPPT | 1 | ₹1,100 | $13.25 |
| 11 | **Solar Charge Controller** | 10A 12V PWM with Dual USB | Battery & Panel Terminals | 1 | ₹380 | $4.55 |
| 12 | **Deep-Cycle Battery** | 12V 7Ah VRLA Lead-Acid Battery | Faston F1 Terminals | 1 | ₹790 | $9.50 |
| 13 | **DC-DC Step-Down Buck** | LM2596 Dual Rail (5V & 4.2V) | Screw Terminals | 2 | ₹190 | $2.30 |
| 14 | **Weatherproof Enclosure** | IP65 ABS Junction Box + Glands | Wall Mount | 1 | ₹450 | $5.40 |
| **Total** | **Complete Core Field Node** | | | | **₹9,850** | **~$118 USD** |

---

## 4. Hardware Wiring & Pin Interconnect Guide

### Raspberry Pi 4 (40-Pin Header) Connection Table

| RPi 4 Pin # | Pin Name / BCM | Wire Color | Connected Component & Pin | Functional Description |
|---|---|---|---|---|
| **Pin 1** | `+3.3V Power` | Red | DHT22 `Pin 1 (VCC)` & Probe `VCC` | Clean 3.3V sensor supply |
| **Pin 2** | `+5.0V Power` | Red | Relay `VCC` & ADS1115 `VDD` | 5V actuator & ADC rail |
| **Pin 3** | `GPIO 2 (I2C1 SDA)`| Green | ADS1115 `SDA` Pin | I2C Serial Data line |
| **Pin 5** | `GPIO 3 (I2C1 SCL)`| Yellow | ADS1115 `SCL` Pin | I2C Serial Clock line |
| **Pin 6** | `GND (Ground)` | Black | System Star Common Ground | Common DC Reference |
| **Pin 7** | `GPIO 4 (GPCLK0)` | Blue | DHT22 `Pin 2 (DATA)` (4.7kΩ pullup) | 1-Wire Microclimate Bus |
| **Pin 8** | `GPIO 14 (UART TX)`| Orange | SIM800L `RXD` (via 1k/2k divider) | Serial AT-Command Out |
| **Pin 10**| `GPIO 15 (UART RX)`| Brown | SIM800L `TXD` Pin | Serial Response In |
| **Pin 11**| `GPIO 17` | White | 5V Relay Module `IN` Pin | **Pump Control (Active-LOW)** |
| **Pin 13**| `GPIO 27` | Grey | FC-37 Rain Detector `DO` Pin | **Rain Sensing (Active-LOW)**|
| **Pin 19**| `GPIO 10 (MOSI)` | Purple | LoRa SX1278 `MOSI` Pin | SPI Master Out |
| **Pin 21**| `GPIO 9 (MISO)` | Blue | LoRa SX1278 `MISO` Pin | SPI Master In |
| **Pin 23**| `GPIO 11 (SCLK)` | Yellow | LoRa SX1278 `SCK` Pin | SPI Clock |
| **Pin 24**| `GPIO 8 (CE0)` | Green | LoRa SX1278 `NSS` (Chip Select) | SPI Slave Select |
| **Pin 22**| `GPIO 25` | Orange | LoRa SX1278 `RST` Pin | Hardware Reset |

### Actuation & Power Wiring Schematic

```
   12V Battery (+) ────────► Charge Controller Battery (+)
   12V Battery (-) ────────► System Star Common Ground (-)

   [ Actuation Relay Circuit ]
   5V Relay COM (Common)   ◄─── +12V DC Rail
   5V Relay NO (Norm Open) ───► 12V DC Pump (+)
   12V DC Pump (-)         ───► Common Star Ground (-)
   5V Relay IN             ◄─── RPi 4 Pin 11 (GPIO 17)
   5V Relay VCC            ◄─── RPi 4 Pin 2 (+5V)
   5V Relay GND            ◄─── RPi 4 Pin 6 (GND)

   [ ADS1115 & Moisture Probe Circuit ]
   ADS1115 VDD             ◄─── +5V (RPi Pin 2)
   ADS1115 GND             ◄─── GND (RPi Pin 6)
   ADS1115 SDA             ◄─── GPIO 2 (RPi Pin 3)
   ADS1115 SCL             ◄─── GPIO 3 (RPi Pin 5)
   Capacitive Probe VCC    ◄─── +3.3V (RPi Pin 1)
   Capacitive Probe GND    ◄─── GND (RPi Pin 9)
   Capacitive Probe AOUT   ───► ADS1115 Channel A0
```

---

## 5. How the System Works & Key Features

### 5.1 Closed-Loop Smart Irrigation & 15-Minute Watchdog
- **Agronomic Math**: Computes reference evapotranspiration ($ET_0$) via the **FAO-56 Hargreaves model** and scales by crop growth stage coefficients ($ET_c = K_c \times ET_0$).
- **Volumetric Deficit ($D_{\text{soil}}$)**: Converts ADS1115 voltage ($1.2\text{V} - 3.0\text{V}$) to soil moisture percentage, calculating exact liters required per square meter.
- **Hardware Rain Lockout**: If rain is detected by the FC-37 sensor, the pump is immediately turned OFF and disabled.
- **15-Minute Fail-Safe Watchdog**: A strict automatic timer shuts off the pump if it runs continuously for $\ge 15.0$ minutes, preventing pump burnout, borehole depletion, or waterlogging.

### 5.2 On-Device Vision, Quality Gating & Pest AI
- **Quality Gates**: Computes **Laplacian blur variance** ($\sigma^2 < 100$ flags motion blur) and **green-chromaticity ratio** ($\ge 12\%$ validates leaf foliage).
- **ONNX MobileNetV2**: Runs on-device inference for 7 foliar diseases with 95.87% validation accuracy (~32ms on RPi 4 CPU).
- **5 Major Indian Pests with ICAR ETLs**: Fall Armyworm, Cotton Aphid, Whitefly Vector, Yellow Stem Borer, and Cotton Bollworm with biological and chemical control remedies.

### 5.3 Multi-Factor Environmental Risk & Bilingual Micro-Alerts
- Computes four distinct agricultural indices: **Drought Deficit**, **Flood & Waterlogging**, **Canopy Heat Stress**, and **Fungal Pathogen Outbreak**, producing a composite 0–100 Farm Vulnerability Score.
- Synthesizes structured, bilingual micro-alerts in English and Hindi for immediate action on feature phones.

### 5.4 Zero-Internet Rural Redundancy (SIM800L SMS & LoRa Mesh)
- **SIM800L GSM Module**: Sends automated Devanagari Hindi SMS directly to the farmer's phone via UART AT-commands.
- **Reyax LoRa SX1278 Radio**: Broadcasts 14-byte binary telemetry packets validated with **CRC-16-CCITT** over an 868MHz local mesh network.

### 5.5 Transparent Explainable AI (XGBoost + SHAP)
- Multi-class crop recommender trained on 2,200 verified vectors achieves **99.09% accuracy**.
- **SHAP TreeExplainer**: Computes exact log-odds attributions for every feature ($N, P, K, \text{pH}, \text{temp}, \text{humidity}, \text{rainfall}$), showing farmers *why* each crop was recommended.

### 5.6 18-Hub ICAR Krishi Vigyan Kendra (KVK) Network
- Integrated with 18 agro-ecological extension centers across India, providing verified scientist contact details, soil typologies, and one-tap WhatsApp diagnostic escalation.

---

## 6. How to Start, Operate, Control & Stop the Project

### 6.1 Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/rajat9para/kisan_sathi-crop-prediction-through-ai-and-many-more-.git
cd kisan_sathi-crop-prediction-through-ai-and-many-more-

# 2. Set up virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux / Raspberry Pi:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
pip install -r edge_node/requirements-edge.txt
```

---

### 6.2 Starting the Edge Daemon (Autonomous Field Loop)

The Edge Daemon continuously acquires sensor data, evaluates irrigation demand, enforces safety limits, and dispatches telemetry.

```bash
# Run continuous autonomous monitoring for Tomato crop:
python edge_node/edge_daemon.py --crop tomato --interval 3.0 --phone +919876543210
```

#### Running Standalone Diagnostic Modes
```bash
# 1. Execute a single cycle and print diagnostics:
python edge_node/edge_daemon.py --once

# 2. Test physical sensors, ADS1115 ADC, and pump actuation:
python edge_node/smart_irrigation.py --eval

# 3. Test camera quality gates, pest classification & ONNX inference:
python edge_node/vision_detector.py --test

# 4. Test environmental risk scoring engines:
python edge_node/environmental_risk.py --test
```

---

### 6.3 Starting the Backend & Web Dashboard

Launch the FastAPI backend server (which also serves the web frontend):

```bash
python backend/run.py
```
- Open browser at: **`http://localhost:8000`**
- Interactive REST API Docs: **`http://localhost:8000/docs`**

---

### 6.4 Operating & Controlling via Web Dashboard

Open `http://localhost:8000` in your web browser:

1. **Edge Field Node Tab (Raspberry Pi 4 Maker Prototype)**:
   - **Telemetry HUD**: View real-time Volumetric Soil Moisture (%), Ambient Temperature (°C), Relative Humidity (%), and Rain Conduction Sensor status.
   - **Manual Relay Override**: Click **`⚡ Toggle Pump Relay`** to immediately engage or disengage the physical pump relay.
   - **Autonomous Mode Switch**: Toggle between Closed-Loop Automatic Irrigation and Manual Override.
   - **Environmental Risk Deck**: Monitor real-time Drought, Flood, Heat Stress, and Pathogen Outbreak risk scores.
   - **Bilingual Alerts Banner**: View live actionable alerts in English and Hindi.
   - **Farm Analytics**: Review 7-day soil moisture trends, water savings (liters), and electricity conserved (kWh).

2. **Crop Advisory Tab**:
   - Select your farm location or choose from 18 Regional Hubs.
   - View top recommended crops, expected yield, costs, and net profits.
   - Inspect the interactive **SHAP waterfall chart** explaining the feature contributions.

3. **Plant Doctor Tab**:
   - Upload or capture a leaf photo.
   - View disease diagnosis, confidence, and ICAR-verified biological/chemical remedies.

4. **Voice Saathi Tab**:
   - Voice assistant supporting Hindi, Punjabi, Marathi, Telugu, Tamil, and English.

5. **APMC Mandi Radar Tab**:
   - Real-time commodity market prices and trend charts fetched from data.gov.in.

---

### 6.5 Operating via Flutter Mobile Application

```bash
cd agrisaathi_app
flutter pub get
flutter run
```
- Provides 100% on-device pure-Dart agronomic ML for zero-connectivity field operations.

---

### 6.6 How to Safely Stop the Project

- **Stopping the Edge Daemon**: Press `Ctrl + C` in the running terminal. The daemon catches `SIGINT`, immediately de-energizes the 5V relay (setting GPIO 17 `HIGH`), cleans up all GPIO resources, and exits cleanly.
- **Stopping Systemd Service**:
  ```bash
  sudo systemctl stop kisan-edge
  ```
- **Stopping Backend Server**: Press `Ctrl + C` in the backend terminal.
- **Emergency Hardware Cutoff**: Disconnect the 12V battery line or trigger the 15-minute software watchdog cutoff.

---

## 7. Automated Verification & Testing Suite (18/18 Passing)

Execute the complete end-to-end verification suite:

```bash
python backend/tests/run_tests.py
```

```
==========================================
RUNNING SUITE: Backend Core Services & APIs
==========================================
  [PASS] test_apmc_market_prices
  [PASS] test_crop_specific_management_schedules
  [PASS] test_dynamic_yield_and_net_profit_forecasting
  [PASS] test_fastapi_advisory_recommend_endpoint
  [PASS] test_fastapi_sms_advisory_endpoint
  [PASS] test_iot_telemetry_endpoint
  [PASS] test_leaf_classifier_rejects_blank_image
  [PASS] test_ml_engine_loaded_and_recommends
  [PASS] test_ocr_parameter_parser
  [PASS] test_pytorch_leaf_pathology_classifier_valid_image
  [PASS] test_satellite_ndvi_service
  [PASS] test_sustainability_score_calculation
  [PASS] test_symptom_triage_for_crops_without_cv_data
Suite Backend Core Services & APIs: 13 passed, 0 failed

==========================================
RUNNING SUITE: Edge Node Hardware & IoT Services
==========================================
  [PASS] test_edge_vision_and_pests
  [PASS] test_fastapi_edge_endpoints
  [PASS] test_gsm_sms_dispatcher
  [PASS] test_lora_mesh_protocol
  [PASS] test_smart_irrigation_controller
Suite Edge Node Hardware & IoT Services: 5 passed, 0 failed

TOTAL: 18 passed, 0 failed (100% SUCCESS RATE)
```

---

## 8. Repository Structure

```
kisan_sathi/
├── edge_node/                       # Edge Hardware Daemon & Drivers (Raspberry Pi 4)
│   ├── edge_daemon.py               # Main autonomous monitoring & actuation loop
│   ├── smart_irrigation.py          # ADS1115 ADC driver, FAO-56 ET₀, 15-min watchdog
│   ├── vision_detector.py           # ONNX MobileNetV2, blur gate, 5 insect pests
│   ├── environmental_risk.py        # Drought, flood, heat, and disease risk engines
│   ├── alert_engine.py              # Structured bilingual micro-alerts generator
│   ├── gsm_sms.py                   # SIM800L UART Devanagari Hindi SMS driver
│   └── lora_mesh.py                 # LoRa SX1278 14-byte binary mesh protocol
│
├── backend/                         # FastAPI REST Microservices & ML Pipelines
│   ├── app/
│   │   ├── main.py                  # API routes, CORS, static UI mounts
│   │   ├── routers/edge.py          # Edge telemetry, actuation & risk endpoints
│   │   └── services/ml_engine.py    # XGBoost + SHAP TreeExplainer engine
│   └── ml/
│       ├── export_edge_models.py    # ONNX export & INT8 quantization pipeline
│       └── artifacts/               # Serialized ONNX, PyTorch, and benchmark files
│
├── public/                          # National Portal Web UI (HTML5 / CSS3 / ES6)
│   ├── index.html                   # Edge HUD, advisory, pathology, mandi tabs
│   ├── app.js                       # Live telemetry polling, relay toggle logic
│   └── style.css                    # Responsive HUD and national portal styling
│
├── hardware/
│   └── BOM.md                       # Complete Bill of Materials and electrical schematics
│
├── docs/
│   ├── kvk_network.md               # 18-Hub ICAR Regional Extension Directory
│   ├── ARCHITECTURE.md              # Software architecture & dataflow contracts
│   └── MODEL_CARD.md                # ML and Computer Vision specifications
│
├── agrisaathi_app/                  # Flutter Cross-Platform Mobile Application
├── THIS_PROJECT_INFO.md             # Master Encyclopedic Technical Reference
└── README.md                        # Primary Project Documentation
```

---

## 9. Deep Architectural Documentation

For the exhaustive technical reference manual covering exact mathematical proofs, competitive matrices, complete pinout schematics, and deep agronomic formulations, consult:

👉 **[THIS_PROJECT_INFO.md](file:///c:/SmartIndiaHackathon/THIS_PROJECT_INFO.md)**  
👉 **[Hardware Bill of Materials (BOM.md)](file:///c:/SmartIndiaHackathon/hardware/BOM.md)**  
👉 **[ICAR KVK Regional Directory (kvk_network.md)](file:///c:/SmartIndiaHackathon/docs/kvk_network.md)**

---

*Authored for the Smart India Hackathon (SIH 2026) Evaluation Committee & Technical Mentors.*
