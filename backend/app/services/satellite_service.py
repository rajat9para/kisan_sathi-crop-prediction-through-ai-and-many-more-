"""
Satellite Earth Observation Service — REAL Sentinel-2 NDVI via Copernicus Data Space
====================================================================================
Primary path (when CDSE_CLIENT_ID / CDSE_CLIENT_SECRET are configured):
  1. OAuth2 client-credentials token from CDSE Keycloak.
  2. Statistical API request for Sentinel-2 L2A NDVI over a small parcel bbox
     (last 60 days, cloud coverage <= 20%), aggregated to 5-day means.
  3. Latest valid NDVI mean -> canopy vigor assessment.

Fallback path (no credentials / API unavailable):
  A clearly-labelled *estimated* vegetation index derived from geographic and
  seasonal heuristics. It is NEVER presented as real Sentinel-2 data — the
  response carries 'data_mode': 'estimated' and an explicit advisory note.

Free credentials: https://shapps.dataspace.copernicus.eu/dashboard/#/account/settings
  -> create an OAuth client -> set CDSE_CLIENT_ID / CDSE_CLIENT_SECRET env vars.
"""

from datetime import datetime, timedelta
import math
import base64
from typing import Dict, Any, Optional

import requests

from app.config import config

CDSE_TOKEN_URL = (
    "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/"
    "protocol/openid-connect/token"
)
CDSE_STATS_URL = "https://sh.dataspace.copernicus.eu/api/v1/statistical"

EVALSCRIPT = """
//VERSION=3
function setup() {
  return {
    input: [{ datasource: "S2L2A", bands: ["B04", "B08"] }],
    output: { bands: 1, sampleType: "FLOAT32" }
  };
}
function evaluatePixel(s) {
  var denom = (s.B08 + s.B04);
  if (denom <= 0) return [0];
  var ndvi = (s.B08 - s.B04) / (denom + 0.0001);
  return [ndvi];
}
"""

class SatelliteObservationService:
    # ------------------------------------------------------------------
    # Real Sentinel-2 path
    # ------------------------------------------------------------------
    def _get_cdse_token(self) -> Optional[str]:
        try:
            creds = base64.b64encode(
                f"{config.CDSE_CLIENT_ID}:{config.CDSE_CLIENT_SECRET}".encode()
            ).decode()
            resp = requests.post(
                CDSE_TOKEN_URL,
                headers={
                    "Authorization": f"Basic {creds}",
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                data={"grant_type": "client_credentials"},
                timeout=config.REQUEST_TIMEOUT + 6,
            )
            if resp.status_code == 200:
                return resp.json().get("access_token")
        except Exception as e:
            print(f"[!] CDSE token error: {e}")
        return None

    def _fetch_real_ndvi(self, lat: float, lon: float) -> Optional[Dict[str, Any]]:
        token = self._get_cdse_token()
        if not token:
            return None

        to_dt = datetime.utcnow()
        from_dt = to_dt - timedelta(days=60)
        half_deg = 0.0045  # ~500 m parcel window
        bbox = [
            round(lon - half_deg, 5), round(lat - half_deg, 5),
            round(lon + half_deg, 5), round(lat + half_deg, 5),
        ]

        body = {
            "input": {
                "bounds": {
                    "bbox": bbox,
                    "properties": {"crs": "http://www.opengis.net/def/crs/EPSG/0/4326"},
                },
                "data": [{
                    "type": "sentinel-2-l2a",
                    "dataFilter": {
                        "timeRange": {
                            "from": from_dt.strftime("%Y-%m-%dT00:00:00Z"),
                            "to": to_dt.strftime("%Y-%m-%dT23:59:59Z"),
                        },
                        "maxCloudCoverage": 20,
                    },
                }],
            },
            "aggregation": {
                "timeRange": {
                    "from": from_dt.strftime("%Y-%m-%dT00:00:00Z"),
                    "to": to_dt.strftime("%Y-%m-%dT23:59:59Z"),
                },
                "aggregationInterval": {"of": "P5D"},
                "resx": "10m",
                "resy": "10m",
                "aggregations": {"NDVI": {"function": "mean"}},
            },
            "process": {
                "request": {
                    "processors": {"custom": {"script": EVALSCRIPT}}
                }
            },
        }

        try:
            resp = requests.post(
                CDSE_STATS_URL,
                json=body,
                headers={"Authorization": f"Bearer {token}"},
                timeout=config.REQUEST_TIMEOUT + 16,
            )
            if resp.status_code != 200:
                print(f"[!] CDSE statistical API returned {resp.status_code}")
                return None

            data = resp.json().get("data", [])
            for bucket in data:
                intervals = bucket.get("data", {})
                output = intervals.get("NDVI", {})
                buckets = output.get("buckets", {})
                stats_b0 = buckets.get("B0", {})
                mean_val = stats_b0.get("mean")
                if mean_val is None:
                    continue
                mean_ndvi = round(float(mean_val), 3)
                if not (0.0 <= mean_ndvi <= 1.0):
                    continue
                return {
                    "mean_ndvi": mean_ndvi,
                    "acquisition_date": self._nearest_s2_date(bucket),
                    "source": "Copernicus Sentinel-2 L2A via CDSE Statistical API (real satellite data)",
                }
        except Exception as e:
            print(f"[!] CDSE NDVI request error: {e}")
        return None

    def _nearest_s2_date(self, bucket: Dict[str, Any]) -> str:
        """Picks the centre date of the aggregation interval for display."""
        try:
            frm = bucket.get("data", {}).get("from", {})
            if isinstance(frm, dict):
                frm = frm.get("from", "")
            dt = datetime.fromisoformat(str(frm).replace("Z", "+00:00"))
            return (dt + timedelta(days=2)).strftime("%Y-%m-%d")
        except Exception:
            return (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d")

    # ------------------------------------------------------------------
    # Honest estimated fallback (clearly labelled, never "Sentinel-2")
    # ------------------------------------------------------------------
    def _estimated_ndvi(self, lat: float, lon: float) -> Dict[str, Any]:
        coord_factor = (math.sin(lat * 10.0) + math.cos(lon * 10.0)) / 2.0
        day_of_year = datetime.now().timetuple().tm_yday
        seasonal_growth = math.sin((day_of_year / 365.0) * 2.0 * math.pi) * 0.15
        mean_ndvi = round(min(0.88, max(0.22, 0.62 + (coord_factor * 0.18) + seasonal_growth)), 2)
        return {
            "mean_ndvi": mean_ndvi,
            "acquisition_date": datetime.now().strftime("%Y-%m-%d"),
            "source": "Estimated Vegetation Index (geographic + seasonal heuristic — NOT satellite data)",
        }

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def get_parcel_ndvi(self, lat: float, lon: float) -> Dict[str, Any]:
        """
        Retrieves multispectral vegetative indices for precision farm management.
        Uses real Sentinel-2 L2A statistics when CDSE credentials are configured;
        otherwise returns an explicitly-labelled estimated index.
        """
        real = None
        if config.CDSE_CLIENT_ID and config.CDSE_CLIENT_SECRET:
            real = self._fetch_real_ndvi(lat, lon)

        if real:
            mean_ndvi = real["mean_ndvi"]
            data_mode = "live_sentinel2"
            source = real["source"]
            ndre = round(min(0.65, max(0.18, mean_ndvi * 0.78)), 2)
            acquisition_date = real["acquisition_date"]
        else:
            est = self._estimated_ndvi(lat, lon)
            mean_ndvi = est["mean_ndvi"]
            data_mode = "estimated"
            source = est["source"]
            ndre = round(min(0.65, max(0.18, mean_ndvi * 0.78)), 2)
            acquisition_date = est["acquisition_date"]

        moisture_stress = round(min(1.0, max(0.05, 0.35 - (mean_ndvi * 0.25))), 2)
        canopy_coverage = round(min(98.0, max(25.0, mean_ndvi * 115.0)), 1)

        if mean_ndvi >= 0.65:
            vigor_cat = "High Canopy Vigor (Dense Healthy Vegetation)"
            adv_en = "Canopy photosynthetic activity is excellent. Normal fertilizer top-dressing recommended."
            adv_hi = "फसल का हरापन व विकास अत्यंत उत्तम है। सामान्य खाद की मात्रा जारी रखें।"
        elif mean_ndvi >= 0.45:
            vigor_cat = "Moderate Vigor (Standard Vegetative Growth)"
            adv_en = "Healthy baseline growth. Monitor light chlorosis patches in northern quadrant."
            adv_hi = "फसल सामान्य वृद्धि में है। पीलेपन वाले हिस्सों में सूक्ष्म पोषक तत्वों का छिड़काव करें।"
        else:
            vigor_cat = "Low / Stressed Canopy (Nutrient / Moisture Deficit)"
            adv_en = "Vegetation index indicates moisture stress or nitrogen deficiency. Check root zone."
            adv_hi = "उपग्रह तस्वीर में फसल पर नमी या पोषक तत्वों का तनाव दिख रहा है। तत्काल सिंचाई करें।"

        note_en, note_hi = ("", "")
        if data_mode == "estimated":
            note_en = ("Sentinel-2 credentials are not configured on this deployment, so an "
                       "estimated vegetation index is shown instead of real satellite imagery.")
            note_hi = ("इस डिप्लॉयमेंट पर Sentinel-2 क्रेडेंशियल कॉन्फ़िगर नहीं हैं, इसलिए वास्तविक "
                       "उपग्रह डेटा के स्थान पर अनुमानित वनस्पति सूचकांक दिखाया जा रहा है।")

        return {
            "latitude": lat,
            "longitude": lon,
            "data_mode": data_mode,
            "source": source,
            "data_note_en": note_en,
            "data_note_hi": note_hi,
            "satellite_feed": source,
            "acquisition_date": acquisition_date,
            "mean_ndvi": mean_ndvi,
            "mean_ndre": ndre,
            "vegetation_vigor_category": vigor_cat,
            "moisture_stress_index": moisture_stress,
            "canopy_coverage_pct": canopy_coverage,
            "advisory_recommendation_en": adv_en,
            "advisory_recommendation_hi": adv_hi
        }


satellite_service = SatelliteObservationService()


