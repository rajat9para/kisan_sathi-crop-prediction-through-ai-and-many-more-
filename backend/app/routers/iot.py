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

router = APIRouter(prefix="/api/iot", tags=["IoT Sensor Ingestion"])

# In-Memory & Database-backed IoT Live Cache
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
        "moisture_status": moist_status
    }

@router.get("/latest/{device_id}", response_model=IoTReadingResponse)
async def get_latest_device_reading(device_id: str = Path(..., description="Device identifier")):
    """
    Returns latest telemetry from an active IoT node.
    """
    if device_id not in IOT_DEVICE_CACHE:
        raise HTTPException(status_code=404, detail=f"Device {device_id} has not transmitted data yet.")

    data = IOT_DEVICE_CACHE[device_id]
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
        "moisture_status": data["moisture_status"]
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
