import os

class Config:
    API_TITLE = "AgriSaathi AI Crop Advisory API"
    API_VERSION = "1.0.0"
    API_DESCRIPTION = "Hyper-local explainable crop advisory backend with SoilGrids, Open-Meteo, Agmarknet, and XGBoost+SHAP ML engine."
    
    # External APIs
    SOILGRIDS_API_URL = "https://rest.isric.org/soilgrids/v2.0/properties/query"
    OPEN_METEO_API_URL = "https://api.open-meteo.com/v1/forecast"
    
    # ML Artifacts Path
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ARTIFACTS_DIR = os.path.join(BASE_DIR, "ml", "artifacts")
    
    # Network timeout (seconds)
    REQUEST_TIMEOUT = 4.0

config = Config()
