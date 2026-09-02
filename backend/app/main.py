import asyncio
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import config
from app.routers import advisory, soil, weather, market, voice, ocr, doctor, iot, satellite
from app.services.supabase_client import supabase_service

app = FastAPI(
    title=config.API_TITLE,
    version=config.API_VERSION,
    description=config.API_DESCRIPTION
)

# CORS: explicit origins (wildcard "*" combined with credentials is invalid per
# the Fetch spec and rejected by browsers). Configure extra origins via the
# ALLOWED_ORIGINS env var (comma-separated), e.g. your Vercel frontend URL.
_allowed_origins = [
    o.strip() for o in os.getenv("ALLOWED_ORIGINS", "").split(",") if o.strip()
]
_DEFAULT_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "https://kisaansathicroppredictionaiandmanym.vercel.app",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_DEFAULT_ORIGINS + _allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(advisory.router)
app.include_router(doctor.router)
app.include_router(soil.router)
app.include_router(weather.router)
app.include_router(market.router)
app.include_router(voice.router)
app.include_router(ocr.router)
app.include_router(iot.router)
app.include_router(satellite.router)

import os
from typing import Optional
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse, Response
from fastapi.staticfiles import StaticFiles

def find_static_file(filename: str) -> Optional[str]:
    """
    Bulletproof static file finder that checks all possible paths across
    local environments, Docker, and Vercel Serverless Lambda runtime.
    """
    candidates = [
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "public", filename),
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public", filename),
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", filename),
        os.path.join(os.getcwd(), "public", filename),
        os.path.join(os.getcwd(), filename),
        os.path.join("/var", "task", "public", filename),
        os.path.join("/var", "task", filename),
    ]
    for path in candidates:
        if os.path.exists(path) and os.path.isfile(path):
            return path
    return None

# Mount static directory if found
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
public_dir = os.path.join(current_dir, "..", "public")
if not os.path.exists(public_dir):
    public_dir = os.path.join(current_dir, "public")
if os.path.exists(public_dir):
    app.mount("/static", StaticFiles(directory=public_dir), name="static")

@app.get("/style.css")
async def get_style():
    p = find_static_file("style.css")
    if p:
        with open(p, "r", encoding="utf-8") as f:
            return Response(content=f.read(), media_type="text/css")
    return Response(content="/* CSS file not found */", media_type="text/css", status_code=200)

@app.get("/app.js")
async def get_app_js():
    p = find_static_file("app.js")
    if p:
        with open(p, "r", encoding="utf-8") as f:
            return Response(content=f.read(), media_type="application/javascript")
    return Response(content="// JS file not found", media_type="application/javascript", status_code=200)

@app.get("/kisaan_sathi_avatar.png")
async def get_avatar():
    p = find_static_file("kisaan_sathi_avatar.png")
    if p:
        return FileResponse(p, media_type="image/png")
    return Response(status_code=404)

@app.get("/hero_farmer_banner.png")
async def get_hero_banner():
    p = find_static_file("hero_farmer_banner.png")
    if p:
        return FileResponse(p, media_type="image/png")
    return Response(status_code=404)

@app.get("/swasth_dhara_banner.png")
async def get_swasth_banner():
    p = find_static_file("swasth_dhara_banner.png")
    if p:
        return FileResponse(p, media_type="image/png")
    return Response(status_code=404)

@app.get("/gov-portal.css")
async def get_gov_css():
    p = find_static_file("gov-portal.css")
    if p:
        with open(p, "r", encoding="utf-8") as f:
            return Response(content=f.read(), media_type="text/css")
    return Response(content="/* not found */", media_type="text/css", status_code=200)

@app.get("/gov-portal.js")
async def get_gov_js():
    p = find_static_file("gov-portal.js")
    if p:
        with open(p, "r", encoding="utf-8") as f:
            return Response(content=f.read(), media_type="application/javascript")
    return Response(content="// not found", media_type="application/javascript", status_code=200)

@app.get("/static/{file_path:path}")
async def serve_static_file(file_path: str):
    p = find_static_file(file_path)
    if p:
        return FileResponse(p)
    return Response(status_code=404)

@app.get("/", response_class=HTMLResponse)
async def root():
    p = find_static_file("index.html")
    if p:
        with open(p, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read(), status_code=200)
    return HTMLResponse(content="""
        <!DOCTYPE html>
        <html>
        <head><title>Kisaan_Sathi AI</title></head>
        <body style="font-family: sans-serif; text-align: center; padding: 50px;">
            <h1>🌾 Kisaan_Sathi (किसान साथी) AI Engine Active</h1>
            <p>API is running smoothly. Visit <a href="/docs">/docs</a> for API documentation.</p>
        </body>
        </html>
    """, status_code=200)

@app.get("/api/status")
async def api_status():
    return {
        "app": "Kisaan_Sathi AI Backend",
        "version": config.API_VERSION,
        "status": "active",
        "llm_engine": f"Groq ({config.GROQ_MODEL})",
        "database": "Supabase PostgreSQL (Active & Keep-Alive Enabled)",
        "docs": "/docs"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "llm": "groq_connected",
        "supabase": "keep_alive_enabled"
    }

@app.get("/api/db-ping")
async def db_ping():
    """Explicit endpoint for Vercel Cron or uptime monitors to keep Supabase awake."""
    res = supabase_service.ping_keep_alive()
    return {
        "keep_alive": "triggered",
        "supabase_status": res
    }

