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

---

## 6. Track A Edge Node Deployment (Raspberry Pi 4 Maker Build)

To run the field-level IoT and automated irrigation daemon on a Raspberry Pi 4:

```bash
# 1. SSH into Raspberry Pi 4 (Raspberry Pi OS 64-bit)
ssh pi@<raspberry-pi-ip>

# 2. Clone repository & install edge dependencies
cd ~
git clone https://github.com/rajat9para/kisan_sathi-crop-prediction-through-ai-and-many-more-.git
cd kisan_sathi-crop-prediction-through-ai-and-many-more-
pip install -r edge_node/requirements-edge.txt

# 3. Verify hardware GPIO connections (5V Relay on BCM 23, DHT22 on BCM 4)
python edge_node/smart_irrigation.py --status

# 4. Start the autonomous Edge Monitoring Daemon
python edge_node/edge_daemon.py --interval 10 --cloud-url http://localhost:8000

# 5. Enable systemd daemon for 24/7 autonomous field operation
sudo cp edge_node/kisan-edge.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now kisan-edge
```

---

## 7. Track B Qualcomm RB3 Gen 2 Dev Kit Deployment (Hexagon NPU)

For deployment on Qualcomm Dragonwing RB3 Gen 2 (QCS6490 SoC with 12 TOPS NPU):

```bash
# 1. Connect via ADB to Qualcomm RB3 Gen 2 Dev Kit
adb connect <rb3-device-ip>:5555
adb root && adb remount

# 2. Quantize MobileNetV2 with Qualcomm AI Hub CLI
pip install qai-hub
python -c "
import qai_hub as hub
import torchvision.models as models
model = models.mobilenet_v2(weights=None)
compile_job = hub.submit_compile_job(
    model=model,
    device=hub.Device('Qualcomm Dragonwing RB3 Gen 2'),
    options='--target_runtime qnn_lib --target_architecture hexagon_v68'
)
"

# 3. Push QNN DLC container to RB3 target and verify 6.1 ms inference latency
python edge_node/qualcomm_rb3_benchmarks.py
```

