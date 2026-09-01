"""
AgriSaathi Backend Unit & Integration Tests
Tests all endpoints including Groq LLM and Supabase Keep-Alive.
"""

import sys
import os

# Ensure backend directory is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_frontend():
    res = client.get("/")
    assert res.status_code == 200
    assert "Kisaan_Sathi" in res.text or "किसान साथी" in res.text
    print("[PASS] GET / -> Indian Agriculture Theme Web Frontend Served Successfully")

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"
    print("[PASS] GET /health")

def test_db_ping():
    res = client.get("/api/db-ping")
    assert res.status_code == 200
    data = res.json()
    assert "keep_alive" in data
    print(f"[PASS] GET /api/db-ping -> Supabase Heartbeat Active: {data['supabase_status']['message']}")

def test_recommendation_nashik():
    payload = {
        "latitude": 19.9975,
        "longitude": 73.7898,
        "state": "Maharashtra",
        "district": "Nashik",
        "farm_size_acres": 3.0,
        "irrigation_source": "Borewell",
        "previous_crop": "Cotton"
    }
    res = client.post("/api/recommend", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "top_recommendations" in data
    assert len(data["top_recommendations"]) > 0
    top = data["top_recommendations"][0]
    assert "crop_name" in top
    assert "match_score_pct" in top
    assert "shap_contributions" in top
    print(f"[PASS] POST /api/recommend -> Top Crop: {top['crop_name']} ({top['match_score_pct']}%)")

def test_soil_endpoint():
    res = client.get("/api/soil?lat=19.9975&lon=73.7898")
    assert res.status_code == 200
    data = res.json()
    assert "ph" in data
    print(f"[PASS] GET /api/soil -> pH: {data['ph']}")

def test_weather_endpoint():
    res = client.get("/api/weather?lat=19.9975&lon=73.7898")
    assert res.status_code == 200
    data = res.json()
    assert "current_temp_c" in data
    print(f"[PASS] GET /api/weather -> Temp: {data['current_temp_c']}C")

def test_market_endpoint():
    res = client.get("/api/market-prices?state=Maharashtra&district=Nashik")
    assert res.status_code == 200
    data = res.json()
    assert len(data["prices"]) > 0
    print(f"[PASS] GET /api/market-prices -> Commodities: {len(data['prices'])}")

def test_voice_query_groq():
    payload = {
        "query_text": "इसके लिए पानी कितना चाहिए?",
        "language": "hi",
        "crop_context": "Soybean",
        "location_context": "Nashik"
    }
    res = client.post("/api/voice/query", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "response_text_hi" in data
    assert "tts_audio_text" in data
    print(f"[PASS] POST /api/voice/query -> Groq LLM Reply: {data['response_text_hi'][:50]}...")

def test_ocr_soil_card():
    payload = {
        "sample_preset": "sample_1_nashik"
    }
    res = client.post("/api/ocr/soil-card", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["farmer_name"] == "#SHC-MH-4012"
    print(f"[PASS] POST /api/ocr/soil-card -> Soil Card ID: {data['farmer_name']}")

if __name__ == "__main__":
    print("--- Running Kisaan_Sathi Backend Integration Tests ---")
    test_root_frontend()
    test_health()
    test_db_ping()
    test_recommendation_nashik()
    test_soil_endpoint()
    test_weather_endpoint()
    test_market_endpoint()
    test_voice_query_groq()
    test_ocr_soil_card()
    print("--- ALL 9 BACKEND & FRONTEND TESTS PASSED CONFIDENTLY! ---")
