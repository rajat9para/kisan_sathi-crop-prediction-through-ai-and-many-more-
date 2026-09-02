import os
from dotenv import load_dotenv

# Load local .env if available
load_dotenv()
# Also check root directory for .env
root_env = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".env")
if os.path.exists(root_env):
    load_dotenv(root_env)

class Config:
    API_TITLE = "Kisaan_Sathi AI Crop Advisory API"
    API_VERSION = "1.1.0"
    API_DESCRIPTION = "Hyper-local explainable crop advisory backend with XGBoost + SHAP, Groq LLaMA LLM, Supabase Database, SoilGrids, and Open-Meteo."
    
    # External APIs
    SOILGRIDS_API_URL = "https://rest.isric.org/soilgrids/v2.0/properties/query"
    OPEN_METEO_API_URL = "https://api.open-meteo.com/v1/forecast"
    
    # ML Artifacts Path
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ARTIFACTS_DIR = os.path.join(BASE_DIR, "ml", "artifacts")
    
    # Network timeout (seconds)
    REQUEST_TIMEOUT = 4.0

    # Groq LLM Configuration
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
    GROQ_FAST_MODEL = os.getenv("GROQ_FAST_MODEL", "llama-3.1-8b-instant")

    # data.gov.in (Agmarknet Live Mandi Prices) Configuration
    # Free API key: https://data.gov.in/user/register -> "Request API Key"
    DATA_GOV_API_KEY = os.getenv("DATA_GOV_API_KEY", "")
    # Official resource: "Current Daily Price of Various Commodities from Various Markets (Mandi)"
    DATA_GOV_MANDI_RESOURCE = os.getenv(
        "DATA_GOV_MANDI_RESOURCE", "9ef84268-d588-465a-a308-a864a43d0070"
    )

    # Copernicus Data Space Ecosystem (real Sentinel-2 NDVI) OAuth credentials
    # Free registration: https://documentation.dataspace.copernicus.eu/ - create OAuth client
    CDSE_CLIENT_ID = os.getenv("CDSE_CLIENT_ID", "")
    CDSE_CLIENT_SECRET = os.getenv("CDSE_CLIENT_SECRET", "")

    # Supabase Database Configuration
    SUPABASE_URL = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
    SUPABASE_PUBLISHABLE_KEY = os.getenv("SUPABASE_PUBLISHABLE_KEY", "")

config = Config()

