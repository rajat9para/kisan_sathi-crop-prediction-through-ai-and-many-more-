"""
Kisan Sathi 2.0 - Edge Daemon Service (Autonomous Monitoring Loop)
Orchestrates continuous sensor reading, camera inference, ET_0 water budgeting,
relay pump actuation, SIM800L SMS dispatch, and LoRa mesh telemetry collection.

Can be run standalone as a systemd service on Raspberry Pi 4:
  python edge_daemon.py --crop tomato --interval 5 --phone +919876543210
"""

import sys
import time
import signal
import logging
import argparse
import random
from typing import Dict, Any

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from smart_irrigation import irrigation_controller
from vision_detector import edge_vision_detector
from gsm_sms import gsm_driver
from lora_mesh import lora_gateway

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("EdgeDaemon")


class EdgeDaemon:
    """
    Main background daemon driving the Kisan Sathi 2.0 field station.
    """

    def __init__(
        self,
        crop: str = "tomato",
        phone_number: str = "+919876543210",
        loop_interval_sec: float = 5.0,
        enable_sms: bool = True
    ):
        self.crop = crop
        self.phone_number = phone_number
        self.loop_interval_sec = loop_interval_sec
        self.enable_sms = enable_sms
        self.running = False
        self.cycle_count = 0
        self.last_sms_sent_at = 0.0

        # Simulated or hardware baseline metrics
        self.current_moisture_pct = 24.0
        self.current_temp_c = 28.5
        self.current_humidity_pct = 54.0

    def start(self):
        self.running = True
        logger.info("=" * 60)
        logger.info("🌾 Kisan Sathi 2.0 - Edge Daemon Started (Track A Prototype)")
        logger.info(f"Target Crop: {self.crop.title()} | Loop Interval: {self.loop_interval_sec}s")
        logger.info(f"Hardware Mode: {irrigation_controller.hardware_mode}")
        logger.info(f"Emergency SMS Contact: {self.phone_number}")
        logger.info("=" * 60)

        while self.running:
            try:
                self.cycle_count += 1
                self.run_cycle()
                time.sleep(self.loop_interval_sec)
            except KeyboardInterrupt:
                logger.info("Keyboard interrupt received. Stopping edge daemon.")
                self.stop()
                break
            except Exception as e:
                logger.error(f"Error during daemon execution cycle: {e}", exc_info=True)
                time.sleep(2.0)

    def run_cycle(self) -> Dict[str, Any]:
        """Executes one single monitoring-decision-actuation cycle."""
        # 1. Update/Simulate sensor dynamics
        if irrigation_controller.pump_state:
            # When pump is running, moisture increases
            self.current_moisture_pct = min(68.0, round(self.current_moisture_pct + 1.2, 1))
        else:
            # Gradual soil drying
            self.current_moisture_pct = max(14.0, round(self.current_moisture_pct - 0.2, 1))

        # 2. Evaluate Irrigation Logic & Actuate Relay
        irrigation_result = irrigation_controller.evaluate_irrigation(
            soil_moisture_pct=self.current_moisture_pct,
            temperature_c=self.current_temp_c,
            humidity_pct=self.current_humidity_pct,
            crop=self.crop
        )

        # 3. Check for Emergency Moisture Alerts -> Dispatch SMS via SIM800L
        now = time.time()
        if (self.current_moisture_pct < 18.0) and (now - self.last_sms_sent_at > 300) and self.enable_sms:
            logger.warning(f"CRITICAL MOISTURE ({self.current_moisture_pct}%)! Dispatching SIM800L SMS alert...")
            sms_res = gsm_driver.dispatch_alert(
                phone_number=self.phone_number,
                alert_type="low_moisture",
                details={"moisture_pct": self.current_moisture_pct, "crop": self.crop},
                lang="hi"
            )
            self.last_sms_sent_at = now
            logger.info(f"SMS Sent: {sms_res['message']} (Status: {sms_res['status']})")

        # 4. Process LoRa Mesh Network Nodes
        lora_nodes = lora_gateway.get_all_nodes()

        # Log cycle heartbeat
        if self.cycle_count % 3 == 0:
            logger.info(
                f"[Cycle #{self.cycle_count}] Moisture: {self.current_moisture_pct}% | "
                f"Temp: {self.current_temp_c}°C | ETc: {irrigation_result['crop_water_demand_etc_mm_day']} mm/day | "
                f"Pump: {'ON (RUNNING)' if irrigation_result['pump_active'] else 'OFF (STANDBY)'} | "
                f"LoRa Nodes: {len(lora_nodes)}"
            )

        return {
            "cycle": self.cycle_count,
            "irrigation": irrigation_result,
            "lora_nodes": lora_nodes
        }

    def stop(self):
        self.running = False
        irrigation_controller.cleanup()
        logger.info("Edge daemon safely terminated. GPIO resources released.")


def handle_exit(signum, frame):
    logger.info(f"Signal {signum} received. Cleaning up...")
    irrigation_controller.cleanup()
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)

    parser = argparse.ArgumentParser(description="Kisan Sathi 2.0 Edge Daemon")
    parser.add_argument("--crop", type=str, default="tomato", help="Crop name (e.g., tomato, wheat, rice)")
    parser.add_argument("--interval", type=float, default=3.0, help="Loop interval in seconds")
    parser.add_argument("--phone", type=str, default="+919876543210", help="Farmer phone number for SMS")
    parser.add_argument("--once", action="store_true", help="Run a single cycle and exit (for testing)")
    args = parser.parse_args()

    daemon = EdgeDaemon(
        crop=args.crop,
        phone_number=args.phone,
        loop_interval_sec=args.interval
    )

    if args.once:
        res = daemon.run_cycle()
        print("Single cycle completed successfully:", res)
        daemon.stop()
    else:
        daemon.start()
