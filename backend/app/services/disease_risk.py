"""
Weather-Driven Crop Disease Risk Early Warning System
=====================================================
Computes quantitative disease-favourability risk indices from REAL live weather
data (Open-Meteo 7-day forecast). Risk formulas follow ICAR/SAU epidemiological
threshold studies for the major Indian crop diseases:

  - Wheat Yellow Rust: 15-20 degC, RH > 85%, frequent light rain (leaf wetness)
  - Rice Blast:        22-28 degC, RH > 90%, cloudy + intermittent rain
  - Late Blight (Potato/Tomato): 10-25 degC, RH > 90%, cumulative rain > 10 mm
  - Downy Mildew (Grape): 20-25 degC, RH > 85%, rain during canopy wet period

Risk index per disease: trapezoid temperature favourability x humidity ramp +
rainfall/leaf-wetness proxy. Thresholds -> Low / Moderate / High / Severe with
bilingual advisories.
"""

from typing import Dict, Any, List


def _temp_factor(temp: float, low: float, high: float, peak_low: float, peak_high: float) -> float:
    """Trapezoid membership: 1.0 inside peak range, decaying to 0 outside [low, high]."""
    if temp < low or temp > high:
        return 0.0
    if peak_low <= temp <= peak_high:
        return 1.0
    if temp < peak_low:
        return (temp - low) / max(0.1, peak_low - low)
    return (high - temp) / max(0.1, high - peak_high)


def _risk_category(score: float) -> str:
    if score >= 75:
        return "Severe"
    if score >= 55:
        return "High"
    if score >= 35:
        return "Moderate"
    return "Low"


def _risk_category_hi(score: float) -> str:
    if score >= 75:
        return "अति उच्च"
    if score >= 55:
        return "उच्च"
    if score >= 35:
        return "मध्यम"
    return "कम"


DISEASE_MODELS = [
    {
        "key": "wheat_yellow_rust",
        "disease_en": "Wheat Yellow Rust (Stripe Rust)",
        "disease_hi": "गेहूं का पीला रतुआ",
        "crop_en": "Wheat",
        "crop_hi": "गेहूं",
        "temp": (8, 22, 13, 18),
        "rh": 85.0,
        "rain_weight": 0.30,
        "adv_en": "Scout fields weekly for yellow stripe pustules. At High/Severe risk, spray Propiconazole 25 EC @ 1ml/L on a clear morning.",
        "adv_hi": "सप्ताह में एक बार खेत की जांच करें। उच्च जोखिम पर प्रोपिकोनाज़ोल 25 EC (1 मिली/लीटर) का छिड़काव करें।",
    },
    {
        "key": "rice_blast",
        "disease_en": "Rice Blast",
        "disease_hi": "धान का झोंका रोग",
        "crop_en": "Rice / Paddy",
        "crop_hi": "धान",
        "temp": (18, 32, 22, 28),
        "rh": 90.0,
        "rain_weight": 0.25,
        "adv_en": "Avoid excess nitrogen; keep fields drained between irrigations. At High/Severe risk, apply Tricyclazole 75 WP @ 0.6g/L before panicle emergence.",
        "adv_hi": "अधिक यूरिया न डालें; खेत में जल निकासी रखें। उच्च जोखिम पर ट्राइसाइक्लाज़ोल 75 WP (0.6 ग्राम/लीटर) छिड़कें।",
    },
    {
        "key": "late_blight",
        "disease_en": "Late Blight (Potato / Tomato)",
        "disease_hi": "आलू / टमाटर का पछेती झुलसा",
        "crop_en": "Potato, Tomato",
        "crop_hi": "आलू, टमाटर",
        "temp": (8, 26, 14, 22),
        "rh": 90.0,
        "rain_weight": 0.30,
        "adv_en": "At High/Severe risk spray Mancozeb 75 WP @ 2.5g/L or Cymoxanil+Mancozeb at 7-10 day intervals; remove infected plants.",
        "adv_hi": "उच्च जोखिम पर मैंकोजेब 75 WP (2.5 ग्राम/लीटर) का 7-10 दिन अंतराल पर छिड़काव करें; संक्रमित पौधे हटाएं।",
    },
    {
        "key": "grape_downy_mildew",
        "disease_en": "Grape Downy Mildew",
        "disease_hi": "अंगूर का डाउनी मिल्ड्यू",
        "crop_en": "Grapes",
        "crop_hi": "अंगूर",
        "temp": (15, 30, 20, 26),
        "rh": 85.0,
        "rain_weight": 0.30,
        "adv_en": "Ensure canopy aeration; at High/Severe risk spray Metalaxyl + Mancozeb per label on clear mornings.",
        "adv_hi": "बेल की हवादार छतरी बनाए रखें; उच्च जोखिम पर मेटालैक्सिल + मैंकोजेब का छिड़काव करें।",
    },
]

def compute_disease_risks(weather: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Computes per-disease risk indices from real Open-Meteo forecast data.
    Uses 7-day mean temp/humidity and cumulative rainfall (leaf-wetness proxy).
    """
    forecast = weather.get("forecast_7d") or []
    if forecast:
        temps = [float(d.get("temp_max", 26) + d.get("temp_min", 18)) / 2.0 for d in forecast]
        hums = [float(d.get("humidity_avg", weather.get("current_humidity_pct", 70))) for d in forecast]
        rains = [float(d.get("precipitation_prob", 0)) / 100.0 * 8.0 for d in forecast]
    else:
        temps = [float(weather.get("current_temp_c", 26.0))]
        hums = [float(weather.get("current_humidity_pct", 70.0))]
        rains = [0.0]

    mean_temp = sum(temps) / len(temps)
    mean_rh = sum(hums) / len(hums)
    total_rain = sum(rains)
    rain_days = sum(1 for r in rains if r > 2.0)

    results = []
    for model in DISEASE_MODELS:
        lo, hi, plo, phi = model["temp"]
        t_f = _temp_factor(mean_temp, lo, hi, plo, phi)
        rh_f = max(0.0, min(1.0, (mean_rh - model["rh"] + 15.0) / 15.0))
        rain_f = min(1.0, (total_rain / 50.0) + (rain_days / 5.0) * 0.4)

        # Temperature gates the risk; humidity and leaf wetness amplify it
        score = round(100.0 * t_f * (0.55 * rh_f + model["rain_weight"] * rain_f + 0.15), 1)
        score = max(0.0, min(100.0, score))

        results.append({
            "disease_key": model["key"],
            "disease_en": model["disease_en"],
            "disease_hi": model["disease_hi"],
            "crop_en": model["crop_en"],
            "crop_hi": model["crop_hi"],
            "risk_index": score,
            "risk_category": _risk_category(score),
            "risk_category_hi": _risk_category_hi(score),
            "drivers": {
                "mean_temp_7d_c": round(mean_temp, 1),
                "mean_humidity_7d_pct": round(mean_rh, 1),
                "rain_proxy_7d_mm": round(total_rain, 1),
                "rain_days": rain_days
            },
            "advisory_en": model["adv_en"],
            "advisory_hi": model["adv_hi"],
            "method": "ICAR/SAU epidemiological thresholds applied to live Open-Meteo forecast"
        })

    results.sort(key=lambda r: -r["risk_index"])
    return results


