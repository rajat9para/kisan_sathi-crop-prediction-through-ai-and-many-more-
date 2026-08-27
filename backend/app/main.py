import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import config
from app.routers import advisory, soil, weather, market, voice, ocr
from app.services.supabase_client import supabase_service

app = FastAPI(
    title=config.API_TITLE,
    version=config.API_VERSION,
    description=config.API_DESCRIPTION
)

# Enable CORS for Flutter Web, Android Emulators, and Vercel clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(advisory.router)
app.include_router(soil.router)
app.include_router(weather.router)
app.include_router(market.router)
app.include_router(voice.router)
app.include_router(ocr.router)

@app.get("/")
async def root():
    return {
        "app": "Kisaan_Sathi AI Backend",
        "version": config.API_VERSION,
        "status": "active",
        "llm_engine": f"Groq ({config.GROQ_MODEL})",
        "database": "Supabase PostgreSQL (Active & Keep-Alive Enabled)",
        "docs": "/docs",
        "demo_hubs": ["Nashik (MH)", "Indore (MP)", "Ludhiana (PB)", "Guntur (AP)"]
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
