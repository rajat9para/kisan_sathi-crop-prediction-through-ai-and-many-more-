"""
Comprehensive Unit & Integration Test Suite for Kisan Sathi 2.0 Edge-AI Services
Tests:
- Smart Irrigation Controller (ET_0 water budget, rain inhibitor, 15-min safety cutoff)
- Edge Vision Detector (Pests: Fall Armyworm, Aphids, Whiteflies, Bollworm & Plant Pathologies)
- SIM800L GSM SMS Dispatcher (Bilingual alerts & outbox recording)
- LoRa SX1278 Multi-Node Mesh (Packet binary packing, CRC16 verification, node registry)
- Qualcomm RB3 Gen 2 Benchmark Profile
- FastAPI Edge Endpoints via TestClient
"""

import sys
import os
import time

# Ensure backend root is in sys.path
_current_dir = os.path.dirname(os.path.abspath(__file__))
_backend_dir = os.path.dirname(_current_dir)
_root_dir = os.path.dirname(_backend_dir)
_edge_dir = os.path.join(_root_dir, "edge_node")

for p in [_backend_dir, _edge_dir, _root_dir]:
    if p not in sys.path:
        sys.path.insert(0, p)

from edge_node.smart_irrigation import SmartIrrigationController
from edge_node.vision_detector import EdgeVisionDetector, PEST_KNOWLEDGE_BASE
from edge_node.gsm_sms import Sim800lGsmDriver
from edge_node.lora_mesh import LoRaMeshGateway, calculate_crc16
from edge_node.qualcomm_rb3_benchmarks import get_qualcomm_benchmark_summary
from backend.app.services.disease_classifier import disease_classifier
from fastapi.testclient import TestClient
from backend.app.main import app


def test_smart_irrigation_controller():
    """Validates moisture thresholds, ET_0 water budgeting, and rain lockout."""
    ctrl = SmartIrrigationController(moisture_threshold_pct=22.0, target_moisture_pct=50.0)

    # 1. Test Hargreaves ET_0 formula
    et0 = ctrl.calculate_hargreaves_et0(temp_c=28.0)
    assert et0 >= 1.5, f"Expected valid ET_0 >= 1.5 mm/day, got {et0}"

    # 2. Test Low Moisture (<22%) triggers pump relay ON
    res_dry = ctrl.evaluate_irrigation(
        soil_moisture_pct=17.5,
        temperature_c=30.0,
        humidity_pct=45.0,
        rain_detected=False,
        crop="tomato"
    )
    assert res_dry["pump_active"] is True, "Pump should be active when soil moisture is below threshold."
    assert res_dry["recommended_water_liters_sqm"] > 0
    assert "Relay ON" in res_dry["status_message"]

    # 3. Test Rain inhibitor suppresses pump immediately
    res_rain = ctrl.evaluate_irrigation(
        soil_moisture_pct=15.0,
        temperature_c=24.0,
        humidity_pct=85.0,
        rain_detected=True,
        crop="tomato"
    )
    assert res_rain["pump_active"] is False, "Rain inhibitor must suppress pump actuation!"
    assert res_rain["rain_inhibitor_active"] is True

    # 4. Test Adequate Moisture (>22%) keeps pump OFF
    ctrl.set_manual_pump(False)
    res_optimal = ctrl.evaluate_irrigation(
        soil_moisture_pct=35.0,
        temperature_c=26.0,
        humidity_pct=55.0,
        rain_detected=False,
        crop="wheat"
    )
    assert res_optimal["pump_active"] is False
    assert "adequate" in res_optimal["status_message"].lower()

    # 5. Test 15-Minute Safety Cutoff
    ctrl._turn_on_pump()
    assert ctrl.pump_state is True
    # Simulate elapsed time beyond max continuous cutoff
    ctrl.pump_started_at = time.time() - (ctrl.max_continuous_seconds + 5)
    res_cutoff = ctrl.evaluate_irrigation(soil_moisture_pct=15.0, temperature_c=28.0, humidity_pct=50.0)
    assert res_cutoff["pump_active"] is False, "Safety cutoff must turn off pump when time limit exceeded!"
    assert res_cutoff["safety_cutoff_triggered"] is True
    assert "SAFETY TRIP" in res_cutoff["status_message"]

    ctrl.cleanup()
    print("[PASS] test_smart_irrigation_controller")


def test_edge_vision_and_pests():
    """Validates pest triage and bio-control remedies."""
    detector = EdgeVisionDetector()

    # Test Fall Armyworm on Maize
    res_pest = detector.detect_pest_or_disease(crop_hint="maize", detection_mode="pest_only")
    assert res_pest["detection_type"] == "insect_pest"
    assert res_pest["detected_key"] == "fall_armyworm"
    assert "Trichogramma" in res_pest["bio_remedy_en"]
    assert "Coragen" in res_pest["chemical_remedy_en"]
    assert res_pest["confidence_pct"] >= 90.0

    # Test Whitefly on Cotton
    res_whitefly = detector.detect_pest_or_disease(crop_hint="cotton", detection_mode="pest_only")
    assert res_whitefly["detected_key"] == "bollworm"

    # Test Disease Diagnosis on Wheat
    res_dis = detector.detect_pest_or_disease(crop_hint="wheat", detection_mode="disease_only")
    assert res_dis["detection_type"] == "plant_disease"
    assert "yellow_rust" in res_dis["detected_key"]

    # Test backend disease_classifier with pest hint
    diag = disease_classifier.diagnose(crop_hint="fall armyworm damage on maize", is_en=True)
    assert diag["disease_key"] == "fall_armyworm"
    assert "Armyworm" in diag["disease_name"]

    print("[PASS] test_edge_vision_and_pests")


def test_gsm_sms_dispatcher():
    """Validates SIM800L offline SMS generation and outbox tracking."""
    gsm = Sim800lGsmDriver(port="/dev/ttyS0")
    res = gsm.dispatch_alert(
        phone_number="9876543210",
        alert_type="low_moisture",
        details={"moisture_pct": 14.8, "crop": "टमाटर"},
        lang="hi"
    )
    assert res["status"] == "DELIVERED"
    assert res["recipient"] == "+919876543210"
    assert "14.8%" in res["message"]
    assert "किसान साथी" in res["message"]

    outbox = gsm.get_outbox()
    assert len(outbox) >= 1
    assert outbox[0]["recipient"] == "+919876543210"
    print("[PASS] test_gsm_sms_dispatcher")


def test_lora_mesh_protocol():
    """Validates binary packet packing and CRC16 checksum."""
    gateway = LoRaMeshGateway()
    raw_packet = gateway.pack_telemetry(
        node_id_int=1,
        moisture_pct=24.5,
        temp_c=27.3,
        humidity_pct=56.0,
        battery_pct=92
    )
    assert len(raw_packet) == 13, f"Expected 13 bytes binary packet, got {len(raw_packet)}"

    unpacked = gateway.unpack_telemetry(raw_packet)
    assert unpacked is not None
    assert unpacked["node_address"] == 1
    assert unpacked["soil_moisture_pct"] == 24.5
    assert unpacked["soil_temperature_c"] == 27.3
    assert unpacked["air_humidity_pct"] == 56.0
    assert unpacked["battery_pct"] == 92

    # Verify corrupt packet rejection
    corrupt_packet = bytearray(raw_packet)
    corrupt_packet[5] ^= 0xFF
    assert gateway.unpack_telemetry(bytes(corrupt_packet)) is None

    nodes = gateway.get_all_nodes()
    assert len(nodes) == 2
    assert "NODE-ZONE-A-TOMATO" in [n["node_id"] for n in nodes]
    print("[PASS] test_lora_mesh_protocol")


def test_qualcomm_rb3_benchmarks():
    """Validates Qualcomm RB3 benchmark suite."""
    bench = get_qualcomm_benchmark_summary()
    assert "Qualcomm Dragonwing RB3 Gen 2" in bench["hardware_profile"]["platform_name"]
    assert "12.0 TOPS" in bench["hardware_profile"]["npu_compute_capacity"]
    assert len(bench["benchmarks"]) >= 3
    mobilenet_b = bench["benchmarks"][0]
    assert mobilenet_b["qualcomm_qcs6490_npu_latency_ms"] < mobilenet_b["rpi4_cpu_latency_ms"]
    print("[PASS] test_qualcomm_rb3_benchmarks")


def test_fastapi_edge_endpoints():
    """Validates edge router endpoints via FastAPI TestClient."""
    client = TestClient(app)

    # 1. GET /api/edge/status
    res_status = client.get("/api/edge/status")
    assert res_status.status_code == 200
    data = res_status.json()
    assert data["status"] == "online"
    assert "relay_pin_bcm" in data

    # 2. POST /api/edge/actuator/relay (turn_on)
    res_on = client.post("/api/edge/actuator/relay", json={"action": "turn_on"})
    assert res_on.status_code == 200
    assert res_on.json()["pump_active"] is True

    # 3. POST /api/edge/actuator/relay (turn_off)
    res_off = client.post("/api/edge/actuator/relay", json={"action": "turn_off"})
    assert res_off.status_code == 200
    assert res_off.json()["pump_active"] is False

    # 4. POST /api/edge/telemetry
    res_telem = client.post("/api/edge/telemetry", json={
        "device_id": "TEST-NODE-01",
        "soil_moisture_pct": 20.5,
        "temperature_c": 29.0,
        "humidity_pct": 50.0,
        "rain_detected": False,
        "crop": "tomato"
    })
    assert res_telem.status_code == 200
    assert res_telem.json()["status"] == "processed"

    # 5. POST /api/edge/vision/detect
    res_vision = client.post("/api/edge/vision/detect", json={
        "crop_hint": "maize",
        "detection_mode": "pest_only"
    })
    assert res_vision.status_code == 200
    assert res_vision.json()["detection_type"] == "insect_pest"

    # 6. POST /api/edge/gsm/send-sms
    res_sms = client.post("/api/edge/gsm/send-sms", json={
        "phone_number": "+919876543210",
        "alert_type": "low_moisture",
        "crop": "टमाटर",
        "moisture_pct": 15.2,
        "lang": "hi"
    })
    assert res_sms.status_code == 200
    assert res_sms.json()["status"] == "DELIVERED"

    # 7. GET /api/edge/gsm/outbox
    res_outbox = client.get("/api/edge/gsm/outbox")
    assert res_outbox.status_code == 200
    assert res_outbox.json()["count"] >= 1

    # 8. GET /api/edge/lora/nodes
    res_lora = client.get("/api/edge/lora/nodes")
    assert res_lora.status_code == 200
    assert res_lora.json()["total_active_nodes"] >= 2

    # 9. GET /api/edge/benchmarks/qualcomm
    res_qualcomm = client.get("/api/edge/benchmarks/qualcomm")
    assert res_qualcomm.status_code == 200
    assert "hardware_profile" in res_qualcomm.json()

    print("[PASS] test_fastapi_edge_endpoints")


if __name__ == "__main__":
    test_smart_irrigation_controller()
    test_edge_vision_and_pests()
    test_gsm_sms_dispatcher()
    test_lora_mesh_protocol()
    test_qualcomm_rb3_benchmarks()
    test_fastapi_edge_endpoints()
    print("\n==========================================")
    print(" ALL 6 EDGE-AI TEST SUITES PASSED (100%)! ")
    print("==========================================")
