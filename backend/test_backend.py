"""
AgriSaathi Backend Unit & Integration Tests
Uses FastAPI TestClient to test all endpoints locally before starting server.
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

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"
    print("[PASS] GET /health")

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
    assert len(top["shap_contributions"]) == 7
    print(f"[PASS] POST /api/recommend -> Top Crop: {top['crop_name']} ({top['match_score_pct']}%), SHAP count: {len(top['shap_contributions'])}")

def test_soil_endpoint():
    res = client.get("/api/soil?lat=19.9975&lon=73.7898")
    assert res.status_code == 200
    data = res.json()
    assert "ph" in data
    assert "nitrogen" in data
    print(f"[PASS] GET /api/soil -> pH: {data['ph']}, N: {data['nitrogen']}")

def test_weather_endpoint():
    res = client.get("/api/weather?lat=19.9975&lon=73.7898")
    assert res.status_code == 200
    data = res.json()
    assert "current_temp_c" in data
    assert "forecast_7d" in data
    print(f"[PASS] GET /api/weather -> Temp: {data['current_temp_c']}C, Forecast Days: {len(data['forecast_7d'])}")

def test_market_endpoint():
    res = client.get("/api/market-prices?state=Maharashtra&district=Nashik")
    assert res.status_code == 200
    data = res.json()
    assert len(data["prices"]) > 0
    print(f"[PASS] GET /api/market-prices -> Found {len(data['prices'])} mandi commodities")

def test_voice_query():
    payload = {
        "query_text": "इसके लिए पानी कितना चाहिए?",
        "language": "hi"
    }
    res = client.post("/api/voice/query", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["detected_intent"] == "water"
    assert "tts_audio_text" in data
    print(f"[PASS] POST /api/voice/query -> Intent: {data['detected_intent']}, TTS: {data['tts_audio_text'][:40]}...")

def test_ocr_soil_card():
    payload = {
        "sample_preset": "sample_1_nashik"
    }
    res = client.post("/api/ocr/soil-card", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["farmer_name"] == "Ramesh Kisan Patil"
    assert data["parameters"]["ph"] == 6.8
    print(f"[PASS] POST /api/ocr/soil-card -> Farmer: {data['farmer_name']}, pH: {data['parameters']['ph']}")

if __name__ == "__main__":
    print("--- Running AgriSaathi Backend Integration Tests ---")
    test_health()
    test_recommendation_nashik()
    test_soil_endpoint()
    test_weather_endpoint()
    test_market_endpoint()
    test_voice_query()
    test_ocr_soil_card()
    print("--- ALL 7 BACKEND TESTS PASSED! ---")
