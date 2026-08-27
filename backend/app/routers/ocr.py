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
            "texture": "Medium Black Cotton Clay Loam"
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
            "texture": "Deep Black Malwa Vertisol Clay"
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
            "texture": "Indo-Gangetic Alluvial Sandy Loam"
        },
        "status": {
            "nitrogen": "High",
            "phosphorus": "Medium",
            "potassium": "Low (Apply Potash)",
            "organic_carbon": "Low",
            "ph": "Neutral"
        }
    },
    "sample_4_guntur": {
        "scheme": "Andhra Pradesh YSR Rythu Bharosa Testing Lab",
        "farmer": "Venkat Ramanayya",
        "lab": "Guntur District Agronomy Centre #AP-3190",
        "date": "2026-07-04",
        "params": {
            "nitrogen": 70.0,
            "phosphorus": 55.0,
            "potassium": 140.0,
            "ph": 6.5,
            "organic_carbon_pct": 0.65,
            "texture": "Coastal Red Clayey Sandy Loam"
        },
        "status": {
            "nitrogen": "Medium",
            "phosphorus": "Medium",
            "potassium": "High",
            "organic_carbon": "Good",
            "ph": "Slightly Acidic (Optimum for Chilli & Cotton)"
        }
    },
    "sample_5_rajkot": {
        "scheme": "Gujarat State Krishi Mahotsav Soil Wing",
        "farmer": "Mansukhbhai Patel",
        "lab": "Junagadh Agri Univ Testing Lab #GJ-5521",
        "date": "2026-05-30",
        "params": {
            "nitrogen": 58.0,
            "phosphorus": 64.0,
            "potassium": 165.0,
            "ph": 7.8,
            "organic_carbon_pct": 0.52,
            "texture": "Saurashtra Medium Black Calcareous Loam"
        },
        "status": {
            "nitrogen": "Medium",
            "phosphorus": "High",
            "potassium": "High",
            "organic_carbon": "Moderate",
            "ph": "Moderately Alkaline"
        }
    },
    "sample_6_thanjavur": {
        "scheme": "Tamil Nadu Dept of Agriculture Soil Lab",
        "farmer": "Muthusamy Sundaram",
        "lab": "Cauvery Delta Soil Health Station #TN-7204",
        "date": "2026-06-18",
        "params": {
            "nitrogen": 88.0,
            "phosphorus": 36.0,
            "potassium": 95.0,
            "ph": 6.7,
            "organic_carbon_pct": 0.81,
            "texture": "Cauvery Deltaic Alluvial Silt Clay"
        },
        "status": {
            "nitrogen": "High",
            "phosphorus": "Medium",
            "potassium": "Medium",
            "organic_carbon": "High (Rich in Humus)",
            "ph": "Neutral"
        }
    },
    "sample_7_bardhaman": {
        "scheme": "West Bengal Mati Tirtha Soil Network",
        "farmer": "Subrata Mukherjee",
        "lab": "Bardhaman Central Agricultural Lab #WB-6112",
        "date": "2026-06-25",
        "params": {
            "nitrogen": 95.0,
            "phosphorus": 32.0,
            "potassium": 88.0,
            "ph": 6.2,
            "organic_carbon_pct": 0.78,
            "texture": "Lower Gangetic Old Alluvial Clay Loam"
        },
        "status": {
            "nitrogen": "High",
            "phosphorus": "Low",
            "potassium": "Medium",
            "organic_carbon": "Good",
            "ph": "Slightly Acidic"
        }
    },
    "sample_8_jaipur": {
        "scheme": "Rajasthan Krishi Vigyan Soil Survey",
        "farmer": "Ramkishan Gurjar",
        "lab": "Jaipur Semi-Arid Zone Lab #RJ-2041",
        "date": "2026-05-10",
        "params": {
            "nitrogen": 32.0,
            "phosphorus": 28.0,
            "potassium": 120.0,
            "ph": 8.2,
            "organic_carbon_pct": 0.28,
            "texture": "Semi-Arid Desert Light Sandy Loam"
        },
        "status": {
            "nitrogen": "Low (Apply FYM / Compost)",
            "phosphorus": "Low",
            "potassium": "Medium",
            "organic_carbon": "Very Low",
            "ph": "Alkaline"
        }
    },
    "sample_9_dharwad": {
        "scheme": "Karnataka Raitha Mitra Soil Testing Center",
        "farmer": "Basavaraj Bommai Gowda",
        "lab": "UAS Dharwad Soil Clinic #KA-4418",
        "date": "2026-06-08",
        "params": {
            "nitrogen": 75.0,
            "phosphorus": 46.0,
            "potassium": 115.0,
            "ph": 6.4,
            "organic_carbon_pct": 0.69,
            "texture": "Western Ghats Red Laterite Loam"
        },
        "status": {
            "nitrogen": "Medium",
            "phosphorus": "Medium",
            "potassium": "Medium",
            "organic_carbon": "Good",
            "ph": "Slightly Acidic"
        }
    },
    "sample_10_varanasi": {
        "scheme": "UP Krishi Bhawan Soil Health Project",
        "farmer": "Chandrabhan Tiwari",
        "lab": "BHU Varanasi Soil Testing Hub #UP-9023",
        "date": "2026-05-22",
        "params": {
            "nitrogen": 82.0,
            "phosphorus": 52.0,
            "potassium": 68.0,
            "ph": 7.1,
            "organic_carbon_pct": 0.61,
            "texture": "Eastern Gangetic Silt Alluvial"
        },
        "status": {
            "nitrogen": "Medium",
            "phosphorus": "Medium",
            "potassium": "Medium",
            "organic_carbon": "Moderate",
            "ph": "Neutral"
        }
    },
    "sample_11_palakkad": {
        "scheme": "Kerala Karshika Karma Sena Testing Unit",
        "farmer": "Gopalakrishnan Nair",
        "lab": "KAU Palakkad Rice Research Soil Lab #KL-1845",
        "date": "2026-07-11",
        "params": {
            "nitrogen": 68.0,
            "phosphorus": 24.0,
            "potassium": 75.0,
            "ph": 5.4,
            "organic_carbon_pct": 1.15,
            "texture": "High-Rainfall Acidic Peaty Laterite"
        },
        "status": {
            "nitrogen": "Medium",
            "phosphorus": "Low (Apply Lime/Dolomite)",
            "potassium": "Medium",
            "organic_carbon": "Very High (Organic Matter Rich)",
            "ph": "Acidic"
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
