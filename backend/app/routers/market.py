from fastapi import APIRouter, Query
from typing import Optional
from datetime import datetime
from app.services.external_apis import fetch_market_prices

router = APIRouter(prefix="/api", tags=["Market Mandi Prices"])

@router.get("/market-prices")
async def get_market_prices(
    state: str = Query("Maharashtra", description="State name"),
    district: str = Query("Nashik", description="District name"),
    lat: float = Query(19.9975, description="Latitude"),
    lon: float = Query(73.7898, description="Longitude"),
    commodity: Optional[str] = Query(None, description="Optional filter for commodity name")
):
    """
    Fetches real Agmarknet Mandi commodity rates and calculates 7-day price momentum.
    """
    prices = fetch_market_prices(state=state, district=district, lat=lat, lon=lon)
    if commodity:
        c_lower = commodity.lower().strip()
        prices = [p for p in prices if c_lower in p["commodity"].lower() or c_lower in p["commodity_hi"]]

    return {
        "state": state,
        "district": district,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data_source": "Agmarknet APMC Radar (Daily Sync)",
        "prices": prices
    }
