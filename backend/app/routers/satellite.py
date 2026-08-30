from fastapi import APIRouter, Query
from app.models.schemas import SatelliteNDVIResponse
from app.services.satellite_service import satellite_service

router = APIRouter(prefix="/api/satellite", tags=["Satellite Earth Observation & NDVI"])

@router.get("/ndvi", response_model=SatelliteNDVIResponse)
async def get_satellite_ndvi(
    lat: float = Query(19.9975, description="Farm Latitude"),
    lon: float = Query(73.7898, description="Farm Longitude")
):
    """
    Returns Sentinel-2 multispectral NDVI, NDRE, canopy coverage %, and moisture stress
    for precision agriculture parcel monitoring.
    """
    data = satellite_service.get_parcel_ndvi(lat=lat, lon=lon)
    return data
