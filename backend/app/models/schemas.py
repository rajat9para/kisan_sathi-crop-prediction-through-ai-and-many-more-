from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any

class SoilParameters(BaseModel):
    nitrogen: float = Field(..., description="Soil Nitrogen (N) content in kg/ha or ppm")
    phosphorus: float = Field(..., description="Soil Phosphorus (P) content in kg/ha or ppm")
    potassium: float = Field(..., description="Soil Potassium (K) content in kg/ha or ppm")
    ph: float = Field(..., description="Soil pH value (3.5 to 9.5)")
    organic_carbon_pct: Optional[float] = Field(0.65, description="Organic Carbon percentage")
    texture: Optional[str] = Field("Clay Loam", description="Soil Texture type")
    soil_moisture_pct: Optional[float] = Field(32.0, description="Volumetric soil moisture percentage (0-100%)")

class WeatherParameters(BaseModel):
    temperature_c: float = Field(..., description="Average temperature in Celsius")
    humidity_pct: float = Field(..., description="Relative humidity percentage")
    rainfall_mm: float = Field(..., description="Seasonal expected rainfall in mm")
    soil_moisture_pct: Optional[float] = Field(32.0, description="Volumetric soil moisture percentage")
    weather_condition: Optional[str] = Field("Sunny", description="Current weather description")

class RecommendationRequest(BaseModel):
    latitude: float = Field(..., description="Farm latitude coordinate")
    longitude: float = Field(..., description="Farm longitude coordinate")
    state: Optional[str] = Field("Maharashtra", description="State name")
    district: Optional[str] = Field("Nashik", description="District name")
    farm_size_acres: Optional[float] = Field(2.5, description="Farm holding size in acres")
    irrigation_source: Optional[str] = Field("Borewell", description="Rainfed, Borewell, Canal, Drip")
    previous_crop: Optional[str] = Field(None, description="Previous season crop name")
    custom_soil: Optional[SoilParameters] = Field(None, description="User provided or OCR soil parameters")
    custom_weather: Optional[WeatherParameters] = Field(None, description="User provided weather override")
    device_id: Optional[str] = Field(None, description="Optional IoT sensor device ID for real-time reading ingestion")
    use_iot_sensor_data: Optional[bool] = Field(False, description="Whether to ingest live hardware telemetry")

class ShapContribution(BaseModel):
    feature: str
    feature_name_hi: str
    impact_score: float # positive means boosted recommendation, negative means penalized
    farmer_explanation_en: str
    farmer_explanation_hi: str
    status: str # "positive", "neutral", "negative"

class CropRecommendation(BaseModel):
    rank: int
    crop_name: str
    crop_name_hi: str
    scientific_name: str
    match_score_pct: float
    base_ml_confidence_pct: float
    
    # 4 Pillar Breakdown
    soil_fit_pct: float
    weather_fit_pct: float
    market_profitability_pct: float
    rotation_impact_pct: float
    
    # Dynamic Economics & Yield Forecasting
    expected_yield_per_acre: str
    estimated_revenue_per_acre: str
    estimated_cost_per_acre_rs: float
    estimated_net_profit_per_acre_rs: float
    mandi_price_per_quintal: str
    price_trend: str # "up", "down", "stable"
    water_requirement_level: str # "Low", "Medium", "High"
    sowing_window: str
    sowing_window_hi: str
    harvest_duration_days: int

    # Sustainability Forecasting (SIH 2026 Core Metric)
    sustainability_score_pct: float
    sustainability_rating: str # "High (Eco-Friendly)", "Moderate", "Requires Soil Care"
    sustainability_factors: Dict[str, Any]
    
    # Explainability & Guidance
    why_this_crop_summary_en: str
    why_this_crop_summary_hi: str
    shap_contributions: List[ShapContribution]
    recommended_fertilizer_schedule: List[Dict[str, str]]
    irrigation_schedule: List[Dict[str, str]]

class RecommendationResponse(BaseModel):
    timestamp: str
    is_cached_demo_location: bool
    location: Dict[str, Any]
    soil_snapshot: Dict[str, Any]
    weather_snapshot: Dict[str, Any]
    top_recommendations: List[CropRecommendation]
    advisory_warnings: List[Dict[str, str]]

class SoilResponse(BaseModel):
    latitude: float
    longitude: float
    source: str
    ph: float
    nitrogen_kg_ha: float
    phosphorus_kg_ha: float
    potassium_kg_ha: float
    organic_carbon_pct: float
    clay_content_pct: float
    sand_content_pct: float
    soil_moisture_pct: float
    soil_type: str

class WeatherDayForecast(BaseModel):
    date: str
    day_name: str
    temp_max: float
    temp_min: float
    humidity_avg: float
    precipitation_prob: float
    weather_desc: str
    spray_condition_rating: str # "Good for Spraying", "Avoid - Rain Expected", "High Wind"

class WeatherResponse(BaseModel):
    latitude: float
    longitude: float
    current_temp_c: float
    current_humidity_pct: float
    current_condition: str
    wind_speed_kmh: float
    rainfall_7d_total_mm: float
    soil_moisture_pct: float
    forecast_7d: List[WeatherDayForecast]
    alerts: List[Dict[str, str]]

class MarketPriceItem(BaseModel):
    commodity: str
    commodity_hi: str
    variety: str
    market_name: str
    state: str
    modal_price_rs_quintal: float
    min_price_rs_quintal: float
    max_price_rs_quintal: float
    trend_pct_7d: float
    trend_direction: str # "up", "down", "stable"
    arrival_date: str

class MarketResponse(BaseModel):
    state: str
    district: str
    prices: List[MarketPriceItem]
    timestamp: str
    data_source: Optional[str] = "Agmarknet APMC Radar (Daily Sync)"

class VoiceQueryRequest(BaseModel):
    query_text: str
    language: Optional[str] = "hi" # "hi" or "en"
    crop_context: Optional[str] = None
    location_context: Optional[str] = "Nashik"

class VoiceQueryResponse(BaseModel):
    query: str
    detected_intent: str
    intent_type: Optional[str] = "GENERAL_AGRONOMY"
    response_text_hi: str
    response_text_en: str
    tts_audio_text: str
    confidence: float
    suggested_followups: List[str]

class OCRSoilCardRequest(BaseModel):
    image_base64: Optional[str] = None
    sample_preset: Optional[str] = None

class OCRSoilCardResponse(BaseModel):
    detected_scheme: str
    farmer_name: Optional[str]
    lab_id: Optional[str]
    sample_date: str
    extraction_source: str # "OCR Image Recognition" or "Demo Preset"
    confidence_score_pct: float
    parameters: SoilParameters
    health_status: Dict[str, str]

# IoT Telemetry Schemas
class IoTReadingRequest(BaseModel):
    device_id: str = Field(..., description="Unique hardware device identifier (e.g. ESP32-SOIL-01)")
    soil_moisture_pct: float = Field(..., description="Volumetric soil moisture percentage (0-100%)")
    soil_temperature_c: float = Field(..., description="Soil temperature in Celsius")
    soil_ph: Optional[float] = Field(6.8, description="Real-time probe soil pH")
    nitrogen_ppm: Optional[float] = Field(None, description="Optical NPK sensor Nitrogen in ppm / mg/kg")
    phosphorus_ppm: Optional[float] = Field(None, description="Optical NPK sensor Phosphorus in ppm")
    potassium_ppm: Optional[float] = Field(None, description="Optical NPK sensor Potassium in ppm")
    battery_level_pct: Optional[float] = Field(98.0, description="Sensor node battery level")
    timestamp: Optional[str] = Field(None, description="ISO timestamp")

class IoTReadingResponse(BaseModel):
    status: str
    device_id: str
    recorded_at: str
    soil_moisture_pct: float
    soil_temperature_c: float
    soil_ph: float
    nitrogen_kg_ha: float
    phosphorus_kg_ha: float
    potassium_kg_ha: float
    moisture_status: str # "Optimal", "Dry (Irrigation Needed)", "Waterlogged"

# Satellite NDVI Schemas
class SatelliteNDVIResponse(BaseModel):
    latitude: float
    longitude: float
    satellite_feed: str
    acquisition_date: str
    mean_ndvi: float # -0.2 to 1.0
    mean_ndre: float
    vegetation_vigor_category: str # "High Canopy Vigor", "Moderate Vigor", "Sparse/Stressed"
    moisture_stress_index: float
    canopy_coverage_pct: float
    advisory_recommendation_en: str
    advisory_recommendation_hi: str
