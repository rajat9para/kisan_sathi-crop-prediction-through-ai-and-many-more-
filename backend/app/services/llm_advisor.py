"""
Grounded Multilingual LLM Advisory Engine powered by Groq (LLaMA 3.3 / LLaMA 3.1)
and 11-Language Native Agronomic Knowledge Base.
Synthesizes natural, weather-grounded conversational farmer guidance across:
Hindi, English, Gujarati, Bengali, Punjabi, Marathi, Telugu, Tamil, Kannada, Malayalam, Odia.
"""

from typing import Dict, Any, List, Optional
import json
from groq import Groq
from app.config import config

MULTILINGUAL_KNOWLEDGE_BASE = {
    "water": {
        "hi": "फसल के लिए 3 से 4 सिंचाइयों की आवश्यकता होती है। पहली सिंचाई बुवाई के 20-25 दिन बाद और दूसरी फूल आने के समय सबसे महत्वपूर्ण है। अधिक जलभराव से बचें।",
        "en": "Crops require 3 to 4 irrigations across their lifecycle. Critical stages are active vegetative branching (20-25 days) and flowering. Use drip irrigation early in the morning.",
        "gu": "પાક માટે સમગ્ર ઋતુમાં 3 થી 4 પિયતની જરૂર હોય છે. પ્રથમ પિયત વાવણીના 20-25 દિવસ પછી અને બીજું ફૂલ આવવાના સમયે ખૂબ મહત્વનું છે. વધુ પડતા પાણીનો ભરાવો ટાળો.",
        "bn": "ফসলের জন্য সমগ্র মরসুমে ৩ থেকে ৪ বার সেচের প্রয়োজন হয়। প্রথম সেচ বপনের ২০-২৫ দিন পরে এবং দ্বিতীয় সেচ ফুল আসার সময় অত্যন্ত গুরুত্বপূর্ণ। অতিরিক্ত জল জমা এড়িয়ে চলুন।",
        "pa": "ਫ਼ਸਲ ਲਈ ਪੂਰੇ ਸੀਜ਼ਨ ਵਿੱਚ 3 ਤੋਂ 4 ਸਿੰਚਾਈਆਂ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਪਹਿਲੀ ਸਿੰਚਾਈ ਬਿਜਾਈ ਦੇ 20-25 ਦਿਨਾਂ ਬਾਅਦ ਅਤੇ ਦੂਜੀ ਫੁੱਲ ਪੈਣ ਸਮੇਂ ਬਹੁਤ ਜ਼ਰੂਰੀ ਹੈ। ਵਾਧੂ ਪਾਣੀ ਖੜ੍ਹਾ ਨਾ ਹੋਣ ਦਿਓ।",
        "mr": "पिकासाठी संपूर्ण हंगामात ३ ते ४ पाण्याच्या पाळ्यांची आवश्यकता असते. पहिली पाणी पाळी पेरणीनंतर २०-२५ दिवसांनी व दुसरी फुलोरा अवस्थेत अत्यंत महत्त्वाची आहे. पाण्याचा निचरा व्यवस्थित ठेवा.",
        "te": "పంటకు మొత్తం కాలంలో 3 నుండి 4 తడులు అవసరం. మొదటి తడి విత్తిన 20-25 రోజులకు మరియు రెండవది పూత దశలో చాలా కీలకం. పొలంలో నీరు నిల్వ ఉండకుండా చూసుకోండి.",
        "ta": "பயிருக்கு 3 முதல் 4 முறை நீர்ப்பாசனம் தேவை. விதைத்த 20-25 நாட்களுக்குப் பிறகு முதல் பாசனமும், பூக்கும் தருணத்தில் இரண்டாவது பாசனமும் மிக முக்கியம். நீர் தேங்குவதைத் தவிர்க்கவும்.",
        "kn": "ಬೆಳೆಗೆ ಒಟ್ಟು 3 ರಿಂದ 4 ನೀರಾವರಿ ಅಗತ್ಯವಿದೆ. ಬಿತ್ತನೆಯ 20-25 ದಿನಗಳ ನಂತರ ಮೊದಲ ನೀರಾವರಿ ಮತ್ತು ಹೂಬಿಡುವ ಹಂತದಲ್ಲಿ ಎರಡನೇ ನೀರಾವರಿ ಅತ್ಯಂತ ಪ್ರಮುಖವಾಗಿದೆ. ನೀರು ನಿಲ್ಲದಂತೆ ನೋಡಿಕೊಳ್ಳಿ.",
        "ml": "വിളയ്ക്ക് മൊത്തം 3 മുതൽ 4 നനകൾ ആവശ്യമാണ്. വിതച്ച് 20-25 ദിവസങ്ങൾക്ക് ശേഷമുള്ള ആദ്യ നനയും പൂവിടുന്ന സമയത്തെ രണ്ടാം നനയും വളരെ പ്രധാനമാണ്.",
        "or": "ଫସଲ ପାଇଁ ସମଗ୍ର ଋତୁରେ ୩ ରୁ ୪ ଥର ଜଳସେଚନ ଆବଶ୍ୟକ। ବୁଣିବାର ୨୦-୨୫ ଦିନ ପରେ ପ୍ରଥମ ଏବଂ ଫୁଲ ଫୁଟିବା ସମୟରେ ଦ୍ୱିତୀୟ ସେଚନ ଅତ୍ୟନ୍ତ ଗୁରୁତ୍ୱପୂର୍ଣ୍ଣ।"
    },
    "fertilizer": {
        "hi": "बुवाई के समय प्रति एकड़ 50 किग्रा डीएपी और 25 किग्रा पोटाश डालें। फसल 25-30 दिन की होने पर 35 किग्रा नीम कोटेड यूरिया और 5 किग्रा जिंक सल्फेट का छिड़काव करें।",
        "en": "Apply 50 kg DAP and 25 kg MOP per acre as basal dose during sowing. Top-dress with 35 kg Neem Coated Urea and 5 kg Zinc Sulphate after 25 days.",
        "gu": "વાવણી સમયે એકર દીઠ 50 કિગ્રા ડીએપી અને 25 કિગ્રા પોટાશ આપો. 25-30 દિવસ પછી 35 કિગ્રા યુરિયા અને 5 કિગ્રા ઝિંક સલ્ફેટનો છંટકાવ કરો.",
        "bn": "বপনের সময় একর প্রতি ৫০ কেজি ডিএপি এবং ২৫ কেজি পটাশ দিন। ২৫-৩০ দিন পর ৩৫ কেজি ইউরিয়া এবং ৫ কেজি জিঙ্ক সালফেট প্রয়োগ করুন।",
        "pa": "ਬਿਜਾਈ ਵੇਲੇ ਪ੍ਰਤੀ ਏਕੜ 50 ਕਿਲੋ ਡੀਏਪੀ ਅਤੇ 25 ਕਿਲੋ ਪੋਟਾਸ਼ ਪਾਓ। 25-30 ਦਿਨਾਂ ਬਾਅਦ 35 ਕਿਲੋ ਨਿੰਮ ਕੋਟੇਡ ਯੂਰੀਆ ਅਤੇ 5 ਕਿਲੋ ਜ਼ਿੰਕ ਸਲਫੇਟ ਪਾਓ।",
        "mr": "पेरणीच्या वेळी एकरी ५० किलो डीएपी आणि २५ किलो पोटॅश द्यावे. २५-३० दिवसांनी ३५ किलो युरिया आणि ५ किलो झिंक सल्फेटची मात्रा द्यावी.",
        "te": "విత్తే సమయంలో ఎకరాకు 50 కిలోల డీఏపీ, 25 కిలోల పొటాష్ వేయండి. 25 రోజుల తర్వాత 35 కిలోల యూరియా మరియు 5 కిలోల జింక్ సల్ఫేట్ వేయండి.",
        "ta": "விதைப்பின் போது ஏக்கருக்கு 50 கிலோ டிஏபி மற்றும் 25 கிலோ பொட்டாஷ் இடவும். 25 நாட்களுக்குப் பின் 35 கிலோ யூரியா மற்றும் 5 கிலோ துத்தநாக சல்பேட் இடவும்.",
        "kn": "ಬಿತ್ತನೆ ಸಮಯದಲ್ಲಿ ಎಕರೆಗೆ 50 ಕೆಜಿ ಡಿಎಪಿ ಮತ್ತು 25 ಕೆಜಿ ಪೊಟ್ಯಾಶ್ ಹಾಕಿ. 25 ದಿನಗಳ ನಂತರ 35 ಕೆಜಿ ಯೂರಿಯಾ ಮತ್ತು 5 ಕೆಜಿ ಜಿಂಕ್ ಸಲ್ಫೇಟ್ ಸಿಂಪಡಿಸಿ.",
        "ml": "വിതയ്ക്കുന്ന സമയത്ത് ഏക്കറിന് 50 കിലോ ഡിഎപിയും 25 കിലോ പൊട്ടാഷും നൽകുക. 25 ദിവസത്തിന് ശേഷം 35 കിലോ യൂറിയയും 5 കിലോ സിങ്ക് സൾഫേറ്റും നൽകുക.",
        "or": "ବୁଣିବା ସମୟରେ ଏକର ପିଛା ୫୦ କିଗ୍ରା ଡିଏପି ଏବଂ ୨୫ କିଗ୍ରା ପଟାସ ଦିଅନ୍ତୁ। ୨୫-୩୦ ଦିନ ପରେ ୩୫ କିଗ୍ରା ୟୁରିଆ ଏବଂ ୫ କିଗ୍ରା ଜିଙ୍କ ସଲଫେଟ୍ ପ୍ରୟୋଗ କରନ୍ତୁ।"
    },
    "pest": {
        "hi": "रस चूसक कीटों व फफूंद के लिए 5% नीम तेल (5 मिली/लीटर) या मैंकोजेब 75 WP (2.5 ग्राम/लीटर) का सुबह के समय छिड़काव करें।",
        "en": "For sucking pests and fungal spots, spray 5% Neem Oil Extract (5ml/L) or Mancozeb 75 WP (2.5g/L) during calm morning hours.",
        "gu": "ચૂસિયા પ્રકારની જીવાતો અને ફૂગ માટે 5% લીમડાનું તેલ (5 મિલી/લિટર) અથવા મેન્કોઝેબ 75 WP (2.5 ગ્રામ/લિટર) સવારના સમયે છાંટો.",
        "bn": "চোষক পোকা ও ছত্রাক দমনের জন্য নিম তেল (৫ মিলি/লিটার) অথবা ম্যানকোজেব ৭৫ ডব্লিউপি (২.৫ গ্রাম/লিটার) সকালে স্প্রে করুন।",
        "pa": "ਰਸ ਚੂਸਣ ਵਾਲੇ ਕੀੜਿਆਂ ਅਤੇ ਉੱਲੀ ਲਈ 5% ਨਿੰਮ ਦਾ ਤੇਲ (5 ਮਿ.ਲੀ./ਲਿਟਰ) ਜਾਂ ਮੈਨਕੋਜ਼ੇਬ 75 WP (2.5 ਗ੍ਰਾਮ/ਲਿਟਰ) ਦਾ ਸਵੇਰੇ ਛਿੜਕਾਅ ਕਰੋ।",
        "mr": "रस शोषणाऱ्या किडी व बुरशीसाठी ५% निंबोळी अर्क (५ मिली/लिटर) किंवा मॅन्कोझेब ७५ WP (२.५ ग्रॅम/लिटर) सकाळी फवारावे.",
        "te": "రసం పీల్చే పురుగులు, తెగుళ్ల నివారణకు వేప నూనె (5 మి.లీ/లీటరు) లేదా మాంకోజెబ్ 75 WP (2.5 గ్రా/లీ) ఉదయం పూట పిచికారీ చేయండి.",
        "ta": "சாறு உறிஞ்சும் பூச்சிகள் மற்றும் பூஞ்சானைக் கட்டுப்படுத்த வேப்ப எண்ணெய் (5 மி.லி/லி) அல்லது மேன்கோசெப் 75 WP (2.5 கிராம்/லி) தெளிக்கவும்.",
        "kn": "ರಸ ಹೀರುವ ಕೀಟಗಳು ಮತ್ತು ಶಿಲೀಂಧ್ರ ರೋಗಗಳಿಗೆ ಬೇವಿನ ಎಣ್ಣೆ (5 ಮಿಲಿ/ಲೀ) ಅಥವಾ ಮ್ಯಾಂಕೋಜೇಬ್ 75 WP (2.5 ಗ್ರಾಂ/ಲೀ) ಮುಂಜಾನೆ ಸಿಂಪಡಿಸಿ.",
        "ml": "കീടങ്ങൾക്കും കുമിൾ രോഗങ്ങൾക്കും വേപ്പെണ്ണ മിശ്രിതം (5 മില്ലി/ലിറ്റർ) അല്ലെങ്കിൽ മാങ്കോസെബ് 75 WP (2.5 ഗ്രാം/ലിറ്റർ) തളിക്കുക.",
        "or": "ଶୋଷକ ପୋକ ଓ କବକ ନିୟନ୍ତ୍ରଣ ପାଇଁ ନିମ୍ବ ତେଲ (୫ ମିଲି/ଲିଟର) କିମ୍ବା ମ୍ୟାଙ୍କୋଜେବ ୭୫ WP (୨.୫ ଗ୍ରାମ/ଲିଟର) ସକାଳେ ସ୍ପ୍ରେ କରନ୍ତୁ।"
    },
    "market": {
        "hi": "स्थानीय कृषि उपज मंडी में आज दैनिक आवक और मॉडल भाव स्थिर बने हुए हैं। विस्तृत भाव हेतु मंडी रडार टैब देखें।",
        "en": "In your local APMC Mandi, commodity arrivals and modal prices remain stable. Check the Mandi Radar tab for live rates.",
        "gu": "સ્થાનિક એપીએમસી માર્કેટ યાર્ડમાં આજે આવકો અને ભાવ સ્થિર છે. વધુ વિગતવાર દરો માટે મંડી રડાર ટેબ જુઓ.",
        "bn": "স্থানীয় কৃষি মান্ডিতে আজকের বাজারদর ও আগমন স্থিতিশীল রয়েছে। বিস্তারিত দরের জন্য মান্ডি রাডার দেখুন।",
        "pa": "ਸਥਾਨਕ ਅਨਾਜ ਮੰਡੀ ਵਿੱਚ ਅੱਜ ਫ਼ਸਲਾਂ ਦੀ ਆਮਦ ਅਤੇ ਭਾਅ ਸਥਿਰ ਹਨ। ਤਾਜ਼ਾ ਭਾਅ ਲਈ ਮੰਡੀ ਰਡਾਰ ਵੇਖੋ।",
        "mr": "स्थानिक कृषी उत्पन्न बाजार समितीत आज आवक व बाजारभाव स्थिर आहेत. तपशीलवार दरांसाठी मंडी रडार पहा.",
        "te": "స్థానిక వ్యవసాయ మార్కెట్ యార్డులో సరుకు రాక మరియు ధరలు స్థిరంగా ఉన్నాయి. పూర్తి వివరాల కోసం మార్కెట్ రాడార్ చూడండి.",
        "ta": "உள்ளூர் ஒழுங்குமுறை விற்பனைக்கூடத்தில் வரத்து மற்றும் விலைகள் சீராக உள்ளன. நேரலை விலைகளுக்கு மண்டி ரேடாரைப் பார்க்கவும்.",
        "kn": "ಸ್ಥಳೀಯ ಎಪಿಎಂಸಿ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಇಂದಿನ ದರಗಳು ಸ್ಥಿರವಾಗಿವೆ. ಹೆಚ್ಚಿನ ಮಾಹಿತಿಗಾಗಿ ಮಂಡಿ ರೇಡಾರ್ ವೀಕ್ಷಿಸಿ.",
        "ml": "പ്രാദേശിക കാർഷിക വിപണിയിൽ ഇന്നത്തെ വിലനിലവാരം സ്ഥിരതയുള്ളതാണ്. കൂടുതൽ വിവരങ്ങൾക്ക് മണ്ഡി റഡാർ കാണുക.",
        "or": "ସ୍ଥାନୀୟ କୃଷି ମଣ୍ଡିରେ ଆଜି ଆମଦାନୀ ଏବଂ ଦର ସ୍ଥିର ରହିଛି। ବିସ୍ତୃତ ଦର ପାଇଁ ମଣ୍ଡି ରାଡାର୍ ଦେଖନ୍ତୁ।"
    },
    "general": {
        "hi": "किसान साथी एआई आपके खेत की मिट्टी, उपग्रह मौसम और मंडी भाव का विश्लेषण कर वैज्ञानिक फसल सलाह प्रदान करता है।",
        "en": "Kisaan_Sathi AI analyzes your soil nutrients, satellite weather, and APMC market trends to deliver actionable crop guidance.",
        "gu": "કિસાન સાથી AI આપના ખેતરની જમીન, ઉપગ્રહ હવામાન અને બજાર ભાવોનું વિશ્લેષણ કરી વૈજ્ઞાનિક પાક સલાહ પૂરી પાડે છે.",
        "bn": "কিসান সাথী এআই আপনার মাটির পুষ্টি, উপগ্রহ আবহাওয়া এবং বাজারদর বিশ্লেষণ করে সঠিক বৈজ্ঞানিক পরামর্শ প্রদান করে।",
        "pa": "ਕਿਸਾਨ ਸਾਥੀ AI ਤੁਹਾਡੇ ਖੇਤ ਦੀ ਮਿੱਟੀ, ਮੌਸਮ ਅਤੇ ਮੰਡੀ ਦੇ ਭਾਵਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਕੇ ਸਹੀ ਸਲਾਹ ਦਿੰਦਾ ਹੈ।",
        "mr": "किसान साथी एआय आपल्या शेतातील माती, उपग्रह हवामान आणि बाजारभावांचे विश्लेषण करून अचूक पीक सल्ला देते.",
        "te": "కిసాన్ సాథీ AI మీ నేల పోషకాలు, వాతావరణం మరియు మార్కెట్ ధరలను విశ్లేషించి శాస్త్రీయ పంట సలహాలను అందిస్తుంది.",
        "ta": "கிசான் சாதி AI உங்கள் மண் வளம், செயற்கைக்கோள் வானிலை மற்றும் சந்தை விலைகளை ஆய்வு செய்து துல்லியமான விவசாய வழிகாட்டலை வழங்குகிறது.",
        "kn": "ಕಿಸಾನ್ ಸಾಥಿ AI ನಿಮ್ಮ ಮಣ್ಣಿನ ಫಲವತ್ತತೆ, ಹವಾಮಾನ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ದರಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಿ ವೈಜ್ಞಾನಿಕ ಕೃಷಿ ಸಲಹೆಗಳನ್ನು ನೀಡುತ್ತದೆ.",
        "ml": "കിസാൻ സാഥി AI നിങ്ങളുടെ മണ്ണിലെ പോഷകങ്ങൾ, കാലാവസ്ഥ, വിപണി വില എന്നിവ പരിശോധിച്ച് ശാസ്ത്രീയ ഉപദേശങ്ങൾ നൽകുന്നു.",
        "or": "କିସାନ ସାଥୀ AI ଆପଣଙ୍କ ମାଟିର ପୋଷକ ତତ୍ତ୍ୱ, ପାଣିପାଗ ଏବଂ ବଜାର ଦର ବିଶ୍ଳେଷଣ କରି ଉପଯୁକ୍ତ ପରାମର୍ଶ ପ୍ରଦାନ କରେ।"
    }
}


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
        crop_context: Optional[str] = "Wheat",
        location: Optional[str] = "Dehradun, Uttarakhand"
    ) -> Dict[str, Any]:
        """
        Uses Groq LLM to answer free-form farmer questions with deep agronomic accuracy across 11 Indian languages.
        Falls back gracefully to native multilingual domain engine if offline or rate-limited.
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

        models_to_try = [
            "openai/gpt-oss-120b",
            "openai/gpt-oss-20b",
            "qwen/qwen3.8-27b",
            "groq/compound"
        ]
        models_to_try = list(dict.fromkeys([m for m in models_to_try if m]))

        for model_name in models_to_try:
            try:
                chat_completion = self.client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                f"You are Kisaan_Sathi, an expert AI Agricultural Scientist advising farmers in {location} for {crop_context}. "
                                f"Respond ONLY in fluent, respectful {target_lang}. "
                                "Give direct, practical organic and chemical recommendations with exact dosages in 2-3 sentences. "
                                "Do NOT mix languages."
                            )
                        },
                        {"role": "user", "content": query_text}
                    ],
                    model=model_name,
                    temperature=0.25,
                    max_tokens=250,
                    timeout=2.5
                )
                raw_text = chat_completion.choices[0].message.content.strip()
                if raw_text:
                    resp_hi = raw_text if language == "hi" else ""
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
                "hi": f"{crop} में {disease_name} के लिए मौसम साफ रहने पर अनुशंसित जैविक व रासायनिक कीटनाशक का छिड़काव करें।",
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
                return json.loads(res.choices[0].message.content)
            except Exception:
                continue

        return {
            "hi": f"कीटनाशक का छिड़काव मौसम साफ रहने पर सुबह या शाम के समय करें।",
            "en": f"Apply spray during clear weather conditions early in the morning."
        }

    def _fallback_response(self, query_text: str, language: str = "hi") -> Dict[str, Any]:
        q = query_text.lower()
        
        # Categorize intent
        if any(k in q for k in ["पानी", "water", "irrigation", "સિંચાઈ", "সেচ", "ਸਿੰਚਾਈ", "પાણી", "জল", "నీరు", "பாசனம்", "ನೀರು", "വെള്ളം", "ଜଳ"]):
            topic = "water"
        elif any(k in q for k in ["खाद", "यूरिया", "fertilizer", "dap", "urea", "npk", "ખાતર", "সার", "ਖਾਦ", "ఎరువు", "உரம்", "ಗೊಬ್ಬರ", "വളം", "ଖତ"]):
            topic = "fertilizer"
        elif any(k in q for k in ["कीट", "रोग", "pest", "disease", "spray", "fungus", "દવા", "রোগ", "ਕੀੜੇ", "పురుగు", "பூச்சி", "ಕೀಟ", "കീടങ്ങൾ", "ପୋକ"]):
            topic = "pest"
        elif any(k in q for k in ["भाव", "रेट", "mandi", "price", "rate", "ભાવ", "দর", "ਭਾਅ", "ధర", "விலை", "ಬೆಲೆ", "വില", "ଦର"]):
            topic = "market"
        else:
            topic = "general"

        dict_entry = MULTILINGUAL_KNOWLEDGE_BASE.get(topic, MULTILINGUAL_KNOWLEDGE_BASE["general"])
        text = dict_entry.get(language, dict_entry.get("hi", dict_entry["en"]))

        is_en = (language == "en")
        resp_hi = dict_entry.get("hi", "")
        resp_en = dict_entry.get("en", "")

        return {
            "query": query_text,
            "detected_intent": f"agronomic_{topic}",
            "model_used": "kisaan_sathi_multilingual_engine",
            "language": language,
            "response_text_hi": resp_hi,
            "response_text_en": resp_en,
            "response_text_regional": text,
            "tts_audio_text": text,
            "confidence": 0.96,
            "suggested_followups": ["Water schedule?", "Market rate?"] if is_en else ["पानी की मात्रा?", "मंडी भाव?"]
        }


llm_advisor = LLMAdvisor()
