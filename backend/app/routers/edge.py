"""
Kisan Sathi 2.0 - Edge-AI Field Node & Smart Actuation Router
Qualcomm Problem Statement #26180 (Agriculture, FoodTech & Rural Development)

Provides complete REST API endpoints for:
- Live Edge Node Status & FAO-56 ET_0 Water Budget
- 5V Relay Actuator Control (Diaphragm Water Pump / Solenoid Valve)
- Edge Vision AI (On-Device Leaf Disease & Insect Pest Detection)
- SIM800L Offline GSM SMS Emergency Alerting
- LoRa SX1278 Multi-Node Mesh Field Telemetry
- Qualcomm Dragonwing RB3 Gen 2 (QCS6490 NPU) vs Raspberry Pi 4 Benchmarks
"""

import os
import sys
import time
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException, Query

# Ensure edge_node is discoverable from workspace root
_current_dir = os.path.dirname(os.path.abspath(__file__))
_root_dir = os.path.dirname(os.path.dirname(os.path.dirname(_current_dir)))
_edge_dir = os.path.join(_root_dir, "edge_node")
if _edge_dir not in sys.path:
    sys.path.insert(0, _edge_dir)

try:
    from smart_irrigation import irrigation_controller
    from vision_detector import edge_vision_detector, PEST_KNOWLEDGE_BASE
    from gsm_sms import gsm_driver
    from lora_mesh import lora_gateway
    from qualcomm_rb3_benchmarks import get_qualcomm_benchmark_summary
except ImportError as e:
    # Fallback to local import if edge_node is adjacent
    print(f"[!] Direct edge_node import notice: {e}. Attempting sibling path resolution.")
    from edge_node.smart_irrigation import irrigation_controller
    from edge_node.vision_detector import edge_vision_detector, PEST_KNOWLEDGE_BASE
    from edge_node.gsm_sms import gsm_driver
    from edge_node.lora_mesh import lora_gateway
    from edge_node.qualcomm_rb3_benchmarks import get_qualcomm_benchmark_summary

router = APIRouter(prefix="/api/edge", tags=["Edge-AI & Smart Irrigation"])


# --- Request & Response Schemas ---
class RelayActuatorRequest(BaseModel):
    action: str = Field(..., description="'turn_on', 'turn_off', 'toggle', or 'auto'")
    crop: Optional[str] = Field("tomato", description="Target crop for ET_0 calculation")

class EdgeTelemetryRequest(BaseModel):
    device_id: str = Field("RPI4-FIELD-NODE-01", description="Edge node hardware ID")
    soil_moisture_pct: float = Field(..., description="Capacitive soil moisture percentage")
    temperature_c: float = Field(..., description="Ambient temperature from DHT22")
    humidity_pct: float = Field(..., description="Relative humidity from DHT22")
    rain_detected: bool = Field(False, description="FC-37 Rain sensor state")
    crop: Optional[str] = Field("tomato", description="Current crop")

class VisionDetectionRequest(BaseModel):
    image_base64: Optional[str] = Field(None, description="Base64 encoded camera frame")
    crop_hint: Optional[str] = Field("tomato", description="Crop type")
    detection_mode: Optional[str] = Field("auto", description="'auto', 'pest_only', 'disease_only'")

class GsmSmsRequest(BaseModel):
    phone_number: str = Field(..., description="Farmer phone number with country code")
    alert_type: str = Field("low_moisture", description="'low_moisture', 'pest_detected', 'pump_cutoff', or 'custom'")
    crop: Optional[str] = Field("टमाटर", description="Crop name")
    moisture_pct: Optional[float] = Field(16.5, description="Moisture reading")
    custom_text: Optional[str] = Field(None, description="Custom message text if alert_type is 'custom'")
    lang: Optional[str] = Field("hi", description="Language code: 'hi' or 'en'")


# --- API Endpoints ---

@router.get("/status")
async def get_edge_system_status():
    """
    Returns real-time status of the Raspberry Pi 4 edge node:
    - Pump relay energized state & running timer
    - Soil moisture, ET_0 reference evapotranspiration & crop water demand
    - Rain inhibitor lock status
    - 15-minute fail-safe watchdog status
    - Connected SIM800L GSM and LoRa mesh node count
    """
    irrigation_status = irrigation_controller.get_status()
    lora_nodes = lora_gateway.get_all_nodes()
    outbox = gsm_driver.get_outbox()

    return {
        "status": "online",
        "system_title": "Kisan Sathi 2.0 Edge Field Controller",
        "hardware_platform": "Raspberry Pi 4 Model B (Arm Cortex-A72)",
        "hardware_mode": irrigation_status["hardware_mode"],
        "relay_pin_bcm": irrigation_status["relay_pin_bcm"],
        "pump_active": irrigation_status["pump_active"],
        "current_run_seconds": irrigation_status["current_run_seconds"],
        "max_safety_seconds": irrigation_status["max_safety_seconds"],
        "soil_moisture_pct": irrigation_status["moisture_pct"],
        "moisture_threshold_pct": irrigation_status["moisture_threshold_pct"],
        "crop_name": irrigation_status["crop_name"],
        "et0_water_demand_mm_day": irrigation_status["crop_water_demand_etc_mm_day"],
        "rain_inhibitor_active": irrigation_status["rain_inhibitor_active"],
        "manual_override_active": irrigation_status["manual_override_active"],
        "safety_cutoff_triggered": irrigation_status["safety_cutoff_triggered"],
        "status_message": irrigation_status["status_message"],
        "last_actuation_time": irrigation_status["last_irrigation_time"],
        "lora_nodes_count": len(lora_nodes),
        "gsm_outbox_count": len(outbox)
    }


@router.post("/actuator/relay")
async def control_pump_relay(payload: RelayActuatorRequest):
    """
    Remote & autonomous actuation of the 5V pump relay:
    - 'turn_on': Starts pump with 15-minute auto-cutoff safety armed
    - 'turn_off': Shuts down pump immediately
    - 'toggle': Inverts current relay state
    - 'auto': Triggers automatic agronomic ET_0 moisture evaluation
    """
    action = payload.action.lower()
    if action == "turn_on":
        res = irrigation_controller.set_manual_pump(True)
    elif action == "turn_off":
        res = irrigation_controller.set_manual_pump(False)
    elif action == "toggle":
        curr = irrigation_controller.pump_state
        res = irrigation_controller.set_manual_pump(not curr)
    elif action == "auto":
        irrigation_controller.manual_override = False
        res = irrigation_controller.evaluate_irrigation(
            soil_moisture_pct=21.0,
            temperature_c=28.0,
            humidity_pct=55.0,
            crop=payload.crop
        )
    else:
        raise HTTPException(status_code=400, detail=f"Invalid action '{payload.action}'. Use 'turn_on', 'turn_off', 'toggle', or 'auto'.")

    return {
        "status": "success",
        "action_executed": action,
        "pump_active": res["pump_active"],
        "status_message": res["status_message"],
        "safety_timer_active": res["pump_active"],
        "hardware_mode": res["hardware_mode"]
    }


@router.post("/telemetry")
async def ingest_edge_telemetry(payload: EdgeTelemetryRequest):
    """
    Ingests live telemetry from field sensors (moisture, temperature, humidity, rain).
    Evaluates ET_0 water balance and triggers automated pump relay decisions.
    """
    result = irrigation_controller.evaluate_irrigation(
        soil_moisture_pct=payload.soil_moisture_pct,
        temperature_c=payload.temperature_c,
        humidity_pct=payload.humidity_pct,
        rain_detected=payload.rain_detected,
        crop=payload.crop
    )
    return {
        "status": "processed",
        "device_id": payload.device_id,
        "evaluation": result
    }


@router.post("/vision/detect")
async def run_edge_vision_inference(payload: VisionDetectionRequest):
    """
    Performs on-device camera inference for either:
    1. Agricultural Insect Pests (Fall Armyworm, Aphids, Whiteflies, Stem Borer, Bollworm)
    2. Leaf Diseases (Yellow Rust, Blast, Early Blight, etc.)
    Returns bounding box coordinates, severity, ETL thresholds, and ICAR bio-chemical controls.
    """
    res = edge_vision_detector.detect_pest_or_disease(
        crop_hint=payload.crop_hint,
        detection_mode=payload.detection_mode or "auto"
    )
    return res


@router.post("/gsm/send-sms")
async def dispatch_emergency_sms(payload: GsmSmsRequest):
    """
    Sends multilingual emergency SMS alert via SIM800L GSM module (or simulated gateway).
    Supports Hindi ('hi') and English ('en').
    """
    details = {
        "crop": payload.crop,
        "moisture_pct": payload.moisture_pct,
        "text": payload.custom_text
    }
    sms_res = gsm_driver.dispatch_alert(
        phone_number=payload.phone_number,
        alert_type=payload.alert_type,
        details=details,
        lang=payload.lang or "hi"
    )
    return sms_res


@router.get("/gsm/outbox")
async def get_gsm_outbox():
    """Returns log of all SMS messages dispatched via SIM800L module."""
    return {
        "count": len(gsm_driver.get_outbox()),
        "messages": gsm_driver.get_outbox()
    }


@router.get("/lora/nodes")
async def get_lora_mesh_nodes():
    """
    Returns live telemetry from all distributed LoRa SX1278 field nodes
    (e.g., Zone A Tomato Field, Zone B Wheat Field) including RSSI signal strength.
    """
    nodes = lora_gateway.get_all_nodes()
    return {
        "gateway_frequency": f"{lora_gateway.frequency_mhz} MHz",
        "total_active_nodes": len(nodes),
        "nodes": nodes
    }


@router.get("/benchmarks/qualcomm")
async def get_qualcomm_benchmarks():
    """
    Returns Qualcomm Dragonwing RB3 Gen 2 / QCS6490 NPU hardware specifications,
    benchmarking comparisons against Raspberry Pi 4, and Qualcomm AI Hub quantization recipes
    for Qualcomm Problem Statement #26180 evaluation.
    """
    return get_qualcomm_benchmark_summary()
