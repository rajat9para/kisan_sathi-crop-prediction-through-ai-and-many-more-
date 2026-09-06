"""
Kisan Sathi 2.0 - Environmental Risk Engine
Target: SIH 2026 Problem Statement #26180 (Agriculture, FoodTech & Rural Development)

Computes multi-factor environmental risk indices on-device:
1. Drought Risk Index (0-100): Moisture depletion, high evapotranspiration, rain absence
2. Flood / Waterlogging Risk Index (0-100): Soil saturation (>70%), active rain, high humidity
3. Heatwave & Thermal Stress Index (0-100): Temperature extremes (>38°C), low vapor pressure deficit
4. Disease Outbreak Risk Index (0-100): High humidity (>78%), moderate warmth (20-30°C), ideal for fungal sporulation
"""

import sys
import logging
from typing import Dict, Any, Optional

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

logger = logging.getLogger("EnvironmentalRisk")


class EnvironmentalRiskEngine:
    """Calculates comprehensive agro-climatic risk scores directly on edge node."""

    def __init__(self):
        pass

    def calculate_drought_risk(
        self,
        soil_moisture_pct: float,
        temperature_c: float,
        rainfall_7d_mm: float = 0.0,
        moisture_threshold_pct: float = 25.0
    ) -> Dict[str, Any]:
        """
        Drought risk scales inversely with soil moisture and rainfall,
        and directly with heat-driven evaporative stress.
        """
        # Moisture score: 0 when moisture >= 50%, 100 when moisture <= 10%
        if soil_moisture_pct <= 10.0:
            moist_score = 100.0
        elif soil_moisture_pct >= 50.0:
            moist_score = 0.0
        else:
            moist_score = ((50.0 - soil_moisture_pct) / 40.0) * 100.0

        # Thermal multiplier: increases above 32°C
        heat_multiplier = 1.0 + max(0.0, (temperature_c - 32.0) * 0.04)

        # Rainfall mitigation: 7-day rainfall dampens drought risk
        rain_mitigation = max(0.0, min(1.0, rainfall_7d_mm / 30.0))

        score = (moist_score * heat_multiplier) * (1.0 - rain_mitigation * 0.8)
        score = max(0.0, min(100.0, score))

        if score >= 75.0:
            status = "CRITICAL"
        elif score >= 50.0:
            status = "HIGH"
        elif score >= 25.0:
            status = "MODERATE"
        else:
            status = "LOW"

        return {
            "score": round(score, 1),
            "status": status,
            "soil_moisture_pct": round(soil_moisture_pct, 1),
            "rainfall_7d_mm": round(rainfall_7d_mm, 1)
        }

    def calculate_flood_risk(
        self,
        soil_moisture_pct: float,
        rain_detected: bool,
        rainfall_7d_mm: float = 0.0
    ) -> Dict[str, Any]:
        """
        Flood / Waterlogging risk evaluated on root-zone saturation and surface precipitation.
        """
        base_score = 0.0
        if soil_moisture_pct >= 85.0:
            base_score += 65.0
        elif soil_moisture_pct >= 70.0:
            base_score += 40.0
        elif soil_moisture_pct >= 55.0:
            base_score += 15.0

        if rain_detected:
            base_score += 35.0

        if rainfall_7d_mm > 80.0:
            base_score += 25.0
        elif rainfall_7d_mm > 40.0:
            base_score += 10.0

        score = max(0.0, min(100.0, base_score))
        if score >= 75.0:
            status = "CRITICAL"
        elif score >= 50.0:
            status = "HIGH"
        elif score >= 25.0:
            status = "MODERATE"
        else:
            status = "LOW"

        return {
            "score": round(score, 1),
            "status": status,
            "rain_detected": rain_detected,
            "soil_saturated": soil_moisture_pct >= 75.0
        }

    def calculate_heatwave_risk(
        self,
        temperature_c: float,
        humidity_pct: float
    ) -> Dict[str, Any]:
        """
        Evaluates thermal stress and Heat Index on crops.
        Temperatures above 38°C cause flower abortion and pollen sterility in tomatoes/cotton.
        """
        # Simple Steadman heat index approximation
        heat_index = temperature_c
        if temperature_c >= 27.0 and humidity_pct >= 40.0:
            heat_index = -8.784 + 1.611 * temperature_c + 2.338 * humidity_pct - 0.146 * temperature_c * humidity_pct

        if temperature_c >= 42.0 or heat_index >= 45.0:
            score = 95.0
            status = "EXTREME"
        elif temperature_c >= 38.0 or heat_index >= 40.0:
            score = 75.0
            status = "HIGH"
        elif temperature_c >= 34.0:
            score = 45.0
            status = "MODERATE"
        else:
            score = max(5.0, min(25.0, (temperature_c / 34.0) * 25.0))
            status = "LOW"

        return {
            "score": round(score, 1),
            "status": status,
            "ambient_temp_c": round(temperature_c, 1),
            "humidity_pct": round(humidity_pct, 1),
            "heat_stress_detected": score >= 50.0
        }

    def calculate_disease_outbreak_risk(
        self,
        temperature_c: float,
        humidity_pct: float,
        rain_detected: bool = False
    ) -> Dict[str, Any]:
        """
        Fungal and bacterial pathogen spores germinate rapidly under:
        - Warm temperatures (20°C to 29°C)
        - High relative humidity (> 80%) or wet leaf surface
        """
        temp_factor = 0.0
        if 20.0 <= temperature_c <= 29.0:
            temp_factor = 1.0  # Optimal fungal growth window
        elif 16.0 <= temperature_c < 20.0 or 29.0 < temperature_c <= 34.0:
            temp_factor = 0.65
        else:
            temp_factor = 0.25

        hum_factor = 0.0
        if humidity_pct >= 85.0:
            hum_factor = 1.0
        elif humidity_pct >= 70.0:
            hum_factor = ((humidity_pct - 70.0) / 15.0) * 0.7 + 0.3
        else:
            hum_factor = max(0.05, (humidity_pct / 70.0) * 0.25)

        base_score = (temp_factor * 0.5 + hum_factor * 0.5) * 100.0
        if rain_detected:
            base_score = min(100.0, base_score * 1.25)

        score = round(max(0.0, min(100.0, base_score)), 1)
        if score >= 75.0:
            status = "CRITICAL"
        elif score >= 50.0:
            status = "HIGH"
        elif score >= 25.0:
            status = "MODERATE"
        else:
            status = "LOW"

        return {
            "score": score,
            "status": status,
            "temp_in_optimal_spore_range": 20.0 <= temperature_c <= 29.0,
            "high_humidity_favoring_fungi": humidity_pct >= 75.0
        }

    def evaluate_all(
        self,
        soil_moisture_pct: float,
        temperature_c: float,
        humidity_pct: float,
        rain_detected: bool = False,
        rainfall_7d_mm: float = 0.0
    ) -> Dict[str, Any]:
        """Aggregates all risk indices and computes overall farm vulnerability score."""
        drought = self.calculate_drought_risk(soil_moisture_pct, temperature_c, rainfall_7d_mm)
        flood = self.calculate_flood_risk(soil_moisture_pct, rain_detected, rainfall_7d_mm)
        heatwave = self.calculate_heatwave_risk(temperature_c, humidity_pct)
        disease = self.calculate_disease_outbreak_risk(temperature_c, humidity_pct, rain_detected)

        # Composite Farm Vulnerability Score: weighted max of active hazards
        scores = [drought["score"], flood["score"], heatwave["score"], disease["score"]]
        composite_score = round(0.5 * max(scores) + 0.5 * (sum(scores) / len(scores)), 1)

        # Determine Primary Hazard
        indexed = [
            ("Drought Deficit", drought["score"]),
            ("Waterlogging / Flood", flood["score"]),
            ("Thermal Heat Stress", heatwave["score"]),
            ("Pathogen Outbreak", disease["score"])
        ]
        indexed.sort(key=lambda x: x[1], reverse=True)
        primary_hazard = indexed[0][0] if indexed[0][1] >= 25.0 else "Normal Agro-Climatic Conditions"

        return {
            "composite_farm_risk_score": composite_score,
            "primary_hazard": primary_hazard,
            "drought_risk": drought,
            "flood_risk": flood,
            "heatwave_risk": heatwave,
            "disease_risk": disease
        }


# Singleton instance
environmental_risk_engine = EnvironmentalRiskEngine()


if __name__ == "__main__":
    print("=" * 70)
    print("KISAN SATHI ENVIRONMENTAL RISK ENGINE EVALUATION")
    print("=" * 70)
    res = environmental_risk_engine.evaluate_all(
        soil_moisture_pct=16.5,
        temperature_c=39.5,
        humidity_pct=42.0,
        rain_detected=False,
        rainfall_7d_mm=2.0
    )
    print(f"Composite Farm Risk: {res['composite_farm_risk_score']}/100")
    print(f"Primary Hazard: {res['primary_hazard']}")
    print(f"Drought Risk: {res['drought_risk']['score']} ({res['drought_risk']['status']})")
    print(f"Flood Risk: {res['flood_risk']['score']} ({res['flood_risk']['status']})")
    print(f"Heatwave Risk: {res['heatwave_risk']['score']} ({res['heatwave_risk']['status']})")
    print(f"Disease Risk: {res['disease_risk']['score']} ({res['disease_risk']['status']})")
    print("=" * 70)
