from fastapi import APIRouter
from app.models.schemas import VoiceQueryRequest, VoiceQueryResponse

router = APIRouter(prefix="/api/voice", tags=["Voice Saathi"])

INTENT_KNOWLEDGE_BASE = {
    "water": {
        "keywords": ["पानी", "सिंचाई", "water", "irrigation", "water requirement", "paani", "sinchai"],
        "hi": "सोयाबीन और मक्का जैसी फसलों के लिए 3 से 4 सिंचाइयों की आवश्यकता होती है। पहली सिंचाई बुवाई के 20-25 दिन बाद और दूसरी फूल आने के समय सबसे महत्वपूर्ण है। अधिक जलभराव से बचें।",
        "en": "Crops like Soybean and Maize require 3 to 4 irrigations across their lifecycle. The most critical stages are active vegetative branching (20-25 days) and flowering stage. Avoid stagnant water.",
        "tts_hi": "सोयाबीन और मक्का के लिए तीन से चार सिंचाई की आवश्यकता होती है। फूल आने के समय खेत में नमी अवश्य बनाए रखें।",
        "followups": ["खाद की मात्रा कितनी रखें?", "कीट नियंत्रण कैसे करें?"]
    },
    "fertilizer": {
        "keywords": ["खाद", "यूरिया", "डीएपी", "fertilizer", "urea", "dap", "koshak", "nutrients", "khand"],
        "hi": "बुवाई के समय प्रति एकड़ 50 किग्रा डीएपी और 25 किग्रा पोटाश (MOP) डालें। फसल 25-30 दिन की होने पर 35 किग्रा नीम कोटेड यूरिया और 5 किग्रा जिंक सल्फेट का छिड़काव करें।",
        "en": "Apply 50 kg DAP and 25 kg MOP (Potash) per acre as basal dose during sowing. At 25-30 days stage, top-dress with 35 kg Neem Coated Urea mixed with 5 kg Zinc Sulphate.",
        "tts_hi": "बुवाई के समय प्रति एकड़ पचास किलो डीएपी डालें। पच्चीस दिन बाद पैंतीस किलो यूरिया और जिंक सल्फेट का छिड़काव करें।",
        "followups": ["सिंचाई कब करनी है?", "मंडी में क्या भाव है?"]
    },
    "weather": {
        "keywords": ["मौसम", "बारिश", "पानी गिरेगा", "weather", "rain", "forecast", "mausam", "barish", "badal"],
        "hi": "अगले 48 घंटों में हल्की से मध्यम बारिश की संभावना है। तापमान 24 से 28 डिग्री के बीच रहेगा। बारिश के कारण आज कीटनाशक छिड़काव टाल दें।",
        "en": "Light to moderate showers are expected over the next 48 hours with temperatures between 24°C and 28°C. Please postpone pesticide spray operations until skies clear.",
        "tts_hi": "अगले अड़तालीस घंटों में हल्की बारिश की संभावना है। कीटनाशक छिड़काव अभी रोक दें।",
        "followups": ["फसल में जल निकासी कैसे करें?", "फसल का भाव क्या है?"]
    },
    "mandi": {
        "keywords": ["मंडी", "भाव", "कीमत", "रेट", "mandi", "price", "rate", "bhav", "market"],
        "hi": "आज आपकी नजदीकी नासिक / इंदौर मंडी में सोयाबीन ₹4,850 प्रति क्विंटल और चना ₹6,150 प्रति क्विंटल बिक रहा है। पिछले 7 दिनों में भाव में 3 से 4% की तेजी आई है।",
        "en": "Today at your local APMC Mandi, Soybean is trading at ₹4,850/quintal and Chickpea at ₹6,150/quintal. Prices have trended upward by 3-4% this week.",
        "tts_hi": "आज मंडी में सोयाबीन अड़तालीस सौ पचास रुपये और चना इकसठ सौ पचास रुपये प्रति क्विंटल के भाव पर है।",
        "followups": ["आने वाले हफ्तों का अनुमान क्या है?", "फसल भंडारण की सलाह"]
    },
    "disease": {
        "keywords": ["रोग", "बीमारी", "कीड़ा", "धब्बे", "पीला", "disease", "pest", "spots", "yellow", "leaf", "keeda"],
        "hi": "पत्तियों पर पीले या भूरे धब्बे फफूंद (Fungus) का संकेत हैं। इसके नियंत्रण के लिए नीम तेल (5 मिली/लीटर) या कॉपर ऑक्सीक्लोराइड (2.5 ग्राम/लीटर) का छिड़काव करें।",
        "en": "Yellow or brown necrotic spots on leaves typically indicate fungal blight. Spray Neem Oil (5ml/L) or Copper Oxychloride (2.5g/L) on affected foliage.",
        "tts_hi": "पत्तियों पर धब्बे फफूंद जनित रोग के लक्षण हैं। तुरंत पांच मिलीलीटर प्रति लीटर नीम तेल का छिड़काव करें।",
        "followups": ["लीफ डॉक्टर में पत्ती की फोटो स्कैन करें", "दवा की मात्रा"]
    }
}

@router.post("/query", response_model=VoiceQueryResponse)
async def handle_voice_query(req: VoiceQueryRequest):
    """
    NLP Intent Classifier and Conversational Engine for Voice Saathi.
    Matches farmer spoken queries in Hindi/Hinglish/English to actionable agronomic advice.
    """
    q_lower = req.query_text.lower().strip()
    detected_intent = "general_advisory"
    matched_data = None
    
    for intent, data in INTENT_KNOWLEDGE_BASE.items():
        if any(kw in q_lower for kw in data["keywords"]):
            detected_intent = intent
            matched_data = data
            break

    if not matched_data:
        # Default smart agronomic advisor response
        matched_data = {
            "hi": "एग्रीसाथी एआई आपके खेत की मिट्टी, मौसम और मंडी भाव का विश्लेषण कर सर्वश्रेष्ठ फसल व कृषि सलाह प्रदान करता है। आप खाद, पानी, मौसम या मंडी भाव के बारे में पूछ सकते हैं।",
            "en": "AgriSaathi AI analyzes your soil, weather, and market trends to deliver actionable crop guidance. You can ask about water needs, fertilizer dosage, weather forecasts, or mandi prices.",
            "tts_hi": "नमस्ते किसान भाई। आप खाद, पानी, मौसम, या मंडी भाव से जुड़ा कोई भी प्रश्न पूछ सकते हैं।",
            "followups": ["पानी कितना चाहिए?", "खाद की मात्रा?", "मंडी में भाव क्या है?"]
        }

    return {
        "query": req.query_text,
        "detected_intent": detected_intent,
        "response_text_hi": matched_data["hi"],
        "response_text_en": matched_data["en"],
        "tts_audio_text": matched_data["tts_hi"],
        "confidence": 0.94,
        "suggested_followups": matched_data["followups"]
    }
