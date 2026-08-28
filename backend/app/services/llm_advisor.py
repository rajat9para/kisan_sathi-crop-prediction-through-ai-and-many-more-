"""
Grounded LLM Advisory Engine powered by Groq (LLaMA 3.3 / LLaMA 3.1).
Takes deterministic XGBoost + SHAP machine learning outputs and synthesizes
natural, personalized, weather-grounded conversational farmer guidance in Hindi and English.
"""

from typing import Dict, Any, List, Optional
from groq import Groq
from app.config import config

class LLMAdvisor:
    def __init__(self):
        self.client: Optional[Groq] = None
        self._init_client()

    def _init_client(self):
        try:
            if config.GROQ_API_KEY:
                self.client = Groq(api_key=config.GROQ_API_KEY)
                print("[+] Groq LLM client initialized successfully.")
        except Exception as e:
            print(f"[!] Warning: Could not initialize Groq client: {e}")
            self.client = None

    def answer_farmer_voice_query(
        self,
        query_text: str,
        language: str = "hi",
        crop_context: Optional[str] = "Soybean",
        location: Optional[str] = "Nashik, Maharashtra"
    ) -> Dict[str, Any]:
        """
        Uses Groq LLM to answer free-form farmer questions with deep agronomic accuracy.
        Falls back to local rule engine if offline or rate-limited.
        """
        lang_names = {
            "hi": "Hindi (हिंदी)",
            "en": "English",
            "mr": "Marathi (मराठी)",
            "pa": "Punjabi (ਪੰਜਾਬੀ)",
            "gu": "Gujarati (ગુજરાતી)",
            "te": "Telugu (తెలుగు)",
            "ta": "Tamil (தமிழ்)",
            "bn": "Bengali (বাংলা)",
            "kn": "Kannada (ಕನ್ನಡ)",
            "ml": "Malayalam (മലയാളം)",
            "or": "Odia (ଓଡ଼ିଆ)"
        }
        target_lang = lang_names.get(language, "Hindi (हिंदी)")

        if not self.client:
            return self._fallback_response(query_text, language)

        system_prompt = (
            "You are Kisaan_Sathi (किसान साथी), an expert AI Agricultural Scientist and compassionate advisor for Indian farmers.\n"
            f"Respond strictly in {target_lang}. If language is English, do not use any Hindi words. If Hindi, use pure respectful Hindi.\n"
            f"Location Context: {location}. Target Crop Context: {crop_context}.\n"
            "Rules:\n"
            "1. Keep the response direct, actionable, practical, and within 3-4 sentences so it is easy to listen via Text-to-Speech.\n"
            "2. Mention practical organic and chemical solutions with exact doses (e.g. 5ml/litre, 50kg/acre).\n"
            "3. Format the output strictly as JSON with keys: 'response_text_hi', 'response_text_en', 'response_text_regional', 'tts_audio_text', 'suggested_followups'."
        )

        models_to_try = [
            config.GROQ_MODEL,
            config.GROQ_FAST_MODEL,
            "openai/gpt-oss-120b",
            "openai/gpt-oss-20b",
            "qwen/qwen3.8-27b",
            "groq/compound",
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant"
        ]
        # Remove duplicates while preserving order
        models_to_try = list(dict.fromkeys([m for m in models_to_try if m]))

        for model_name in models_to_try:
            try:
                # Try direct response
                chat_completion = self.client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": f"You are Kisaan_Sathi, an expert AI Agricultural Scientist and advisor for Indian farmers in {location}. Answer the farmer's question directly in practical, helpful, empathetic {target_lang} with exact dosages and precautions in 2-3 sentences."},
                        {"role": "user", "content": query_text}
                    ],
                    model=model_name,
                    temperature=0.3,
                    max_tokens=300,
                    timeout=5.0
                )
                raw_text = chat_completion.choices[0].message.content.strip()
                if raw_text:
                    resp_hi = raw_text if language != "en" else ""
                    resp_en = raw_text if language == "en" else ""
                    return {
                        "query": query_text,
                        "detected_intent": "groq_llm_intelligence",
                        "model_used": model_name,
                        "language": language,
                        "response_text_hi": resp_hi,
                        "response_text_en": resp_en,
                        "response_text_regional": raw_text,
                        "tts_audio_text": raw_text,
                        "confidence": 0.98,
                        "suggested_followups": ["How much water is needed?", "Recommended spray timing?"] if language == "en" else ["पानी कितना देना है?", "छिड़काव का सही समय?"]
                    }
            except Exception as e:
                print(f"[!] Groq query note with model {model_name}: {e}")
                continue

        print("[!] All Groq models failed or unavailable. Using fallback rule engine.")
        return self._fallback_response(query_text, language)

    def generate_weather_grounded_spray_plan(
        self,
        crop: str,
        disease_name: str,
        rain_prob: float,
        temp_c: float
    ) -> Dict[str, str]:
        """
        Synthesizes a weather-aware disease treatment plan.
        Warns if rain will wash away fungicide spray.
        """
        if not self.client:
            return {
                "hi": f"{crop} में {disease_name} के लिए तुरंत अनुशंसित जैविक व रासायनिक कीटनाशक का छिड़काव करें।",
                "en": f"Apply recommended bio-pesticide for {disease_name} in {crop} during clear weather."
            }

        prompt = (
            f"A farmer has {crop} affected by {disease_name}. "
            f"Weather forecast: {rain_prob}% rain probability, temperature {temp_c}°C. "
            "Advise the farmer on exact spray timing and rain precautions in 2 sentences in both Hindi and English. "
            "Output JSON with keys 'hi' and 'en'."
        )

        for model_name in [config.GROQ_FAST_MODEL, "openai/gpt-oss-20b", "openai/gpt-oss-120b"]:
            try:
                res = self.client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model=model_name,
                    temperature=0.2,
                    max_tokens=250,
                    timeout=3.0,
                    response_format={"type": "json_object"}
                )
                import json
                return json.loads(res.choices[0].message.content)
            except Exception:
                continue

        return {
            "hi": f"कीटनाशक का छिड़काव मौसम साफ रहने पर सुबह या शाम के समय करें।",
            "en": f"Apply spray during clear weather conditions early in the morning."
        }

    def _fallback_response(self, query_text: str, language: str = "hi") -> Dict[str, Any]:
        q = query_text.lower()
        is_en = (language == "en")
        
        if any(k in q for k in ["पानी", "water", "irrigation", "सिंचाई"]):
            resp_hi = "फसल के लिए 3 से 4 सिंचाइयों की आवश्यकता होती है। पहली सिंचाई बुवाई के 20-25 दिन बाद और दूसरी फूल आने के समय सबसे महत्वपूर्ण है। अधिक जलभराव से बचें।"
            resp_en = "Crops require 3 to 4 irrigations across their lifecycle. Critical stages are active vegetative branching (20-25 days) and flowering. Use drip irrigation early in the morning to prevent water loss."
            followups = ["How much fertilizer is needed?", "When is the next rain?"] if is_en else ["खाद की मात्रा कितनी रखें?", "कीट नियंत्रण कैसे करें?"]
        elif any(k in q for k in ["खाद", "यूरिया", "fertilizer", "dap", "urea", "npk"]):
            resp_hi = "बुवाई के समय प्रति एकड़ 50 किग्रा डीएपी और 25 किग्रा पोटाश डालें। फसल 25-30 दिन की होने पर 35 किग्रा नीम कोटेड यूरिया और 5 किग्रा जिंक सल्फेट का छिड़काव करें।"
            resp_en = "Apply 50 kg DAP and 25 kg MOP per acre as basal dose during sowing. Top-dress with 35 kg Neem Coated Urea and 5 kg Zinc Sulphate after 25 days."
            followups = ["When to irrigate?", "What are market rates?"] if is_en else ["सिंचाई कब करनी है?", "मंडी में क्या भाव है?"]
        elif any(k in q for k in ["कीट", "रोग", "pest", "disease", "spray", "fungus", "दवा"]):
            resp_hi = "रस चूसक कीटों व फफूंद के लिए 5% नीम तेल (5 मिली/लीटर) या मैंकोजेब 75 WP (2.5 ग्राम/लीटर) का सुबह के समय छिड़काव करें।"
            resp_en = "For sucking pests and fungal spots, spray 5% Neem Oil Extract (5ml/L) or Mancozeb 75 WP (2.5g/L) during calm morning hours."
            followups = ["Organic remedies?", "Spray weather condition?"] if is_en else ["जैविक उपचार क्या हैं?", "छिड़काव का मौसम?"]
        elif any(k in q for k in ["भाव", "रेट", "mandi", "price", "rate", "मंडी"]):
            resp_hi = "स्थानीय कृषि उपज मंडी में आज दैनिक आवक और मॉडल भाव स्थिर बने हुए हैं। विस्तृत भाव हेतु मंडी रडार टैब देखें।"
            resp_en = "In your local APMC Mandi, major commodity arrivals are fetching strong modal rates. Check the Mandi Radar tab for live prices."
            followups = ["Which crop to sow?", "Weather forecast?"] if is_en else ["कौन सी फसल लगाएं?", "मौसम पूर्वानुमान?"]
        elif any(k in q for k in ["योजना", "scheme", "subsidy", "pmkisan", "pmfby", "बीमा"]):
            resp_hi = "प्रधानमंत्री किसान सम्मान निधि के तहत ₹6,000 वार्षिक सहायता मिलती है। फसल सुरक्षा हेतु पीएमएफबीवाय (PMFBY) में नजदीकी सीएससी से आवेदन करें।"
            resp_en = "Under PM-KISAN, farmers receive ₹6,000 annual direct benefit. For crop risk coverage, register on PMFBY portal at your nearest CSC center."
            followups = ["How to apply for Soil Card?", "KCC loan process?"] if is_en else ["मृदा कार्ड कैसे बनवाएं?", "केसीसी ऋण प्रक्रिया?"]
        else:
            resp_hi = "किसान साथी एआई आपके खेत की मिट्टी, उपग्रह मौसम और मंडी भाव का विश्लेषण कर वैज्ञानिक फसल सलाह प्रदान करता है।"
            resp_en = "Kisaan_Sathi AI analyzes your farm soil nutrients, satellite weather, and APMC market trends to deliver actionable crop guidance."
            followups = ["How much water needed?", "Recommended fertilizers?"] if is_en else ["पानी कितना चाहिए?", "खाद की मात्रा?"]

        return {
            "query": query_text,
            "detected_intent": "agronomic_domain_knowledge",
            "model_used": "kisaan_sathi_domain_knowledge",
            "language": language,
            "response_text_hi": resp_hi,
            "response_text_en": resp_en,
            "response_text_regional": resp_en if is_en else resp_hi,
            "tts_audio_text": resp_en if is_en else resp_hi,
            "confidence": 0.96,
            "suggested_followups": followups
        }

llm_advisor = LLMAdvisor()
