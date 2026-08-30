"""
AgriSaathi Comprehensive Automated Service & API Test Suite
Covers:
- XGBoost & SHAP Machine Learning Recommendation Engine
- Dynamic Yield, Cost, and Net Profit Forecasting
- Quantitative 4-Pillar Sustainability Scoring (0-100)
- Crop-Specific Agronomic Fertilizer & Irrigation Schedules
- PyTorch MobileNetV2 Leaf Pathology Classifier & Input Validation
- Soil Health Card OCR Parser & Fertility Classifier
- Open-Meteo Volumetric Soil Moisture & APMC Mandi Prices
- IoT Telemetry Ingestion Node & Optical NPK Conversions
- Sentinel-2 Satellite NDVI Earth Observation Service
- FastAPI Endpoints via TestClient
"""

import os
import sys
import io
from PIL import Image
import numpy as np
from fastapi.testclient import TestClient

# Add backend directory to sys.path
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from app.main import app
from app.services.ml_engine import ml_engine
from app.services.disease_classifier import disease_classifier
from app.services.ocr_engine import ocr_engine
from app.services.satellite_service import satellite_service
from app.services.external_apis import fetch_market_prices, fetch_soilgrids_data, fetch_weather_data

client = TestClient(app)


def test_ml_engine_loaded_and_recommends():
    """Verify XGBoost + SHAP inference and ranking."""
    features = {
        "N": 80.0, "P": 45.0, "K": 40.0,
        "temperature": 25.0, "humidity": 80.0,
        "ph": 6.5, "rainfall": 200.0
    }
    recs = ml_engine.recommend_crops(features=features, previous_crop=None, irrigation="Borewell", top_k=3)
    assert len(recs) == 3
    assert recs[0]["rank"] == 1
    assert "crop_name" in recs[0]
    assert "match_score_pct" in recs[0]
    assert len(recs[0]["shap_contributions"]) == 7


def test_dynamic_yield_and_net_profit_forecasting():
    """Verify dynamic economics change with soil and weather fit."""
    econ_optimal = ml_engine.calculate_dynamic_yield_and_economics("chickpea", soil_fit_pct=95.0, weather_fit_pct=95.0, farm_size_acres=2.5)
    econ_suboptimal = ml_engine.calculate_dynamic_yield_and_economics("chickpea", soil_fit_pct=50.0, weather_fit_pct=50.0, farm_size_acres=2.5)

    assert econ_optimal["min_yield"] > econ_suboptimal["min_yield"]
    assert econ_optimal["estimated_net_profit_per_acre_rs"] > econ_suboptimal["estimated_net_profit_per_acre_rs"]
    assert "Quintals" in econ_optimal["expected_yield_per_acre"]


def test_sustainability_score_calculation():
    """Verify sustainability scoring differentiates legumes from heavy feeders."""
    features = {"N": 50.0, "P": 40.0, "K": 40.0, "temperature": 22.0, "humidity": 50.0, "ph": 6.5, "rainfall": 80.0}
    
    # Chickpea (Legume, low water, N-fixer)
    score_chickpea, rating_c, factors_c = ml_engine.calculate_sustainability_score("chickpea", features, previous_crop="wheat", irrigation="Drip")
    
    # Rice (High water, cereal)
    score_rice, rating_r, factors_r = ml_engine.calculate_sustainability_score("rice", features, previous_crop="rice", irrigation="Rainfed")

    assert score_chickpea >= 85.0
    assert score_chickpea > score_rice
    assert factors_c["biological_n_fixation"] is True
    assert factors_r["biological_n_fixation"] is False


def test_crop_specific_management_schedules():
    """Verify different crops receive distinct agronomic management schedules."""
    rice_fert, rice_irrig = ml_engine.generate_management_schedules("rice")
    cotton_fert, cotton_irrig = ml_engine.generate_management_schedules("cotton")
    grapes_fert, grapes_irrig = ml_engine.generate_management_schedules("grapes")

    assert rice_fert[0]["dosage"] != cotton_fert[0]["dosage"]
    assert "Pruning" in grapes_fert[0]["stage"] or "Pruning" in grapes_irrig[0]["timing"]
    assert len(rice_fert) >= 3
    assert len(cotton_irrig) >= 3


def test_pytorch_leaf_pathology_classifier_valid_image():
    """Verify PyTorch MobileNetV2 leaf disease classification on a generated leaf image."""
    img = Image.new("RGB", (224, 224), color=(34, 139, 34))
    arr = np.array(img)
    arr[50:100, 50:100] = [220, 200, 30] # Yellow
    arr[120:160, 120:160] = [139, 69, 19] # Brown
    test_img = Image.fromarray(arr)

    buf = io.BytesIO()
    test_img.save(buf, format="JPEG")
    image_bytes = buf.getvalue()

    diag = disease_classifier.diagnose_image(image_bytes=image_bytes, crop_hint="wheat", language="hi")
    assert diag.get("error") is not True
    assert "disease_name" in diag
    assert "confidence_pct" in diag
    assert diag["confidence_pct"] >= 75.0
    assert "organic_remedy" in diag
    assert "chemical_remedy" in diag


def test_leaf_classifier_rejects_blank_image():
    """Verify non-leaf / zero contrast image rejection."""
    blank_img = Image.new("RGB", (100, 100), color=(255, 255, 255))
    buf = io.BytesIO()
    blank_img.save(buf, format="JPEG")
    image_bytes = buf.getvalue()

    diag = disease_classifier.diagnose_image(image_bytes=image_bytes)
    assert diag.get("error") is True
    assert "contrast" in diag.get("message", "").lower() or "blank" in diag.get("message", "").lower()


def test_apmc_market_prices():
    """Verify APMC mandi price generator creates timestamped quotes with min/max spreads."""
    prices = fetch_market_prices(state="Maharashtra", district="Nashik")
    assert len(prices) > 0
    first = prices[0]
    assert first["modal_price_rs_quintal"] > 0
    assert first["min_price_rs_quintal"] <= first["modal_price_rs_quintal"]
    assert first["max_price_rs_quintal"] >= first["modal_price_rs_quintal"]
    assert first["arrival_date"] is not None
    assert first["trend_direction"] in ["up", "down", "stable"]


def test_ocr_parameter_parser():
    """Verify Soil Health Card OCR regex parser extracts N, P, K, pH values."""
    mock_shc_text = """
    Govt of India - Soil Health Card Scheme
    Farmer Name: Ramesh Patil
    Lab ID: MH-4012
    Available Nitrogen (N): 85.5 kg/ha
    Available Phosphorus (P): 48.0 kg/ha
    Available Potassium (K): 190.0 kg/ha
    Soil pH Value: 6.8
    Organic Carbon (OC): 0.72 %
    """
    params, status, conf = ocr_engine.parse_soil_parameters(mock_shc_text)
    assert params["nitrogen"] == 85.5
    assert params["phosphorus"] == 48.0
    assert params["potassium"] == 190.0
    assert params["ph"] == 6.8
    assert params["organic_carbon_pct"] == 0.72
    assert status["ph"] == "Neutral (Ideal)"
    assert conf >= 90.0


def test_iot_telemetry_endpoint():
    """Verify IoT telemetry ingestion and device caching."""
    payload = {
        "device_id": "ESP32-PROBE-TEST-01",
        "soil_moisture_pct": 36.5,
        "soil_temperature_c": 23.4,
        "soil_ph": 6.7,
        "nitrogen_ppm": 35.0,
        "phosphorus_ppm": 20.0,
        "potassium_ppm": 80.0,
        "battery_level_pct": 99.0
    }
    response = client.post("/api/iot/reading", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success_ingested"
    assert data["soil_moisture_pct"] == 36.5
    assert data["nitrogen_kg_ha"] == round(35.0 * 2.24, 1)

    # Verify querying latest reading
    get_res = client.get("/api/iot/latest/ESP32-PROBE-TEST-01")
    assert get_res.status_code == 200
    assert get_res.json()["device_id"] == "ESP32-PROBE-TEST-01"


def test_satellite_ndvi_service():
    """Verify Sentinel-2 NDVI canopy health computation."""
    data = satellite_service.get_parcel_ndvi(lat=19.9975, lon=73.7898)
    assert 0.1 <= data["mean_ndvi"] <= 1.0
    assert "vegetation_vigor_category" in data
    assert "advisory_recommendation_en" in data
    assert data["canopy_coverage_pct"] > 0


def test_fastapi_advisory_recommend_endpoint():
    """Verify /api/recommend returns complete response with dynamic economics & sustainability."""
    req_body = {
        "latitude": 19.9975,
        "longitude": 73.7898,
        "state": "Maharashtra",
        "district": "Nashik",
        "farm_size_acres": 3.0,
        "irrigation_source": "Drip",
        "previous_crop": "Wheat",
        "custom_soil": {
            "nitrogen": 80.0,
            "phosphorus": 45.0,
            "potassium": 160.0,
            "ph": 6.8,
            "organic_carbon_pct": 0.65,
            "texture": "Clay Loam",
            "soil_moisture_pct": 32.0
        },
        "custom_weather": {
            "temperature_c": 26.0,
            "humidity_pct": 72.0,
            "rainfall_mm": 85.0,
            "soil_moisture_pct": 32.0,
            "weather_condition": "Sunny"
        }
    }
    res = client.post("/api/recommend", json=req_body)
    assert res.status_code == 200
    data = res.json()
    assert len(data["top_recommendations"]) > 0
    top1 = data["top_recommendations"][0]
    assert "sustainability_score_pct" in top1
    assert "estimated_net_profit_per_acre_rs" in top1
    assert "expected_yield_per_acre" in top1
    assert len(top1["recommended_fertilizer_schedule"]) >= 3


def test_fastapi_sms_advisory_endpoint():
    """Verify SMS / USSD broadcast advisory generation."""
    req_body = {
        "phone_number": "9876543210",
        "crop_name": "Wheat",
        "language": "hi"
    }
    res = client.post("/api/advisory/sms-advisory", json=req_body)
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "ready_for_dispatch"
    assert "किसान साथी" in data["sms_text_hi"]


if __name__ == "__main__":
    tests = [
        ("1. XGBoost & SHAP ML Recommendation Engine", test_ml_engine_loaded_and_recommends),
        ("2. Dynamic Yield, Cost & Net Profit Forecasting", test_dynamic_yield_and_net_profit_forecasting),
        ("3. Quantitative 4-Pillar Sustainability Scoring", test_sustainability_score_calculation),
        ("4. Crop-Specific Agronomic Schedules", test_crop_specific_management_schedules),
        ("5. PyTorch MobileNetV2 Leaf Pathology Inference", test_pytorch_leaf_pathology_classifier_valid_image),
        ("6. Input Validation (Blank Image Rejection)", test_leaf_classifier_rejects_blank_image),
        ("7. Agmarknet APMC Mandi Price Generator", test_apmc_market_prices),
        ("8. Soil Health Card OCR Parameter Parser", test_ocr_parameter_parser),
        ("9. IoT Telemetry Ingestion Node", test_iot_telemetry_endpoint),
        ("10. Sentinel-2 Satellite NDVI Earth Observation", test_satellite_ndvi_service),
        ("11. FastAPI /api/recommend Endpoint", test_fastapi_advisory_recommend_endpoint),
        ("12. USSD / SMS Regional Advisory Gateway", test_fastapi_sms_advisory_endpoint),
    ]

    print("=" * 80)
    print("RUNNING AGRISAATHI COMPLETE SYSTEM VERIFICATION SUITE")
    print("=" * 80)
    passed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"[PASS] {name}")
            passed += 1
        except Exception as e:
            print(f"[FAIL] {name} -> {e}")

    print("=" * 80)
    print(f"RESULTS: {passed}/{len(tests)} TESTS PASSED ({passed / len(tests) * 100:.1f}%)")
    print("=" * 80)
    if passed == len(tests):
        sys.exit(0)
    else:
        sys.exit(1)
