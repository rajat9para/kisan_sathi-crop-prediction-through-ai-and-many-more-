"""
Kisan Sathi 2.0 - Structured Bilingual Micro-Alert Engine
Target: SIH 2026 Problem Statement #26180 (Qualcomm Inc.)

Generates actionable, punchy micro-alerts in English and Hindi for:
1. "Irrigate now / delay irrigation" (soil deficit or rain lockout)
2. "Heat-stress warning" (canopy thermal spikes > 38°C)
3. "Flood-risk alert" (root-zone saturation & precipitation)
4. "Disease-outbreak risk" (microclimate favoring fungal pathogens)
5. "Pest attack alert" (ICAR Economic Threshold Level breaches)

Dispatches via dual-track channels: SIM800L GSM SMS, LoRa SX1278 mesh, and local API dashboard.
"""

import sys
import time
import uuid
import logging
from typing import Dict, Any, List, Optional

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

logger = logging.getLogger("AlertEngine")


class AlertEngine:
    """Evaluates field conditions and synthesizes structured bilingual micro-alerts."""

    def __init__(self):
        self.alert_history: List[Dict[str, Any]] = []

    def generate_alerts(
        self,
        irrigation_data: Dict[str, Any],
        environmental_risk: Dict[str, Any],
        vision_diagnostic: Optional[Dict[str, Any]] = None,
        crop_name: str = "tomato"
    ) -> List[Dict[str, Any]]:
        """
        Synthesizes active micro-alerts based on real-time sensor & risk evaluation.
        """
        alerts: List[Dict[str, Any]] = []
        now_str = time.strftime("%Y-%m-%d %H:%M:%S")

        # 1. IRRIGATION ADVISORY MICRO-ALERT
        moist_pct = irrigation_data.get("moisture_pct", 35.0)
        thresh_pct = irrigation_data.get("moisture_threshold_pct", 25.0)
        rain_active = irrigation_data.get("rain_inhibitor_active", False)
        rec_liters = irrigation_data.get("recommended_water_liters_sqm", 0.0)
        rec_mins = irrigation_data.get("recommended_duration_min", 0.0)

        if rain_active:
            alerts.append({
                "alert_id": f"ALT-IRR-{uuid.uuid4().hex[:6]}",
                "category": "irrigation",
                "alert_type": "delay_irrigation",
                "severity": "WARNING",
                "headline_en": "Delay Irrigation: Active Rain Detected",
                "headline_hi": "सिंचाई स्थगित करें: वर्षा संसूचक सक्रिय है",
                "action_en": f"Precipitation confirmed by sensor. Irrigation suspended to conserve power and prevent root hypoxia.",
                "action_hi": f"बारिश दर्ज की गई है। जड़ों में सड़न रोकने व बिजली बचत हेतु पंप को बंद रखा गया है।",
                "channels": ["SMS", "DASHBOARD"],
                "timestamp": now_str
            })
        elif moist_pct < thresh_pct:
            alerts.append({
                "alert_id": f"ALT-IRR-{uuid.uuid4().hex[:6]}",
                "category": "irrigation",
                "alert_type": "irrigate_now",
                "severity": "CRITICAL" if moist_pct < 15.0 else "WARNING",
                "headline_en": f"Irrigate Now: Soil Moisture at {moist_pct}%",
                "headline_hi": f"तुरंत सिंचाई करें: मृदा नमी {moist_pct}% पर पहुंची",
                "action_en": f"Moisture is below threshold ({thresh_pct}%). Apply ~{rec_liters} L/m² ({rec_mins} min drip cycle) to restore root zone.",
                "action_hi": f"नमी स्तर न्यूनतम सीमा ({thresh_pct}%) से कम है। जड़ क्षेत्र के लिए लगभग {rec_liters} ली/मी² ({rec_mins} मिनट) ड्रिप सिंचाई दें।",
                "channels": ["SMS", "LORA", "DASHBOARD"],
                "timestamp": now_str
            })

        # 2. HEAT STRESS WARNING
        heat_risk = environmental_risk.get("heatwave_risk", {})
        temp_c = heat_risk.get("ambient_temp_c", 28.0)
        if heat_risk.get("heat_stress_detected", False) or temp_c >= 38.0:
            alerts.append({
                "alert_id": f"ALT-HEAT-{uuid.uuid4().hex[:6]}",
                "category": "heatwave",
                "alert_type": "heat_stress_warning",
                "severity": "CRITICAL" if temp_c >= 42.0 else "WARNING",
                "headline_en": f"Heat-Stress Warning: Canopy Temp {temp_c}°C",
                "headline_hi": f"लू व तीव्र ताप चेतावनी: तापमान {temp_c}°C",
                "action_en": f"Extreme heat causes flower drop and fruit scorching. Maintain straw mulching and schedule night micro-sprinkling.",
                "action_hi": f"अत्यधिक तापमान से फूल झड़ने और फल झुलसने का खतरा है। पराली की मल्चिंग करें व शाम को हल्का छिड़काव दें।",
                "channels": ["SMS", "DASHBOARD"],
                "timestamp": now_str
            })

        # 3. FLOOD / WATERLOGGING RISK ALERT
        flood_risk = environmental_risk.get("flood_risk", {})
        if flood_risk.get("score", 0) >= 50.0 or moist_pct >= 80.0:
            alerts.append({
                "alert_id": f"ALT-FLD-{uuid.uuid4().hex[:6]}",
                "category": "flood",
                "alert_type": "flood_risk_alert",
                "severity": "CRITICAL" if moist_pct >= 85.0 else "WARNING",
                "headline_en": f"Flood-Risk Alert: Soil Saturation at {moist_pct}%",
                "headline_hi": f"जलभराव व बाढ़ चेतावनी: मृदा संतृप्ति {moist_pct}%",
                "action_en": f"Root asphyxiation danger. Inspect field drainage bunds and clear runoff ditches to prevent root rot.",
                "action_hi": f"जड़ों में ऑक्सीजन की कमी का खतरा है। मेड़ों से अतिरिक्त पानी की निकासी करें ताकि जड़ सड़न न हो।",
                "channels": ["SMS", "LORA", "DASHBOARD"],
                "timestamp": now_str
            })

        # 4. DISEASE OUTBREAK RISK
        disease_risk = environmental_risk.get("disease_risk", {})
        if disease_risk.get("score", 0) >= 50.0:
            alerts.append({
                "alert_id": f"ALT-DIS-{uuid.uuid4().hex[:6]}",
                "category": "disease",
                "alert_type": "disease_outbreak_risk",
                "severity": "WARNING",
                "headline_en": "Disease-Outbreak Risk: High Foliar Humidity",
                "headline_hi": "पादप रोग चेतावनी: फंगल बीजाणु वृद्धि के अनुकूल मौसम",
                "action_en": f"Prolonged humidity and moderate temperatures favor fungal blight. Apply preventative bio-spray (Trichoderma viride @ 5g/L).",
                "action_hi": f"अधिक नमी व अनुकूल तापमान फफूंद जनित रोगों को बढ़ावा देते हैं। जैविक कवकनाशी (ट्राइकोडर्मा @ 5 ग्राम/लीटर) का छिड़काव करें।",
                "channels": ["SMS", "DASHBOARD"],
                "timestamp": now_str
            })

        # 5. VISION DETECTOR FINDINGS (PEST OR PATHOLOGY)
        if vision_diagnostic:
            det_type = vision_diagnostic.get("detection_type")
            conf = vision_diagnostic.get("confidence_pct", 85.0)
            if det_type == "insect_pest":
                alerts.append({
                    "alert_id": f"ALT-PST-{uuid.uuid4().hex[:6]}",
                    "category": "pest",
                    "alert_type": "pest_outbreak_alert",
                    "severity": "CRITICAL" if conf >= 90.0 else "WARNING",
                    "headline_en": f"Pest Alert: {vision_diagnostic.get('label_en')} ({conf}%)",
                    "headline_hi": f"कीट प्रकोप चेतावनी: {vision_diagnostic.get('label_hi')} ({conf}%)",
                    "action_en": f"ETL: {vision_diagnostic.get('etl_threshold')}. Bio: {vision_diagnostic.get('bio_remedy_en')}",
                    "action_hi": f"ईटीएल स्तर: {vision_diagnostic.get('etl_threshold')}. जैविक उपचार: {vision_diagnostic.get('bio_remedy_hi')}",
                    "channels": ["SMS", "LORA", "DASHBOARD"],
                    "timestamp": now_str
                })
            elif det_type == "plant_disease" and vision_diagnostic.get("detected_key") != "healthy_leaf":
                alerts.append({
                    "alert_id": f"ALT-PAT-{uuid.uuid4().hex[:6]}",
                    "category": "pathology",
                    "alert_type": "pathology_alert",
                    "severity": "WARNING",
                    "headline_en": f"Pathology Diagnosed: {vision_diagnostic.get('label_en')}",
                    "headline_hi": f"फसल रोग निदान: {vision_diagnostic.get('label_hi')}",
                    "action_en": f"Organic: {vision_diagnostic.get('bio_remedy_en')}. Chemical: {vision_diagnostic.get('chemical_remedy_en')}",
                    "action_hi": f"जैविक: {vision_diagnostic.get('bio_remedy_hi')}. रासायनिक: {vision_diagnostic.get('chemical_remedy_hi')}",
                    "channels": ["SMS", "DASHBOARD"],
                    "timestamp": now_str
                })

        # If no alerts triggered, emit nominal status
        if not alerts:
            alerts.append({
                "alert_id": f"ALT-NOM-{uuid.uuid4().hex[:6]}",
                "category": "nominal",
                "alert_type": "system_nominal",
                "severity": "INFO",
                "headline_en": "Nominal: Agro-Climatic Conditions Optimal",
                "headline_hi": "सामान्य: खेत में नमी व मौसमी परिस्थितियां अनुकूल",
                "action_en": f"Soil moisture at {moist_pct}%. Continue standard crop monitoring.",
                "action_hi": f"मृदा नमी {moist_pct}% पर संतुलित है। सामान्य निगरानी जारी रखें।",
                "channels": ["DASHBOARD"],
                "timestamp": now_str
            })

        self.alert_history.extend(alerts)
        if len(self.alert_history) > 100:
            self.alert_history = self.alert_history[-100:]

        return alerts


# Singleton instance
alert_engine = AlertEngine()


if __name__ == "__main__":
    print("=" * 70)
    print("KISAN SATHI STRUCTURED BILINGUAL ALERT ENGINE EVALUATION")
    print("=" * 70)
    test_alerts = alert_engine.generate_alerts(
        irrigation_data={
            "moisture_pct": 17.5,
            "moisture_threshold_pct": 25.0,
            "rain_inhibitor_active": False,
            "recommended_water_liters_sqm": 12.5,
            "recommended_duration_min": 15.0
        },
        environmental_risk={
            "heatwave_risk": {"ambient_temp_c": 39.5, "heat_stress_detected": True},
            "flood_risk": {"score": 0.0},
            "disease_risk": {"score": 65.0}
        }
    )

    for i, a in enumerate(test_alerts, 1):
        print(f"\n[{i}] {a['headline_en']} [{a['severity']}]")
        print(f"    Hindi:  {a['headline_hi']}")
        print(f"    Action: {a['action_en']}")
        print(f"    Channels: {', '.join(a['channels'])}")
    print("=" * 70)
