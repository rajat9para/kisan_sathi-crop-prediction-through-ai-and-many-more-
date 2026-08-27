"""
Kisaan_Sathi 11-Soil & 11-Language Comprehensive Verification Suite
Tests all 11 Indian Soil Presets, Regional Hubs, ML Recommendations,
OCR Presets, Weather, Mandi, Multi-lingual Voice, and Supabase Keep-Alive.
"""

import sys
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

SOIL_PRESETS = [
    ("sample_1_nashik", "Maharashtra", "Nashik", "Medium Black Cotton (Regur) Loam", 85, 48, 190, 6.8),
    ("sample_2_indore", "Madhya Pradesh", "Indore", "Deep Black Malwa Vertisol Clay", 45, 62, 82, 7.4),
    ("sample_3_ludhiana", "Punjab", "Ludhiana", "Indo-Gangetic Alluvial Sandy Loam", 92, 42, 38, 7.2),
    ("sample_4_guntur", "Andhra Pradesh", "Guntur", "Coastal Red Clayey Sandy Loam", 70, 55, 140, 6.5),
    ("sample_5_rajkot", "Gujarat", "Rajkot", "Saurashtra Medium Black Calcareous Loam", 58, 64, 165, 7.8),
    ("sample_6_thanjavur", "Tamil Nadu", "Thanjavur", "Cauvery Deltaic Alluvial Silt Clay", 88, 36, 95, 6.7),
    ("sample_7_bardhaman", "West Bengal", "Bardhaman", "Lower Gangetic Old Alluvial Clay Loam", 95, 32, 88, 6.2),
    ("sample_8_jaipur", "Rajasthan", "Jaipur", "Semi-Arid Desert Light Sandy Loam", 32, 28, 120, 8.2),
    ("sample_9_dharwad", "Karnataka", "Dharwad", "Western Ghats Red Laterite Loam", 75, 46, 115, 6.4),
    ("sample_10_varanasi", "Uttar Pradesh", "Varanasi", "Eastern Gangetic Silt Alluvial", 82, 52, 68, 7.1),
    ("sample_11_palakkad", "Kerala", "Palakkad", "High-Rainfall Acidic Peaty Laterite", 68, 24, 75, 5.4),
]

LANGUAGES = ["hi", "en", "mr", "pa", "te", "ta", "gu", "bn", "kn", "ml", "or"]

def run_tests():
    print("=" * 70)
    print("RUNNING KISAAN_SATHI 11-SOIL & 11-LANGUAGE COMPREHENSIVE VERIFICATION")
    print("=" * 70)
    passed = 0
    total = 0

    # 1. Test Root and Health
    print("\n[1] Testing Root & Core Health Endpoints:")
    for path in ["/", "/health", "/api/db-ping"]:
        total += 1
        res = client.get(path)
        assert res.status_code == 200, f"Failed on {path}: {res.status_code}"
        print(f"  [PASS] GET {path:20} -> 200 OK")
        passed += 1

    # 2. Test All 11 Soil Presets via OCR
    print("\n[2] Testing All 11 Indian Soil Health Card Presets:")
    for pid, state, dist, texture, n, p, k, ph in SOIL_PRESETS:
        total += 1
        res = client.post("/api/ocr/soil-card", json={"sample_preset": pid})
        assert res.status_code == 200, f"OCR failed for {pid}: {res.status_code}"
        data = res.json()
        params = data.get("parameters", {})
        assert params.get("nitrogen") == n
        assert params.get("phosphorus") == p
        assert params.get("potassium") == k
        assert params.get("ph") == ph
        print(f"  [PASS] Soil Card: {pid:22} -> {texture} (N:{n}, P:{p}, K:{k}, pH:{ph})")
        passed += 1

    # 3. Test Crop Recommendations across All 11 Regions & Soils
    print("\n[3] Testing XGBoost + Agronomic Crop Recommendations for All 11 Hubs:")
    for pid, state, dist, texture, n, p, k, ph in SOIL_PRESETS:
        total += 1
        payload = {
            "latitude": 20.0,
            "longitude": 75.0,
            "state": state,
            "district": dist,
            "farm_size_acres": 2.5,
            "irrigation_source": "Borewell",
            "previous_crop": "Cotton",
            "custom_soil": {
                "nitrogen": n,
                "phosphorus": p,
                "potassium": k,
                "ph": ph
            }
        }
        res = client.post("/api/recommend", json=payload)
        assert res.status_code == 200, f"Recommend failed for {dist}: {res.status_code}"
        data = res.json()
        assert "top_recommendations" in data
        assert len(data["top_recommendations"]) > 0
        top = data["top_recommendations"][0]
        print(f"  [PASS] Recommendation: {dist:12} ({state:15}) -> Top Crop: {top.get('crop_name')} (Score: {top.get('match_score_pct')}%)")
        passed += 1

    # 4. Test Weather, SoilGrids, and Mandi Endpoints
    print("\n[4] Testing Live Weather, Soil & Mandi Endpoints:")
    for ep, name in [
        ("/api/weather?latitude=19.9975&longitude=73.7898", "Open-Meteo Weather"),
        ("/api/soil?latitude=19.9975&longitude=73.7898", "SoilGrids ISRIC Soil"),
        ("/api/market-prices?state=Maharashtra&district=Nashik", "Agmarknet APMC Prices")
    ]:
        total += 1
        res = client.get(ep)
        assert res.status_code == 200, f"Failed on {ep}"
        print(f"  [PASS] API Endpoint: {name:25} -> 200 OK")
        passed += 1

    # 5. Test Voice Saathi Queries across All 11 Indian Languages
    print("\n[5] Testing Conversational Voice Queries Across 11 Indian Languages:")
    for lang in LANGUAGES:
        total += 1
        res = client.post("/api/voice/query", json={
            "query_text": "पानी कितना देना चाहिए?",
            "language": lang,
            "crop_context": "Wheat",
            "location_context": "Varanasi, Uttar Pradesh"
        })
        assert res.status_code == 200
        data = res.json()
        assert "response_text_hi" in data
        print(f"  [PASS] Voice Query [{lang.upper():2}]: Response received with confidence {data.get('confidence')}")
        passed += 1

    # 6. Test Static Assets Serving
    print("\n[6] Testing Static Assets Route Handlers for Vercel/Local Delivery:")
    for asset in ["/style.css", "/app.js", "/kisaan_sathi_avatar.png"]:
        total += 1
        res = client.get(asset)
        assert res.status_code == 200, f"Failed to serve {asset}"
        print(f"  [PASS] Static Asset: {asset:25} -> 200 OK ({len(res.content)} bytes)")
        passed += 1

    print("\n" + "=" * 70)
    print(f"ALL TESTS COMPLETED: {passed}/{total} PASSED (100% SUCCESS RATE)")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
