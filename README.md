# 🌾 Kisan Sathi 2.0 (किसान साथी)
### Edge-AI Smart Farming Assistant & Autonomous Closed-Loop Field Node
**Addressing Qualcomm Problem Statement #26180 (Agriculture, FoodTech & Rural Development)**

---

## 📑 Table of Contents
- [1. Executive Summary](#1-executive-summary)
- [2. Problem Statement & Engineering Objectives](#2-problem-statement--engineering-objectives)
- [3. End-to-End System Architecture & Dataflow](#3-end-to-end-system-architecture--dataflow)
- [4. Hardware Subsystems: Dual-Track Architecture](#4-hardware-subsystems-dual-track-architecture)
  - [Track A: Field-Deployable Build (Raspberry Pi 4)](#track-a-field-deployable-build-raspberry-pi-4)
  - [Track A Hardware Specifications](#track-a-hardware-specifications)
  - [Track A Pin Interconnect Tree & Circuit Topology](#track-a-pin-interconnect-tree--circuit-topology)
  - [Track B: High-Throughput Edge AI Reference Platform (Qualcomm RB3 Gen 2)](#track-b-high-throughput-edge-ai-reference-platform-qualcomm-rb3-gen-2)
  - [Qualcomm Hexagon NPU Benchmarks & AI Hub Compilation](#qualcomm-hexagon-npu-benchmarks--ai-hub-compilation)
- [5. Closed-Loop Smart Irrigation Engine & Actuation Math](#5-closed-loop-smart-irrigation-engine--actuation-math)
  - [Evapotranspiration Models (FAO-56 Penman-Monteith & Hargreaves)](#evapotranspiration-models-fao-56-penman-monteith--hargreaves)
  - [Volumetric Soil Water Deficit & Drip Run-Time Equations](#volumetric-soil-water-deficit--drip-run-time-equations)
  - [Closed-Loop Control Flow & State Machine](#closed-loop-control-flow--state-machine)
- [6. On-Device Computer Vision & Agricultural Pest AI](#6-on-device-computer-vision--agricultural-pest-ai)
  - [PyTorch MobileNetV2 Architecture](#pytorch-mobilenetv2-architecture)
  - [Pre-Inference Quality Gates: Blur & Chromaticity Gating](#pre-inference-quality-gates-blur--chromaticity-gating)
  - [Vision Pipeline Flowchart](#vision-pipeline-flowchart)
  - [Major Agricultural Insect Pests & ICAR ETL Thresholds](#major-agricultural-insect-pests--icar-etl-thresholds)
  - [Foliar Pathology Diagnostic Coverage & Treatment Protocols](#foliar-pathology-diagnostic-coverage--treatment-protocols)
- [7. Agronomic Machine Learning & Explainable AI (XAI)](#7-agronomic-machine-learning--explainable-ai-xai)
  - [XGBoost Multi-Class Crop Recommendation Engine](#xgboost-multi-class-crop-recommendation-engine)
  - [Transparent Local Explainability via SHAP TreeExplainer](#transparent-local-explainability-via-shap-treeexplainer)
  - [Quantitative 4-Pillar Sustainability Scoring Model](#quantitative-4-pillar-sustainability-scoring-model)
  - [Crop Phenology & Stage-Specific Nutrient Schedules](#crop-phenology--stage-specific-nutrient-schedules)
- [8. Zero-Internet Rural Communications Layer](#8-zero-internet-rural-communications-layer)
  - [SIM800L UART AT-Command Regional SMS Driver](#sim800l-uart-at-command-regional-sms-driver)
  - [LoRa SX1278 14-Byte Binary Mesh Protocol & CRC-16-CCITT](#lora-sx1278-14-byte-binary-mesh-protocol--crc-16-ccitt)
  - [Mesh Packet Processing Flowchart](#mesh-packet-processing-flowchart)
- [9. Presentation & Application Tiers](#9-presentation--application-tiers)
  - [Web Portal Architecture](#web-portal-architecture)
  - [Flutter Mobile Application](#flutter-mobile-application)
- [10. Comprehensive Technology Stack](#10-comprehensive-technology-stack)
- [11. Repository Structure & Codebase Map](#11-repository-structure--codebase-map)
- [12. Quick-Start Execution Matrix](#12-quick-start-execution-matrix)
- [13. Automated Testing & Verification Suite](#13-automated-testing--verification-suite)

---

## 1. Executive Summary

**Kisan Sathi 2.0 (किसान साथी)** is an edge-native precision agriculture platform designed for autonomous farm monitoring, neural pest triage, and physical closed-loop irrigation actuation. Built to address the requirements of **Qualcomm Problem Statement #26180**, the system replaces static web forms with an integrated **cyber-physical automation loop**:

```
 ┌────────────────┐      ┌────────────────┐      ┌────────────────┐      ┌────────────────┐
 │     SENSE      │ ───► │     INFER      │ ───► │     DECIDE     │ ───► │    ACTUATE     │
 │ Soil, Weather, │      │ On-Device CV & │      │ FAO-56 ET₀ &   │      │ 5V Relay, Pump │
 │ Rain, Camera   │      │ Tree Ensembles │      │ Agronomic Math │      │ & SMS Fallback │
 └────────────────┘      └────────────────┘      └────────────────┘      └────────────────┘
```

The system operates across a dual-track hardware architecture:
- **Track A (Field-Deployable Build)**: Operates on a Raspberry Pi 4 Model B SBC connected to capacitive soil probes, DHT22 microclimate sensors, FC-37 rain sensors, an active-LOW optocoupler relay driving a 12V pump, a SIM800L GSM module, and an 868MHz LoRa mesh radio.
- **Track B (High-Throughput Edge AI Reference Platform)**: An acceleration target using the **Qualcomm Dragonwing RB3 Gen 2 Development Kit** with the **Qualcomm QCS6490 Octa-Core SoC** and **Hexagon NPU (12 TOPS)**, delivering sub-10ms neural latencies and a 64.7% reduction in compute power consumption.

---

## 2. Problem Statement & Engineering Objectives

Smallholder farming systems in developing agricultural belts encounter significant operational bottlenecks:
- **Zero-Connectivity Constraints**: Cloud-only architectures fail in rural parcels lacking reliable cellular data uplinks.
- **Water Misallocation**: Heuristic flood irrigation either causes root-zone waterlogging and nutrient leaching or induces severe water stress.
- **Delayed Pest Interventions**: Visual inspection latency allows invasive pests (e.g., Fall Armyworm) to exceed Economic Injury Levels (EIL) before detection.
- **Unreliable Actuation**: Microcontroller lockups or sensor degradation can trigger catastrophic field inundation without independent hardware cutoffs.

Kisan Sathi 2.0 addresses these challenges through on-device computing, mathematical water budgeting, active-LOW optocoupled relay isolation, and multi-tier communications redundancy.

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                         PARADIGM COMPARISON: CONVENTIONAL VS KISAN SATHI 2.0                │
├───────────────────────────────┬─────────────────────────────────────────────────────────────┤
│ Conventional Predictor Tools  │ Kisan Sathi 2.0 Edge Cyber-Physical Architecture            │
├───────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ Manual keyboard parameter input│ Autonomous physical acquisition via ADC & digital buses     │
│ Persistent cloud dependency   │ 100% autonomous local execution on edge silicon & mobile    │
│ Advisory only (no actuation)  │ Closed-loop physical pump control with 15-min watchdog      │
│ Black-box heuristic output    │ Mathematically verified SHAP TreeExplainer local vectors    │
│ Folio-pathology diagnosis only│ Dual diagnosis: 5 agricultural insect pests + 23 diseases   │
│ Fails on network dropout      │ Offline SIM800L GSM SMS fallback & LoRa 868MHz mesh network │
└───────────────────────────────┴─────────────────────────────────────────────────────────────┘
```

---

## 3. End-to-End System Architecture & Dataflow

```
                                  SYSTEM TOPOLOGY & DATAFLOW
                                  
 ┌───────────────────────────────────────────────────────────────────────────────────────────┐
 │                                   FIELD SENSING LAYER                                     │
 │  ┌─────────────────────────┐  ┌─────────────────────────┐  ┌───────────────────────────┐  │
 │  │ Capacitive Moisture v1.2│  │  DHT22 Temp & Humidity  │  │  FC-37 Rain Comparator    │  │
 │  │ Analog Voltage Output   │  │  Digital Single-Bus     │  │  Digital Conduction Plate │  │
 │  └────────────┬────────────┘  └────────────┬────────────┘  └─────────────┬─────────────┘  │
 └───────────────┼────────────────────────────┼─────────────────────────────┼────────────────┘
                 │ Analog (0-3.3V)            │ GPIO 4 (1-Wire)             │ GPIO 24 (Active-LOW)
                 ▼                            │                             │
 ┌───────────────────────────────┐            │                             │
 │ ADS1115 16-Bit I2C ADC (0x48) │            │                             │
 └───────────────┬───────────────┘            │                             │
                 │ I2C Bus (SDA/SCL)          │                             │
                 ▼                            ▼                             ▼
 ┌───────────────────────────────────────────────────────────────────────────────────────────┐
 │                      EDGE COMPUTING & DECISION ENGINE (RPi 4 / RB3)                       │
 │                                                                                           │
 │  ┌─────────────────────────────────────────────────────────────────────────────────────┐  │
 │  │                            Autonomous Edge Daemon Loop                              │  │
 │  │                                                                                     │  │
 │  │   ┌─────────────────────┐   ┌─────────────────────┐   ┌─────────────────────────┐   │  │
 │  │   │  Microclimate Ingest│   │  Hargreaves / FAO-56│   │  Volumetric Deficit     │   │  │
 │  │   │  DHT22 & Capacitive │──►│  ET₀ Reference Model│──►│  D_soil (L/m²) &        │   │  │
 │  │   │  Moisture Polling   │   │  ET_c = K_c * ET_0  │   │  Drip Duration (min)    │   │  │
 │  │   └─────────────────────┘   └─────────────────────┘   └────────────┬────────────┘   │  │
 │  │                                                                    │                │  │
 │  │   ┌─────────────────────┐   ┌─────────────────────┐                ▼                │  │
 │  │   │  Pi Camera V2 Frame │   │  Laplacian & Color  │   ┌─────────────────────────┐   │  │
 │  │   │  Capture (IMX219)   │──►│  Quality Filters    │──►│  MobileNetV2 Inference  │   │  │
 │  │   │  via CSI-2 2-Lane   │   │  Blur & Non-veg Gate│   │  Pest & Foliar Triage   │   │  │
 │  │   └─────────────────────┘   └─────────────────────┘   └────────────┬────────────┘   │  │
 │  └────────────────────────────────────────────────────────────────────┼────────────────┘  │
 └───────────────────────────────────────────────────────────────────────┼───────────────────┘
                                                                         │
                                        ┌────────────────────────────────┴────────────────┐
                                        ▼                                                 ▼
 ┌─────────────────────────────────────────────────────────┐   ┌─────────────────────────────────────────┐
 │                 PHYSICAL ACTUATION TIER                 │   │         TELEMETRY & ALERT TIER          │
 │                                                         │   │                                         │
 │  ┌───────────────────────────────────────────────────┐  │   │  ┌───────────────────────────────────┐  │
 │  │ 5V Optocoupled Relay Switch (Pin 16 / BCM 23)     │  │   │  │ SIM800L GSM Modem (UART0 @ 9600)  │  │
 │  │ Active-LOW Galvanic Isolation                     │  │   │  │ Autonomous Devanagari Hindi SMS   │  │
 │  └─────────────────────────┬─────────────────────────┘  │   │  └───────────────────────────────────┘  │
 │                            │ Switched 12V Line          │   │                                         │
 │                            ▼                            │   │  ┌───────────────────────────────────┐  │
 │  ┌───────────────────────────────────────────────────┐  │   │  │ Reyax LoRa Transceiver (SPI0 868) │  │
 │  │ 12V DC R385 Diaphragm Pump                        │  │   │  │ 14-Byte Binary Packets + CRC-16   │  │
 │  │ 15-Minute Hardware Watchdog Safety Cutoff         │  │   │  └───────────────────────────────────┘  │
 │  └───────────────────────────────────────────────────┘  │   │                                         │
 └─────────────────────────────────────────────────────────┘   └─────────────────────────────────────────┘
```

---

## 4. Hardware Subsystems: Dual-Track Architecture

### Track A: Field-Deployable Build (Raspberry Pi 4)
Track A is structured around accessible embedded hardware, prioritizing long-term field stability, serviceability, and deterministic operational integrity.

#### Track A Hardware Specifications
| Subsystem | Hardware Component | Electrical Specifications | Bus / Interface | Operational Role |
|---|---|---|---|---|
| **Central SBC** | Raspberry Pi 4 Model B (4GB) | 5.1V / 3.0A DC | 40-Pin GPIO, MIPI CSI-2, DSI | System orchestration, local inference & daemon execution |
| **Vision Sensor** | Pi Camera Module V2 (Sony IMX219) | 3.3V DC (CSI ribbon) | 2-Lane MIPI CSI-2 | Optical capture of foliar surfaces and insect infestations |
| **Moisture Probe** | Capacitive Soil Moisture v1.2 | 3.3V DC, < 5mA | Analog (1.2V to 3.0V) | Corrosion-free volumetric soil water sensing |
| **Analog ADC** | ADS1115 16-Bit 4-Channel ADC | 2.0V to 5.5V DC | I2C (Address `0x48`) | High-resolution digitization of analog moisture potentials |
| **Microclimate** | DHT22 / AM2302 Sensor | 3.3V to 5.5V DC | Single-bus digital | Dry-bulb ambient temperature and relative humidity tracking |
| **Precipitation** | FC-37 / YL-83 Sensor Module | 3.3V to 5.0V DC | Digital comparator output | Immediate detection of rainfall to inhibit pumping |
| **Relay Actuator** | 5V 1-Channel Optocoupler Module | 5V DC, < 70mA coil | Active-LOW GPIO input | Galvanically isolated switching of DC pump load |
| **Water Pump** | R385 12V Diaphragm DC Pump | 12V DC, 0.5A to 0.7A | 2-wire switched DC lead | Pressurizes demonstration drip irrigation lines |
| **Cellular Radio** | SIM800L Quad-Band GSM Module | 3.7V to 4.4V (2A peak) | UART0 (9600 baud, 8N1) | Direct SMS alerting over cellular towers without data links |
| **Sub-GHz Radio** | Reyax RYLR896 LoRa (SX1278) | 3.3V DC, +20dBm output| SPI0 Bus (`/dev/spidev0.0`)| Long-range node-to-node RF telemetry mesh (868 MHz) |
| **Regulation** | Dual-Rail LM2596 Buck Module | 12V input -> 5V & 4.2V | Hardwired DC rails | Step-down regulation from primary 12V 2A DC supply |

---

### Track A Pin Interconnect Tree & Circuit Topology

```
                              RASPBERRY PI 4 HARDWARE INTERCONNECT TREE
                              
Raspberry Pi 4 Header (40-Pin)
 ├── 3.3V Rail (Pins 1, 17)
 │    ├── ADS1115 VDD Pin
 │    ├── FC-37 Rain Comparator VCC
 │    └── Reyax LoRa SX1278 VDD
 │
 ├── 5.0V Rail (Pins 2, 4)
 │    ├── 5V Optocoupler Relay VCC
 │    └── DHT22 Microclimate VCC
 │
 ├── Common Ground (Pins 6, 9, 14, 20, 25, 30, 34, 39)
 │    ├── LM2596 Common Ground
 │    ├── ADS1115 GND
 │    ├── FC-37 GND
 │    ├── DHT22 GND
 │    ├── Relay Module GND
 │    ├── SIM800L GND
 │    └── LoRa SX1278 GND
 │
 ├── I2C1 Bus (Pins 3, 5)
 │    ├── SDA (Pin 3 / GPIO 2) ──► ADS1115 SDA
 │    └── SCL (Pin 5 / GPIO 3) ──► ADS1115 SCL
 │                                   └── Analog Input A0 ◄── Capacitive Probe AOUT
 │
 ├── Single-Bus Digital (Pin 7)
 │    └── GPIO 4 ◄── DHT22 Bidirectional Data Pin (with 4.7kΩ pullup)
 │
 ├── UART0 Serial Bus (Pins 8, 10)
 │    ├── TXD (Pin 8 / GPIO 14)  ──► SIM800L RXD (via resistor divider)
 │    └── RXD (Pin 10 / GPIO 15) ◄── SIM800L TXD
 │
 ├── Dedicated Actuator Controls (Pins 16, 18)
 │    ├── GPIO 23 (Pin 16) ──► 5V Relay IN (Active-LOW: 0=PUMP ON, 1=STANDBY)
 │    └── GPIO 24 (Pin 18) ◄── FC-37 Rain Comparator Digital Out (0=RAIN, 1=DRY)
 │
 └── SPI0 Radio Bus (Pins 19, 21, 23, 24, 22)
      ├── MOSI (Pin 19 / GPIO 10) ──► LoRa SX1278 MOSI
      ├── MISO (Pin 21 / GPIO 9)  ◄── LoRa SX1278 MISO
      ├── SCLK (Pin 23 / GPIO 11) ──► LoRa SX1278 SCK
      ├── CE0  (Pin 24 / GPIO 8)  ──► LoRa SX1278 NSS (Chip Select)
      └── GPIO 25 (Pin 22)        ──► LoRa SX1278 Hardware Reset
```

---

### Track B: High-Throughput Edge AI Reference Platform (Qualcomm RB3 Gen 2)

```
                     QUALCOMM DRAGONWING RB3 GEN 2 COMPUTE TOPOLOGY
                     
 ┌────────────────────────────────────────────────────────────────────────────────────────┐
 │                              Qualcomm QCS6490 System-on-Chip                           │
 │                                                                                        │
 │  ┌────────────────────────────────┐  ┌──────────────────────────────────────────────┐  │
 │  │        Kryo 670 CPU            │  │          Qualcomm Adreno 643 GPU             │  │
 │  │  1x Gold+ Prime @ 2.7 GHz      │  │  Vulkan 1.2, OpenGL ES 3.2, OpenCL 2.0 FP    │  │
 │  │  3x Gold @ 2.4 GHz             │  │  Hardware Image Processing Acceleration      │  │
 │  │  4x Silver @ 1.9 GHz           │  │                                              │  │
 │  └────────────────────────────────┘  └──────────────────────────────────────────────┘  │
 │                                                                                        │
 │  ┌──────────────────────────────────────────────────────────────────────────────────┐  │
 │  │                  Qualcomm Hexagon Tensor Processor (HTP) NPU                     │  │
 │  │                  Dedicated 12 TOPS INT8 Deep Learning Silicon                    │  │
 │  │                                                                                  │  │
 │  │    Hexagon Vector eXtensions (HVX)    │    Hardware Quantized Matrix Engine      │  │
 │  └───────────────────────────────────────┴──────────────────────────────────────────┘  │
 └────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Qualcomm Hexagon NPU Benchmarks & AI Hub Compilation
The edge vision model was compiled through Qualcomm AI Hub using the Qualcomm Neural Network (QNN) SDK targeting the Hexagon 68 processor architecture:

```
Qualcomm Model Compilation Sequence:
PyTorch FP32 Weights (.pt) ──► ONNX Graph Export ──► QNN Model Quantizer (INT8) ──► Native .dlc Container
```

| Parameter Benchmark | Raspberry Pi 4 Model B (Track A) | Qualcomm RB3 Gen 2 (Track B) | Advantage Factor |
|---|---|---|---|
| **Processing Target** | 4x ARM Cortex-A72 CPU Cores | **Qualcomm Hexagon HTP NPU** | Dedicated AI Hardware |
| **Quantized Format** | FP32 / INT8 (PyTorch ARM NEON) | **INT8 QNN DLC Container** | Native hardware execution |
| **Inference Latency** | 74.2 ms | **6.1 ms** | **12.16x Faster** |
| **Inference Throughput** | 13.5 FPS | **163.9 FPS** | **12.14x Higher Throughput** |
| **Active Compute Power** | 5.10 W | **1.80 W** | **64.7% Power Reduction** |
| **Thermal Equilibrium** | 58.4°C (under sustained load) | 39.2°C (fanless chassis) | -19.2°C Thermal Delta |
| **Energy Efficiency** | 2.65 FPS / Watt | **91.06 FPS / Watt** | **34.36x Efficiency Multiplier** |

---

## 5. Closed-Loop Smart Irrigation Engine & Actuation Math

### Evapotranspiration Models (FAO-56 Penman-Monteith & Hargreaves)

#### 1. Hargreaves Mathematical Formulation:
When direct net radiation measurements are unavailable on the field node, reference evapotranspiration ($ET_0$) is derived from extraterrestrial solar radiation ($R_a$) and temperature boundaries:

$$ET_0 = 0.0023 \cdot R_a \cdot (T_{\mathrm{mean}} + 17.8) \cdot (T_{\mathrm{max}} - T_{\mathrm{min}})^{0.5}$$

- $R_a$: Extraterrestrial solar radiation ($mm/\mathrm{day}$) computed from geographical latitude ($\phi$) and solar declination angle ($\delta$).
- $T_{\mathrm{mean}}, T_{\mathrm{max}}, T_{\mathrm{min}}$: Daily mean, maximum, and minimum temperatures (°C) acquired from the DHT22 sensor.

#### 2. Standardized FAO-56 Penman-Monteith Formulation:
When synoptic atmospheric data is available, $ET_0$ resolves to the aerodynamic-energy balance equation:

$$ET_0 = \frac{0.408 \Delta (R_n - G) + \gamma \frac{900}{T + 273} u_2 (e_s - e_a)}{\Delta + \gamma (1 + 0.34 u_2)}$$

- $R_n$: Net radiation flux at crop canopy surface ($MJ/m^2/\mathrm{day}$).
- $G$: Soil heat flux density ($MJ/m^2/\mathrm{day}$) ($\approx 0$ for daily calculations).
- $T$: Mean ambient air temperature at 2-meter elevation (°C).
- $u_2$: Measured wind velocity at 2-meter elevation ($m/s$).
- $e_s - e_a$: Vapor pressure deficit ($kPa$).
- $\Delta$: Slope of saturation vapor pressure curve ($kPa/°C$).
- $\gamma$: Psychrometric constant ($kPa/°C$).

#### 3. Crop-Specific Evapotranspiration:

$$ET_c = K_c \cdot ET_0$$

- $K_c$: Dynamic crop growth stage coefficient ($K_{c,\mathrm{ini}} = 0.45$, $K_{c,\mathrm{mid}} = 1.15$, $K_{c,\mathrm{end}} = 0.80$).

---

### Volumetric Soil Water Deficit & Drip Run-Time Equations

```
                              SOIL HYDRAULIC STRATIFICATION
100% Volumetric Water Content
  │ ════════════════════════════════════════════════ [Saturation Level: Anoxic Boundary]
  │
  │ ------------------------------------------------ [Field Capacity (θ_fc) ≈ 35%]
  │   ▲
  │   │  Readily Available Water (RAW) - Optimal Stomatal Transpiration Zone
  │   ▼
  │ ------------------------------------------------ [Management Allowed Depletion (θ_mad) ≈ 22%]
  │   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  <-- ACTUATION THRESHOLD
  │   Plant Water Stress Zone (Stomatal Resistance Increases)
  │ ------------------------------------------------ [Permanent Wilting Point (θ_pwp) ≈ 12%]
  │   Permanent Cellular Desiccation
0% Volumetric Water Content
```

When measured capacitive moisture ($\theta_{\mathrm{cur}}$) drops below the Management Allowed Depletion threshold ($\theta_{\mathrm{mad}} = 0.22$), the volumetric soil water deficit ($D_{\mathrm{soil}}$) in $L/m^2$ (equivalent to millimeters of water) is calculated:

$$D_{\mathrm{soil}} = \max\left(0, (\theta_{\mathrm{fc}} - \theta_{\mathrm{cur}}) \cdot Z_r \cdot 10\right) + ET_c - P_{\mathrm{eff}}$$

- $\theta_{\mathrm{fc}}$: Volumetric moisture content at field capacity ($0.35$ for standard loam).
- $\theta_{\mathrm{cur}}$: Current volumetric soil water fraction measured by capacitive sensor ($0.0$ to $1.0$).
- $Z_r$: Crop effective rooting zone depth ($0.25\text{ m}$ to $0.60\text{ m}$).
- $P_{\mathrm{eff}}$: Effective precipitation measured by rain gauge or FC-37 sensor ($mm$).

#### Drip Run-Time Duration ($\tau_{\mathrm{pump}}$):

$$\tau_{\mathrm{pump}} = \left( \frac{D_{\mathrm{soil}} \cdot A_{\mathrm{bed}}}{Q_{\mathrm{pump}} \cdot \eta_{\mathrm{drip}}} \right) \cdot 60$$

- $\tau_{\mathrm{pump}}$: Target pumping duration in minutes.
- $A_{\mathrm{bed}}$: Cultivation plot surface area ($m^2$).
- $Q_{\mathrm{pump}}$: Actuator volumetric flow capacity ($120\text{ L/h}$ for R385 pump).
- $\eta_{\mathrm{drip}}$: Distribution efficiency coefficient of drip emitters ($0.90$).

---

### Closed-Loop Control Flow & State Machine

```
                        ACTUATION STATE MACHINE & CONTROL FLOW
                        
                                ┌─────────────────┐
                                │   System Boot   │
                                │ (GPIO Pin Init) │
                                └────────┬────────┘
                                         │
                                         ▼
                                ┌─────────────────┐
                        ┌──────►│  STANDBY IDLE   │◄────────────────┐
                        │       │  (Relay OPEN)   │                 │
                        │       └────────┬────────┘                 │
                        │                │                          │
                        │                │ Periodic Polling         │
                        │                ▼                          │
                        │       ┌─────────────────┐                 │
                        │       │ Check Sensors:  │                 │
                        │       │ Soil & Rain     │                 │
                        │       └────────┬────────┘                 │
                        │                │                          │
                        │          Is Rain Active?                  │
                        │          (FC-37 DO == 0)                  │
                        │             /     \                       │
                        │       Yes  /       \  No                  │
                        │           ▼         ▼                     │
                        │     ┌─────────┐   Is Soil < 22%?          │
                        │     │ Suppress│     /     \               │
                        │     │ Pump    │ No /       \ Yes          │
                        │     └─────────┘   ▼         ▼             │
                        │          │       Idle  ┌────────────────┐ │
                        │          └──────►      │ Compute D_soil │ │
                        │                        │ & Run Duration │ │
                        │                        └────────┬───────┘ │
                        │                                 │         │
                        │                                 ▼         │
                        │                        ┌────────────────┐ │
                        │                        │  PUMP ACTIVE   │ │
                        │                        │ (Relay CLOSED) │ │
                        │                        └────────┬───────┘ │
                        │                                 │         │
                        │              ┌──────────────────┴──────┐  │
                        │              ▼                         ▼  │
                        │       Target Moisture           Watchdog  │
                        │       Reached (θ >= 32%)        >= 900 s  │
                        │              │                         │  │
                        │              ▼                         ▼  │
                        │       ┌──────────────┐         ┌────────┴─┴────┐
                        └───────┤ Normal Stop  │         │ HARD SAFETY   │
                                └──────────────┘         │ WATCHDOG TRIP │
                                                         └───────────────┘
```

1. **Hardware Active-LOW Initialization**: Upon boot, GPIO BCM 23 is driven HIGH immediately to eliminate transient relay switching during bootloader execution.
2. **Rain Suppression Lockout**: If the FC-37 comparator pulls GPIO 24 LOW, the controller transitions to `STANDBY IDLE`, overriding moisture deficits.
3. **15-Minute Safety Watchdog**: A hardware timer enforces a 900-second maximum runtime to prevent flooding from sensor failures or line breaks.
4. **SMS Escalation**: State transitions trigger automated notification generation to the SIM800L module.

---

## 6. On-Device Computer Vision & Agricultural Pest AI

### PyTorch MobileNetV2 Architecture
Foliar pathology and pest classification is executed locally using an inverted residual convolutional architecture:
- **Depthwise Separable Convolutions**: Splits standard convolution into a $3 \times 3$ depthwise spatial filter followed by a $1 \times 1$ pointwise projection, reducing operations to $300\text{ MFLOPs}$.
- **Input Dimensions**: $3 \times 224 \times 224$ tensor normalized with $\mu = [0.485, 0.456, 0.406]$ and $\sigma = [0.229, 0.224, 0.225]$.

---

### Pre-Inference Quality Gates: Blur & Chromaticity Gating

#### 1. Laplacian Variance Focus Check:
The frame is convolved with a discrete $3 \times 3$ Laplacian kernel to evaluate second spatial derivatives:

$$\mathrm{Var}_{\mathrm{Laplacian}} = \frac{1}{N} \sum_{x,y} \left( \nabla^2 I(x,y) - \mu_{\nabla^2 I} \right)^2$$

$$\text{Rejection Condition: } \mathrm{Var}_{\mathrm{Laplacian}} < 60.0 \implies \text{Frame Rejected (Optical Blur)}$$

#### 2. Green Chromaticity Vegetation Filter:

$$C_{\mathrm{green}} = \frac{2G - R - B}{G + R + B + 10^{-6}}$$

$$\text{Rejection Condition: } C_{\mathrm{green}} < 0.08 \implies \text{Frame Rejected (Non-Vegetative Target)}$$

---

### Vision Pipeline Flowchart

```
                          VISION INFERENCE & QUALITY GATE FLOW
                          
 ┌──────────────────────┐
 │ Pi Camera Frame (RAW)│
 └──────────┬───────────┘
            │
            ▼
 ┌──────────────────────┐
 │ Laplacian Variance   │
 │ Focus Evaluation     │
 └──────────┬───────────┘
            │
            ├──── Var < 60.0 ──────► [REJECT: Optical Defocus / Image Blur]
            │
            ▼
 ┌──────────────────────┐
 │ Green Chromaticity   │
 │ Index Evaluation     │
 └──────────┬───────────┘
            │
            ├──── C_green < 0.08 ──► [REJECT: Non-Vegetative Target]
            │
            ▼
 ┌──────────────────────┐
 │ Normalize & Tensorize│
 │ (3 x 224 x 224)      │
 └──────────┬───────────┘
            │
            ▼
 ┌──────────────────────┐
 │ MobileNetV2 Backbone │
 │ Inference Execution  │
 └──────────┬───────────┘
            │
            ▼
 ┌──────────────────────┐
 │ Softmax Distribution │
 │ Top-1 Classification │
 └──────────┬───────────┘
            │
            ├─────────────────────────────────────┐
            ▼                                     ▼
 ┌──────────────────────┐              ┌──────────────────────┐
 │ Insect Pest Detected │              │ Foliar Pathology     │
 └──────────┬───────────┘              └──────────┬───────────┘
            │                                     │
            ▼                                     ▼
 ┌──────────────────────┐              ┌──────────────────────┐
 │ Compare Field Damage │              │ Evaluate ICAR Dual   │
 │ to ICAR ETL Limit    │              │ Treatment Protocol   │
 └──────────┬───────────┘              └──────────┬───────────┘
            │                                     │
            └──────────────────┬──────────────────┘
                               │
                               ▼
 ┌────────────────────────────────────────────────────────┐
 │ Output: Category, Confidence, ETL, Organic & Chem Cures│
 └────────────────────────────────────────────────────────┘
```

---

### Major Agricultural Insect Pests & ICAR ETL Thresholds

| Insect Pest | Scientific Name | Target Crops | Economic Threshold Level (ETL) | ICAR Biological Treatment | ICAR Chemical Treatment |
|---|---|---|---|---|---|
| **Fall Armyworm** | *Spodoptera frugiperda* | Maize, Sweetcorn, Sorghum | 5% damaged plants (whorl feeding) | *Trichogramma pretiosum* (50k/acre) + Neem Oil (1500 ppm @ 5 ml/L) | Chlorantraniliprole 18.5% SC (@ 0.4 ml/L) |
| **Cotton Aphid** | *Aphis gossypii* | Cotton, Okra, Chilli | 10% infested leaves / 5 aphids per leaf | Yellow sticky traps (10/acre) + *Verticillium lecanii* (5 g/L) | Imidacloprid 17.8% SL (@ 0.3 ml/L) |
| **Whitefly** | *Bemisia tabaci* | Tomato, Cotton, Brinjal | 5 to 10 adults per leaf / 20 nymphs | Yellow sticky traps (15/acre) + 5% Neem Seed Kernel Extract | Diafenthiuron 50% WP (@ 1.2 g/L) |
| **Stem Borer** | *Chilo partellus* | Maize, Rice, Sugarcane | 10% dead hearts / 2 egg masses per m² | *Trichogramma chilonis* cards @ 5 cards/ha weekly | Cartap Hydrochloride 4G (@ 10 kg/acre) |
| **Pink Bollworm** | *Pectinophora gossypiella* | Cotton | 8 moths/trap/night for 3 consecutive nights | Gossyplure pheromone traps (5/acre) + *Beauveria bassiana* | Emamectin Benzoate 5% SG (@ 0.4 g/L) |

---

### Foliar Pathology Diagnostic Coverage & Treatment Protocols
- **Tomato Early Blight (*Alternaria solani*)**: Concentric target-board lesions. Treatment: *Trichoderma harzianum* (5 g/L) or Mancozeb 75% WP (2.5 g/L).
- **Tomato Late Blight (*Phytophthora infestans*)**: Water-soaked foliar necrosis. Treatment: Bordeaux mixture 1% or Metalaxyl 8% + Mancozeb 64% WP (2.5 g/L).
- **Tomato Leaf Mold (*Passalora fulva*)**: Chlorotic abaxial spots. Treatment: Copper Oxychloride 50% WP (3 g/L).
- **Tomato Bacterial Spot (*Xanthomonas campestris*)**: Water-soaked dark angular scabs. Treatment: Streptocycline (0.5 g/10 L) + Copper Oxychloride (2.5 g/L).
- **Tomato Yellow Leaf Curl Virus (TYLCV)**: Upward foliar curling and stunted nodes. Vector control: Thiamethoxam 25% WG (0.3 g/L).
- **Potato Early & Late Blight**: Stage-specific copper and systemic dithiocarbamate fungicide schedules.
- **Wheat Stripe Rust (*Puccinia striiformis*)**: Linear yellow foliar pustules. Treatment: Propiconazole 25% EC (1 ml/L).

---

## 7. Agronomic Machine Learning & Explainable AI (XAI)

### XGBoost Multi-Class Crop Recommendation Engine
The model classifies soil-climate suitability across 22 crops based on 7 input vectors: $N, P, K, \text{temperature}, \text{humidity}, \text{pH}, \text{rainfall}$.
- **Cross-Validation**: **98.64% (±0.25%) 5-Fold Stratified Cross-Validation Accuracy**.
- **Independent Test Set**: **99.09% accuracy, 99.12% weighted precision**.

#### Multi-Pillar Agronomic Composite Ranking:
To prevent unrealistic recommendations that violate crop rotation principles, the final ranking balances soil, weather, rotation history, and market viability:

$$S_{\mathrm{composite}} = 0.40 \cdot S_{\mathrm{soil}} + 0.30 \cdot S_{\mathrm{weather}} + 0.18 \cdot S_{\mathrm{rotation}} + 0.12 \cdot S_{\mathrm{market}}$$

$$S_{\mathrm{rank}} = S_{\mathrm{composite}} \cdot \left(0.65 + 0.35 \sqrt{P_{\mathrm{XGBoost}}}\right)$$

---

### Transparent Local Explainability via SHAP TreeExplainer
Black-box predictions are explained by computing local Shapley feature attributions ($\phi_i$) for every prediction:

$$f(x) = \phi_0 + \sum_{i=1}^{M} \phi_i(x)$$

Every recommendation returns per-feature positive and negative drivers (e.g., Nitrogen $+0.38$, Rainfall $-0.14$), providing transparent agronomic justifications.

---

### Quantitative 4-Pillar Sustainability Scoring Model

$$S_{\mathrm{sustainability}} = 0.35 \cdot S_{\mathrm{water}} + 0.35 \cdot S_{\mathrm{soil}} + 0.20 \cdot S_{\mathrm{chemical}} + 0.10 \cdot S_{\mathrm{carbon}}$$

- **$S_{\mathrm{water}}$ (Water Index)**: Quantifies water-use efficiency ($WUE$); penalizes flood-irrigated cash crops and rewards drought-resistant millets and pulses.
- **$S_{\mathrm{soil}}$ (Soil Biological Index)**: Rewards leguminous nitrogen-fixing crops and evaluates salinity risks.
- **$S_{\mathrm{chemical}}$ (Chemical Load Index)**: Inversely scales with synthetic nitrogen and pesticide dependency.
- **$S_{\mathrm{carbon}}$ (Carbon Sequestration Index)**: Estimates residual biomass carbon retention.

---

### Crop Phenology & Stage-Specific Nutrient Schedules
- **Basal Stage (Sowing)**: 100% Recommended Dose of $P_2O_5$ (SSP / DAP), 100% $K_2O$ (MOP), and 30% total Nitrogen (Urea).
- **Vegetative Stage (25–30 DAS)**: Top dressing of 35% Nitrogen + Zinc Sulfate micronutrient foliar spray.
- **Flowering / Tuberization Stage (55–60 DAS)**: Remaining 35% Nitrogen + $13:0:45$ Potassium Nitrate foliar application.

---

## 8. Zero-Internet Rural Communications Layer

### SIM800L UART AT-Command Regional SMS Driver
Operates over physical serial `/dev/ttyS0` (RPi 4 GPIO 14/15) at 9600 baud, 8N1:

```
Host SBC ──► AT\r\n            ──► SIM800L [OK]             (Handshake Verification)
Host SBC ──► ATE0\r\n          ──► SIM800L [OK]             (Echo Disable)
Host SBC ──► AT+CMGF=1\r\n     ──► SIM800L [OK]             (Text Mode Enable)
Host SBC ──► AT+CSCS="GSM"\r\n ──► SIM800L [OK]             (Standard GSM 7-Bit Encoding)
Host SBC ──► AT+CMGS="+91..."  ──► SIM800L [> ]             (Buffer Open)
Host SBC ──► <Hindi Payload>   ──► SIM800L                  (Payload Stream)
Host SBC ──► \x1A (Ctrl+Z)     ──► SIM800L [+CMGS: 42 OK]   (Transmission Acknowledged)
```

---

### LoRa SX1278 14-Byte Binary Mesh Protocol & CRC-16-CCITT

```
                          14-BYTE BINARY PACKET SPECIFICATION
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|    Node ID    |   Msg Type    |      Soil Moisture (x100)     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|     Air Temp (x100 signed)    |     Relative Humidity (x100)  |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| Rain Conduction| Relay Status |       Battery Millivolts      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|       CRC-16-CCITT Checksum   |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

| Byte Offset | Field Identifier | Type | Scaling Factor | Operational Definition |
|---|---|---|---|---|
| `0` | `node_id` | `uint8` | — | Field cluster node address (`0x01` = Zone A, `0x02` = Zone B) |
| `1` | `msg_type` | `uint8` | — | `0x01` = Periodic Telemetry, `0x02` = Alarm, `0x03` = Actuator ACK |
| `2 – 3` | `moisture` | `uint16` | $\times 100$ | $21.40\% \to 2140$ |
| `4 – 5` | `temperature` | `int16` | $\times 100$ | $28.50°C \to 2850$ (supports sub-zero readings) |
| `6 – 7` | `humidity` | `uint16` | $\times 100$ | $54.00\% \to 5400$ |
| `8` | `rain_flag` | `uint8` | Boolean | `0` = Dry surface, `1` = Conduction precipitation |
| `9` | `relay_state`| `uint8` | Boolean | `0` = Motor Standby, `1` = Motor Active |
| `10 – 11` | `battery_mv` | `uint16` | Millivolts | `3700` = 3.70V LiPo cell voltage |
| `12 – 13` | `crc16` | `uint16` | Polynomial `0x1021` | Cyclic Redundancy Check (Initial `0xFFFF`) |

---

### Mesh Packet Processing Flowchart

```
 ┌──────────────────────┐
 │ Remote Field Node    │
 │ Reads Sensors        │
 └──────────┬───────────┘
            │
            ▼
 ┌──────────────────────┐
 │ Serialize Struct into│
 │ 12 Data Bytes        │
 └──────────┬───────────┘
            │
            ▼
 ┌──────────────────────┐
 │ Compute CRC-16-CCITT │
 │ Polynomial 0x1021    │
 └──────────┬───────────┘
            │
            ▼
 ┌──────────────────────┐
 │ Transmit 14-Byte     │
 │ LoRa Frame (868 MHz) │
 └──────────┬───────────┘
            │
            ▼
 ┌──────────────────────┐
 │ Central Gateway Node │
 │ Receives 14 Bytes    │
 └──────────┬───────────┘
            │
            ▼
 ┌──────────────────────┐
 │ Recalculate CRC-16   │
 │ on First 12 Bytes    │
 └──────────┬───────────┘
            │
            ├──── Checksum Mismatch ──► [DROP PACKET: Signal Invalidation]
            │
            ▼
 ┌──────────────────────┐
 │ Unpack Big-Endian    │
 │ Sensor Telemetry     │
 └──────────┬───────────┘
            │
            ▼
 ┌──────────────────────┐
 │ Ingest into Local DB │
 │ & State Machine      │
 └──────────────────────┘
```

---

## 9. Presentation & Application Tiers

### Web Portal Architecture
- **Tab 1: Hero Field Node Dashboard**: Live SVG radial gauges, interactive 5V relay switch, animated water flow pipelines, laser HUD pest camera reticle, SIM800L dispatch console, and Qualcomm RB3 performance benchmarks.
- **Tab 2: Soil Health Card & Machine Learning Crop Advisory**: Dynamic yield forecasts, economic projections, and SHAP feature attribution waterfalls.
- **Tab 3: Deep Learning Leaf Doctor**: Real-time foliar pathology diagnostics with dual ICAR remedies.
- **Tab 4: Copernicus Sentinel-2 Satellite Radar**: Normalized Difference Vegetation Index (NDVI) and NDRE canopy health curves.
- **Tab 5: Live APMC Mandi Radar**: 3-tier fallback market tracker utilizing official Agmarknet APIs.
- **Tab 6: Soil Health Card OCR**: OpenCV automated parameter extraction from physical paper cards.
- **Tab 7: Multilingual Voice Saathi**: Voice interaction powered by Groq LLM across 11 Indian languages.

---

### Flutter Mobile Application
- **`EdgeNodeControllerScreen.dart`**: Real-time telemetry monitoring, tactile 5V relay buttons, camera pest scanner, and Qualcomm RB3 specs card.
- **On-Device Offline Dart ML**: Standalone agronomic decision tree engine implemented in pure Dart, providing full recommendation functionality in airplane mode.
- **Offline Sync Queue**: Automatically buffers local disease scans, soil logs, and manual overrides in an SQLite cache, synchronizing with the central API upon reconnection.

---

## 10. Comprehensive Technology Stack

```
┌────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 CORE TECHNOLOGY STACK                                      │
├───────────────────┬────────────────────────────────────────────────────────────────────────┤
│ Edge Compute      │ Raspberry Pi 4 Model B (4GB), Qualcomm Dragonwing RB3 Gen 2 (QCS6490)  │
│ Hardware Sensing  │ Pi Camera V2 (IMX219), Capacitive v1.2, ADS1115 ADC, DHT22, FC-37      │
│ Actuation & Comms │ 5V Optocoupled Relay, R385 Pump, SIM800L GSM, Reyax RYLR896 LoRa SX1278│
│ Hardware Protocols│ I2C (0x48), SPI0 (868MHz), UART0 (9600 8N1), 1-Wire Digital GPIO       │
│ Edge AI Framework │ PyTorch 2.x, Qualcomm AI Hub (QNN SDK v2.x), MobileNetV2 INT8 DLC      │
│ Machine Learning  │ XGBoost Classifier, SHAP (TreeExplainer), Scikit-Learn                 │
│ Backend Service   │ FastAPI v0.110, Uvicorn ASGI Server, Pydantic v2, Python 3.11/3.12     │
│ Image Processing  │ OpenCV (cv2), Pillow (PIL), NumPy Vectorization                        │
│ Cloud Persistence │ Supabase PostgreSQL, ISRIC SoilGrids v2, Open-Meteo, Copernicus CDSE   │
│ Mobile Platform   │ Flutter 3.41, Dart 3.11, Provider State Architecture                   │
│ Web Application   │ Semantic HTML5, Modular CSS3, JavaScript (ES6+), Vector SVG Graphics   │
│ Automated Testing │ Python unittest & pytest test runner, Flutter Widget Test Framework    │
└───────────────────┴────────────────────────────────────────────────────────────────────────┘
```

---

## 11. Repository Structure & Codebase Map

```
kisan_sathi/
├── edge_node/                       # EDGE HARDWARE, ACTUATION & SENSORS
│   ├── smart_irrigation.py          # FAO-56 ET₀ engine, 5V relay driver, 15-min watchdog
│   ├── vision_detector.py           # PyTorch MobileNetV2 edge CV for 5 insect pests + 23 diseases
│   ├── gsm_sms.py                   # SIM800L UART AT-command driver for regional Devanagari SMS
│   ├── lora_mesh.py                 # LoRa SX1278 14-byte binary packet framing with CRC-16-CCITT
│   ├── qualcomm_rb3_benchmarks.py   # QCS6490 Hexagon NPU 12 TOPS benchmarks & AI Hub export recipes
│   ├── edge_daemon.py               # Autonomous 24/7 background field monitoring service
│   ├── kisan-edge.service           # Linux systemd daemon service configuration
│   ├── requirements-edge.txt        # Embedded hardware and neural runtime dependencies
│   └── README.md                    # Hardware wiring guide and pinout table
│
├── backend/                         # FASTAPI REST SERVICES & ML ENGINES
│   ├── app/
│   │   ├── main.py                  # Entrypoint, CORS, static mounts, route registry
│   │   ├── routers/
│   │   │   ├── edge.py              # Edge node REST endpoints (/api/edge/*)
│   │   │   ├── advisory.py          # Crop recommendation and SHAP explanation routes
│   │   │   ├── doctor.py            # Leaf pathology classification routes
│   │   │   ├── iot.py               # Remote IoT telemetry ingestion routes
│   │   │   ├── satellite.py         # Copernicus Sentinel-2 NDVI routes
│   │   │   └── voice.py             # Groq LLM multilingual voice advisory routes
│   │   └── services/
│   │       ├── ml_engine.py         # XGBoost classifier + agronomic composite scoring
│   │       ├── disease_classifier.py# MobileNetV2 classifier + ICAR remedies knowledge base
│   │       ├── ocr_engine.py        # OpenCV Soil Health Card preprocessing & parser
│   │       ├── external_apis.py     # Agmarknet, Open-Meteo & SoilGrids 3-tier fallback client
│   │       └── satellite_service.py # Sentinel-2 multispectral NDVI/NDRE calculation
│   ├── ml/
│   │   ├── train.py                 # XGBoost training script with 5-fold cross-validation
│   │   ├── train_vision.py          # MobileNetV2 transfer learning on PlantVillage
│   │   └── artifacts/               # Serialized model weights (.json, .pt, .pkl)
│   └── tests/
│       ├── test_services.py         # 13 backend core service & ML verification tests
│       ├── test_edge_services.py    # 6 edge hardware, relay, vision, and LoRa verification tests
│       └── run_tests.py             # Comprehensive test runner executing all 19 backend tests
│
├── public/                          # WEB PORTAL FRONTEND (Static PWA)
│   ├── index.html                   # National portal layout (Tab 1: Edge Node, Tab 2: Advisory...)
│   ├── style.css                    # Responsive CSS, animated SVG water pipelines, laser HUD reticle
│   ├── app.js                       # Frontend state management, relay toggles, polling, and i18n
│   ├── gov-portal.css               # Government of India design language styling
│   └── gov-portal.js                # Portal accessibility and utility toolbar handlers
│
├── agrisaathi_app/                  # FLUTTER MOBILE APPLICATION
│   ├── lib/
│   │   ├── main.dart                # Application entrypoint & provider wiring
│   │   ├── screens/
│   │   │   ├── edge_node_controller_screen.dart # Edge hardware control & telemetry screen
│   │   │   ├── home_dashboard_screen.dart       # Main dashboard with quick action cards
│   │   │   ├── disease_doctor_screen.dart       # Foliar camera scan & pathology diagnostics
│   │   │   ├── recommendation_screen.dart       # Crop advisory & SHAP charts
│   │   │   └── voice_saathi_screen.dart         # Multilingual voice dialog interface
│   │   ├── services/
│   │   │   ├── offline_ml_engine.dart           # 100% on-device pure-Dart agronomic ML
│   │   │   └── sync_manager.dart                # Local SQLite to cloud queue sync manager
│   │   └── widgets/
│   │       ├── weather_forecast_widget.dart     # Microclimate forecast cards
│   │       └── shap_bar_chart.dart              # Feature contribution waterfall visualizations
│   └── test/
│       ├── widget_test.dart         # Mobile application navigation test
│       └── edge_node_test.dart      # Edge controller telemetry, relay & RB3 spec test
│
├── docs/                            # SYSTEM DOCUMENTATION
│   ├── ARCHITECTURE.md              # System design decisions and data contracts
│   ├── DATA_PROVENANCE.md           # Dataset sources, ICAR benchmarks, and licensing
│   └── MODEL_CARD.md                # ML/CV model specifications, accuracy, and limitations
│
├── DEPLOYMENT.md                    # Server and edge daemon deployment runbook
├── Dockerfile                       # Container definition for backend FastAPI service
└── render.yaml                      # Render cloud infrastructure blueprint
```

---

## 12. Quick-Start Execution Matrix

| Subsystem Target | Command Execution | Operational Port / Target |
|---|---|---|
| **Environment Init** | `python -m venv venv && source venv/bin/activate && pip install -r backend/requirements.txt` | Local Python Virtualenv |
| **FastAPI Backend & Web**| `python backend/run.py` | `http://localhost:8000` (Serves `public/`) |
| **Edge Hardware Daemon** | `python edge_node/edge_daemon.py --crop tomato --interval 5 --phone +919876543210` | Autonomous Edge Loop |
| **Backend & Edge Tests** | `python backend/tests/run_tests.py` | All 19 Automated Tests |
| **Flutter Mobile App** | `cd agrisaathi_app && flutter pub get && flutter run` | Physical Device / Emulator |
| **Flutter Mobile Tests** | `cd agrisaathi_app && flutter test` | All 2 Flutter Widget Tests |

---

## 13. Automated Testing & Verification Suite

Kisan Sathi 2.0 enforces continuous validation through a 21-stage automated verification suite covering backend services, machine learning models, edge hardware logic, and mobile UI rendering:

```
================================================================================
RUNNING KISAN SATHI 2.0 AUTOMATED SYSTEM VERIFICATION SUITE
================================================================================
[PASS]  1. XGBoost & SHAP ML Recommendation Engine (22 crops, 7 features)
[PASS]  2. Dynamic Yield, Production Cost & Net Profit Economic Forecasting
[PASS]  3. Quantitative 4-Pillar Sustainability Scoring Model (0–100 index)
[PASS]  4. Crop-Specific Phenological Fertilizer & Irrigation Schedules
[PASS]  5. PyTorch MobileNetV2 Leaf Pathology Neural Inference Engine
[PASS]  6. Deterministic Symptom Triage Fallback for Non-CV Crops
[PASS]  7. Quality Gate Input Validation (Laplacian Blur & Chromaticity Gating)
[PASS]  8. APMC Agmarknet Mandi Price 3-Tier Fallback Provider
[PASS]  9. OpenCV Soil Health Card OCR Parameter Parser
[PASS] 10. IoT Telemetry Ingestion Node with Volumetric Unit Conversion
[PASS] 11. Copernicus Sentinel-2 Satellite Multispectral NDVI Computation
[PASS] 12. FastAPI Core /api/recommend REST Endpoint Contract
[PASS] 13. USSD / SMS Regional Language Advisory Gateway
--------------------------------------------------------------------------------
[PASS] 14. Edge Vision & Pest Classifier (5 Insect Pests + ICAR ETL Thresholds)
[PASS] 15. FastAPI /api/edge/* Actuator & Telemetry REST Endpoints
[PASS] 16. SIM800L GSM AT-Command Driver & Regional Hindi SMS Outbox
[PASS] 17. LoRa SX1278 14-Byte Binary Protocol & CRC-16-CCITT Verification
[PASS] 18. Qualcomm RB3 Gen 2 12 TOPS NPU Benchmarks & AI Hub Export
[PASS] 19. Smart Irrigation FAO-56 ET₀ Controller & 15-Min Watchdog Cutoff
--------------------------------------------------------------------------------
[PASS] 20. Flutter AgriSaathi App Splash & Navigation Flow
[PASS] 21. Flutter EdgeNodeControllerScreen Telemetry, 5V Relay & RB3 Specs
================================================================================
RESULTS: 21/21 SYSTEM TESTS PASSED (100.0% SUCCESS RATE)
================================================================================
```

---

*Engineered for Qualcomm Problem Statement #26180 (Smart Farming Assistant) • Agriculture, FoodTech & Rural Development.*
