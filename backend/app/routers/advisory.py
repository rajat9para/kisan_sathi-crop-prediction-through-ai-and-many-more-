from fastapi import APIRouter, HTTPException
from datetime import datetime
from app.models.schemas import RecommendationRequest, RecommendationResponse
from app.services.external_apis import fetch_soilgrids_data, fetch_weather_data, fetch_market_prices
from app.services.ml_engine import ml_engine
from app.services.demo_cache import find_nearest_hub

router = APIRouter(prefix="/api", tags=["Crop Advisory"])

@router.post("/recommend", response_model=RecommendationResponse)
async def get_crop_recommendations(req: RecommendationRequest):
    """
    Main endpoint for hyper-local explainable crop recommendations.
    Pulls real soil and weather (or uses custom overrides/fallback cache),
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

        # 4. Run ML Inference, SHAP Calculation & Multi-factor Re-ranking
        recommendations = ml_engine.recommend_crops(
            features=features,
            previous_crop=req.previous_crop,
            irrigation=req.irrigation_source or "Borewell",
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

        # Asynchronously log to Supabase in background
        from app.services.supabase_client import supabase_service
        try:
            supabase_service.save_recommendation(response_payload)
        except Exception as se:
            print(f"[!] Supabase background log note: {se}")

        return response_payload
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Recommendation engine error: {str(e)}")
