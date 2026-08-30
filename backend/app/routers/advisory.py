from fastapi import APIRouter, HTTPException
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from app.models.schemas import RecommendationRequest, RecommendationResponse
from app.services.external_apis import fetch_soilgrids_data, fetch_weather_data, fetch_market_prices
from app.services.ml_engine import ml_engine
from app.services.demo_cache import find_nearest_hub

router = APIRouter(prefix="/api", tags=["Crop Advisory"])

class SMSAdvisoryRequest(BaseModel):
    phone_number: Optional[str] = "9876543210"
    crop_name: str = "Wheat"
    language: str = "hi" # "hi" or "en"
    state: Optional[str] = "Maharashtra"

class SMSAdvisoryResponse(BaseModel):
    status: str
    channel: str # "USSD / SMS Broadcast"
    sms_text_hi: str
    sms_text_en: str
    character_count: int
    broadcast_timestamp: str

@router.post("/recommend", response_model=RecommendationResponse)
async def get_crop_recommendations(req: RecommendationRequest):
    """
    Main endpoint for hyper-local explainable crop recommendations.
    Pulls real soil and weather (or uses custom overrides/IoT/fallback cache),
    runs XGBoost + SHAP feature importance, and returns ranked crops with explainability breakdown.
    """
    try:
        # 1. Soil Data
        if req.custom_soil:
            soil = {
                "ph": req.custom_soil.ph,
                "nitrogen": req.custom_soil.nitrogen,
                "phosphorus": req.custom_soil.phosphorus,
                "potassium": req.custom_soil.potassium,
                "organic_carbon_pct": req.custom_soil.organic_carbon_pct,
                "clay_content_pct": 35.0,
                "sand_content_pct": 30.0,
                "soil_moisture_pct": req.custom_soil.soil_moisture_pct or 32.0,
                "soil_type": req.custom_soil.texture or "Custom Soil Input",
                "source": "Farmer Soil Health Card / Manual Input"
            }
        else:
            soil = fetch_soilgrids_data(req.latitude, req.longitude)

        # 2. Weather Data
        if req.custom_weather:
            weather = {
                "current_temp_c": req.custom_weather.temperature_c,
                "current_humidity_pct": req.custom_weather.humidity_pct,
                "current_condition": req.custom_weather.weather_condition or "Custom Weather",
                "wind_speed_kmh": 10.0,
                "rainfall_7d_total_mm": req.custom_weather.rainfall_mm,
                "soil_moisture_pct": req.custom_weather.soil_moisture_pct or 32.0,
                "forecast_7d": []
            }
        else:
            weather = fetch_weather_data(req.latitude, req.longitude)

        # 3. Assemble ML Feature Vector (N, P, K, temp, humidity, ph, rainfall)
        features = {
            "N": float(soil.get("nitrogen", 70.0)),
            "P": float(soil.get("phosphorus", 45.0)),
            "K": float(soil.get("potassium", 40.0)),
            "temperature": float(weather.get("current_temp_c", 26.0)),
            "humidity": float(weather.get("current_humidity_pct", 70.0)),
            "ph": float(soil.get("ph", 6.8)),
            "rainfall": float(weather.get("rainfall_7d_total_mm", 75.0))
        }

        # 4. Run ML Inference, SHAP Calculation, Dynamic Economics & Sustainability Re-ranking
        recommendations = ml_engine.recommend_crops(
            features=features,
            previous_crop=req.previous_crop,
            irrigation=req.irrigation_source or "Borewell",
            farm_size_acres=req.farm_size_acres or 2.5,
            top_k=4
        )

        # Warnings / Actionable alerts
        warnings = []
        if soil.get("ph", 7.0) > 8.0:
            warnings.append({
                "title_en": "High Soil Alkalinity",
                "title_hi": "मिट्टी में क्षारीयता अधिक है",
                "desc_en": "Gypsum application (100 kg/acre) recommended before sowing to balance pH.",
                "desc_hi": "पीएच संतुलित करने के लिए बुवाई से पहले 100 किग्रा/एकड़ जिप्सम डालने की सलाह दी जाती है।"
            })
        if weather.get("rainfall_7d_total_mm", 0) > 100:
            warnings.append({
                "title_en": "Heavy Rain Alert (Next 7 Days)",
                "title_hi": "भारी बारिश का अलर्ट (अगले 7 दिन)",
                "desc_en": "Ensure proper drainage channels in fields to prevent waterlogging.",
                "desc_hi": "खेत में जलभराव से बचने के लिए उचित जल निकासी नालियां सुनिश्चित करें।"
            })
        if weather.get("soil_moisture_pct", 30) < 18.0:
            warnings.append({
                "title_en": "Low Soil Moisture Warning",
                "title_hi": "मिट्टी में नमी की कमी",
                "desc_en": "Soil volumetric moisture is critically low (<18%). Schedule light irrigation before sowing.",
                "desc_hi": "मिट्टी की नमी 18% से कम है। बुवाई से पहले पलेवा या हल्की सिंचाई करें।"
            })

        is_cached = find_nearest_hub(req.latitude, req.longitude) is not None

        response_payload = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "is_cached_demo_location": is_cached,
            "location": {
                "latitude": req.latitude,
                "longitude": req.longitude,
                "state": req.state,
                "district": req.district,
                "farm_size_acres": req.farm_size_acres,
                "irrigation_source": req.irrigation_source,
                "previous_crop": req.previous_crop
            },
            "soil_snapshot": soil,
            "weather_snapshot": weather,
            "top_recommendations": recommendations,
            "advisory_warnings": warnings
        }
        return response_payload

    except Exception as e:
        print(f"[!] Error generating recommendations: {e}")
        raise HTTPException(status_code=500, detail=f"Recommendation Engine error: {str(e)}")

@router.post("/advisory/sms-advisory", response_model=SMSAdvisoryResponse)
async def generate_sms_advisory(req: SMSAdvisoryRequest):
    """
    Generates concise, bandwidth-efficient SMS / USSD advisories for feature phones (Non-smartphone farmers).
    SIH 2026 Innovation Differentiator.
    """
    crop_lower = req.crop_name.lower().strip()
    schedules = ml_engine.generate_management_schedules(crop_lower)
    fert = schedules[0][0] if schedules[0] else {"dosage": "50kg DAP/acre"}
    irrig = schedules[1][0] if schedules[1] else {"note": "Light watering"}

    sms_hi = f"किसान साथी: {req.crop_name} के लिए सलाह- बुवाई पर {fert['dosage']}। सिंचाई: {irrig['note']}। हेल्पलाइन 1800-180-1551"
    sms_en = f"Kisaan Sathi: {req.crop_name} advisory- Apply {fert['dosage']}. Irrig: {irrig['note']}. Kisan Call Center: 1800-180-1551"

    return {
        "status": "ready_for_dispatch",
        "channel": "USSD / SMS Broadcast Gateway",
        "sms_text_hi": sms_hi,
        "sms_text_en": sms_en,
        "character_count": len(sms_hi),
        "broadcast_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
