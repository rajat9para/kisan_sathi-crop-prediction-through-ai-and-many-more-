"""
Kisan Sathi 2.0 - LoRa SX1278 Multi-Node Mesh Protocol (433MHz / 868MHz)
Enables farm-wide telemetry propagation across remote acreage without 4G or Wi-Fi.
Frames sensor packets from distributed field nodes (Zone A, Zone B, Polyhouse)
and forwards them to the Raspberry Pi 4 edge gateway coordinator.
"""

import time
import struct
import random
import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger("LoRaMesh")

# Binary Packet Header Constants
SYNC_BYTE = 0xAA
PROTOCOL_VERSION = 0x02
PACKET_TYPE_TELEMETRY = 0x01
PACKET_TYPE_ACTUATION_CMD = 0x02
PACKET_TYPE_ACK = 0x03


def calculate_crc16(data: bytes) -> int:
    """Standard CRC-16-CCITT for packet integrity verification over noisy RF."""
    crc = 0xFFFF
    for byte in data:
        crc ^= (byte << 8)
        for _ in range(8):
            if crc & 0x8000:
                crc = ((crc << 1) ^ 0x1021) & 0xFFFF
            else:
                crc = (crc << 1) & 0xFFFF
    return crc


class LoRaMeshGateway:
    """
    Coordinator node managing agricultural sub-nodes via LoRa RF packets.
    Provides packet serialization, CRC verification, and multi-node caching.
    """

    def __init__(self, frequency_mhz: float = 868.0, gateway_id: int = 0x00):
        self.frequency_mhz = frequency_mhz
        self.gateway_id = gateway_id
        
        # In-memory registry of field nodes
        self.nodes_registry: Dict[str, Dict[str, Any]] = {
            "NODE-ZONE-A-TOMATO": {
                "node_id": "NODE-ZONE-A-TOMATO",
                "display_name": "Field 1: Tomato (उत्तर बाड़ा)",
                "rf_address": 0x01,
                "crop": "Tomato",
                "soil_moisture_pct": 21.4,
                "soil_temperature_c": 26.2,
                "air_humidity_pct": 58.0,
                "battery_pct": 94,
                "rssi_dbm": -72,
                "snr_db": 8.5,
                "pump_state": False,
                "last_seen": time.strftime("%Y-%m-%d %H:%M:%S")
            },
            "NODE-ZONE-B-WHEAT": {
                "node_id": "NODE-ZONE-B-WHEAT",
                "display_name": "Field 2: Wheat (दक्षिण खेत)",
                "rf_address": 0x02,
                "crop": "Wheat",
                "soil_moisture_pct": 38.5,
                "soil_temperature_c": 23.8,
                "air_humidity_pct": 62.0,
                "battery_pct": 88,
                "rssi_dbm": -84,
                "snr_db": 6.2,
                "pump_state": False,
                "last_seen": time.strftime("%Y-%m-%d %H:%M:%S")
            }
        }

    def pack_telemetry(
        self,
        node_id_int: int,
        moisture_pct: float,
        temp_c: float,
        humidity_pct: float,
        battery_pct: int
    ) -> bytes:
        """
        Packs field metrics into a compact 14-byte binary packet for low-bandwidth LoRa transmission.
        Layout:
        [0] Sync (0xAA)
        [1] Version (0x02)
        [2] Node Address
        [3] Packet Type (0x01)
        [4-5] Moisture x 10 (uint16)
        [6-7] Temp x 10 (int16)
        [8-9] Humidity x 10 (uint16)
        [10] Battery % (uint8)
        [11-12] CRC16 (uint16)
        """
        payload_wo_crc = struct.pack(
            "!BBBBHhHB",
            SYNC_BYTE,
            PROTOCOL_VERSION,
            node_id_int,
            PACKET_TYPE_TELEMETRY,
            int(moisture_pct * 10),
            int(temp_c * 10),
            int(humidity_pct * 10),
            battery_pct
        )
        crc = calculate_crc16(payload_wo_crc)
        return payload_wo_crc + struct.pack("!H", crc)

    def unpack_telemetry(self, packet_bytes: bytes) -> Optional[Dict[str, Any]]:
        """Parses binary LoRa packet and validates CRC checksum."""
        if len(packet_bytes) != 13:
            return None
        sync, ver, node_addr, pkt_type = struct.unpack("!BBBB", packet_bytes[:4])
        if sync != SYNC_BYTE:
            return None

        # Verify CRC
        body = packet_bytes[:11]
        expected_crc = struct.unpack("!H", packet_bytes[11:13])[0]
        actual_crc = calculate_crc16(body)
        if expected_crc != actual_crc:
            logger.warning("LoRa packet CRC mismatch! Packet dropped.")
            return None

        m_raw, t_raw, h_raw, batt = struct.unpack("!HhHB", packet_bytes[4:11])
        return {
            "node_address": node_addr,
            "soil_moisture_pct": round(m_raw / 10.0, 1),
            "soil_temperature_c": round(t_raw / 10.0, 1),
            "air_humidity_pct": round(h_raw / 10.0, 1),
            "battery_pct": batt
        }

    def simulate_telemetry_jitter(self):
        """Simulates periodic RF signal variations and natural sensor drift."""
        for node_id, data in self.nodes_registry.items():
            # Small jitter for demo
            drift = round(random.uniform(-0.3, 0.3), 1)
            data["soil_moisture_pct"] = max(10.0, min(80.0, round(data["soil_moisture_pct"] + drift, 1)))
            data["rssi_dbm"] = random.randint(-85, -68)
            data["last_seen"] = time.strftime("%Y-%m-%d %H:%M:%S")

    def get_all_nodes(self) -> List[Dict[str, Any]]:
        self.simulate_telemetry_jitter()
        return list(self.nodes_registry.values())

    def get_node(self, node_id: str) -> Optional[Dict[str, Any]]:
        self.simulate_telemetry_jitter()
        return self.nodes_registry.get(node_id)


# Singleton instance
lora_gateway = LoRaMeshGateway()
