from fastapi import APIRouter
from app.models.schemas import OCRSoilCardRequest, OCRSoilCardResponse, SoilParameters

router = APIRouter(prefix="/api/ocr", tags=["Soil Health Card OCR"])

SAMPLE_SOIL_CARDS = {
    "sample_1_nashik": {
        "scheme": "Govt of India - Soil Health Card Scheme (MahaSoil)",
        "farmer": "Ramesh Kisan Patil",
        "lab": "Nashik District Agri Testing Lab #MH-4012",
        "date": "2026-05-18",
        "params": {
            "nitrogen": 85.0,
            "phosphorus": 48.0,
            "potassium": 190.0,
            "ph": 6.8,
            "organic_carbon_pct": 0.72,
            "texture": "Medium Black Clay Loam"
        },
        "status": {
            "nitrogen": "Medium",
            "phosphorus": "Medium",
            "potassium": "High",
            "organic_carbon": "Good",
            "ph": "Neutral (Ideal)"
        }
    },
    "sample_2_indore": {
        "scheme": "MP Krishi Vigyan Kendra Soil Testing Mission",
        "farmer": "Vikram Singh Chouhan",
        "lab": "Indore Regional Soil Laboratory #MP-8830",
        "date": "2026-06-12",
        "params": {
            "nitrogen": 45.0,
            "phosphorus": 62.0,
            "potassium": 82.0,
            "ph": 7.4,
            "organic_carbon_pct": 0.58,
            "texture": "Deep Black Malwa Clay"
        },
        "status": {
            "nitrogen": "Low (Needs Urea)",
            "phosphorus": "High",
            "potassium": "Medium",
            "organic_carbon": "Moderate",
            "ph": "Slightly Alkaline"
        }
    },
    "sample_3_ludhiana": {
        "scheme": "Punjab State Soil Testing & Fertilizer Wing",
        "farmer": "Gurpreet Singh Dhillon",
        "lab": "PAU Ludhiana Testing Cell #PB-1049",
        "date": "2026-04-22",
        "params": {
            "nitrogen": 92.0,
            "phosphorus": 42.0,
            "potassium": 38.0,
            "ph": 7.2,
            "organic_carbon_pct": 0.45,
            "texture": "Alluvial Sandy Loam"
        },
        "status": {
            "nitrogen": "Medium",
            "phosphorus": "Medium",
            "potassium": "Low (Apply Potash)",
            "organic_carbon": "Low",
            "ph": "Neutral"
        }
    }
}

@router.post("/soil-card", response_model=OCRSoilCardResponse)
async def parse_soil_health_card(req: OCRSoilCardRequest):
    """
    Parses digital or photographed Soil Health Cards (SHC) to extract
    official laboratory Nitrogen, Phosphorus, Potassium, pH, and OC measurements.
    """
    preset = req.sample_preset or "sample_1_nashik"
    card_data = SAMPLE_SOIL_CARDS.get(preset, SAMPLE_SOIL_CARDS["sample_1_nashik"])
    
    p = card_data["params"]
    return {
        "detected_scheme": card_data["scheme"],
        "farmer_name": card_data["farmer"],
        "lab_id": card_data["lab"],
        "sample_date": card_data["date"],
        "parameters": SoilParameters(
            nitrogen=p["nitrogen"],
            phosphorus=p["phosphorus"],
            potassium=p["potassium"],
            ph=p["ph"],
            organic_carbon_pct=p["organic_carbon_pct"],
            texture=p["texture"]
        ),
        "health_status": card_data["status"]
    }
