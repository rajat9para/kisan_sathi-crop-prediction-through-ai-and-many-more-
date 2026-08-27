<div align="center">

<img src="docs/assets/kisaan_sathi_avatar.png" width="180" height="180" alt="Kisaan Sathi AI Avatar" style="border-radius: 50%; box-shadow: 0 8px 24px rgba(19, 117, 71, 0.25);" />

# 🌾 Kisaan_Sathi (किसान साथी)
### AI-Powered Hyper-Local, Explainable Crop Advisory & Diagnostics System
**Hybrid ML + Groq LLaMA LLM • Vercel Serverless • Supabase PostgreSQL (Anti-Sleep Active)**

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI%20v0.110-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com)
[![Flutter](https://img.shields.io/badge/Mobile-Flutter%203.41%20%7C%20Dart%203.11-02569B.svg?logo=flutter)](https://flutter.dev)
[![XGBoost](https://img.shields.io/badge/ML%20Engine-XGBoost%2099.09%25-FF6F00.svg)](https://xgboost.readthedocs.io)
[![SHAP](https://img.shields.io/badge/Explainability-SHAP%20TreeExplainer-4CAF50.svg)](https://shap.readthedocs.io)
[![Groq LLM](https://img.shields.io/badge/LLM%20Engine-Groq%20LLaMA%203.1-F55036.svg)](https://groq.com)
[![Supabase](https://img.shields.io/badge/Database-Supabase%20PostgreSQL-3ECF8E.svg?logo=supabase)](https://supabase.com)
[![Vercel](https://img.shields.io/badge/Deploy-Vercel%20Serverless-000000.svg?logo=vercel)](https://vercel.com)

</div>

---

## 📌 1. Executive Summary & Problem Context

Small and marginal farmers across India face severe agricultural uncertainty due to changing micro-climates, soil degradation, fluctuating mandi prices, and delayed advisory. Existing solutions provide generic district-level suggestions, operate as opaque black-box models, lack regional language support, and critically fail when internet connectivity drops in remote fields.

**Kisaan_Sathi (किसान साथी)** solves this through a **Hybrid AI Architecture**:
1. **Deterministic Machine Learning (XGBoost + SHAP)**: Computes multi-class crop ranking and mathematical feature force vectors with 99.09% accuracy.
2. **Conversational Synthesis (Groq LLaMA 3.1 LLM)**: Translates technical metrics into warm, respectful Hindi farmer guidance and dynamic spray timing.
3. **Cloud & Anti-Sleep Resilience (Vercel + Supabase)**: Serverless backend with automated database heartbeat keep-alive so the database never goes to sleep.
4. **Offline-First Mobile Client (Flutter)**: 100% on-device disease diagnosis, cached advisory, and background auto-sync.

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
│  Vercel Serverless Backend   │                               │ SharedPreferences / SQLite   │
│ (FastAPI + Groq LLaMA LLM)   │                               │ Persistent Cache & History   │
└─────────────┬────────────────┘                               └──────────────┬───────────────┘
              │                                                               │
 ┌────────────┼────────────┬─────────────┬─────────────┐                      │
 ▼            ▼            ▼             ▼             ▼                      ▼
SoilGrids  Open-Meteo  Agmarknet    XGBoost +       Supabase         Offline Advisory,
REST API    Weather      Mandi        SHAP          PostgreSQL       SHAP Visuals &
(ISRIC)     Forecast     Trends      Engine        (Keep-Alive)      On-Device Leaf AI
```

---

## 🧠 3. Hybrid AI: ML Prediction + Groq LLM Synthesis

```
[Raw Soil + Weather Data]
           │
           ▼
┌────────────────────────────────────────────────────────┐
│ 1. XGBOOST ML ENGINE + SHAP EXPLAINER (The Brain)      │
│    - Rank #1: Grapes (94.8% Match)                     │
│    - SHAP: Potash (+28%), pH (+18%), Rain (-4%)        │
│    - Mandi Price: ₹6,200/Qtl (Trending Up)             │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ 2. GROQ LLAMA LLM ADVISOR (Conversational Intelligence)│
│    Grounded strictly on XGBoost numbers & forecast:    │
│    "Generate 3-sentence Hindi voice advisory"          │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ 3. FARMER AUDIO / TEXT OUTPUT (Voice Saathi)           │
│    "रामेश्वर जी, आपकी मिट्टी में पोटाश बहुत अच्छा है,  │
│     इसलिए अंगूर सबसे उत्तम है। पर शनिवार को बारिश है, │
│     इसलिए छिड़काव रविवार सुबह ही करें।"              │
└────────────────────────────────────────────────────────┘
```

---

## 🗄️ 4. Supabase Database & Anti-Sleep Keep-Alive System

Free-tier cloud databases often pause or enter sleep mode after inactivity. Kisaan_Sathi solves this with an **Automated Anti-Sleep Heartbeat Engine**:

1. **Heartbeat Table (`app_keepalive`)**: Automatically created in Supabase PostgreSQL.
2. **Periodic Keep-Alive Ping**:
   - Every 6 hours, the backend background worker touches the Supabase database.
   - Vercel Cron automatically calls `GET /api/db-ping` twice daily (`0 */12 * * *`).
3. **Database Schema**:
   - `app_keepalive`: Heartbeat timestamp and health status.
   - `crop_recommendations`: Saved farmer queries, soil parameters, top crops, and SHAP vectors.
   - `disease_scans`: Leaf photo diagnostic records with confidence scores.

To set up the tables in Supabase, execute [`backend/supabase_schema.sql`](file:///c:/SmartIndiaHackathon/backend/supabase_schema.sql) in your **Supabase Dashboard -> SQL Editor**.

---

## ☁️ 5. Vercel Hosting & Environment Variables Guide

To host Kisaan_Sathi on **Vercel**, follow these steps:

### Step 1: Import Repository to Vercel
1. Go to [vercel.com](https://vercel.com) and click **"Add New Project"**.
2. Select your GitHub repository: `kisan_sathi-crop-prediction-through-ai-and-many-more-`.
3. Vercel will automatically detect `vercel.json` and the Python serverless runtime.

### Step 2: Fill Environment Variables in Vercel Dashboard
In **Project Settings -> Environment Variables**, add the following key-value pairs:

| Variable Name | Example / Where to find | Purpose |
|---|---|---|
| `GROQ_API_KEY` | `gsk_...` (from console.groq.com) | Groq LLaMA ultra-fast inference |
| `GROQ_MODEL` | `llama-3.1-8b-instant` | Default conversational LLM model |
| `SUPABASE_URL` | `https://<project-id>.supabase.co` | Supabase Cloud Database URL |
| `SUPABASE_KEY` | `sb_secret_...` (Service Role Secret) | Supabase Serverless DB Admin Key |
| `SUPABASE_PUBLISHABLE_KEY` | `sb_publishable_...` (Anon Key) | Supabase Client Anon Key |
| `SUPABASE_JWKS_URL` | `https://<project-id>.supabase.co/auth/v1/...` | Auth JWKS Endpoint |

*(These are also documented in [`.env.example`](file:///c:/SmartIndiaHackathon/.env.example))*

### Step 3: Deploy
Click **"Deploy"**. Vercel will deploy:
- `/api/*` $\rightarrow$ Serverless FastAPI backend with XGBoost, SHAP, and Groq LLM.
- `/api/db-ping` $\rightarrow$ Scheduled keep-alive cron keeping Supabase warm 24/7.

---

## 📱 6. Technology Stack

| Layer | Component | Description |
|---|---|---|
| **Mobile Client** | **Flutter (Dart 3.11)** | Android, Windows, and Web offline-first interface with rural-tech styling. |
| **Serverless Backend** | **FastAPI on Vercel** | Asynchronous Python microservice hosting ML models, Groq LLM, and API aggregators. |
| **Prediction Engine** | **XGBoost Classifier (99.09%)** | Deterministic 22-class crop recommendation model. |
| **Explainable AI (XAI)** | **SHAP TreeExplainer** | Mathematical feature attribution for every nutrient. |
| **Conversational LLM** | **Groq LLaMA 3.1** | Real-time Hindi & English voice assistance and spray planning. |
| **Cloud Database** | **Supabase PostgreSQL** | Cloud storage for recommendation history with automated anti-sleep keep-alive. |
| **Offline Leaf AI** | **On-Device MobileNet** | Instant on-device blight and pathogen vision classification. |

---

<div align="center">
  <sub>Built with ❤️ for Indian Agriculture and Smart India Hackathon</sub>
</div>
