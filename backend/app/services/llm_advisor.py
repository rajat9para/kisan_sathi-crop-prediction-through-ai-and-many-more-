"""
Grounded Multilingual LLM Advisory Engine powered by Groq (LLaMA 3.3 / LLaMA 3.1)
and 11-Language Native Agronomic Knowledge Base.
Synthesizes natural, weather-grounded conversational farmer guidance across:
Hindi, English, Gujarati, Bengali, Punjabi, Marathi, Telugu, Tamil, Kannada, Malayalam, Odia, and Hinglish.
"""

from typing import Dict, Any, List, Optional
import json
import re
from groq import Groq
from app.config import config

MULTILINGUAL_KNOWLEDGE_BASE = {
    "sugarcane_water": {
        "hi": "गन्ने में बुवाई के बाद पहली सिंचाई 10-15 दिन के अंतराल पर अंकुरण हेतु करें। इसके बाद कल्ले निकलते समय (Tillering) 8-10 दिन के अंतर पर पानी दें। तेज धूप में सुबह या शाम ही सिंचाई करें और जलभराव न होने दें।",
        "en": "For sugarcane, apply the first irrigation 10-15 days after planting for germination. During the tillering phase, irrigate every 8-10 days. Avoid waterlogging and irrigate early morning or evening.",
        "gu": "શેરડીમાં વાવણી પછી પ્રથમ પિયત 10-15 દિવસ પછી અંકુરણ માટે આપો. ફૂટ અવસ્થા દરમિયાન દર 8-10 દિવસે પાણી આપો. ખેતરમાં પાણી ભરાવા ન દો.",
        "bn": "আখ চাষে রোপণের ১০-১৫ দিন পর প্রথম সেচ দিন। কুশি গজানোর সময় ৮-১০ দিনের ব্যবধানে সেচ প্রদান করুন। জমিতে অতিরিক্ত জল জমতে দেবেন না।",
        "pa": "ਕਮਾਦ (ਗੰਨੇ) ਵਿੱਚ ਬਿਜਾਈ ਤੋਂ 10-15 ਦਿਨ ਬਾਅਦ ਪਹਿਲੀ ਸਿੰਚਾਈ ਕਰੋ। ਫੁਟਾਰੇ ਵੇਲੇ 8-10 ਦਿਨਾਂ ਦੇ ਵਕਫੇ 'ਤੇ ਪਾਣੀ ਦਿਓ ਅਤੇ ਪਾਣੀ ਖੜ੍ਹਾ ਨਾ ਹੋਣ ਦਿਓ।",
        "mr": "उसात लागवडीनंतर पहिले पाणी १०-१५ दिवसांनी उगवणीसाठी द्यावे. फुटवे फुटण्याच्या अवस्थेत ८-१० दिवसांच्या अंतराने पाणी द्यावे. पाणी साचू देऊ नका.",
        "te": "చెరకులో నాటిన 10-15 రోజులకు మొదటి తడి ఇవ్వండి. పిలకలు వచ్చే దశలో ప్రతి 8-10 రోజులకు నీటిపారుదల చేయండి.",
        "ta": "கரும்பில் நடவு செய்த 10-15 நாட்களுக்குப் பிறகு முதல் பாசனம் செய்யவும். தூstocks வரும் பருவத்தில் 8-10 நாட்களுக்கு ஒருமுறை பாசனம் செய்யவும்.",
        "kn": "ಕಬ್ಬಿನಲ್ಲಿ ಬಿತ್ತನೆಯ 10-15 ದಿನಗಳ ನಂತರ ಮೊದಲ ನೀರಾವರಿ ನೀಡಿ. ಮೊಳಕೆ ಒಡೆಯುವ ಹಂತದಲ್ಲಿ ಪ್ರತಿ 8-10 ದಿನಗಳಿಗೊಮ್ಮೆ ನೀರುಣಿಸಿ.",
        "ml": "കരിമ്പിൽ നടീലിനു ശേഷം 10-15 ദിവസത്തിനകം ആദ്യ നന നൽകുക. ചിനപ്പുകൾ പൊട്ടുമ്പോൾ 8-10 ദിവസത്തിൽ നനയ്ക്കുക.",
        "or": "ଆଖୁରେ ରୋପଣର ୧୦-୧୫ ଦିନ ପରେ ପ୍ରଥମ ଜଳସେଚନ କରନ୍ତୁ। କାଣ୍ଡ ବାହାରିବା ସମୟରେ ୮-୧୦ ଦିନ ବ୍ୟବଧାନରେ ପାଣି ଦିଅନ୍ତୁ।"
    },
    "sugarcane_fertilizer": {
        "hi": "गन्ने में बुवाई के समय प्रति एकड़ 60 किग्रा डीएपी और 40 किग्रा पोटाश डालें। 30, 60 और 90 दिन की अवस्था पर 40-40 किग्रा नीम कोटेड यूरिया तीन बार में दें।",
        "en": "For sugarcane, apply 60 kg DAP and 40 kg MOP per acre at planting. Top-dress with 40 kg Urea at 30, 60, and 90 days after sowing.",
        "gu": "શેરડીમાં વાવણી વખતે એકર દીઠ 60 કિગ્રા ડીએપી અને 40 કિગ્રા પોટાશ આપો. 30, 60 અને 90 દિવસે 40-40 કિગ્રા યુરિયા આપો.",
        "bn": "আখ চাষে বপনের সময় ৬০ কেজি ডিএপি ও ৪০ কেজি পটাশ দিন। ৩০, ৬০ ও ৯০ দিনে ৪০ কেজি করে ইউরিয়া প্রয়োগ করুন।",
        "pa": "ਕਮਾਦ ਵਿੱਚ ਬਿਜਾਈ ਵੇਲੇ 60 ਕਿਲੋ ਡੀਏਪੀ ਅਤੇ 40 ਕਿਲੋ ਪੋਟਾਸ਼ ਪਾਓ। 30, 60 ਅਤੇ 90 ਦਿਨਾਂ 'ਤੇ 40-40 ਕਿਲੋ ਯੂਰੀਆ ਪਾਓ।",
        "mr": "उसात लागवडीच्या वेळी एकरी ६० किलो डीएपी आणि ४० किलो पोटॅश द्यावे. ३०, ६० आणि ९० दिवसांनी ४० किलो युरिया द्यावा.",
        "te": "చెరకులో నాటేటప్పుడు ఎకరాకు 60 కిలోల డీఏపీ, 40 కిలోల పొటాష్ వేయండి. 30, 60, 90 రోజులకు యూరియా వేయండి.",
        "ta": "கரும்பில் நடவின் போது 60 கிலோ டிஏபி மற்றும் 40 கிலோ பொட்டாஷ் இடவும். 30, 60 மற்றும் 90 நாட்களில் யூரியா இடவும்.",
        "kn": "ಕಬ್ಬಿನಲ್ಲಿ ಬಿತ್ತನೆಯ ಸಮಯದಲ್ಲಿ 60 ಕೆಜಿ ಡಿಎಪಿ ಮತ್ತು 40 ಕೆಜಿ ಪೊಟ್ಯಾಶ್ ಹಾಕಿ. 30, 60 ಮತ್ತು 90 ದಿನಗಳಲ್ಲಿ ಯೂರಿಯಾ ಹಾಕಿ.",
        "ml": "കരിമ്പിൽ അടിവളമായി 60 കിലോ ഡിഎപിയും 40 കിലോ പൊട്ടാഷും നൽകുക. 30, 60, 90 ദിവസങ്ങളിൽ യൂറിയ നൽകുക.",
        "or": "ଆଖୁରେ ବୁଣିବା ସମୟରେ ୬୦ କିଗ୍ରା ଡିଏପି ଏବଂ ୪୦ କିଗ୍ରା ପଟାସ ଦିଅନ୍ତୁ। ୩୦, ୬୦ ଏବଂ ୯୦ ଦିନରେ ୟୁରିଆ ପ୍ରୟୋଗ କରନ୍ତୁ।"
    },
    "wheat_water": {
        "hi": "गेहूं में पहली सिंचाई (CRI - क्राउन रूट इनीशिएशन) बुवाई के 20-25 दिन बाद अनिवार्य रूप से करें। इसके बाद कल्ले फूटते समय (40-45 दिन), गांठ बनते समय (60-65 दिन) और दाना भरते समय सिंचाई करें।",
        "en": "In wheat, the first irrigation at the CRI (Crown Root Initiation) stage (20-25 days after sowing) is most critical. Subsequent irrigations at tillering (40-45 days), jointing (60-65 days), and grain filling are recommended.",
        "gu": "ઘઉંમાં પ્રથમ પિયત (CRI સ્ટેજ) વાવણીના 20-25 દિવસ પછી ખૂબ જ મહત્વનું છે. ત્યારપછી ફૂટ અને દાણા ભરાવાના સમયે પિયત આપો.",
        "bn": "গমে প্রথম সেচ (সিআরআই পর্যায়) বপনের ২০-২৫ দিন পরে দেওয়া বাধ্যতামূলক। এরপর কুশি গজানো ও দানার পুষ্টিকালে সেচ দিন।",
        "pa": "ਕਣਕ ਵਿੱਚ ਪਹਿਲਾ ਪਾਣੀ (CRI ਸਟੇਜ) ਬਿਜਾਈ ਤੋਂ 20-25 ਦਿਨਾਂ ਬਾਅਦ ਜ਼ਰੂਰ ਲਾਓ। ਇਸ ਤੋਂ ਬਾਅਦ ਗੰਢਾਂ ਬਣਨ ਅਤੇ ਦੁੱਧਾ ਪੈਣ ਸਮੇਂ ਸਿੰਚਾਈ ਕਰੋ।",
        "mr": "गव्हामध्ये पहिले पाणी (CRI अवस्था) पेरणीनंतर २०-२५ दिवसांनी देणे अत्यंत आवश्यक आहे. त्यानंतर फुटवे व दाणे भरण्याच्या वेळी पाणी द्यावे.",
        "te": "గోధుమలో మొదటి తడి (CRI దశ) విత్తిన 20-25 రోజులకు తప్పనిసరిగా ఇవ్వాలి. తర్వాత గింజ పాలుపోసుకునే దశలో నీరు అందించండి.",
        "ta": "கோதுமையில் முதல் பாசனம் (CRI நிலை) விதைத்த 20-25 நாட்களுக்குப் பிறகு மிகவும் முக்கியம்.",
        "kn": "ಗೋಧಿಯಲ್ಲಿ ಮೊದಲ ನೀರಾವರಿ (CRI ಹಂತ) ಬಿತ್ತನೆಯ 20-25 ದಿನಗಳ ನಂತರ ನೀಡುವುದು ಅತ್ಯಗತ್ಯ.",
        "ml": "ഗോതമ്പിൽ ആദ്യ നന (CRI സ്റ്റേജ്) വിതച്ച് 20-25 ദിവസങ്ങൾക്ക് ശേഷം നൽകേണ്ടതാണ്.",
        "or": "ଗହମରେ ପ୍ରଥମ ସେଚନ (CRI ପର୍ଯ୍ୟାୟ) ବୁଣିବାର ୨୦-୨୫ ଦିନ ପରେ ଅତ୍ୟନ୍ତ ଆବଶ୍ୟକ।"
    },
    "paddy_water_fertilizer": {
        "hi": "धान की रोपाई के बाद शुरुआती 15 दिन खेत में 2-3 सेमी पानी रखें। कल्ले फूटते समय (20-25 दिन) 35 किग्रा यूरिया और 15 किग्रा पोटाश की टॉप-ड्रेसिंग करें। दाना पकने से 10 दिन पूर्व पानी निकाल दें।",
        "en": "For paddy, maintain 2-3 cm standing water during the first 15 days after transplanting. Top-dress with 35 kg Urea and 15 kg Potash at tillering. Drain water 10 days before harvest.",
        "gu": "ડાંગરમાં ફેરરોપણી પછી શરૂઆતના 15 દિવસ ખેતરમાં 2-3 સેમી પાણી રાખો. ફૂટ અવસ્થાએ યુરિયા અને પોટાશ આપો.",
        "bn": "ধানে চারা রোপণের পর প্রথম ১৫ দিন ২-৩ সেমি জল ধরে রাখুন। কুশি আসার সময় ইউরিয়া ও পটাশ প্রয়োগ করুন।",
        "pa": "ਝੋਨੇ ਵਿੱਚ ਲੁਆਈ ਤੋਂ ਬਾਅਦ ਪਹਿਲੇ 15 ਦਿਨ 2-3 ਸੈ.ਮੀ. ਪਾਣੀ ਖੜ੍ਹਾ ਰੱਖੋ। ਫੁਟਾਰੇ ਵੇਲੇ ਯੂਰੀਆ ਅਤੇ ਪੋਟਾਸ਼ ਪਾਓ।",
        "mr": "भातामध्ये पुनर्लागवडीनंतर पहिले १५ दिवस २-३ सेमी पाणी ठेवावे. फुटवे फुटताना युरिया व पोटॅश द्यावे.",
        "te": "వరిలో నాటిన మొదటి 15 రోజులు 2-3 సెం.మీ నీరు ఉంచండి. పిలకల దశలో యూరియా, పొటాష్ వేయండి.",
        "ta": "நெல்லில் நடவு செய்த முதல் 15 நாட்களுக்கு 2-3 செ.மீ தண்ணீர் தேக்கி வைக்கவும்.",
        "kn": "ಭತ್ತದಲ್ಲಿ ನಾಟಿ ಮಾಡಿದ ಮೊದಲ 15 ದಿನಗಳು 2-3 ಸೆಂ.ಮೀ ನೀರನ್ನು ನಿಲ್ಲಿಸಿ.",
        "ml": "നെല്ലിൽ നടീലിനു ശേഷമുള്ള ആദ്യ 15 ദിവസം 2-3 സെ.മീ വെള്ളം നിർത്തുക.",
        "or": "ଧାନରେ ରୁଆ ପରେ ପ୍ରଥମ ୧୫ ଦିନ ୨-୩ ସେମି ପାଣି ରଖନ୍ତୁ।"
    },
    "cotton_pest": {
        "hi": "कपास में गुलाबी सुंडी (Pink Bollworm) और रस चूसक कीटों के नियंत्रण के लिए फेरोमोन ट्रैप (5 प्रति एकड़) लगाएं और 5% नीम तेल (NSKE) या प्रोफेनोफॉस 50 EC (2 मिली/लीटर) का छिड़काव करें।",
        "en": "For cotton pink bollworm and sucking pests, install 5 pheromone traps per acre. Spray 5% Neem Seed Kernel Extract (NSKE) or Profenofos 50 EC (2 ml/L).",
        "gu": "કપાસમાં ગુલાબી ઈયળ અને ચૂસિયા જીવાતો માટે ફેરોમોન ટ્રેપ લગાવો અને લીમડાનું તેલ અથવા પ્રોફેનોફોસ 50 EC છાંટો.",
        "bn": "তুলায় গোলাপী পোকা ও চোষক পোকার জন্য ফেরোমোন ফাঁদ লাগান এবং নিম তেল স্প্রে করুন।",
        "pa": "ਨਰਮੇ/ਕਪਾਹ ਵਿੱਚ ਗੁਲਾਬੀ ਸੁੰਡੀ ਲਈ ਫੇਰੋਮੋਨ ਟਰੈਪ ਲਾਓ ਅਤੇ ਨਿੰਮ ਦੇ ਤੇਲ ਜਾਂ ਪ੍ਰੋਫੇਨੋਫਾਸ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।",
        "mr": "कापसात बोंडअळी व रस शोषणाऱ्या किडींसाठी कामगंध सापळे लावा आणि ५% निंबोळी अर्क किंवा प्रोफेनोफॉस फवारा.",
        "te": "పత్తిలో గులాబీ రంగు పురుగు నివారణకు లింగాకర్షక బుట్టలు అమర్చండి మరియు వేప నూనె పిచికారీ చేయండి.",
        "ta": "பருத்தியில் இளஞ்சிவப்பு காய் புழுவிற்கு இனக்கவர்ச்சி பொறிகளை வைக்கவும் மற்றும் வேப்ப எண்ணெய் தெளிக்கவும்.",
        "kn": "ಹತ್ತಿಯಲ್ಲಿ ಗುಲಾಬಿ ಕಾಯಿಕೊರಕ ಹುಳುಗಳಿಗೆ ಫೆರೋಮೋನ್ ಬಲೆಗಳನ್ನು ಇರಿಸಿ ಮತ್ತು ಬೇವಿನ ಎಣ್ಣೆ ಸಿಂಪಡಿಸಿ.",
        "ml": "പരുത്തിയിലെ പിങ്ക് കായതുരപ്പൻ പുഴുവിനെതിരെ ഫെറമോൺ കെണികൾ വെയ്ക്കുക, വേപ്പെണ്ണ തളിക്കുക.",
        "or": "କପାରେ ଗୋଲାପୀ ପୋକ ପାଇଁ ଫେରୋମୋନ୍ ଟ୍ରାପ୍ ଲଗାନ୍ତୁ ଏବଂ ନିମ୍ବ ତେଲ ସ୍ପ୍ରେ କରନ୍ତୁ।"
    },
    "blight_disease": {
        "hi": "टमाटर और आलू में अगेती/पछेती झुलसा (Early/Late Blight) रोकने के लिए मैंकोजेब 75 WP (2.5 ग्राम/लीटर) या कॉपर ऑक्सीक्लोराइड का 10-12 दिन के अंतराल पर छिड़काव करें।",
        "en": "To control Early and Late Blight in tomato and potato, spray Mancozeb 75 WP (2.5g/L) or Copper Oxychloride at 10-12 day intervals during clear weather.",
        "gu": "ટામેટાં અને બટાકામાં સુકારો (બ્લાઈટ) રોગ અટકાવવા માટે મેન્કોઝેબ 75 WP (2.5 ગ્રામ/લિટર) અથવા કોપર ઓક્સીક્લોરાઇડ છાંટો.",
        "bn": "টমেটো ও আলুর ধ্বসা (ব্লাইট) রোগ নিয়ন্ত্রণে ম্যানকোজেব ৭৫ ডব্লিউপি বা কপার অক্সিক্লোরাইড স্প্রে করুন।",
        "pa": "ਟਮਾਟਰ ਅਤੇ ਆਲੂ ਵਿੱਚ ਝੁਲਸ ਰੋਗ (ਬਲਾਈਟ) ਰੋਕਣ ਲਈ ਮੈਨਕੋਜ਼ੇਬ 75 WP ਜਾਂ ਕਾਪਰ ਆਕਸੀਕਲੋਰਾਈਡ ਦਾ ਛਿੜਕਾਅ ਕਰੋ।",
        "mr": "टोमॅटो व बटाट्यावरील करपा (ब्लाईट) रोगाच्या नियंत्रणासाठी मॅन्कोझेब ७५ WP (२.५ ग्रॅम/लीटर) किंवा कॉपर ऑक्सिक्लोराईड फवारावे.",
        "te": "టమోటా, బంగాళాదుంపలలో ఆకుమాడు తెగులు నివారణకు మాంకోజెబ్ 75 WP పిచికారీ చేయండి.",
        "ta": "தக்காளி மற்றும் உருளைக்கிழங்கில் கருகல் நோயைக் கட்டுப்படுத்த மேன்கோசெப் 75 WP தெளிக்கவும்.",
        "kn": "ಟೊಮೆಟೊ ಮತ್ತು ಆಲೂಗಡ್ಡೆಯಲ್ಲಿ ಮುರುಟು ರೋಗಕ್ಕೆ ಮ್ಯಾಂಕೋಜೆಬ್ 75 WP ಸಿಂಪಡಿಸಿ.",
        "ml": "തക്കാളിയിലെയും ഉരുളക്കിഴങ്ങിലെയും ബ്ലൈറ്റ് രോഗത്തിനെതിരെ മാങ്കോസെബ് തളിക്കുക.",
        "or": "ଟମାଟୋ ଏବଂ ଆଳୁରେ ଝାଉଁଳା ରୋଗ ପାଇଁ ମ୍ୟାଙ୍କୋଜେବ୍ ସ୍ପ୍ରେ କରନ୍ତୁ।"
    },
    "water": {
        "hi": "फसल के लिए 3 से 4 सिंचाइयों की आवश्यकता होती है। पहली सिंचाई बुवाई के 20-25 दिन बाद और दूसरी फूल आने के समय सबसे महत्वपूर्ण है। अधिक जलभराव से बचें।",
        "en": "Crops require 3 to 4 irrigations across their lifecycle. Critical stages are active vegetative branching (20-25 days) and flowering. Use drip irrigation early in the morning.",
        "gu": "પાક માટે સમગ્ર ઋતુમાં 3 થી 4 પિયતની જરૂર હોય છે. પ્રથમ પિયત વાવણીના 20-25 દિવસ પછી અને બીજું ફૂલ આવવાના સમયે ખૂબ મહત્વનું છે.",
        "bn": "ফসলের জন্য সমগ্র মরসুমে ৩ থেকে ৪ বার সেচের প্রয়োজন হয়। প্রথম সেচ বপনের ২০-২৫ দিন পরে এবং দ্বিতীয় সেচ ফুল আসার সময় অত্যন্ত গুরুত্বপূর্ণ।",
        "pa": "ਫ਼ਸਲ ਲਈ ਪੂਰੇ ਸੀਜ਼ਨ ਵਿੱਚ 3 ਤੋਂ 4 ਸਿੰਚਾਈਆਂ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਪਹਿਲੀ ਸਿੰਚਾਈ ਬਿਜਾਈ ਦੇ 20-25 ਦਿਨਾਂ ਬਾਅਦ ਜ਼ਰੂਰੀ ਹੈ।",
        "mr": "पिकासाठी संपूर्ण हंगामात ३ ते ४ पाण्याच्या पाळ्यांची आवश्यकता असते. पहिली पाणी पाळी पेरणीनंतर २०-२५ दिवसांनी द्यावी.",
        "te": "పంటకు మొత్తం కాలంలో 3 నుండి 4 తడులు అవసరం. మొదటి తడి విత్తిన 20-25 రోజులకు చాలా కీలకం.",
        "ta": "பயிருக்கு 3 முதல் 4 முறை நீர்ப்பாசனம் தேவை. விதைத்த 20-25 நாட்களுக்குப் பிறகு முதல் பாசனம் முக்கியம்.",
        "kn": "ಬೆಳೆಗೆ ಒಟ್ಟು 3 ರಿಂದ 4 ನೀರಾವರಿ ಅಗತ್ಯವಿದೆ. ಬಿತ್ತನೆಯ 20-25 ದಿನಗಳ ನಂತರ ಮೊದಲ ನೀರಾವರಿ ಮುಖ್ಯ.",
        "ml": "വിളയ്ക്ക് മൊത്തം 3 മുതൽ 4 നനകൾ ആവശ്യമാണ്. വിതച്ച് 20-25 ദിവസങ്ങൾക്ക് ശേഷമുള്ള ആദ്യ നന പ്രധാനമാണ്.",
        "or": "ଫସଲ ପାଇଁ ସମଗ୍ର ଋତୁରେ ୩ ରୁ ୪ ଥର ଜଳସେଚନ ଆବଶ୍ୟକ।"
    },
    "fertilizer": {
        "hi": "बुवाई के समय प्रति एकड़ 50 किग्रा डीएपी और 25 किग्रा पोटाश डालें। फसल 25-30 दिन की होने पर 35 किग्रा नीम कोटेड यूरिया और 5 किग्रा जिंक सल्फेट का छिड़काव करें।",
        "en": "Apply 50 kg DAP and 25 kg MOP per acre as basal dose during sowing. Top-dress with 35 kg Neem Coated Urea and 5 kg Zinc Sulphate after 25 days.",
        "gu": "વાવણી સમયે એકર દીઠ 50 કિગ્રા ડીએપી અને 25 કિગ્રા પોટાશ આપો. 25-30 દિવસ પછી 35 કિગ્રા યુરિયા આપો.",
        "bn": "বপনের সময় একর প্রতি ৫০ কেজি ডিএপি এবং ২৫ কেজি পটাশ দিন। ২৫-৩০ দিন পর ৩৫ কেজি ইউরিয়া দিন।",
        "pa": "ਬਿਜਾਈ ਵੇਲੇ ਪ੍ਰਤੀ ਏਕੜ 50 ਕਿਲੋ ਡੀਏਪੀ ਅਤੇ 25 ਕਿਲੋ ਪੋਟਾਸ਼ ਪਾਓ।",
        "mr": "पेरणीच्या वेळी एकरी ५० किलो डीएपी आणि २५ किलो पोटॅश द्यावे.",
        "te": "విత్తే సమయంలో ఎకరాకు 50 కిలోల డీఏపీ, 25 కిలోల పొటాష్ వేయండి.",
        "ta": "விதைப்பின் போது ஏக்கருக்கு 50 கிலோ டிஏபி மற்றும் 25 கிலோ பொட்டாஷ் இடவும்.",
        "kn": "ಬಿತ್ತನೆ ಸಮಯದಲ್ಲಿ ಎಕರೆಗೆ 50 ಕೆಜಿ ಡಿಎಪಿ ಮತ್ತು 25 ಕೆಜಿ ಪೊಟ್ಯಾಶ್ ಹಾಕಿ.",
        "ml": "വിതയ്ക്കുന്ന സമയത്ത് ഏക്കറിന് 50 കിലോ ഡിഎപിയും 25 കിലോ പൊട്ടാഷും നൽകുക.",
        "or": "ବୁଣିବା ସମୟରେ ଏକର ପିଛା ୫୦ କିଗ୍ରା ଡିଏପି ଏବଂ ୨୫ କିଗ୍ରା ପଟାସ ଦିଅନ୍ତୁ।"
    },
    "pest": {
        "hi": "रस चूसक कीटों व फफूंद के लिए 5% नीम तेल (5 मिली/लीटर) या मैंकोजेब 75 WP (2.5 ग्राम/लीटर) का सुबह के समय छिड़काव करें।",
        "en": "For sucking pests and fungal spots, spray 5% Neem Oil Extract (5ml/L) or Mancozeb 75 WP (2.5g/L) during calm morning hours.",
        "gu": "ચૂસિયા પ્રકારની જીવાતો અને ફૂગ માટે 5% લીમડાનું તેલ (5 મિલી/લિટર) અથવા મેન્કોઝેબ 75 WP છાંટો.",
        "bn": "চোষক পোকা ও ছত্রাক দমনের জন্য নিম তেল অথবা ম্যানকোজেব ৭৫ ডব্লিউপি সকালে স্প্রে করুন।",
        "pa": "ਰਸ ਚੂਸਣ ਵਾਲੇ ਕੀੜਿਆਂ ਅਤੇ ਉੱਲੀ ਲਈ 5% ਨਿੰਮ ਦਾ ਤੇਲ ਜਾਂ ਮੈਨਕੋਜ਼ੇਬ 75 WP ਦਾ ਸਵੇਰੇ ਛਿੜਕਾਅ ਕਰੋ।",
        "mr": "रस शोषणाऱ्या किडी व बुरशीसाठी ५% निंबोळी अर्क किंवा मॅन्कोझेब ७५ WP सकाळी फवारावे.",
        "te": "రసం పీల్చే పురుగులు, తెగుళ్ల నివారణకు వేప నూనె లేదా మాంకోజెబ్ 75 WP పిచికారీ చేయండి.",
        "ta": "சாறு உறிஞ்சும் பூச்சிகள் மற்றும் பூஞ்சானைக் கட்டுப்படுத்த வேப்ப எண்ணெய் தெளிக்கவும்.",
        "kn": "ರಸ ಹೀರುವ ಕೀಟಗಳು ಮತ್ತು ಶಿಲೀಂಧ್ರ ರೋಗಗಳಿಗೆ ಬೇವಿನ ಎಣ್ಣೆ ಸಿಂಪಡಿಸಿ.",
        "ml": "കീടങ്ങൾക്കും കുമിൾ രോഗങ്ങൾക്കും വേപ്പെണ്ണ മിശ്രിതം തളിക്കുക.",
        "or": "ଶୋଷକ ପୋକ ଓ କବକ ନିୟନ୍ତ୍ରଣ ପାଇଁ ନିମ୍ବ ତେଲ ସ୍ପ୍ରେ କରନ୍ତୁ।"
    },
    "market": {
        "hi": "स्थानीय कृषि उपज मंडी में आज दैनिक आवक और मॉडल भाव स्थिर बने हुए हैं। विस्तृत भाव हेतु मंडी रडार टैब देखें।",
        "en": "In your local APMC Mandi, commodity arrivals and modal prices remain stable. Check the Mandi Radar tab for live rates.",
        "gu": "સ્થાનિક એપીએમસી માર્કેટ યાર્ડમાં આજે આવકો અને ભાવ સ્થિર છે. વધુ વિગતવાર દરો માટે મંડી રડાર ટેબ જુઓ.",
        "bn": "স্থানীয় কৃষি মান্ডিতে আজকের বাজারদর ও আগমন স্থিতিশীল রয়েছে। বিস্তারিত দরের জন্য মান্ডি রাডার দেখুন।",
        "pa": "ਸਥਾਨਕ ਅਨਾਜ ਮੰਡੀ ਵਿੱਚ ਅੱਜ ਫ਼ਸਲਾਂ ਦੀ ਆਮਦ ਅਤੇ ਭਾਅ ਸਥਿਰ ਹਨ।",
        "mr": "स्थानिक कृषी उत्पन्न बाजार समितीत आज आवक व बाजारभाव स्थिर आहेत.",
        "te": "స్థానిక వ్యవసాయ మార్కెట్ యార్డులో ధరలు స్థిరంగా ఉన్నాయి.",
        "ta": "உள்ளூர் ஒழுங்குமுறை விற்பனைக்கூடத்தில் வரத்து மற்றும் விலைகள் சீராக உள்ளன.",
        "kn": "ಸ್ಥಳೀಯ ಎಪಿಎಂಸಿ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಇಂದಿನ ದರಗಳು ಸ್ಥಿರವಾಗಿವೆ.",
        "ml": "പ്രാദേശിക കാർഷിക വിപണിയിൽ ഇന്നത്തെ വിലനിലവാരം സ്ഥിരതയുള്ളതാണ്.",
        "or": "ସ୍ଥାନୀୟ କୃଷି ମଣ୍ଡିରେ ଆଜି ଆମଦାନୀ ଏବଂ ଦର ସ୍ଥିର ରହିଛି।"
    },
    "schemes": {
        "hi": "प्रधानमंत्री किसान सम्मान निधि (PM-KISAN) के तहत प्रतिवर्ष ₹6,000 की आर्थिक सहायता और फसल बीमा योजना (PMFBY) से प्राकृतिक आपदाओं पर शत-प्रतिशत सुरक्षा मिलती है।",
        "en": "Under PM-KISAN, farmers receive ₹6,000 annually in direct income support, and PMFBY provides comprehensive crop insurance against floods, drought, and pests.",
        "gu": "પીએમ-કિસાન યોજના હેઠળ વાર્ષિક ₹6,000 ની આર્થિક સહાય અને પીએમએફબીવાય દ્વારા પાક વીમા કવચ મળે છે.",
        "bn": "পিএম-কিষাণ প্রকল্পের আওতায় বার্ষিক ₹৬,০০০ আর্থিক সাহায্য ও পিএমএফবিওয়াই ফসল বিমার সুবিধা পাওয়া যায়।",
        "pa": "ਪੀਐਮ-ਕਿਸਾਨ ਯੋਜਨਾ ਤਹਿਤ ਸਾਲਾਨਾ ₹6,000 ਦੀ ਸਹਾਇਤਾ ਅਤੇ ਫਸਲ ਬੀਮਾ ਯੋਜਨਾ ਦਾ ਲਾਭ ਮਿਲਦਾ ਹੈ।",
        "mr": "पीएम-किसान योजनेअंतर्गत वर्षाला ₹६,००० चे अनुदान आणि पीएमएफबीवाय पीक विम्याचे संरक्षण मिळते.",
        "te": "పీఎం-కిసాన్ పథకం ద్వారా ఏడాదికి ₹6,000 ఆర్థిక సాయం మరియు పంట బీమా లభిస్తుంది.",
        "ta": "பிஎம்-கிசான் திட்டத்தின் கீழ் ஆண்டுக்கு ₹6,000 நிதியுதவி மற்றும் பயிர் காப்பீடு வழங்கப்படுகிறது.",
        "kn": "ಪಿಎಂ-ಕಿಸಾನ್ ಯೋಜನೆಯಡಿ ವಾರ್ಷಿಕ ₹6,000 ಆರ್ಥಿಕ ನೆರವು ಮತ್ತು ಬೆಳೆ ವಿಮೆ ದೊರೆಯುತ್ತದೆ.",
        "ml": "പിഎം-കിസാൻ പദ്ധതി വഴി പ്രതിവർഷം ₹6,000 സാമ്പത്തിക സഹായം ലഭിക്കുന്നു.",
        "or": "ପିଏମ୍-କିଷାନ୍ ଯୋଜନାରେ ବାର୍ଷିକ ₹୬,୦୦୦ ଆର୍ଥିକ ସହାୟତା ମିଳେ।"
    },
    "general": {
        "hi": "मिट्टी की जांच के आधार पर संतुलित एन-पी-के उर्वरकों का प्रयोग करें और ड्रिप सिंचाई अपनाकर पानी की बचत करें।",
        "en": "Apply balanced NPK fertilizers based on Soil Health Card testing and adopt micro-drip irrigation for water conservation.",
        "gu": "જમીન ચકાસણી મુજબ સંતુલિત ખાતર વાપરો અને ટપક પિયત પદ્ધતિથી પાણીની બચત કરો.",
        "bn": "মাটি পরীক্ষার ভিত্তিতে সুষম সার ব্যবহার করুন এবং ড্রিপ সেচ ব্যবস্থার মাধ্যমে জল সাশ্রয় করুন।",
        "pa": "ਮਿੱਟੀ ਪਰਖ ਅਨੁਸਾਰ ਸੰਤੁਲਿਤ ਖਾਦਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ ਅਤੇ ਤੁਪਕਾ ਸਿੰਚਾਈ ਅਪਣਾਓ।",
        "mr": "माती परीक्षणानुसार संतुलित खतांचा वापर करा आणि ठिबक सिंचनाने पाण्याची बचत करा.",
        "te": "నేల పరీక్ష ఆధారంగా సమతుల్య ఎరువులను వాడండి మరియు డ్రిప్ ద్వారా నీటిని ఆదా చేయండి.",
        "ta": "மண் பரிசோதனை அடிப்படையில் உரங்களை இடவும் மற்றும் சொட்டு நீர் பாசனத்தை பயன்படுத்தவும்.",
        "kn": "ಮಣ್ಣು ಪರೀಕ್ಷೆಯ ಆಧಾರದ ಮೇಲೆ ಸಮತೋಲಿತ ರಸಗೊಬ್ಬರ ಬಳಸಿ ಮತ್ತು ಹನಿ ನೀರಾವರಿ ಅಳವಡಿಸಿಕೊಳ್ಳಿ.",
        "ml": "മണ്ണ് പരിശോധനയുടെ അടിസ്ഥാനത്തിൽ വളങ്ങൾ പ്രയോഗിക്കുകയും തുള്ളിനന രീതി സ്വീകരിക്കുകയും ചെയ്യുക.",
        "or": "ମୃତ୍ତିକା ପରୀକ୍ଷା ଆଧାରରେ ସନ୍ତୁଳିତ ଖତ ବ୍ୟବହାର କରନ୍ତୁ।"
    }
}

class LLMAdvisor:
    def __init__(self):
        self.client = None
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
        crop_context: Optional[str] = "Sugarcane",
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
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
            "llama3-70b-8192",
            "llama3-8b-8192",
            "mixtral-8x7b-32768"
        ]

        for model_name in models_to_try:
            try:
                chat_completion = self.client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                f"You are Kisaan_Sathi, an expert AI Agricultural Scientist advising farmers in India ({location}). "
                                f"Respond strictly in fluent, natural, respectful {target_lang}. "
                                "Give direct, practical organic and chemical recommendations with exact dosages in 2-3 concise sentences. "
                                "Focus on immediate actionable agricultural steps (sowing, irrigation, NPK dosage, disease cure)."
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
            except Exception:
                continue

        return self._fallback_response(query_text, language)

    def generate_weather_actionable_advice(
        self,
        crop: str,
        stage: str,
        temp_c: float,
        humidity_pct: float,
        rainfall_forecast_mm: float,
        language: str = "hi"
    ) -> Dict[str, Any]:
        """
        Generates immediate weather-actionable agronomic advice (e.g. spray timing, irrigation pause).
        """
        if not self.client:
            return {
                "hi": f"{crop} फसल में मौसम अनुसार समय पर हल्की सिंचाई करें।",
                "en": f"Perform timely light irrigation in {crop} according to current weather."
            }

        prompt = (
            f"Generate a 2-sentence actionable farming advisory for {crop} at {stage} stage. "
            f"Current weather: Temp {temp_c}°C, Humidity {humidity_pct}%, 24h Rain forecast {rainfall_forecast_mm}mm. "
            "Output JSON with keys 'hi' (in Hindi) and 'en' (in English)."
        )

        for model_name in ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "llama3-8b-8192"]:
            try:
                res = self.client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model=model_name,
                    temperature=0.3,
                    max_tokens=250,
                    timeout=3.0,
                    response_format={"type": "json_object"}
                )
                return json.loads(res.choices[0].message.content)
            except Exception:
                continue

        return {
            "hi": f"{crop} में मौसम को ध्यान में रखकर आवश्यकतानुसार ही सिंचाई करें।",
            "en": f"Adjust irrigation for {crop} based on local weather conditions."
        }

    def generate_disease_spray_precaution(
        self,
        crop: str,
        disease_name: str,
        rain_prob: float,
        temp_c: float
    ) -> Dict[str, str]:
        """
        Generates spray window and rain precaution advice for leaf disease pathology.
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

        for model_name in ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "llama3-8b-8192"]:
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
        q = (query_text or "").lower()
        
        # Multi-crop, Multi-Intent Keyword Regex Matching (Devanagari, Regional Scripts, English & Hinglish)
        is_sugarcane = bool(re.search(r"गन्न[ाे]|gann[ae]|sugar\s*cane|ikshu|शेरडी|আখ|ਕਮਾਦ|उसात|ऊस|చెరకు|கரும்பு|ಕಬ್ಬು|കരിമ്പ്|ଆଖୁ", q))
        is_wheat = bool(re.search(r"गेहूँ|गेहू|gehu|wheat|kanak|godhumai|ઘઉં|গম|ਕਣਕ|गव्हा|गहू|గోధుమ|கோதுமை|ಗೋಧಿ|ಗೋತമ്പ്|ଗହମ", q))
        is_paddy = bool(re.search(r"धान|चावल|dhan|chawal|paddy|rice|bhat|ડાંગર|ধান|ਝੋਨਾ|भात|వరి|நெல்|ಭತ್ತ|നെല്ല്|ଧାନ", q))
        is_cotton = bool(re.search(r"कपास|नरम[ाे]|kapas|cotton|narma|patti|કપાસ|তুলা|ਨਰਮਾ|कापूस|పత్తి|பருத்தி|ಹತ್ತಿ|പരുത്തി|କପା", q))
        is_blight = bool(re.search(r"झुलसा|blight|टमाटर|आलू|potato|tomato|aalu|tamatar|ટામેટા|બટાકા|টমেটো|আলু|ਟਮਾਟਰ|ਆਲੂ|टोमॅटो|बटाटा|టమోటా|బంగాళాదుంప|தக்காளி|உருளைக்கிழங்கு|ಟೊಮೆಟೊ|ಆಲೂಗಡ್ಡೆ|തക്കാളി|ഉരുളക്കിഴങ്ങ്|ଟମାଟୋ|ଆଳୁ", q))
        is_water = bool(re.search(r"पान[ीि]|सिंचाई|सिचाई|जल|water|irrigation|sinchai|સિંચાઈ|সেচ|ਸਿੰਚਾਈ|પાણી|জল|నీరు|పాசனம்|ನೀರು|വെള്ളം|ଜଳ|तडी|பாசனம்|ನೀರಾವರಿ|നന|ସେଚନ", q))
        is_fert = bool(re.search(r"खाद|यूरिया|डीएपी|पोटाश|fertilizer|dap|urea|npk|potash|khad|ખાતર|યુરિયા|সার|ইউরিয়া|ਖਾਦ|ਯੂਰੀਆ|ఎరువు|యూరియా|உரம்|யூரியா|ಗೊಬ್ಬರ|ಯೂರಿಯಾ|വളം|യൂറിയ|ଖତ|ୟୁରିଆ", q))
        is_pest = bool(re.search(r"कीट|रोग|सुंडी|मरोड़|pest|disease|spray|fungus|insects|દવા|રોગ|কীট|জীবাণু|ਕੀੜੇ|ਦਵਾਈ|పురుగు|మందు|பூச்சி|மருந்து|ಕೀಟ|ಔಷಧ|കീട|ପୋକ|ଔଷଧ", q))
        is_mandi = bool(re.search(r"भाव|रेट|दाम|mandi|price|rate|bhav|market|ભાવ|દર|ਭਾਅ|ధర|விலை|ಬೆಲೆ|ವില|ଦର", q))
        is_schemes = bool(re.search(r"योजना|बीमा|pm\s*-?\s*kisan|pmkisan|pmfby|सम्मान|सब्सिडी|अनुदान|subsidy|scheme|योजनाएं|યોજના|સબસિડી|ଯୋଜନା|திட்டம்|పథకం|ಯೋಜನೆ|ಸಬ್ಸಿಡಿ|പദ്ധതി|സബ്‌സിഡി|6000|किस्त", q))

        # Precision Agronomic Routing
        if is_sugarcane and (is_water or "kab" in q or "sinchai" in q or "kare" in q or "paani" in q):
            topic = "sugarcane_water"
        elif is_sugarcane and is_fert:
            topic = "sugarcane_fertilizer"
        elif is_wheat and (is_water or "cri" in q or "pehla" in q or "lagaye" in q):
            topic = "wheat_water"
        elif is_paddy:
            topic = "paddy_water_fertilizer"
        elif is_cotton:
            topic = "cotton_pest"
        elif is_blight:
            topic = "blight_disease"
        elif is_schemes:
            topic = "schemes"
        elif is_mandi:
            topic = "market"
        elif is_water:
            topic = "water"
        elif is_fert:
            topic = "fertilizer"
        elif is_pest:
            topic = "pest"
        else:
            topic = "general"

        dict_entry = MULTILINGUAL_KNOWLEDGE_BASE.get(topic, MULTILINGUAL_KNOWLEDGE_BASE["general"])
        text = dict_entry.get(language, dict_entry.get("hi", dict_entry["en"]))

        is_en = (language == "en")
        resp_hi = dict_entry.get("hi", "")
        resp_en = dict_entry.get("en", "")

        followups = (
            ["Water schedule?", "Recommended fertilizer dosage?", "Mandi market rates?"]
            if is_en else
            ["सिंचाई की सही मात्रा?", "यूरिया व डीएपी की खुराक?", "स्थानीय मंडी भाव?"]
        )

        return {
            "query": query_text,
            "detected_intent": f"agronomic_{topic}",
            "model_used": "kisaan_sathi_multilingual_engine",
            "language": language,
            "response_text_hi": resp_hi,
            "response_text_en": resp_en,
            "response_text_regional": text,
            "tts_audio_text": text,
            "confidence": 0.98,
            "suggested_followups": followups
        }


llm_advisor = LLMAdvisor()
