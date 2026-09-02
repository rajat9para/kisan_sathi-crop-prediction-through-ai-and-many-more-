"""
IoT Sensor Hardware Telemetry Ingestion Router (SIH 2026 Problem Statement)
Ingests real-time telemetry from ESP32 / Arduino / LoRaWAN agricultural soil sensor nodes:
- Volumetric Soil Moisture (%)
- Soil Temperature (°C)
- Soil pH & Electrical Conductivity (EC)
- Optical NPK sensor levels (ppm -> kg/ha)
"""

from fastapi import APIRouter, HTTPException, Path
from datetime import datetime
from typing import Dict, Any, List, Optional
from app.models.schemas import IoTReadingRequest, IoTReadingResponse
from app.services.supabase_client import supabase_service

router = APIRouter(prefix="/api/iot", tags=["IoT Sensor Ingestion"])

# In-Memory cache mirrors the DB and keeps the last reading per device available
# even when Supabase is unreachable (offline demo resilience).
IOT_DEVICE_CACHE: Dict[str, Dict[str, Any]] = {
    "ESP32-SOIL-DEMO": {
        "device_id": "ESP32-SOIL-DEMO",
        "recorded_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "soil_moisture_pct": 34.2,
        "soil_temperature_c": 24.8,
        "soil_ph": 6.8,
        "nitrogen_kg_ha": 82.0,
        "phosphorus_kg_ha": 48.0,
        "potassium_kg_ha": 185.0,
        "battery_level_pct": 96.0,
        "moisture_status": "Optimal"
    }
}


def _persist_reading(entry: Dict[str, Any]) -> bool:
    """Persists telemetry to Supabase (iot_telemetry table). Returns success flag."""
    if not supabase_service or not supabase_service.client:
        return False
    try:
        supabase_service.client.table("iot_telemetry").insert({
            "device_id": entry["device_id"],
            "recorded_at": entry["recorded_at"],
            "soil_moisture_pct": entry["soil_moisture_pct"],
            "soil_temperature_c": entry["soil_temperature_c"],
            "soil_ph": entry["soil_ph"],
            "nitrogen_kg_ha": entry["nitrogen_kg_ha"],
            "phosphorus_kg_ha": entry["phosphorus_kg_ha"],
            "potassium_kg_ha": entry["potassium_kg_ha"],
            "battery_level_pct": entry["battery_level_pct"],
            "moisture_status": entry["moisture_status"]
        }).execute()
        return True
    except Exception as e:
        print(f"[!] IoT persistence failed (serving from memory cache): {e}")
        return False

# __IOT_PART2__


@router.post("/reading", response_model=IoTReadingResponse)
async def ingest_iot_reading(payload: IoTReadingRequest):
    """
    Ingests live telemetry payload from field IoT sensor probe.
    Converts optical NPK ppm readings to kg/ha for ML engine consumption.
    """
    moist = payload.soil_moisture_pct
    if moist < 20.0:
        moist_status = "Dry (Irrigation Needed)"
    elif moist > 65.0:
        moist_status = "Waterlogged (Drainage Required)"
    else:
        moist_status = "Optimal"

    # Conversion factor: ppm (mg/kg) * 2.24 = approximate kg/ha in topsoil
    n_kgha = (payload.nitrogen_ppm * 2.24) if payload.nitrogen_ppm is not None else 75.0
    p_kgha = (payload.phosphorus_ppm * 2.24) if payload.phosphorus_ppm is not None else 45.0
    k_kgha = (payload.potassium_ppm * 2.24) if payload.potassium_ppm is not None else 160.0

    recorded_time = payload.timestamp or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = {
        "device_id": payload.device_id,
        "recorded_at": recorded_time,
        "soil_moisture_pct": round(payload.soil_moisture_pct, 1),
        "soil_temperature_c": round(payload.soil_temperature_c, 1),
        "soil_ph": round(payload.soil_ph if payload.soil_ph is not None else 6.8, 2),
        "nitrogen_kg_ha": round(n_kgha, 1),
        "phosphorus_kg_ha": round(p_kgha, 1),
        "potassium_kg_ha": round(k_kgha, 1),
        "battery_level_pct": payload.battery_level_pct or 100.0,
        "moisture_status": moist_status
    }

    IOT_DEVICE_CACHE[payload.device_id] = entry
    persisted = _persist_reading(entry)

    return {
        "status": "success_ingested",
        "device_id": payload.device_id,
        "recorded_at": recorded_time,
        "soil_moisture_pct": entry["soil_moisture_pct"],
        "soil_temperature_c": entry["soil_temperature_c"],
        "soil_ph": entry["soil_ph"],
        "nitrogen_kg_ha": entry["nitrogen_kg_ha"],
        "phosphorus_kg_ha": entry["phosphorus_kg_ha"],
        "potassium_kg_ha": entry["potassium_kg_ha"],
        "moisture_status": moist_status,
        "persisted_to_database": persisted,
        "storage": "supabase_iot_telemetry" if persisted else "in_memory_cache_fallback"
    }

@router.get("/latest/{device_id}", response_model=IoTReadingResponse)
async def get_latest_device_reading(device_id: str = Path(..., description="Device identifier")):
    """
    Returns latest telemetry from an active IoT node.
    Reads from the Supabase iot_telemetry history first (durable across restarts),
    falling back to the in-memory cache for offline demo resilience.
    """
    data = None
    if supabase_service and supabase_service.client:
        try:
            res = supabase_service.client.table("iot_telemetry").select(
                "*"
            ).eq("device_id", device_id).order("recorded_at", desc=True).limit(1).execute()
            if res.data:
                row = res.data[0]
                data = {
                    "device_id": row["device_id"],
                    "recorded_at": row["recorded_at"],
                    "soil_moisture_pct": row.get("soil_moisture_pct"),
                    "soil_temperature_c": row.get("soil_temperature_c"),
                    "soil_ph": row.get("soil_ph"),
                    "nitrogen_kg_ha": row.get("nitrogen_kg_ha"),
                    "phosphorus_kg_ha": row.get("phosphorus_kg_ha"),
                    "potassium_kg_ha": row.get("potassium_kg_ha"),
                    "battery_level_pct": row.get("battery_level_pct", 100.0),
                    "moisture_status": row.get("moisture_status", "Optimal"),
                    "storage": "supabase_iot_telemetry"
                }
        except Exception as e:
            print(f"[!] IoT DB read failed, using memory cache: {e}")

    if data is None:
        if device_id not in IOT_DEVICE_CACHE:
            raise HTTPException(status_code=404, detail=f"Device {device_id} has not transmitted data yet.")
        data = dict(IOT_DEVICE_CACHE[device_id])
        data["storage"] = "in_memory_cache_fallback"

    return {
        "status": "active",
        "device_id": device_id,
        "recorded_at": data["recorded_at"],
        "soil_moisture_pct": data["soil_moisture_pct"],
        "soil_temperature_c": data["soil_temperature_c"],
        "soil_ph": data["soil_ph"],
        "nitrogen_kg_ha": data["nitrogen_kg_ha"],
        "phosphorus_kg_ha": data["phosphorus_kg_ha"],
        "potassium_kg_ha": data["potassium_kg_ha"],
        "moisture_status": data["moisture_status"],
        "persisted_to_database": data.get("storage") == "supabase_iot_telemetry",
        "storage": data.get("storage")
    }

@router.get("/devices")
async def list_active_devices():
    """
    Lists all active IoT sensor nodes currently broadcasting telemetry.
    """
    return {
        "active_devices_count": len(IOT_DEVICE_CACHE),
        "devices": list(IOT_DEVICE_CACHE.values())
    }
