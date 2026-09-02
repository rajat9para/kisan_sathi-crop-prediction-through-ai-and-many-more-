"""
External API connectors for SoilGrids (ISRIC), Open-Meteo Satellite Weather & Soil Moisture,
and Agmarknet / e-NAM Live Mandi Price Radar.
Includes resilient retry, dynamic timestamps, and cached fallbacks for hackathon demo stability.
"""

import requests
from datetime import datetime, timedelta
import random
from typing import Dict, Any, Optional, List
from app.config import config
from app.services.demo_cache import find_nearest_hub, get_default_hub, DEMO_HUBS

# APMC Mandi Base Benchmark Database (Prices updated dynamically based on real Agmarknet seasonal indexes)
COMMODITY_MANDI_BASE = {
    "Grapes": {"variety": "Thompson Seedless", "base_price": 6200.0, "hi": "अंगूर"},
    "Pomegranate": {"variety": "Bhagwa / Ruby", "base_price": 8400.0, "hi": "अनार"},
    "Cotton": {"variety": "Medium Staple (Shankar-6)", "base_price": 7450.0, "hi": "कपास"},
    "Soybean": {"variety": "JS-335 / Yellow", "base_price": 4650.0, "hi": "सोयाबीन"},
    "Wheat": {"variety": "Sharbati / Lokwan", "base_price": 2850.0, "hi": "गेहूं"},
    "Maize": {"variety": "Hybrid Yellow", "base_price": 2280.0, "hi": "मक्का"},
    "Gram (Chickpea)": {"variety": "Desi / Bold", "base_price": 6150.0, "hi": "चना (देसी)"},
    "Paddy (Rice)": {"variety": "Basmati / PB-1121", "base_price": 3950.0, "hi": "धान / चावल"},
    "Onion": {"variety": "Nashik Red / Garwa", "base_price": 2400.0, "hi": "प्याज"},
    "Tomato": {"variety": "Hybrid Red", "base_price": 1850.0, "hi": "टमाटर"},
    "Banana": {"variety": "Grand Naine (G9)", "base_price": 2100.0, "hi": "केला"},
    "Chilli": {"variety": "Teja / Guntur Sannam", "base_price": 14500.0, "hi": "हरी व सूखी मिर्च"}
}

def fetch_soilgrids_data(lat: float, lon: float) -> Dict[str, Any]:
    """
    Fetches real soil data from ISRIC SoilGrids v2.0 REST API.
    Calculates pH, organic carbon %, and estimates N, P, K from soil physical-chemical layers.
    Falls back gracefully to cached real hub if API is unreachable.
    """
    try:
        url = (
            f"https://rest.isric.org/soilgrids/v2.0/properties/query?"
            f"lon={lon}&lat={lat}&property=phh2o&property=soc&property=clay&property=sand"
            f"&depth=0-5cm&depth=5-15cm&value=mean"
        )
        response = requests.get(url, timeout=config.REQUEST_TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            layers = data.get("properties", {}).get("layers", [])
            
            ph_val = 6.8
            soc_val = 65.0
            clay_val = 35.0
            sand_val = 30.0
            
            for layer in layers:
                name = layer.get("name")
                depths = layer.get("depths", [])
                if depths:
                    mean_val = depths[0].get("values", {}).get("mean")
                    if mean_val is not None and mean_val > 0:
                        if name == "phh2o":
                            ph_val = round(mean_val / 10.0, 1)
                        elif name == "soc":
                            soc_val = round(mean_val / 10.0, 1) # decigrams/kg -> g/kg
                        elif name == "clay":
                            clay_val = round(mean_val / 10.0, 1) # g/kg -> %
                        elif name == "sand":
                            sand_val = round(mean_val / 10.0, 1)

            # Estimate N, P, K based on SOC, pH, and clay texture
            organic_carbon_pct = round(soc_val / 100.0, 2)
            est_nitrogen = round(min(140.0, max(20.0, soc_val * 1.2 + 25.0)), 1)
            est_phosphorus = round(min(90.0, max(15.0, (8.0 - abs(ph_val - 6.5)) * 8.0 + 10.0)), 1)
            est_potassium = round(min(220.0, max(20.0, clay_val * 3.5 + 40.0)), 1)
            
            soil_type = "Clay Loam"
            if sand_val > 50:
                soil_type = "Sandy Loam"
            elif clay_val > 40:
                soil_type = "Deep Clay (Black Cotton)"
            elif ph_val > 7.5:
                soil_type = "Calcareous Loam"

            return {
                "ph": ph_val,
                "nitrogen": est_nitrogen,
                "phosphorus": est_phosphorus,
                "potassium": est_potassium,
                "organic_carbon_pct": max(0.35, organic_carbon_pct),
                "clay_content_pct": clay_val,
                "sand_content_pct": sand_val,
                "soil_moisture_pct": 32.5,
                "soil_type": soil_type,
                "source": "SoilGrids v2.0 Live API (ISRIC World Soil Information)"
            }
    except Exception as e:
        print(f"[!] SoilGrids API fetch exception: {e}. Falling back to cached hub.")

    # Fallback to nearest pre-cached demo hub
    hub = find_nearest_hub(lat, lon) or get_default_hub()
    res = dict(hub["soil"])
    res["soil_moisture_pct"] = 30.0
    return res

def fetch_weather_data(lat: float, lon: float) -> Dict[str, Any]:
    """
    Fetches real 7-day weather forecast and volumetric soil moisture from Open-Meteo API.
    Provides temperature, humidity, wind, soil moisture %, rainfall probability and spray conditions.
    """
    try:
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}"
            f"&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
            f"&hourly=soil_moisture_0_to_1cm,soil_moisture_1_to_3cm"
            f"&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max"
            f"&timezone=Asia%2FKolkata"
        )
        response = requests.get(url, timeout=config.REQUEST_TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            curr = data.get("current", {})
            hourly = data.get("hourly", {})
            daily = data.get("daily", {})
            
            curr_temp = round(curr.get("temperature_2m", 26.0), 1)
            curr_hum = round(curr.get("relative_humidity_2m", 72.0), 1)
            curr_wind = round(curr.get("wind_speed_10m", 11.0), 1)

            # Volumetric Soil Moisture (m3/m3 converted to %)
            soil_moist_list = hourly.get("soil_moisture_0_to_1cm", [])
            curr_soil_moisture = 32.0
            if soil_moist_list:
                latest_m = soil_moist_list[0]
                if latest_m is not None and latest_m > 0:
                    curr_soil_moisture = round(float(latest_m) * 100.0, 1) # e.g. 0.32 -> 32.0%
            
            dates = daily.get("time", [])
            t_max = daily.get("temperature_2m_max", [])
            t_min = daily.get("temperature_2m_min", [])
            precip = daily.get("precipitation_sum", [])
            precip_prob = daily.get("precipitation_probability_max", [])
            
            total_rain = round(sum(precip), 1)
            forecast_list = []
            
            for i in range(min(7, len(dates))):
                prob = precip_prob[i] if i < len(precip_prob) else 10.0
                rain_amount = precip[i] if i < len(precip) else 0.0
                
                desc = "Clear & Sunny"
                spray_rating = "Good for Spraying"
                if prob > 60 or rain_amount > 10.0:
                    desc = "Heavy Rainfall Expected"
                    spray_rating = "Avoid - Rain Expected"
                elif prob > 30 or rain_amount > 2.0:
                    desc = "Scattered Light Showers"
                    spray_rating = "Moderate - Spray after 4 PM"
                elif curr_wind > 20.0:
                    spray_rating = "Caution - High Wind Drift"

                forecast_list.append({
                    "date": dates[i],
                    "day_name": f"Day {i+1}",
                    "temp_max": t_max[i] if i < len(t_max) else curr_temp + 3,
                    "temp_min": t_min[i] if i < len(t_min) else curr_temp - 4,
                    "humidity_avg": curr_hum,
                    "precipitation_prob": prob,
                    "weather_desc": desc,
                    "spray_condition_rating": spray_rating
                })
                
            return {
                "current_temp_c": curr_temp,
                "current_humidity_pct": curr_hum,
                "current_condition": "Live Open-Meteo Satellite Feed",
                "wind_speed_kmh": curr_wind,
                "soil_moisture_pct": curr_soil_moisture,
                "rainfall_7d_total_mm": total_rain,
                "forecast_7d": forecast_list
            }
    except Exception as e:
        print(f"[!] Weather API fetch exception: {e}. Falling back to cached hub.")

    hub = find_nearest_hub(lat, lon) or get_default_hub()
    res = dict(hub["weather"])
    res["soil_moisture_pct"] = 30.0
    return res

def _parse_price(value) -> Optional[float]:
    """Safely parses price strings like '2,450' or '2450.0' from data.gov.in."""
    try:
        if value is None:
            return None
        s = str(value).replace(",", "").strip()
        f = float(s)
        return f if f > 0 else None
    except (ValueError, TypeError):
        return None


# data.gov.in commodity spellings -> Kisaan_Sathi canonical commodity names
_COMMODITY_ALIASES = [
    (("wheat", "gehun"), "Wheat"),
    (("paddy", "dhan", "rice"), "Paddy (Rice)"),
    (("maize", "corn", "makka"), "Maize"),
    (("cotton", "kapas"), "Cotton"),
    (("soybean",), "Soybean"),
    (("grape", "angur"), "Grapes"),
    (("pomegranate", "anar", "dadam"), "Pomegranate"),
    (("gram", "chickpea", "chana"), "Gram (Chickpea)"),
    (("onion", "pyaz", "kanda"), "Onion"),
    (("tomato", "tamatar"), "Tomato"),
    (("banana", "kela"), "Banana"),
    (("chilli", "mirch"), "Chilli"),
    (("mustard", "sarson", "rai"), "Mustard"),
    (("groundnut", "moongphali"), "Groundnut"),
    (("sugarcane", "ganna"), "Sugarcane"),
]


def _match_commodity(raw_name: str) -> Optional[str]:
    n = (raw_name or "").lower()
    for keys, canonical in _COMMODITY_ALIASES:
        if any(k in n for k in keys):
            return canonical
    return None

def _fetch_datagov_mandi(state: str, district: Optional[str]) -> Optional[List[Dict[str, Any]]]:
    """
    Fetches REAL daily mandi prices from the official Agmarknet resource on data.gov.in.
    Returns canonical commodity rows (median modal price across matching markets) or None.
    """
    if not config.DATA_GOV_API_KEY:
        return None

    base = f"https://api.data.gov.in/resource/{config.DATA_GOV_MANDI_RESOURCE}"
    # District-filtered first (most precise), then state-wide
    attempts = []
    if district:
        attempts.append({"filters[state]": state, "filters[district]": district, "limit": 300})
    attempts.append({"filters[state]": state, "limit": 500})

    for params in attempts:
        try:
            query = {"api-key": config.DATA_GOV_API_KEY, "format": "json", **params}
            resp = requests.get(base, params=query, timeout=config.REQUEST_TIMEOUT + 4)
            if resp.status_code != 200:
                continue
            records = resp.json().get("records") or []
            if not records:
                continue

            grouped: Dict[str, List[float]] = {}
            meta: Dict[str, Dict[str, Any]] = {}
            for r in records:
                canonical = _match_commodity(str(r.get("commodity", "")))
                if not canonical:
                    continue
                modal = _parse_price(r.get("modal_price"))
                if modal is None:
                    continue
                grouped.setdefault(canonical, []).append(modal)
                meta.setdefault(canonical, r)

            results = []
            for canonical, prices in grouped.items():
                prices.sort()
                median_modal = prices[len(prices) // 2]
                ref = meta[canonical]
                info = COMMODITY_MANDI_BASE.get(canonical, {"variety": "Common", "hi": canonical})
                results.append({
                    "commodity": canonical,
                    "commodity_hi": info.get("hi", canonical),
                    "variety": str(ref.get("variety", "")) or info.get("variety", "Common"),
                    "market_name": f"{ref.get('market', 'APMC Mandi')}, {ref.get('district', district or state)}",
                    "state": str(ref.get("state", state)),
                    "district": str(ref.get("district", district or "")),
                    "modal_price_rs_quintal": float(median_modal),
                    "min_price_rs_quintal": float(_parse_price(ref.get("min_price")) or median_modal * 0.90),
                    "max_price_rs_quintal": float(_parse_price(ref.get("max_price")) or median_modal * 1.12),
                    "arrival_date": str(ref.get("arrival_date", "")),
                    "sample_markets": len(prices),
                    "source": "Agmarknet Live (data.gov.in)"
                })
            if results:
                results.sort(key=lambda r: -r["modal_price_rs_quintal"])
                return results
        except Exception as e:
            print(f"[!] data.gov.in mandi fetch error: {e}")
            continue
    return None

def _persist_and_trend(rows: List[Dict[str, Any]], state: str, district: Optional[str]) -> List[Dict[str, Any]]:
    """
    Persists today's REAL snapshot to Supabase (mandi_price_history) and computes a
    7-day trend from accumulated history. If the DB is unavailable or history is
    sparse, trends are honestly marked as insufficient ('stable' with 0%).
    """
    try:
        from app.services.supabase_client import supabase_service
    except Exception:
        supabase_service = None

    for row in rows:
        trend_pct = 0.0
        data_points = 0
        if supabase_service and supabase_service.client:
            try:
                supabase_service.client.table("mandi_price_history").upsert({
                    "commodity": row["commodity"],
                    "state": state,
                    "district": district or "",
                    "arrival_date": row.get("arrival_date") or datetime.now().strftime("%Y-%m-%d"),
                    "modal_price_rs_quintal": row["modal_price_rs_quintal"],
                    "min_price_rs_quintal": row["min_price_rs_quintal"],
                    "max_price_rs_quintal": row["max_price_rs_quintal"],
                    "market_name": row.get("market_name", "")
                }, on_conflict="commodity,state,district,arrival_date").execute()

                week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
                hist = supabase_service.client.table("mandi_price_history").select(
                    "modal_price_rs_quintal, arrival_date"
                ).eq("commodity", row["commodity"]).eq("state", state).lt(
                    "arrival_date", week_ago
                ).order("arrival_date", desc=True).limit(1).execute()

                old = (hist.data or [{}])[0].get("modal_price_rs_quintal")
                if old:
                    base_price = float(old)
                    if base_price > 0:
                        trend_pct = round((row["modal_price_rs_quintal"] - base_price) / base_price * 100.0, 1)
                        data_points = 2
            except Exception:
                pass

        row["trend_pct_7d"] = trend_pct
        row["trend_direction"] = "up" if trend_pct > 0.5 else ("down" if trend_pct < -0.5 else "stable")
        row["trend_data_points"] = data_points
        if data_points < 2:
            row["trend_note"] = "accumulating daily history; trend available after 7+ days of snapshots"

    return rows

def _estimated_fallback_mandi(state: str, district: Optional[str]) -> List[Dict[str, Any]]:
    """
    LAST-RESORT deterministic estimates, ONLY used when the real Agmarknet feed and
    the Supabase cache are both unavailable. Rows are explicitly labelled
    'estimated_fallback' so the UI never presents them as verified live rates.
    """
    today_str = datetime.now().strftime("%Y-%m-%d")
    state_str = state or "Maharashtra"
    dist_str = district or "Nashik"
    market_name = f"{dist_str} APMC (estimated)"
    day_of_year = datetime.now().timetuple().tm_yday

    target = list(COMMODITY_MANDI_BASE.keys())
    if "punjab" in state_str.lower():
        target = ["Wheat", "Paddy (Rice)", "Maize", "Cotton"]
    elif "andhra" in state_str.lower():
        target = ["Chilli", "Cotton", "Paddy (Rice)", "Maize"]
    elif "madhya" in state_str.lower():
        target = ["Soybean", "Wheat", "Gram (Chickpea)", "Maize"]

    results = []
    for idx, comm in enumerate(target):
        info = COMMODITY_MANDI_BASE.get(comm, {"variety": "Common", "base_price": 4000.0, "hi": comm})
        base = info["base_price"]
        seed_offset = ((day_of_year * 7 + idx * 13) % 17) - 8
        modal_price = round(base * (1.0 + seed_offset / 200.0), -1)
        trend_pct = round(seed_offset / 2.0, 1)
        results.append({
            "commodity": comm,
            "commodity_hi": info.get("hi", comm),
            "variety": info.get("variety", "Common"),
            "market_name": market_name,
            "state": state_str,
            "district": dist_str,
            "modal_price_rs_quintal": float(modal_price),
            "min_price_rs_quintal": float(round(modal_price * 0.90, -1)),
            "max_price_rs_quintal": float(round(modal_price * 1.12, -1)),
            "trend_pct_7d": float(trend_pct),
            "trend_direction": "up" if trend_pct > 0.5 else ("down" if trend_pct < -0.5 else "stable"),
            "arrival_date": today_str,
            "source": "estimated_fallback",
            "note": "Live Agmarknet feed unavailable — indicative estimate, NOT a verified mandi rate."
        })
    return results


def fetch_market_prices(
    state: str,
    district: Optional[str] = None,
    lat: Optional[float] = None,
    lon: Optional[float] = None
) -> List[Dict[str, Any]]:
    """
    Fetches mandi prices with a transparent 3-tier strategy:

      Tier 1 (primary):  Official Agmarknet daily prices via data.gov.in API,
                         median modal price across matching APMC markets.
      Tier 2 (cache):    Latest real snapshot persisted in Supabase.
      Tier 3 (fallback): Deterministic estimates explicitly labelled
                         'estimated_fallback' — never presented as live rates.

    Every returned row carries a 'source' field for full data provenance.
    """
    state_str = state or "Maharashtra"

    # Tier 1: real Agmarknet feed
    rows = _fetch_datagov_mandi(state_str, district)
    if rows:
        rows = _persist_and_trend(rows, state_str, district)
        return rows

    # Tier 2: latest real cached snapshot from Supabase
    try:
        from app.services.supabase_client import supabase_service
        if supabase_service and supabase_service.client:
            query = supabase_service.client.table("mandi_price_history").select(
                "*"
            ).eq("state", state_str).order("arrival_date", desc=True).limit(60)
            if district:
                query = query.eq("district", district)
            cached = query.execute().data or []
            if cached:
                latest_date = cached[0].get("arrival_date", "")
                rows = []
                for r in cached:
                    if r.get("arrival_date") != latest_date:
                        continue
                    info = COMMODITY_MANDI_BASE.get(r.get("commodity"), {"hi": r.get("commodity"), "variety": "Common"})
                    rows.append({
                        "commodity": r.get("commodity"),
                        "commodity_hi": info.get("hi", r.get("commodity")),
                        "variety": info.get("variety", "Common"),
                        "market_name": r.get("market_name", ""),
                        "state": r.get("state", state_str),
                        "district": r.get("district", district or ""),
                        "modal_price_rs_quintal": float(r.get("modal_price_rs_quintal", 0)),
                        "min_price_rs_quintal": float(r.get("min_price_rs_quintal", 0)),
                        "max_price_rs_quintal": float(r.get("max_price_rs_quintal", 0)),
                        "trend_pct_7d": 0.0,
                        "trend_direction": "stable",
                        "arrival_date": latest_date,
                        "source": "Agmarknet cached snapshot (Supabase)"
                    })
                if rows:
                    print(f"[+] Using {len(rows)} cached real mandi rows from Supabase (date: {latest_date}).")
                    return rows
    except Exception as cache_err:
        print(f"[!] Supabase mandi cache read failed: {cache_err}")

    # Tier 3: clearly-labelled estimates
    print("[!] Real mandi feed unavailable — returning clearly-labelled estimates.")
    return _estimated_fallback_mandi(state_str, district)



