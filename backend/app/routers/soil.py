from fastapi import APIRouter, Query
from app.models.schemas import SoilResponse
from app.services.external_apis import fetch_soilgrids_data

router = APIRouter(prefix="/api", tags=["Soil Information"])

@router.get("/soil")
async def get_soil_data(
    lat: float = Query(19.9975, description="Latitude coordinate"),
    lon: float = Query(73.7898, description="Longitude coordinate")
):
    """
    Fetches real soil physicochemical data from ISRIC SoilGrids REST API v2.0
    with smart local hub fallback for demo locations.
    """
    data = fetch_soilgrids_data(lat, lon)
    return {
        "latitude": lat,
        "longitude": lon,
        **data
    }
