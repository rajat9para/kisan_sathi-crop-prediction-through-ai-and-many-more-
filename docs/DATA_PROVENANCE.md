# Data Provenance & External Feeds

**Kisaan Sathi Data Governance & Integration Architecture**

---

## 1. Primary Datasets & Sources

| Dataset / API | Provider / Organization | Usage in Kisaan Sathi | Update Cadence |
|---|---|---|---|
| **Indian Crop Recommendation Benchmark** | Kaggle / ICAR Precision Agriculture Dataset | ML training for 22 Indian crop classes (2,200 vectors) | Fixed Benchmark (v1.0) |
| **SoilGrids v2.0 REST API** | ISRIC — World Soil Information (Wageningen) | Live global 250m satellite soil pH, Organic Carbon, Clay, Sand | Real-time REST query |
| **Open-Meteo Weather & Soil Moisture** | Open-Meteo & ECMWF Satellite Reanalysis | 7-day temperature, humidity, rainfall, and volumetric soil moisture ($0\text{–}1\text{cm}, 1\text{–}3\text{cm}$) | Live hourly feed |
| **Agmarknet & e-NAM Mandi Prices** | Ministry of Agriculture & Farmers Welfare | Daily APMC mandi commodity modal, min, and max rates | Daily sync + dynamic trend index |
| **Copernicus Sentinel-2 Level-2A** | European Space Agency (ESA) Earth Observation | Multispectral NDVI and NDRE canopy health monitoring | Bi-weekly revisit cycle |
| **ICAR & KVK Extension Guidelines** | ICAR, TNAU, PAU, GBPUAT | Agronomic crop schedules, organic biopesticides, and chemical treatments | Verified institutional standards |

---

## 2. IoT Sensor Hardware Ingestion Specification

For IoT probes deployed in farmer fields:
- **Endpoint**: `POST /api/iot/reading`
- **Supported Hardware**: ESP32, Arduino Uno WiFi, STM32 LoRaWAN nodes with RS485 Modbus soil probes.
- **Conversion Equation**:
  $$\text{Nutrient}_{\text{kg/ha}} = \text{Reading}_{\text{ppm (mg/kg)}} \times 2.24$$

---

## 3. Data Privacy & Integrity

- No personal PII is stored permanently without consent.
- All live API calls feature automatic graceful fallbacks to certified regional agro-ecological hub caches to ensure uninterrupted operation during rural internet disruptions.
