# 🚀 Deployment Guide — Kisaan_Sathi

This project deploys as **two independent services**:

```
┌─────────────────────┐         ┌──────────────────────────────┐
│  FRONTEND (static)  │  fetch  │   BACKEND (FastAPI + ML)     │
│  Vercel / static    │ ──────► │   Render / Railway / Fly.io  │
│  public/ folder     │         │   backend/Dockerfile         │
└─────────────────────┘         └──────────────┬───────────────┘
                                               │
                                    ┌──────────▼──────────┐
                                    │  Supabase Postgres  │
                                    └─────────────────────┘
```

> ⚠️ **Why not Vercel serverless for the backend?** The ML stack (PyTorch +
> SHAP + XGBoost + model artifacts) exceeds Vercel's 250 MB serverless bundle
> limit. A container platform (Render/Railway/Fly.io) is required.

---

## 1. One-time: Supabase schema

Open your Supabase dashboard → **SQL Editor** → paste and run
[`supabase_schema.sql`](supabase_schema.sql). This creates:

- `mandi_price_history` — real Agmarknet daily snapshots + 7-day trend source
- `iot_telemetry` — durable IoT sensor history
- `crop_recommendations`, `disease_scans`, `app_keepalive` — advisory history

## 2. Backend on Render (free tier works, "Starter" recommended for RAM)

1. Push this repo to GitHub.
2. On [render.com](https://render.com) → **New → Blueprint** → select the repo
   (Render reads `render.yaml`), **or** create a Web Service manually with:
   - **Root directory**: `backend`
   - **Runtime**: Docker
   - **Health check path**: `/health`
3. Set environment variables (from `.env.example`):
   `GROQ_API_KEY`, `DATA_GOV_API_KEY`, `CDSE_CLIENT_ID`, `CDSE_CLIENT_SECRET`,
   `SUPABASE_URL`, `SUPABASE_KEY`, `ALLOWED_ORIGINS=https://<your-vercel-url>`
4. Deploy. Note the service URL, e.g. `https://kisaan-sathi-api.onrender.com`.
5. Verify: `curl https://<render-url>/api/status` → `{"status": "active", ...}`

**Keeping Supabase awake**: point an uptime monitor (cron-job.org, UptimeRobot)
at `https://<render-url>/api/db-ping` once per day, or schedule it on the
Render paid tier's cron.

## 3. Frontend on Vercel (static PWA)

1. Import the repo on Vercel. `vercel.json` sets `outputDirectory: public`.
2. Point the frontend at your backend — pick ONE:
   - **Option A (recommended)**: after deploying the frontend once, open your
     PWA at `https://<your-vercel-url>/?api=https://<render-url>` once — the
     base URL is remembered in localStorage.
   - **Option B**: hardcode it — in `public/app.js` set:
     ```js
     window.KISAAN_API_BASE = "https://<render-url>";
     ```
3. Redeploy.

## 4. Local development (everything on one origin — zero config)

```bash
pip install -r backend/requirements.txt
python backend/run.py
# open http://localhost:8000 — the backend serves the frontend,
# so relative /api/* calls just work with no configuration.
```

## 5. Retraining the vision model

```bash
# 1. Download PlantVillage (2.1 GB, once) and extract the 7 trainable classes:
python -c "from huggingface_hub import snapshot_download; \
  snapshot_download('mohanty/PlantVillage', repo_type='dataset', \
  local_dir='ml_training/hf', allow_patterns=['data.zip'])"
# unzip ml_training/hf/data.zip -> ml_training/extracted/raw/color

# 2. Train (frozen-backbone head fine-tuning; ~10 min on a modern CPU):
python backend/ml/train_vision.py --epochs 8 --batch 64 --img-size 160 \
  --data-root ml_training/extracted/raw/color
```

Artifacts exported to `backend/ml/artifacts/`: retrained weights,
`vision_evaluation_metrics.json` (per-class F1 + confusion matrix) and
`vision_training_history.json` (per-epoch loss/accuracy curve).
