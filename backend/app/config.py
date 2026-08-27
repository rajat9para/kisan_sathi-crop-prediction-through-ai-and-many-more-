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

    # Supabase Database Configuration
    SUPABASE_URL = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
    SUPABASE_PUBLISHABLE_KEY = os.getenv("SUPABASE_PUBLISHABLE_KEY", "")

config = Config()
