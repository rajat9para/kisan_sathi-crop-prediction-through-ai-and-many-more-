from fastapi import APIRouter, Query
from app.services.external_apis import fetch_weather_data

router = APIRouter(prefix="/api", tags=["Weather Forecast"])

@router.get("/weather")
async def get_weather_forecast(
    lat: float = Query(19.9975, description="Latitude coordinate"),
    lon: float = Query(73.7898, description="Longitude coordinate")
):
    """
    Fetches real 7-day weather forecast, rainfall probability, and agro-spray conditions from Open-Meteo API.
    """
    data = fetch_weather_data(lat, lon)
    
    alerts = []
    if data.get("rainfall_7d_total_mm", 0) > 80:
        alerts.append({
            "type": "rain_alert",
            "title_en": "Monsoon Shower Advisory",
            "title_hi": "मानसून वर्षा की सलाह",
            "message_en": "Significant rainfall expected in next 72 hours. Postpone chemical spray and fertilizer broadcast.",
            "message_hi": "अगले 72 घंटों में मध्यम से भारी बारिश की संभावना। कीटनाशक छिड़काव और यूरिया का छिड़काव रोकें।"
        })
    else:
        alerts.append({
            "type": "favorable_weather",
            "title_en": "Optimal Spray Window",
            "title_hi": "कीटनाशक छिड़काव के लिए अनुकूल समय",
            "message_en": "Clear skies and moderate wind. Ideal for foliar fertilizer and bio-spray application.",
            "message_hi": "साफ मौसम और हल्की हवा। पर्ण उर्वरक और जैविक कीटनाशक छिड़काव के लिए उत्तम समय।"
        })

    return {
        "latitude": lat,
        "longitude": lon,
        **data,
        "alerts": alerts
    }
