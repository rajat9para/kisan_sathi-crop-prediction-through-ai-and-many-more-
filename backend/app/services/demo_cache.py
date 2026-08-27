"""
Pre-cached high-fidelity dataset for key Indian agricultural demo hubs.
Provides 100% demo stability even during spotty internet or government API rate limits.
"""

from typing import Dict, Any, Optional

DEMO_HUBS = {
    "nashik": {
        "name": "Nashik, Maharashtra",
        "district": "Nashik",
        "state": "Maharashtra",
        "lat": 19.9975,
        "lon": 73.7898,
        "soil": {
            "ph": 6.8,
            "nitrogen": 85.0,
            "phosphorus": 48.0,
            "potassium": 190.0,
            "organic_carbon_pct": 0.72,
            "clay_content_pct": 42.0,
            "sand_content_pct": 24.0,
            "soil_type": "Black Cotton (Regur) Loam",
            "source": "SoilGrids v2.0 (ISRIC) + MahaSoil Health Portal"
        },
        "weather": {
            "current_temp_c": 26.5,
            "current_humidity_pct": 74.0,
            "current_condition": "Partly Cloudy",
            "wind_speed_kmh": 12.0,
            "rainfall_7d_total_mm": 68.0,
            "forecast_7d": [
                {"date": "2026-08-28", "day_name": "Friday", "temp_max": 28.5, "temp_min": 21.0, "humidity_avg": 78.0, "precipitation_prob": 35.0, "weather_desc": "Light Rain showers", "spray_condition_rating": "Moderate - Spray after 4 PM"},
                {"date": "2026-08-29", "day_name": "Saturday", "temp_max": 29.0, "temp_min": 21.5, "humidity_avg": 72.0, "precipitation_prob": 15.0, "weather_desc": "Clear Skies", "spray_condition_rating": "Good for Spraying"},
                {"date": "2026-08-30", "day_name": "Sunday", "temp_max": 30.0, "temp_min": 22.0, "humidity_avg": 68.0, "precipitation_prob": 10.0, "weather_desc": "Sunny", "spray_condition_rating": "Good for Spraying"},
                {"date": "2026-08-31", "day_name": "Monday", "temp_max": 28.0, "temp_min": 20.5, "humidity_avg": 75.0, "precipitation_prob": 45.0, "weather_desc": "Scattered Thunderstorms", "spray_condition_rating": "Avoid - Rain Expected"},
                {"date": "2026-09-01", "day_name": "Tuesday", "temp_max": 27.5, "temp_min": 20.0, "humidity_avg": 80.0, "precipitation_prob": 60.0, "weather_desc": "Moderate Rain", "spray_condition_rating": "Avoid - Rain Expected"},
                {"date": "2026-09-02", "day_name": "Wednesday", "temp_max": 28.0, "temp_min": 21.0, "humidity_avg": 70.0, "precipitation_prob": 20.0, "weather_desc": "Overcast", "spray_condition_rating": "Good for Spraying"},
                {"date": "2026-09-03", "day_name": "Thursday", "temp_max": 29.5, "temp_min": 21.5, "humidity_avg": 66.0, "precipitation_prob": 10.0, "weather_desc": "Sunny", "spray_condition_rating": "Good for Spraying"}
            ]
        },
        "market": [
            {"commodity": "Grapes", "commodity_hi": "अंगूर", "variety": "Thompson Seedless", "market_name": "Nashik APMC", "state": "Maharashtra", "modal_price_rs_quintal": 6200.0, "min_price_rs_quintal": 5400.0, "max_price_rs_quintal": 7100.0, "trend_pct_7d": 5.4, "trend_direction": "up", "arrival_date": "2026-08-27"},
            {"commodity": "Pomegranate", "commodity_hi": "अनार", "variety": "Bhagwa", "market_name": "Nashik APMC", "state": "Maharashtra", "modal_price_rs_quintal": 8400.0, "min_price_rs_quintal": 7200.0, "max_price_rs_quintal": 9600.0, "trend_pct_7d": 3.8, "trend_direction": "up", "arrival_date": "2026-08-27"},
            {"commodity": "Cotton", "commodity_hi": "कपास", "variety": "Medium Staple", "market_name": "Malegaon APMC", "state": "Maharashtra", "modal_price_rs_quintal": 7450.0, "min_price_rs_quintal": 6900.0, "max_price_rs_quintal": 7800.0, "trend_pct_7d": -1.2, "trend_direction": "stable", "arrival_date": "2026-08-27"},
            {"commodity": "Maize", "commodity_hi": "मक्का", "variety": "Yellow Hybrid", "market_name": "Yeola APMC", "state": "Maharashtra", "modal_price_rs_quintal": 2280.0, "min_price_rs_quintal": 2100.0, "max_price_rs_quintal": 2420.0, "trend_pct_7d": 2.1, "trend_direction": "up", "arrival_date": "2026-08-27"}
        ]
    },
    "indore": {
        "name": "Indore, Madhya Pradesh",
        "district": "Indore",
        "state": "Madhya Pradesh",
        "lat": 22.7196,
        "lon": 75.8577,
        "soil": {
            "ph": 7.4,
            "nitrogen": 45.0,
            "phosphorus": 62.0,
            "potassium": 82.0,
            "organic_carbon_pct": 0.58,
            "clay_content_pct": 48.0,
            "sand_content_pct": 18.0,
            "soil_type": "Deep Black Malwa Clay",
            "source": "SoilGrids v2.0 (ISRIC) + MP Krishi Vigyan"
        },
        "weather": {
            "current_temp_c": 24.8,
            "current_humidity_pct": 68.0,
            "current_condition": "Mild Breeze",
            "wind_speed_kmh": 10.5,
            "rainfall_7d_total_mm": 75.0,
            "forecast_7d": [
                {"date": "2026-08-28", "day_name": "Friday", "temp_max": 27.0, "temp_min": 19.5, "humidity_avg": 70.0, "precipitation_prob": 20.0, "weather_desc": "Clear Skies", "spray_condition_rating": "Good for Spraying"},
                {"date": "2026-08-29", "day_name": "Saturday", "temp_max": 28.0, "temp_min": 20.0, "humidity_avg": 65.0, "precipitation_prob": 10.0, "weather_desc": "Sunny", "spray_condition_rating": "Good for Spraying"},
                {"date": "2026-08-30", "day_name": "Sunday", "temp_max": 28.5, "temp_min": 20.5, "humidity_avg": 64.0, "precipitation_prob": 5.0, "weather_desc": "Sunny", "spray_condition_rating": "Good for Spraying"},
                {"date": "2026-08-31", "day_name": "Monday", "temp_max": 26.5, "temp_min": 19.0, "humidity_avg": 72.0, "precipitation_prob": 30.0, "weather_desc": "Passing Clouds", "spray_condition_rating": "Good for Spraying"},
                {"date": "2026-09-01", "day_name": "Tuesday", "temp_max": 25.0, "temp_min": 18.5, "humidity_avg": 78.0, "precipitation_prob": 55.0, "weather_desc": "Thunderstorms", "spray_condition_rating": "Avoid - Rain Expected"},
                {"date": "2026-09-02", "day_name": "Wednesday", "temp_max": 26.0, "temp_min": 19.0, "humidity_avg": 74.0, "precipitation_prob": 25.0, "weather_desc": "Light Drizzle", "spray_condition_rating": "Moderate - Check Field"},
                {"date": "2026-09-03", "day_name": "Thursday", "temp_max": 27.5, "temp_min": 20.0, "humidity_avg": 66.0, "precipitation_prob": 10.0, "weather_desc": "Sunny", "spray_condition_rating": "Good for Spraying"}
            ]
        },
        "market": [
            {"commodity": "Chickpea", "commodity_hi": "चना", "variety": "Desi Gram", "market_name": "Indore Mandi", "state": "Madhya Pradesh", "modal_price_rs_quintal": 6150.0, "min_price_rs_quintal": 5700.0, "max_price_rs_quintal": 6400.0, "trend_pct_7d": 4.2, "trend_direction": "up", "arrival_date": "2026-08-27"},
            {"commodity": "Soybean", "commodity_hi": "सोयाबीन", "variety": "Yellow JS-9560", "market_name": "Ujjain Mandi", "state": "Madhya Pradesh", "modal_price_rs_quintal": 4850.0, "min_price_rs_quintal": 4500.0, "max_price_rs_quintal": 5100.0, "trend_pct_7d": 1.8, "trend_direction": "up", "arrival_date": "2026-08-27"},
            {"commodity": "Maize", "commodity_hi": "मक्का", "variety": "Desi", "market_name": "Dhar APMC", "state": "Madhya Pradesh", "modal_price_rs_quintal": 2220.0, "min_price_rs_quintal": 2050.0, "max_price_rs_quintal": 2350.0, "trend_pct_7d": -0.8, "trend_direction": "stable", "arrival_date": "2026-08-27"},
            {"commodity": "Blackgram", "commodity_hi": "उड़द", "variety": "Bold Black", "market_name": "Indore Mandi", "state": "Madhya Pradesh", "modal_price_rs_quintal": 8200.0, "min_price_rs_quintal": 7600.0, "max_price_rs_quintal": 8700.0, "trend_pct_7d": 3.1, "trend_direction": "up", "arrival_date": "2026-08-27"}
        ]
    },
    "ludhiana": {
        "name": "Ludhiana, Punjab",
        "district": "Ludhiana",
        "state": "Punjab",
        "lat": 30.9010,
        "lon": 75.8573,
        "soil": {
            "ph": 7.2,
            "nitrogen": 92.0,
            "phosphorus": 42.0,
            "potassium": 38.0,
            "organic_carbon_pct": 0.45,
            "clay_content_pct": 22.0,
            "sand_content_pct": 52.0,
            "soil_type": "Indo-Gangetic Alluvial Sandy Loam",
            "source": "SoilGrids v2.0 (ISRIC) + PAU Soil Lab"
        },
        "weather": {
            "current_temp_c": 27.2,
            "current_humidity_pct": 82.0,
            "current_condition": "Humid / Sunny",
            "wind_speed_kmh": 8.0,
            "rainfall_7d_total_mm": 195.0,
            "forecast_7d": [
                {"date": "2026-08-28", "day_name": "Friday", "temp_max": 31.0, "temp_min": 24.0, "humidity_avg": 80.0, "precipitation_prob": 40.0, "weather_desc": "Humid / Rain spells", "spray_condition_rating": "Moderate - High Humidity"},
                {"date": "2026-08-29", "day_name": "Saturday", "temp_max": 32.0, "temp_min": 24.5, "humidity_avg": 76.0, "precipitation_prob": 20.0, "weather_desc": "Sunny & Humid", "spray_condition_rating": "Good for Spraying"},
                {"date": "2026-08-30", "day_name": "Sunday", "temp_max": 32.5, "temp_min": 25.0, "humidity_avg": 74.0, "precipitation_prob": 15.0, "weather_desc": "Sunny", "spray_condition_rating": "Good for Spraying"},
                {"date": "2026-08-31", "day_name": "Monday", "temp_max": 30.5, "temp_min": 23.5, "humidity_avg": 82.0, "precipitation_prob": 50.0, "weather_desc": "Rain Showers", "spray_condition_rating": "Avoid - Rain Expected"},
                {"date": "2026-09-01", "day_name": "Tuesday", "temp_max": 29.0, "temp_min": 23.0, "humidity_avg": 85.0, "precipitation_prob": 65.0, "weather_desc": "Heavy Rain", "spray_condition_rating": "Avoid - Rain Expected"},
                {"date": "2026-09-02", "day_name": "Wednesday", "temp_max": 30.0, "temp_min": 23.5, "humidity_avg": 78.0, "precipitation_prob": 25.0, "weather_desc": "Partly Cloudy", "spray_condition_rating": "Good for Spraying"},
                {"date": "2026-09-03", "day_name": "Thursday", "temp_max": 31.5, "temp_min": 24.0, "humidity_avg": 72.0, "precipitation_prob": 10.0, "weather_desc": "Sunny", "spray_condition_rating": "Good for Spraying"}
            ]
        },
        "market": [
            {"commodity": "Rice", "commodity_hi": "चावल / धान", "variety": "Basmati 1121", "market_name": "Khanna Grain Market", "state": "Punjab", "modal_price_rs_quintal": 3950.0, "min_price_rs_quintal": 3600.0, "max_price_rs_quintal": 4300.0, "trend_pct_7d": 2.8, "trend_direction": "up", "arrival_date": "2026-08-27"},
            {"commodity": "Maize", "commodity_hi": "मक्का", "variety": "Kharif Hybrid", "market_name": "Ludhiana APMC", "state": "Punjab", "modal_price_rs_quintal": 2310.0, "min_price_rs_quintal": 2150.0, "max_price_rs_quintal": 2450.0, "trend_pct_7d": 1.5, "trend_direction": "up", "arrival_date": "2026-08-27"},
            {"commodity": "Cotton", "commodity_hi": "कपास", "variety": "American Cotton", "market_name": "Abohar Mandi", "state": "Punjab", "modal_price_rs_quintal": 7380.0, "min_price_rs_quintal": 6800.0, "max_price_rs_quintal": 7700.0, "trend_pct_7d": -0.5, "trend_direction": "stable", "arrival_date": "2026-08-27"}
        ]
    },
    "guntur": {
        "name": "Guntur, Andhra Pradesh",
        "district": "Guntur",
        "state": "Andhra Pradesh",
        "lat": 16.3067,
        "lon": 80.4365,
        "soil": {
            "ph": 6.9,
            "nitrogen": 115.0,
            "phosphorus": 52.0,
            "potassium": 22.0,
            "organic_carbon_pct": 0.62,
            "clay_content_pct": 36.0,
            "sand_content_pct": 38.0,
            "soil_type": "Red Clayey Sandy Loam",
            "source": "SoilGrids v2.0 (ISRIC) + AP Agri Portal"
        },
        "weather": {
            "current_temp_c": 28.5,
            "current_humidity_pct": 78.0,
            "current_condition": "Tropical Warm",
            "wind_speed_kmh": 14.0,
            "rainfall_7d_total_mm": 85.0,
            "forecast_7d": [
                {"date": "2026-08-28", "day_name": "Friday", "temp_max": 33.0, "temp_min": 25.5, "humidity_avg": 76.0, "precipitation_prob": 25.0, "weather_desc": "Warm & Humid", "spray_condition_rating": "Good for Spraying early morning"},
                {"date": "2026-08-29", "day_name": "Saturday", "temp_max": 34.0, "temp_min": 26.0, "humidity_avg": 72.0, "precipitation_prob": 15.0, "weather_desc": "Sunny", "spray_condition_rating": "Good for Spraying"},
                {"date": "2026-08-30", "day_name": "Sunday", "temp_max": 33.5, "temp_min": 25.5, "humidity_avg": 75.0, "precipitation_prob": 30.0, "weather_desc": "Passing Showers", "spray_condition_rating": "Moderate - Spray after 4 PM"},
                {"date": "2026-08-31", "day_name": "Monday", "temp_max": 32.0, "temp_min": 25.0, "humidity_avg": 80.0, "precipitation_prob": 50.0, "weather_desc": "Thunderstorms", "spray_condition_rating": "Avoid - Rain Expected"},
                {"date": "2026-09-01", "day_name": "Tuesday", "temp_max": 31.5, "temp_min": 24.5, "humidity_avg": 82.0, "precipitation_prob": 60.0, "weather_desc": "Moderate Rain", "spray_condition_rating": "Avoid - Rain Expected"},
                {"date": "2026-09-02", "day_name": "Wednesday", "temp_max": 32.5, "temp_min": 25.0, "humidity_avg": 77.0, "precipitation_prob": 20.0, "weather_desc": "Partly Sunny", "spray_condition_rating": "Good for Spraying"},
                {"date": "2026-09-03", "day_name": "Thursday", "temp_max": 33.5, "temp_min": 25.5, "humidity_avg": 73.0, "precipitation_prob": 10.0, "weather_desc": "Sunny", "spray_condition_rating": "Good for Spraying"}
            ]
        },
        "market": [
            {"commodity": "Cotton", "commodity_hi": "कपास", "variety": "DCH-32 Long Staple", "market_name": "Guntur APMC", "state": "Andhra Pradesh", "modal_price_rs_quintal": 7650.0, "min_price_rs_quintal": 7100.0, "max_price_rs_quintal": 8100.0, "trend_pct_7d": 3.4, "trend_direction": "up", "arrival_date": "2026-08-27"},
            {"commodity": "Maize", "commodity_hi": "मक्का", "variety": "High Starch", "market_name": "Guntur APMC", "state": "Andhra Pradesh", "modal_price_rs_quintal": 2290.0, "min_price_rs_quintal": 2120.0, "max_price_rs_quintal": 2430.0, "trend_pct_7d": 2.0, "trend_direction": "up", "arrival_date": "2026-08-27"},
            {"commodity": "Rice", "commodity_hi": "चावल / धान", "variety": "Sona Masoori (BPT 5204)", "market_name": "Tenali Mandi", "state": "Andhra Pradesh", "modal_price_rs_quintal": 2850.0, "min_price_rs_quintal": 2600.0, "max_price_rs_quintal": 3050.0, "trend_pct_7d": 1.2, "trend_direction": "stable", "arrival_date": "2026-08-27"}
        ]
    }
}

def find_nearest_hub(lat: float, lon: float, threshold_distance: float = 3.0) -> Optional[Dict[str, Any]]:
    """Matches lat/lon to nearest known hub if within reasonable range, or returns None."""
    best_hub = None
    min_dist = float("inf")
    for key, data in DEMO_HUBS.items():
        dist = ((data["lat"] - lat) ** 2 + (data["lon"] - lon) ** 2) ** 0.5
        if dist < min_dist:
            min_dist = dist
            best_hub = data
            
    if min_dist <= threshold_distance:
        return best_hub
    return None

def get_default_hub() -> Dict[str, Any]:
    """Returns Nashik as primary demo hub."""
    return DEMO_HUBS["nashik"]
