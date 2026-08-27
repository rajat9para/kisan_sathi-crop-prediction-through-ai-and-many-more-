import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("[1/4] Testing ML Engine...")
from app.services.ml_engine import ml_engine
features = {
    "N": 80.0,
    "P": 45.0,
    "K": 40.0,
    "temperature": 26.5,
    "humidity": 70.0,
    "ph": 6.8,
    "rainfall": 150.0
}
res = ml_engine.recommend_crops(
    features=features,
    previous_crop="Cotton",
    irrigation="Borewell",
    top_k=3
)
print(f"[PASS] Top Crop: {res[0]['crop_name']} ({res[0]['match_score_pct']}%), SHAP count: {len(res[0]['shap_contributions'])}")

print("[2/4] Testing Groq LLM Advisor (LLaMA 3.3)...")
from app.services.llm_advisor import llm_advisor
voice_res = llm_advisor.answer_farmer_voice_query("इसके लिए पानी कितना चाहिए?", "hi", "Soybean", "Nashik")
print(f"[PASS] Groq LLM Reply: {voice_res['response_text_hi'][:60]}...")

print("[3/4] Testing Supabase Client...")
from app.services.supabase_client import supabase_service
ping_res = supabase_service.ping_keep_alive()
print(f"[PASS] Supabase Ping: {ping_res['message']}")

print("[4/4] Testing External APIs Demo Hub...")
from app.services.external_apis import get_soil_data, get_weather_forecast
soil = get_soil_data(19.9975, 73.7898)
weather = get_weather_forecast(19.9975, 73.7898)
print(f"[PASS] Soil pH: {soil.ph}, Weather Temp: {weather.current_temp_c}C")

print("--- ALL QUICK TESTS PASSED! (Groq LLM + Supabase + ML Engine Verified) ---")
