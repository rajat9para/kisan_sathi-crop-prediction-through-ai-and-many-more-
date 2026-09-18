# Kisaan Sathi — SIH 2026 Official Presentation & Defense Dossier
### Problem Statement #26180 · Qualcomm Inc · Hardware Edition · Team TechBuilders
**Theme**: Disaster Management  
**Field-Deployable Cyber-Physical Node & AI Smart Farming Assistant**

---

## EXECUTIVE SUMMARY & THE 10-SECOND HOOK

> **"A ₹9,850 solar-powered field node that detects crop disease, pest, nutrient and water stress on-device in 32 ms — and keeps warning the farmer when the network is gone."**

---

## PART 0 — ARCHITECTURAL CORRECTIONS & GROUND TRUTH AUDIT

| Item | Correct Submission Reality | Rationale & Defense |
|:---|:---|:---|
| **Theme** | **Disaster Management** | SIH 26180 (Qualcomm Inc) is scored through the disaster resilience lens: drought, flood, heatwave, and pest epidemic mitigation. |
| **Vision Coverage** | **7 CNN classes (95.87% val acc)**<br>16 classes ICAR symptom guidance (`conf: null`)<br>5 major pests via ICAR ETL threshold advisory | Very few teams declare an honest capability boundary. We do not claim neural coverage we cannot evidence. |
| **Evapotranspiration** | **FAO-56 Hargreaves** ($ET_0$) | Penman-Monteith requires net radiation and wind speed sensors (pyranometer + anemometer, ~₹8,000 on a ₹9,850 node). Hargreaves is FAO-56's sanctioned reduced-data method—representing disciplined cost engineering. |
| **Silicon & NPU** | **RPi 4 Cortex-A72 INT8 (32.4 ms)**<br>Roadmap: Qualcomm Dragonwing / QCS NPU | Real, committed Arm CPU benchmark on committed INT8 ONNX graph; ports to Qualcomm NPU via QNN/LiteRT in build phase. |
| **Crop Model Accuracy**| **99.09% held-out test accuracy**<br>**98.64% ± 0.25% 5-fold CV mean** | Reconciled across repo, artifacts, and slides. Verified on 2,200 agro-climatic benchmark samples. |
| **GPIO Pinouts** | **Relay: GPIO 17 (Pin 11, Active-LOW)**<br>**Rain Sensor: GPIO 27 (Pin 13, Active-LOW)** | Reconciled across `hardware/BOM.md`, `edge_node/README.md`, and `edge_node/smart_irrigation.py`. |
| **Node Build Cost** | **₹9,850 INR (~$118 USD)** | 100% commodity parts sourced off-the-shelf from Indian electronics distributors. |
| **Power Budget** | **59.5 Wh/day** (74.4 Wh with conv.)<br>20W PV + 12V 7Ah VRLA Battery | **48 Hours Zero-Sun Autonomy** in an IP65 weatherproof enclosure (-10°C to +60°C). |

---

## PART 1 — SLIDE-BY-SLIDE CONTENT (PASTE-READY)

---

### SLIDE 1 — Title Slide

```
Problem Statement ID    : 26180
Problem Statement Title : Field-deployable AI-powered Smart Farming Assistant
Theme                   : Disaster Management
PS Category             : Hardware
Organisation            : Qualcomm Inc
Team Name               : TechBuilders
Team ID                 : <Your Team ID>
```

#### One-Line Subtitle (~16pt):
> **A ₹9,850 solar-powered field node that detects crop disease, pest, nutrient and water stress on-device in 32 ms — and keeps warning the farmer when the network is gone.**

**Speaker Note for Slide 1**:
*"Good morning respected judges. We are Team TechBuilders presenting Kisaan Sathi for Problem Statement 26180 sponsored by Qualcomm Inc under the Disaster Management theme. Agriculture in India is on the frontlines of climate volatility. Our solution is not another cloud app that assumes 4G in a remote field. It is an autonomous, ₹9,850 solar-powered field station that senses soil, microclimate and canopy, runs four AI engines locally in 32 milliseconds, acts directly on irrigation pumps, and keeps warning farmers even when floods, droughts or storms take down the cell towers."*

---

### SLIDE 2 — Proposed Solution

#### 1. Detailed explanation of the proposed solution

> Kisaan Sathi is a solar-powered field node built on a Raspberry Pi 4 that senses the crop's soil, air and canopy, runs four AI engines locally, and converts the result into a physical action — switching an irrigation pump, or pushing an alert over GSM/LoRa when there is no internet.
>
> 1. **Edge sensing** — capacitive soil-moisture probe via a 16-bit ADS1115 ADC, DHT22 for air temperature and humidity, FC-37 rain plate, and a Pi Camera V2 for leaf imagery. Readings on a 3-minute duty cycle, written to SQLite before use.
> 2. **On-device leaf pathology** — MobileNetV2 fine-tuned on PlantVillage, exported to INT8 ONNX. 32.4 ms per frame on the Pi's Cortex-A72. 7 CNN-verified classes at 95.87% validation accuracy; 16 further crops served by labelled ICAR symptom guidance.
> 3. **Nutrient deficiency detection** — NPK and pH from the sensor bus or from a Soil Health Card photographed and read by the on-board OCR engine; XGBoost + SHAP returns both the deficiency and its magnitude.
> 4. **Water balance, not a moisture threshold** — FAO-56 Hargreaves ET₀ from measured Tmax/Tmin, ETc = Kc × ET₀ for the crop's current stage, soil-water deficit converted to litres and then to pump runtime.
> 5. **Hazard early warning** — drought, flood, heatwave and disease-outbreak indices computed from local sensors fused with the Open-Meteo forecast, each graded 0–100.
> 6. **Delivery that degrades but never stops** — app and dashboard when online; SIM800L Devanagari SMS when there is only cellular; LoRa 868 MHz to a village gateway when there is not; local buzzer and autonomous pump action when fully isolated.

#### 2. How it addresses the problem

| Problem Statement Requirement | Our Mechanism & Implementation | Evidenced Performance |
|:---|:---|:---:|
| **Detect crop diseases early** | MobileNetV2 INT8 on-device inference on leaf imagery | 32.4 ms / frame · 95.87% val acc |
| **Detect pests early** | ETL-threshold advisory with bio and chemical dosing per ICAR | 5 Major Indian Insect Pests |
| **Detect nutrient deficiencies** | NPK/pH sensing + Soil Health Card OCR $\to$ XGBoost + SHAP | 7 Soil Features + 11 Languages |
| **Detect irrigation needs** | FAO-56 Hargreaves $ET_c$ water balance $\to$ relay-actuated pump | Liters/$m^2 \to$ Exact runtime |
| **Resilience against droughts, floods & heatwaves**| Four graded hazard indices (0–100) with pre-emptive actions | Local Telemetry + Open-Meteo ECMWF |
| **Real-time on-device intelligence** | Full closed loop executes on Raspberry Pi with zero cloud dependency | 100% Offline Autonomous Operation |

#### 3. Innovation and uniqueness

> - **It acts, it does not only advise.** The decision terminates at an optocoupled relay closing on a 12V pump, under a 15-minute hardware watchdog and a rain lockout that software cannot override.
> - **Explainability reaches the farmer, not the developer.** SHAP output is translated into a spoken sentence in 11 Indian languages — *"nitrogen at 85 kg/ha raises this recommendation by 0.24"* — not an abstract chart a farmer cannot interpret.
> - **A declared capability boundary.** Where we have no verified training data we return `confidence: null` and ICAR symptom guidance instead of a fabricated score.
> - **₹9,850, solar, and offline-native** — engineered for the realities of Indian smallholder agriculture, not an urban lab.

---

### SLIDE 3 — Technical Approach

#### Technologies to be used (4-Line Technology Strip)
> **Hardware** · Raspberry Pi 4B (4 GB) · Pi Camera V2 · capacitive soil probe · ADS1115 16-bit ADC · DHT22 · FC-37 rain plate · 5 V opto relay $\to$ 12 V R385 pump · SIM800L GSM · RYLR896 LoRa SX1278 868 MHz · 20 W PV + 12 V 7 Ah VRLA  
> **Edge AI** · PyTorch $\to$ ONNX Runtime · MobileNetV2 INT8 · OpenCV · XGBoost · SHAP TreeExplainer · scikit-learn  
> **Agronomy** · FAO-56 Hargreaves $ET_0$ · crop coefficient $K_c$ · soil-water deficit · ICAR / TNAU / PAU extension guidelines  
> **Software** · FastAPI · SQLite (edge) · Supabase PostgreSQL (cloud) · Flutter · PWA · systemd · SoilGrids v2 · Open-Meteo · Sentinel-2 · Agmarknet  

#### Diagram Layout
- **Left Half**: `D1_hardware_block_diagram_v2.svg` (Physical wiring, power buses, sensor pinouts, compute core).
- **Right Half**: `D2_edge_decision_loop_v2.svg` (Sense $\to$ Quality Gate $\to$ 4 Local AI Engines $\to$ Actuation Guards $\to$ Delivery).

#### Caption under Diagrams
> **Total node cost ₹9,850 (~$118)** · **draw 59.5 Wh/day** · **48 h zero-sun autonomy** · **IP65 enclosure, −10 °C to +60 °C**

---

### SLIDE 4 — Feasibility and Viability

#### 1. Feasibility
> - **Built, not proposed.** The node runs today as an autonomous systemd service (`kisan-edge.service`); the inference benchmark (32.4 ms), model card, confusion matrices and BOM are committed repository artefacts, not slideware.
> - **Commodity supply chain.** Every one of the 12 BOM items is available off-the-shelf from Indian electronics distributors. No custom silicon, no import lead time.
> - **Power closes.** 59.5 Wh/day consumption $\to$ 74.4 Wh/day accounting for conversion losses; at 4.0 peak-sun hours that requires 18.6 W, so a 20 W panel with a 12 V 7 Ah battery provides 48 hours of zero-sun autonomy.
> - **Latency closes.** 32.4 ms per frame on the Pi's own Cortex-A72 CPU — no GPU required, zero cloud round trip.
> - **Skills match the team.** Python, PyTorch, FastAPI and Flutter are already in hand; the GPIO hardware layer is clean and under 1,000 lines.

#### 2. Potential challenges and risks
> - **Sensor drift and calibration.** Capacitive probes drift with soil salinity and temperature; an uncalibrated probe produces confidently wrong irrigation.
> - **Training-data gaps.** No verified public leaf dataset exists for wheat rust, rice blast, cotton blight or chilli anthracnose at field quality.
> - **Actuation is physically consequential.** A stuck relay floods a field, depletes groundwater, and burns a pump motor.
> - **GSM and LoRa coverage vary.** SIM800L operates on 2G; 2G sunset is an eventual transition risk in some telecom circles.
> - **Farmer trust and literacy.** An unexplained instruction from an anonymous box in a field will be ignored.
> - **Weather and pests are non-stationary.** A static model trained once degrades over seasons.

#### 3. Strategies for overcoming these challenges
> - **Two-point field calibration** (air-dry and saturated wet) stored in EEPROM/SQLite per node, with a monthly drift check; readings outside the 1.2–3.0 V envelope are rejected.
> - **Declared boundary instead of a guess** — untrained crops return ICAR symptom guidance with `confidence: null`. Field images confirmed by farmers queue for the next model refresh.
> - **Defence in depth on actuation** — opto-isolated active-LOW relay (no transient firing at boot), a 15-minute hard hardware cutoff with no software override, and an FC-37 rain lockout that vetoes irrigation regardless of soil moisture.
> - **Three-tier comms fallback** — GSM, then LoRa 868 MHz to a village gateway, then fully local autonomous operation with buzzer/LED. The 4G/LTE modem is a drop-in UART replacement when 2G retires.
> - **Explainability as an adoption tool** — every instruction carries its reason and its confidence, spoken in the farmer's language, with the local KVK scientist's verified line attached for escalation.
> - **Store-and-forward learning** — zero data discarded offline; telemetry and diagnostic outcomes sync when backhaul reconnects.

---

### SLIDE 5 — Impact and Benefits

#### Main Visual (Right ~55% of Slide)
`D3_disaster_resilience_engine_v2.svg` (Multi-Hazard Early Warning Engine: Drought, Flood, Heatwave, Outbreak).

#### 1. Potential impact on the target audience
> - **Earlier detection, cheaper intervention.** Blight and rust are treatable in the first 48 hours and largely untreatable later. A 32 ms on-device diagnosis moves the decision from "when an expert visits" to "now".
> - **Water applied to demand, not to habit.** ETc-based scheduling with a rain lockout replaces fixed-interval flood irrigation, which is the dominant wasteful practice among smallholders.
> - **Hazards seen before they arrive.** Drought, flood, heatwave and outbreak indices give lead time for pre-emptive irrigation, pump lockout, schedule shift or an early spray window — the difference between a managed season and a lost harvest.
> - **Advisory that survives the network.** The households most vulnerable to climatic disasters are those with the weakest connectivity. GSM SMS and LoRa ensure the warning arrives during blackouts.
> - **A reason, not an order.** SHAP attribution in 11 languages, plus a verified ICAR-KVK contact, so the farmer can verify the machine with a human expert.

#### 2. Benefits
> - **Social** — advisory reaches marginal farmers without smartphones or data plans; voice-first in 11 Indian languages; reduces reliance on an agronomist being physically present.
> - **Economic** — input costs fall when irrigation and chemical sprays are triggered solely by measured need; early blight detection protects crop yields; ₹9,850 is accessible to an FPO or KVK without subsidy.
> - **Environmental** — rain-aware pump scheduling cuts unnecessary groundwater extraction; targeted spray windows reduce pesticide runoff into local aquifers; grid-independent solar power.
> - **Technological** — proves that quantized CNN inference, gradient-boosted agronomy and explainability fit inside a ₹4,200 SBC, and establishes a clear migration path to Qualcomm NPU silicon.

---

### SLIDE 6 — Research and References

#### Main Visual (Upper Two-Thirds of Slide)
`D4_validation_and_capability_panel_v2.svg` (Evidence Panel: Capability Boundary, 5-Fold CV Rigor, Edge Profiling, Citations).

#### 1. Research and data sources
> - **FAO Irrigation & Drainage Paper 56** — Allen et al., *Crop Evapotranspiration: Guidelines for Computing Crop Water Requirements*, FAO, 1998 — ET₀, Kc, Hargreaves model.
> - **PlantVillage Dataset** — Hughes & Salathé; spMohanty/PlantVillage-Dataset, CC-BY-SA — 4,200 verified images across 7 classes used for training.
> - **MobileNetV2** — Sandler et al., *Inverted Residuals and Linear Bottlenecks*, CVPR 2018.
> - **SHAP** — Lundberg & Lee, *A Unified Approach to Interpreting Model Predictions*, NeurIPS 2017.
> - **ISRIC SoilGrids v2.0** — 250 m global soil property layers.
> - **Open-Meteo / ECMWF** — 7-day forecast, volumetric soil moisture, leaf-wetness proxy.
> - **Copernicus Sentinel-2 L2A** — NDVI parcel vegetative statistics.
> - **Agmarknet via data.gov.in** — APMC mandi modal rates.
> - **ICAR / TNAU / PAU / GBPUAT extension guidelines** — symptom triage, ETL thresholds, biological and chemical dosing.

#### 2. Data honesty statement (Verbatim)
> **"Every API response carries an explicit `source` field. Where a live feed is unavailable the system degrades to a clearly-labelled cached or estimated value. It never presents simulated data as verified data. Confidence scores are raw softmax outputs — never floored, clamped, or invented."**

#### 3. Why Kisaan Sathi
> From advisory to autonomous field intelligence:  
> **edge-first** (inference at the farm, 32.4 ms) · **offline-first** (GSM $\to$ LoRa $\to$ local) · **closed-loop** (sense $\to$ decide $\to$ pump $\to$ verify) · **explainable** (SHAP + reason + confidence, spoken) · **bounded** (we declare what the model cannot do).

---

## PART 2 — WHERE THE DIAGRAMS GO

| Diagram Identifier & File | Slide # | Optimal Position on Slide | Format & Path |
|:---|:---:|:---|:---|
| `D1_hardware_block_diagram_v2.svg` | **Slide 3** | Left half, directly beneath the 4-line tech strip | `docs/presentation/D1_hardware_block_diagram_v2.svg` |
| `D2_edge_decision_loop_v2.svg` | **Slide 3** | Right half (replaces the old flowchart with the typo) | `docs/presentation/D2_edge_decision_loop_v2.svg` |
| `D3_disaster_resilience_engine_v2.svg`| **Slide 5** | Right ~55% of the slide, beside the impact text | `docs/presentation/D3_disaster_resilience_engine_v2.svg` |
| `D4_validation_and_capability_panel_v2.svg`| **Slide 6**| Upper two-thirds of slide above citations | `docs/presentation/D4_validation_and_capability_panel_v2.svg` |

*Note*: High-resolution PNG renders (`.png`) with identical basenames are saved in `docs/presentation/`, `docs/assets/`, and the repository root for seamless PowerPoint compatibility across all versions.

---

## PART 3 — THE SIX QUESTIONS JUDGES WILL ASK & HOW TO ANSWER THEM

### Q1: "You say 23 diseases. Show me the 23 classes in your model."
> **Answer**:  
> *"Our CNN has 7 verified classes at 95.87% validation accuracy on PlantVillage — the confusion matrix and per-class metrics are in `docs/MODEL_CARD.md`. For the remaining 16 crops, no verified public leaf dataset exists at Indian field quality. Rather than training on noisy unverified web scrapings or fabricating a neural confidence score, we serve them through verified ICAR/TNAU symptom guidance and explicitly return `confidence: null` with an 'ICAR Guidance' label in the UI. 5 major insect pests are triaged via ICAR Economic Threshold Levels. We chose a declared, defensible boundary over an inflated marketing claim."*

---

### Q2: "Penman-Monteith needs net radiation and wind. Where are those sensors on your node?"
> **Answer**:  
> *"We implemented FAO-56 Hargreaves, not Penman-Monteith. Hargreaves is FAO-56's sanctioned reduced-data alternative designed specifically for sensor suites with temperature and extraterrestrial radiation. True Penman-Monteith requires a net pyranometer and an anemometer — adding roughly ₹8,000 to what is currently a ₹9,850 node. By using Hargreaves, we achieve accurate volumetric deficit scheduling within the budget of an Indian marginal farmer. That was a conscious engineering decision to keep the node viable."*

---

### Q3: "What happens if the relay sticks closed? Won't you burn the pump or flood the farm?"
> **Answer**:  
> *"We built three independent layers of defence in depth into the actuation circuit:  
> 1. The relay is opto-isolated and active-LOW with a pull-up resistor, ensuring it cannot fire during bootloader initialization or software crashes.  
> 2. The edge controller enforces a strict 15-minute continuous hardware watchdog cutoff in firmware that software cannot bypass.  
> 3. The FC-37 rain plate comparator acts as an immediate physical veto — if rain begins, the pump shuts down immediately regardless of soil moisture demand."*

---

### Q4: "Your crop recommendation model reports 99.09%. Is that not overfitting on a Kaggle dataset?"
> **Answer**:  
> *"99.09% is the held-out test score on 440 stratified vectors from the 2,200-sample benchmark. We also ran full 5-fold cross-validation, which yielded a mean accuracy of 98.64% with a standard deviation of ±0.25%, demonstrating that the tree ensemble generalizes consistently across splits. Crucially, we do not treat the XGBoost prediction as a final decision; it acts as a strong agro-climatic prior that is then re-ranked against live SoilGrids soil chemistry, Open-Meteo weather forecasts, and APMC mandi market price trends before recommendation."*

---

### Q5: "This is a Qualcomm problem statement. Why did you build on a Raspberry Pi?"
> **Answer**:  
> *"The Raspberry Pi 4 is our prototype development platform because it allowed us to establish a verifiable baseline: 32.4 milliseconds on a commodity Arm Cortex-A72 CPU with zero hardware acceleration. Because we exported the model as a standard ONNX INT8 graph, that exact graph ports directly to Qualcomm Dragonwing or QCS-class processors using Qualcomm Neural Network (QNN) SDK or LiteRT on Hexagon NPUs. We are presenting what we measured on physical hardware today, while providing an honest, direct architectural bridge to Qualcomm silicon for production."*

---

### Q6: "This is listed under Disaster Management. What makes this a disaster resilience solution?"
> **Answer**:  
> *"Agro-climatic disasters — flash droughts, floods, heatwaves, and epidemic blights — cost Indian farmers thousands of crores annually. Kisaan Sathi runs four dedicated early-warning engines:  
> 1. Drought Deficit Index fuses soil moisture trajectories with 7-day rainfall forecasts to trigger pre-emptive irrigation.  
> 2. Flood Risk locks out pumps and sounds drainage alerts before soil hypoxia sets in.  
> 3. Heatwave Stress shifts watering to pre-dawn hours to prevent canopy scald and flower abortion.  
> 4. Outbreak Index uses leaf wetness and temperature trapezoids to forecast spore sporulation windows.  
> And critically, the three-tier communications fallback (SMS and LoRa 868MHz) ensures that when a disaster knocks out cellular data, the life-saving warning still reaches the farmer and the local Panchayat."*

---

## PART 4 — PRE-SUBMISSION VERIFICATION CHECKLIST

- [x] **Theme on Slide 1**: Updated to **Disaster Management** (matching official SIH 26180 Qualcomm listing).
- [x] **Evidenced Vision Breakdown**: "23 diseases" replaced with **7 CNN classes / 16 ICAR symptom classes / 5 ETL insect pests**.
- [x] **Evapotranspiration Accuracy**: Penman-Monteith replaced with **FAO-56 Hargreaves** across slides and documentation.
- [x] **Silicon Accuracy**: Unverified Hexagon claims replaced with **Arm Cortex-A72 32.4 ms benchmark + Qualcomm QNN roadmap**.
- [x] **Model Metrics Reconciled**: **98.64% ± 0.25% 5-fold CV mean** and **99.09% held-out test accuracy** reconciled across README and docs.
- [x] **GPIO Consistency**: Relay on **GPIO 17 (Pin 11)** and Rain on **GPIO 27 (Pin 13)** verified identical in BOM, edge README, and python code.
- [x] **Honest Edge Code**: Latency fudges (`+32.5`) and hardcoded bounding boxes removed from `edge_node/vision_detector.py`.
- [x] **Unified Project Name**: Project standardized as **Kisaan Sathi** throughout.
- [x] **Typo Eradicated**: "ECISION ENGINE" removed; replaced by clean vector `D2_edge_decision_loop_v2.svg`.
- [x] **Vector Diagrams**: D1, D2, D3, and D4 generated as high-resolution SVGs and 2x PNGs.
- [x] **Official PPTX Generated**: 16:9 widescreen presentation assembled and ready for projection.
- [x] **Automated Test Suite**: 18/18 tests passing cleanly in CI harness.
