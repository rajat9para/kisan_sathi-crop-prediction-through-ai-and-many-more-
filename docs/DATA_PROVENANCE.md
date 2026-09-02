# Data Provenance & External Feeds

**Kisaan Sathi Data Governance & Integration Architecture**

> **Data honesty statement**: every data row and API response in Kisaan_Sathi
> carries an explicit `source` field. When a live feed is unavailable, the
> system degrades to clearly-labelled cached or estimated values — it never
> presents simulated data as verified real data.

---

## 1. Primary Datasets & Sources

| Dataset / API | Provider / Organization | Usage in Kisaan Sathi | Update Cadence | Status |
|---|---|---|---|---|
| **Indian Crop Recommendation Benchmark** | Kaggle / ICAR Precision Agriculture Dataset | ML training for 22 Indian crop classes (2,200 vectors) | Fixed Benchmark (v1.0) | ✅ Real, trained |
| **PlantVillage Leaf Imagery** | spMohanty / Penn State (CC-BY-SA) | Vision training for 7 CV-diagnosable classes (4,200 images, 95.87% val acc) | Fixed Benchmark | ✅ Real, trained |
| **SoilGrids v2.0 REST API** | ISRIC — World Soil Information (Wageningen) | Live global 250m satellite soil pH, Organic Carbon, Clay, Sand | Real-time REST query | ✅ Real, live |
| **Open-Meteo Weather & Soil Moisture** | Open-Meteo & ECMWF Satellite Reanalysis | 7-day temperature, humidity, rainfall, volumetric soil moisture, spray windows, disease-risk early warning | Live hourly feed | ✅ Real, live |
| **Agmarknet via data.gov.in API** | Ministry of Agriculture & Farmers Welfare | Daily APMC mandi modal/min/max rates; 7-day trends computed from accumulated Supabase snapshots | Daily (Vercel/uptime cron or on-request) | ✅ Real when `DATA_GOV_API_KEY` set → cached snapshot → clearly-labelled `estimated_fallback` |
| **Copernicus Sentinel-2 L2A (CDSE Statistical API)** | ESA / Copernicus Data Space Ecosystem | Real NDVI parcel statistics (60-day window, ≤20% cloud, 5-day means) | Per request | ✅ Real when CDSE OAuth client configured; otherwise response is explicitly labelled `estimated` |
| **ICAR & KVK Extension Guidelines** | ICAR, TNAU, PAU, GBPUAT | Agronomic crop schedules, organic biopesticides, chemical treatments, symptom-based disease triage | Verified institutional standards | ✅ Curated knowledge |

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
