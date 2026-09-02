# 🏗️ Kisaan_Sathi — Project Architecture & Repository Structure

**Smart India Hackathon 2026 • Clean-repo reference (post-cleanup v2.0)**

---

## 1. Repository Layout (every file has a job)

```
kisan_sathi/
├── public/                        # 🎨 FRONTEND (single source — served by Vercel AND FastAPI)
│   ├── index.html                 # National-portal UI (GOI chrome + carousel + schemes + app tabs)
│   ├── style.css                  # Application styles (tabs, cards, dynamic content)
│   ├── gov-portal.css             # Government of India design layer (chrome, carousel, footer)
│   ├── gov-portal.js              # Carousel + accessibility toolbar + quick-services
│   ├── app.js                     # Application logic (recommendations, doctor, voice, mandi)
│   └── *.png                      # Banner / avatar imagery
│
├── backend/                       # ⚙️ FASTAPI + ML ENGINE (Docker-deployed: Render/Railway)
│   ├── Dockerfile                 # Container build (python:3.11-slim + artifacts)
│   ├── requirements.txt           # Pinned runtime dependencies
│   ├── run.py                     # Local entrypoint (uvicorn)
│   ├── app/
│   │   ├── main.py                # FastAPI app, CORS, static file serving
│   │   ├── config.py              # Env-driven configuration (keys, timeouts)
│   │   ├── models/schemas.py      # Pydantic v2 request/response contracts
│   │   ├── routers/               # advisory, doctor, weather, soil, market,
│   │   │                          # voice, ocr, iot, satellite
│   │   └── services/
│   │       ├── ml_engine.py       # XGBoost + SHAP + v2 agronomy-first ranking + economics
│   │       ├── disease_classifier.py  # MobileNetV2 (PlantVillage-trained) + ICAR knowledge base
│   │       ├── disease_risk.py    # Weather-driven epidemiological risk indices
│   │       ├── external_apis.py   # SoilGrids, Open-Meteo, Agmarknet (data.gov.in) 3-tier feed
│   │       ├── satellite_service.py   # Copernicus CDSE NDVI + labelled estimate fallback
│   │       ├── llm_advisor.py     # Groq multilingual advisory + 11-language KB
│   │       ├── ocr_engine.py      # OpenCV preprocessing + regex parameter parser
│   │       ├── supabase_client.py # DB persistence (recommendations, scans, mandi, IoT)
│   │       └── demo_cache.py      # 18-hub offline fallback profiles + KVK directory
│   ├── ml/
│   │   ├── train.py               # XGBoost training + 5-fold CV + SHAP export
│   │   ├── train_vision.py        # PlantVillage fine-tuning pipeline (real training)
│   │   ├── data/Crop_recommendation.csv  # 2,200-vector Kaggle/ICAR benchmark
│   │   └── artifacts/             # Trained weights + evaluation metrics (see MODEL_CARD)
│   └── tests/
│       └── test_services.py       # 13-stage verification suite (run by CI)
│
├── agrisaathi_app/                # 📲 FLUTTER MOBILE APP (on-device Dart ML, offline sync)
├── docs/                          # MODEL_CARD, DATA_PROVENANCE, ARCHITECTURE (this file)
├── .github/workflows/ci.yml       # CI: trains model + runs 13-test verification suite
├── supabase_schema.sql            # One-time DB schema (mandi history, IoT, advisory logs)
├── vercel.json                    # Static frontend deployment (outputDirectory: public)
├── render.yaml                    # Backend blueprint (Docker web service)
├── DEPLOYMENT.md                  # Step-by-step deployment guide
└── README.md                      # Project overview
```

**Removed in the v2.0 cleanup** (duplicates and dead weight):
root-level `index.html`/`app.js`/`style.css`/banner PNGs (duplicates of `public/`),
7 ad-hoc `backend/test_*.py` scripts, duplicate `backend/supabase_schema.sql`,
`backend/generate_avatar.py`, and the broken Vercel `api/` serverless function
(Python ML stack exceeds Vercel's 250 MB limit — backend now ships as a Docker service).

---

## 2. Request Flow (recommendation pipeline)

```
Farmer (PWA / Flutter)
   │  GPS / hub-chip selection
   ▼
POST /api/recommend
   ├─► GET SoilGrids v2.0 (ISRIC)      → live N-P-K, pH, SOC
   ├─► GET Open-Meteo                  → 7-day temp / RH / rain
   ├─► GET Agmarknet (data.gov.in)     → live mandi trends
   │      └─ fallback: Supabase snapshot → labelled estimates
   ▼
MLEngine.recommend_crops (v2 ranking)
   ├─ 27 verified crop profiles (soil / weather fit)
   ├─ Rotation impact + market pillar from live trends
   ├─ pillar_composite = soil·0.40 + weather·0.30 + rotation·0.18 + market·0.12
   ├─ ML damper: 0.65 + 0.35·√(XGBoost confidence)
   ├─ SHAP TreeExplainer per-feature attributions
   ├─ Dynamic yield / cost / net-profit economics
   └─ 4-pillar sustainability score
   ▼
JSON response (bilingual, per-crop schedules + SHAP)
```

## 3. Frontend Layering

```
index.html
  ├── gov-portal.css  (GOI chrome: a11y bar, national band, carousel,
  │                    schemes grid, stats, GOI footer, contrast mode)
  ├── gov-portal.js   (carousel autoplay/swipe, accessibility persistence,
  │                    quick-service deep links)   ← loaded BEFORE app logic
  ├── style.css       (application styles for tabs / cards / dynamic content)
  └── app.js          (advisory, doctor, voice, mandi radar, i18n, API_BASE)
```

The portal layer is strictly additive: `app.js` renders dynamic content into
existing IDs/classes, so the GOI skin never touches application logic — and the
app works with or without the portal chrome.

## 4. Data Honesty Contract

Every external-data response embeds a `source` field. Degradation is always
explicit, never cosmetic:

| Feed | Primary | Fallback 1 | Fallback 2 |
|---|---|---|---|
| Mandi prices | Agmarknet (data.gov.in) | Supabase snapshot | `estimated_fallback` (labelled) |
| NDVI | Sentinel-2 CDSE stats | — | `estimated` (labelled) |
| Soil | SoilGrids live | 18-hub cache (labelled) | — |
| Weather | Open-Meteo live | 18-hub cache (labelled) | — |
| Vision DX | MobileNetV2 (PlantVillage) | ICAR symptom triage (`confidence: null`) | — |

