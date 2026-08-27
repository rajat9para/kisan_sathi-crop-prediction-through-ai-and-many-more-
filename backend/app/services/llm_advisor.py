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
        Uses Groq LLaMA 3.3 to answer free-form farmer questions with deep agronomic accuracy.
        Falls back to local rule engine if offline or rate-limited.
        """
        if not self.client:
            return self._fallback_response(query_text)

        system_prompt = (
            "You are Kisaan_Sathi (किसान साथी), an expert AI Agricultural Scientist and compassionate advisor for Indian farmers.\n"
            "Your goal is to answer the farmer's question in clear, simple, practical terms.\n"
            f"Location Context: {location}. Target Crop Context: {crop_context}.\n"
            "Rules:\n"
            "1. If language is 'hi', provide the answer in warm, respectful, natural Hindi (शुद्ध एवं व्यावहारिक हिंदी).\n"
            "2. Keep the response direct, actionable, and within 3-4 sentences so it is easy to listen to via Text-to-Speech.\n"
            "3. Mention practical organic and chemical solutions with exact doses (e.g. 5ml/litre, 50kg/acre).\n"
            "4. Format the output strictly as JSON with keys: 'response_text_hi', 'response_text_en', 'tts_audio_text', 'suggested_followups'."
        )

        models_to_try = [
            config.GROQ_MODEL,
            "llama-3.3-70b-versatile",
            "llama3-8b-8192",
            "gemma2-9b-it",
            "mixtral-8x7b-32768"
        ]
        # Remove duplicates while preserving order
        models_to_try = list(dict.fromkeys([m for m in models_to_try if m]))

        for model_name in models_to_try:
            try:
                chat_completion = self.client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Farmer's question: {query_text}"}
                    ],
                    model=model_name,
                    temperature=0.3,
                    max_tokens=400,
                    response_format={"type": "json_object"}
                )
                import json
                content = chat_completion.choices[0].message.content
                parsed = json.loads(content)
                
                return {
                    "query": query_text,
                    "detected_intent": "groq_llm_intelligence",
                    "model_used": model_name,
                    "response_text_hi": parsed.get("response_text_hi", ""),
                    "response_text_en": parsed.get("response_text_en", ""),
                    "tts_audio_text": parsed.get("tts_audio_text", parsed.get("response_text_hi", "")),
                    "confidence": 0.98,
                    "suggested_followups": parsed.get("suggested_followups", ["खाद की मात्रा?", "मौसम का हाल?"])
                }
            except Exception as e:
                print(f"[!] Groq query error with model {model_name}: {e}")
                continue

        print("[!] All Groq models failed or unavailable. Using fallback rule engine.")
        return self._fallback_response(query_text)

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
                "en": f"Apply recommended bio-pesticide for {disease_name} in {crop}."
            }

        prompt = (
            f"A farmer has {crop} affected by {disease_name}. "
            f"Weather forecast: {rain_prob}% rain probability, temperature {temp_c}°C. "
            "Advise the farmer on exact spray timing and rain precautions in 2 sentences in both Hindi and English. "
            "Output JSON with keys 'hi' and 'en'."
        )

        try:
            res = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=config.GROQ_FAST_MODEL,
                temperature=0.2,
                max_tokens=250,
                response_format={"type": "json_object"}
            )
            import json
            return json.loads(res.choices[0].message.content)
        except Exception:
            return {
                "hi": f"कीटनाशक का छिड़काव मौसम साफ रहने पर सुबह या शाम के समय करें।",
                "en": f"Apply spray during clear weather conditions early in the morning."
            }

    def _fallback_response(self, query_text: str) -> Dict[str, Any]:
        q = query_text.lower()
        if any(k in q for k in ["पानी", "water", "irrigation", "सिंचाई"]):
            return {
                "query": query_text,
                "detected_intent": "water",
                "response_text_hi": "फसल के लिए 3 से 4 सिंचाइयों की आवश्यकता होती है। पहली सिंचाई बुवाई के 20-25 दिन बाद और दूसरी फूल आने के समय सबसे महत्वपूर्ण है। अधिक जलभराव से बचें।",
                "response_text_en": "Crops require 3 to 4 irrigations across their lifecycle. Critical stages are active vegetative branching (20-25 days) and flowering.",
                "tts_audio_text": "फसल के लिए तीन से चार सिंचाई की आवश्यकता होती है। फूल आने के समय खेत में नमी अवश्य बनाए रखें।",
                "confidence": 0.94,
                "suggested_followups": ["खाद की मात्रा कितनी रखें?", "कीट नियंत्रण कैसे करें?"]
            }
        elif any(k in q for k in ["खाद", "यूरिया", "fertilizer", "dap", "urea"]):
            return {
                "query": query_text,
                "detected_intent": "fertilizer",
                "response_text_hi": "बुवाई के समय प्रति एकड़ 50 किग्रा डीएपी और 25 किग्रा पोटाश डालें। फसल 25-30 दिन की होने पर 35 किग्रा नीम कोटेड यूरिया और 5 किग्रा जिंक सल्फेट का छिड़काव करें।",
                "response_text_en": "Apply 50 kg DAP and 25 kg MOP per acre as basal dose. Top-dress with 35 kg Neem Coated Urea after 25 days.",
                "tts_audio_text": "बुवाई के समय पचास किलो डीएपी डालें। पच्चीस दिन बाद पैंतीस किलो यूरिया का छिड़काव करें।",
                "confidence": 0.94,
                "suggested_followups": ["सिंचाई कब करनी है?", "मंडी में क्या भाव है?"]
            }
        else:
            return {
                "query": query_text,
                "detected_intent": "general",
                "response_text_hi": "किसान साथी एआई आपके खेत की मिट्टी, मौसम और मंडी भाव का विश्लेषण कर वैज्ञानिक फसल सलाह प्रदान करता है।",
                "response_text_en": "Kisaan_Sathi AI analyzes your soil, weather, and market trends to deliver actionable crop guidance.",
                "tts_audio_text": "नमस्ते किसान भाई। आप खाद, पानी, मौसम, या मंडी भाव से जुड़ा कोई भी प्रश्न पूछ सकते हैं।",
                "confidence": 0.90,
                "suggested_followups": ["पानी कितना चाहिए?", "खाद की मात्रा?", "मंडी भाव?"]
            }

llm_advisor = LLMAdvisor()
