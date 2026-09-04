"""
Kisan Sathi 2.0 - SIM800L GSM/GPRS SMS Dispatcher
Provides zero-internet offline emergency alerting for critical farm events:
- Soil moisture below wilting threshold (<18%)
- Critical pest infestation detected (Fall armyworm / Locust / Bollworm)
- Auto-irrigation pump safety cutoff tripped
- Extreme frost/heatwave alert

Communicates via UART AT commands (AT+CMGF=1, AT+CMGS) over /dev/ttyS0 or /dev/ttyUSB0.
Includes complete simulated fallback for development and testing environments.
"""

import time
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger("GSM_SMS")

# Attempt pyserial import for hardware UART communication
try:
    import serial
    SERIAL_AVAILABLE = True
except ImportError:
    serial = None
    SERIAL_AVAILABLE = False


class Sim800lGsmDriver:
    """
    SIM800L / SIM900 GSM Module AT-Command Driver with multilingual SMS templates.
    """

    def __init__(self, port: str = "/dev/ttyS0", baudrate: int = 9600, timeout: float = 2.0):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None
        self.is_hardware_connected = False
        self.outbox_history = []

        self._connect_serial()

    def _connect_serial(self):
        if SERIAL_AVAILABLE:
            try:
                self.serial_conn = serial.Serial(
                    self.port,
                    baudrate=self.baudrate,
                    timeout=self.timeout
                )
                # Send test handshake
                self.serial_conn.write(b"AT\r\n")
                time.sleep(0.3)
                resp = self.serial_conn.read_all().decode("utf-8", errors="ignore")
                if "OK" in resp:
                    self.is_hardware_connected = True
                    logger.info(f"SIM800L initialized on {self.port} at {self.baudrate} baud.")
                    # Set SMS text mode
                    self.serial_conn.write(b"AT+CMGF=1\r\n")
                    time.sleep(0.3)
            except Exception as e:
                logger.warning(f"Could not open physical GSM port {self.port}: {e}. Using simulated GSM driver.")
                self.is_hardware_connected = False
        else:
            self.is_hardware_connected = False

    def send_sms(
        self,
        phone_number: str,
        message: str,
        lang: str = "hi"
    ) -> Dict[str, Any]:
        """
        Sends SMS to farmer via AT commands.
        Fallback to internal simulated GSM outbox if hardware unavailable.
        """
        clean_phone = phone_number.strip().replace(" ", "").replace("-", "")
        if not clean_phone.startswith("+"):
            if len(clean_phone) == 10:
                clean_phone = "+91" + clean_phone
            elif len(clean_phone) == 12 and clean_phone.startswith("91"):
                clean_phone = "+" + clean_phone

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        success = False
        at_log = []

        if self.is_hardware_connected and self.serial_conn:
            try:
                # Text mode
                self.serial_conn.write(b"AT+CMGF=1\r\n")
                time.sleep(0.2)
                # Phone number
                cmd = f'AT+CMGS="{clean_phone}"\r\n'
                self.serial_conn.write(cmd.encode("utf-8"))
                time.sleep(0.3)
                # Message body + Ctrl+Z (ASCII 26)
                msg_payload = f"{message}\x1A"
                self.serial_conn.write(msg_payload.encode("utf-8", errors="replace"))
                time.sleep(3.0)
                resp = self.serial_conn.read_all().decode("utf-8", errors="ignore")
                at_log.append(resp)
                success = "+CMGS:" in resp or "OK" in resp
            except Exception as e:
                logger.error(f"Error sending AT SMS: {e}")
                success = False
        else:
            # Emulated delivery
            success = True
            at_log.append(f"SIMULATED_UART: AT+CMGS=\"{clean_phone}\" -> SENT OK (Ctrl+Z)")

        record = {
            "recipient": clean_phone,
            "message": message,
            "sent_at": timestamp,
            "status": "DELIVERED" if success else "FAILED",
            "hardware_mode": "Physical SIM800L UART" if self.is_hardware_connected else "Simulated GSM Gateway",
            "at_debug": at_log
        }
        self.outbox_history.insert(0, record)
        if len(self.outbox_history) > 20:
            self.outbox_history.pop()

        return record

    def dispatch_alert(
        self,
        phone_number: str,
        alert_type: str,
        details: Dict[str, Any],
        lang: str = "hi"
    ) -> Dict[str, Any]:
        """
        Creates bilingual agronomic alert and dispatches SMS.
        """
        if alert_type == "low_moisture":
            moist = details.get("moisture_pct", 18.0)
            crop = details.get("crop", "फसल")
            if lang == "hi":
                msg = f"[किसान साथी अलर्ट] खेत में नमी केवल {moist}% है। {crop} को तुरंत पानी चाहिए। स्वचालित मोटर शुरू कर दी गई है।"
            else:
                msg = f"[Kisan Sathi Alert] Soil moisture is critically low at {moist}%. Pump activated for {crop}."

        elif alert_type == "pest_detected":
            pest = details.get("pest_name", "कीट")
            remedy = details.get("remedy", "नीम अर्क छिड़कें")
            if lang == "hi":
                msg = f"[किसान साथी चेतावनी] खेत में {pest} का प्रकोप दिखा है! रोकथाम: {remedy}।"
            else:
                msg = f"[Kisan Sathi Warning] Pest {pest} detected! Advisory: {remedy}."

        elif alert_type == "pump_cutoff":
            mins = details.get("minutes", 15)
            if lang == "hi":
                msg = f"[किसान साथी सूचना] मोटर लगातार {mins} मिनट चलने के बाद स्वतः बंद हो गई है (सुरक्षा कटऑफ)।"
            else:
                msg = f"[Kisan Sathi Info] Irrigation pump automatically stopped after {mins} min safety limit."

        else:
            msg = f"[Kisan Sathi Alert] {details.get('text', 'Field status update.')}"

        return self.send_sms(phone_number, msg, lang=lang)

    def get_outbox(self):
        return self.outbox_history


# Singleton instance
gsm_driver = Sim800lGsmDriver()
