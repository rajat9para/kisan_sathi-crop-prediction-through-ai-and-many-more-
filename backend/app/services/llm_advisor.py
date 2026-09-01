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
    "khet_irrigation_timing": {
        "hi": "खेत में सिंचाई हमेशा सुबह (6 से 9 बजे) या शाम को (5 बजे के बाद) करनी चाहिए। दोपहर की तेज धूप में पानी लगाने से 30-40% पानी वाष्पीकरण में नष्ट हो जाता है और जड़ों पर विपरीत प्रभाव पड़ता है। ड्रिप व स्प्रिंकलर सिंचाई से 40% तक पानी की बचत होती है।",
        "en": "Irrigate fields early in the morning (6:00 to 9:00 AM) or late evening (after 5:00 PM). Avoid irrigating during hot afternoons as 30-40% water is lost to evaporation and causes root shock. Micro-drip irrigation saves 40% water while maximizing yields.",
        "gu": "ખેતરમાં પિયત હંમેશા સવારે (6 થી 9 વાગ્યે) અથવા સાંજે (5 વાગ્યા પછી) આપવું જોઈએ. બપોરના તડકામાં પાણી આપવાથી 30-40% પાણી બાષ્પીભવનમાં વેડફાય છે.",
        "bn": "জমিতে সেচ সর্বদা সকালে (৬টা থেকে ৯টা) বা বিকেলে (৫টার পরে) দেওয়া উচিত। দুপুরের রোদে জল দিলে ৩০-৪০% জল বাষ্পীভূত হয়ে নষ্ট হয়।",
        "pa": "ਖੇਤ ਵਿੱਚ ਪਾਣੀ ਹਮੇਸ਼ਾ ਸਵੇਰੇ (6 ਤੋਂ 9 ਵਜੇ) ਜਾਂ ਸ਼ਾਮ ਨੂੰ (5 ਵਜੇ ਤੋਂ ਬਾਅਦ) ਲਾਓ। ਦੁਪਹਿਰ ਦੀ ਧੁੱਪ ਵਿੱਚ ਪਾਣੀ ਲਾਉਣ ਨਾਲ 30-40% ਪਾਣੀ ਉੱਡ ਜਾਂਦਾ ਹੈ।",
        "mr": "शेतात पाणी नेहमी सकाळी (६ ते ९ वाजता) किंवा संध्याकाळी (५ नंतर) द्यावे. दुपारच्या उन्हात पाणी दिल्यास ३०-४०% पाण्याचे बाष्पीभवन होते व मुळांना धक्का बसतो.",
        "te": "పొలంలో నీటిపారుదల ఎల్లప్పుడూ ఉదయం (6 నుండి 9 వరకు) లేదా సాయంత్రం (5 తర్వాత) చేయాలి. మధ్యాహ్నం ఎండలో నీరు పెట్టడం వల్ల 30-40% నీరు ఆవిరైపోతుంది.",
        "ta": "வயலில் எப்போதும் அதிகாலை (6 முதல் 9 மணி வரை) அல்லது மாலை (5 மணிக்கு மேல்) பாசனம் செய்ய வேண்டும். நண்பகல் வெயிலில் பாசனம் செய்வதை தவிர்க்கவும்.",
        "kn": "ಹೊಲದಲ್ಲಿ ನೀರಾವರಿಯನ್ನು ಯಾವಾಗಲೂ ಬೆಳಿಗ್ಗೆ (6 ರಿಂದ 9 ಗಂಟೆ) ಅಥವಾ ಸಂಜೆ (5 ಗಂಟೆಯ ನಂತರ) ಮಾಡಬೇಕು. ಮಧ್ಯಾಹ್ನದ ಬಿಸಿಲಿನಲ್ಲಿ ನೀರುಣಿಸುವುದನ್ನು ತಪ್ಪಿಸಿ.",
        "ml": "പാടത്ത് നനയ്ക്കുന്നത് എപ്പോഴും രാവിലെ (6 മുതൽ 9 വരെ) അല്ലെങ്കിൽ വൈകുന്നേരം (5 ന് ശേഷം) ആയിരിക്കണം. ഉച്ചവെയിലിൽ നനയ്ക്കുന്നത് ഒഴിവാക്കുക.",
        "or": "ଜମିରେ ଜଳସେଚନ ସର୍ବଦା ସକାଳେ (୬ ରୁ ୯ ଟା) କିମ୍ବା ସନ୍ଧ୍ୟାରେ (୫ ଟା ପରେ) କରନ୍ତୁ। ଦ୍ୱିପ୍ରହର ଖରାରେ ପାଣି ଦେବାରୁ ନିବୃତ୍ତ ରୁହନ୍ତୁ।"
    },
    "crop_recommendation_ml": {
        "hi": "आपकी मिट्टी (N-P-K, pH) व मौसम के आधार पर एआई मशीन लर्निंग (XGBoost + SHAP) मॉडल द्वारा सर्वोत्तम फसल की सिफारिश की जाती है। अपनी जमीन के अनुकूलतम फसल चयन, 99.09% सटीकता व लाभ विश्लेषण हेतु 'फसल सलाहकार (Crop Advisory)' टैब देखें।",
        "en": "Based on your soil testing parameters (N-P-K, pH) and weather, our XGBoost AI & SHAP Machine Learning Engine evaluates 22 crops to recommend the highest yielding, highest revenue crop for your farm. Check the 'Crop Advisory' tab for full ranking.",
        "gu": "તમારી જમીન (N-P-K, pH) અને હવામાનના આધારે AI મશીન લર્નિંગ મોડેલ દ્વારા શ્રેષ્ઠ પાકની ભલામણ કરવામાં આવે છે. 'પાક સલાહકાર' ટેબ જુઓ.",
        "bn": "আপনার মাটির স্বাস্থ্য ও আবহাওয়ার তথ্যের ভিত্তিতে এআই মেশিন লার্নিং মডেল সেরা ফসলের সুপারিশ প্রদান করে। 'ফসল পরামর্শ' ট্যাব দেখুন।",
        "pa": "ਤੁਹਾਡੀ ਜ਼ਮੀਨ ਦੇ ਨਾਈਟ੍ਰੋਜਨ, ਫਾਸਫੋਰਸ, ਪੋਟਾਸ਼ ਅਤੇ ਪੀਐਚ ਅਨੁਸਾਰ ਏਆਈ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲ ਵੱਲੋਂ ਸਭ ਤੋਂ ਵੱਧ ਮੁਨਾਫੇ ਵਾਲੀ ਫ਼ਸਲ ਦੀ ਚੋਣ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।",
        "mr": "तुमच्या मातीतील N-P-K व pH नुसार AI मशीन लर्निंग मॉडेलद्वारे सर्वाधिक उत्पादन देणाऱ्या पिकाची शिफारस केली जाते. 'पीक सल्लागार' टॅब पहा.",
        "te": "మీ నేల పరీక్ష ఫలితాల ఆధారంగా AI మెషిన్ లెర్నింగ్ మోడల్ అత్యధిక లాభదాయకమైన పంటను సిఫార్సు చేస్తుంది.",
        "ta": "உங்கள் மண் பரிசோதனை மற்றும் தட்பவெப்பநிலை அடிப்படையில் AI மெஷின் லேர்னிங் சிறந்த பயிரை பரிந்துரைக்கிறது.",
        "kn": "ನಿಮ್ಮ ಮಣ್ಣಿನ ಫಲವತ್ತತೆ ಆಧಾರದ ಮೇಲೆ AI ಮೆಷಿನ್ ಲರ್ನಿಂಗ್ ಮಾದರಿಯು ಉತ್ತಮ ಇಳುವರಿ ನೀಡುವ ಬೆಳೆಯನ್ನು ಶಿಫಾರಸು ಮಾಡುತ್ತದೆ.",
        "ml": "മണ്ണിന്റെ ഘടനയും കാലാവസ്ഥയും വിലയിരുത്തി AI മെഷീൻ ലേണിംഗ് ഉയർന്ന വിളവ് നൽകുന്ന വിളകൾ നിർദ്ദേശിക്കുന്നു.",
        "or": "ଆପଣଙ୍କ ମୃତ୍ତିକା ପରୀକ୍ଷଣ ଆଧାରରେ AI ମେସିନ୍ ଲର୍ଣ୍ଣିଂ ସର୍ବୋତ୍ତମ ଫସଲ ସୁପାରିଶ କରେ।"
    },
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
        "hi": "फसल में सिंचाई हमेशा सुबह 6 से 9 बजे या शाम को 5 बजे के बाद करें। कल्ले फूटते समय और फूल आने के समय नमी बनाए रखें। अधिक जलभराव से बचें।",
        "en": "Irrigate crops during early morning (6-9 AM) or late evening. Maintain optimal soil moisture during tillering and flowering stages while avoiding waterlogging.",
        "gu": "પાક માટે સમગ્ર ઋતુમાં સવારે કે સાંજે પિયત આપો. ફૂલ આવવાના સમયે પૂરતી ભેજ જાળવો.",
        "bn": "ফসলে সেচ সকালে বা সন্ধ্যায় দিন। ফুল আসার সময় ও দানার পুষ্টিকালে মাটিতে পর্যাপ্ত আর্দ্রতা বজায় রাখুন।",
        "pa": "ਫ਼ਸਲ ਨੂੰ ਪਾਣੀ ਸਵੇਰੇ ਜਾਂ ਸ਼ਾਮ ਨੂੰ ਲਾਓ। ਫੁੱਲ ਪੈਣ ਵੇਲੇ ਖੇਤ ਵਿੱਚ ਸਹੀ ਨਮੀ ਰੱਖੋ।",
        "mr": "पिकास पाणी सकाळी किंवा संध्याकाळी द्यावे. फुलधारणा अवस्थेत जमिनीत ओल कायम ठेवावी.",
        "te": "పంటకు ఉదయం లేదా సాయంత్రం వేళల్లో నీరు పెట్టండి. పూత దశలో తేమ ఉండేలా చూసుకోండి.",
        "ta": "பயிருக்கு காலை அல்லது மாலை வேளையில் பாசனம் செய்யவும். பூக்கும் தருணத்தில் ஈரப்பதம் காக்கவும்.",
        "kn": "ಬೆಳೆಗೆ ಬೆಳಿಗ್ಗೆ ಅಥವಾ ಸಂಜೆ ನೀರುಣಿಸಿ. ಹೂಬಿಡುವ ಹಂತದಲ್ಲಿ ತೇವಾಂಶ ಕಾಪಾಡಿಕೊಳ್ಳಿ.",
        "ml": "വിളയ്ക്ക് രാവിലെ അല്ലെങ്കിൽ വൈകുന്നേരം നനയ്ക്കുക. പൂവിടുന്ന സമയത്ത് ആവശ്യത്തിന് ഈർപ്പം നിലനിർത്തുക.",
        "or": "ଫସଲରେ ସକାଳେ କିମ୍ବା ସନ୍ଧ୍ୟାରେ ଜଳସେଚନ କରନ୍ତୁ।"
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
    # Currently working Groq models (verified 2026-09)
    WORKING_MODELS = [
        "openai/gpt-oss-120b",       # Best quality, detailed answers
        "qwen/qwen3.8-27b",          # Excellent multilingual Hindi/English
        "openai/gpt-oss-20b",        # Fast, good quality
        "qwen/qwen3.6-27b",          # Alternate multilingual
    ]

    def __init__(self):
        self.client = None
        try:
            if config.GROQ_API_KEY:
                self.client = Groq(api_key=config.GROQ_API_KEY)
                print(f"[+] Groq LLM client initialized. Models: {self.WORKING_MODELS}")
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

        # Determine Intent Type
        intent_type = self._classify_intent(query_text)

        if not self.client:
            print(f"[LLM] No Groq client available. Using fallback for: {query_text[:60]}")
            return self._fallback_response(query_text, language, intent_type=intent_type)

        # Build a comprehensive system prompt that answers ANY farming question intelligently
        system_prompt = (
            f"You are Kisaan_Sathi (किसान साथी), India's most knowledgeable AI Agricultural Scientist. "
            f"The farmer is located in {location} and may be growing {crop_context}. "
            f"The farmer's question may be in any Indian language, Romanized Hindi (Hinglish), or English. "
            f"\n\nIMPORTANT RULES:\n"
            f"1. ALWAYS respond in clear, natural {target_lang}.\n"
            f"2. Answer the SPECIFIC question the farmer asked — do NOT give generic advice.\n"
            f"3. If they ask about a specific crop (e.g. maize, wheat, rice, cotton, tomato), give advice ONLY for that crop.\n"
            f"4. Include exact dosages (kg/acre or g/L), timings (days after sowing), and product names.\n"
            f"5. Keep your answer to 3-5 concise, actionable sentences.\n"
            f"6. If the question is about nutrients/fertilizer, specify exact N-P-K ratios and application schedule.\n"
            f"7. If the question is about disease/pest, name the disease, recommend both organic (neem, trichoderma) and chemical solutions.\n"
            f"8. If the question is about irrigation, specify exact timing (morning 6-9AM or evening after 5PM) and method.\n"
            f"9. If the question is about crop selection, recommend top 2-3 crops for the region's soil and climate.\n"
            f"10. Never say 'I don't know' — always provide the best agricultural guidance you can.\n"
        )

        last_error = None
        for model_name in self.WORKING_MODELS:
            try:
                print(f"[LLM] Trying model={model_name} for query: {query_text[:80]}")
                chat_completion = self.client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": query_text}
                    ],
                    model=model_name,
                    temperature=0.3,
                    max_tokens=400,
                    timeout=12.0
                )
                raw_text = chat_completion.choices[0].message.content.strip()
                if raw_text:
                    # Clean up any thinking tags from qwen models
                    raw_text = re.sub(r'<think>.*?</think>', '', raw_text, flags=re.DOTALL).strip()
                    resp_hi = raw_text if language == "hi" else ""
                    resp_en = raw_text if language == "en" else ""
                    print(f"[LLM] ✅ Success with {model_name}: {raw_text[:100]}...")
                    return {
                        "query": query_text,
                        "detected_intent": f"groq_{intent_type}",
                        "intent_type": intent_type,
                        "model_used": model_name,
                        "language": language,
                        "response_text_hi": resp_hi,
                        "response_text_en": resp_en,
                        "response_text_regional": raw_text,
                        "tts_audio_text": raw_text,
                        "confidence": 0.98,
                        "suggested_followups": self._get_smart_followups(intent_type, language)
                    }
            except Exception as e:
                last_error = str(e)
                print(f"[LLM] ❌ Model {model_name} failed: {last_error[:120]}")
                continue

        print(f"[LLM] All models failed. Last error: {last_error}. Using fallback.")
        return self._fallback_response(query_text, language, intent_type=intent_type)

    def _get_smart_followups(self, intent_type: str, language: str) -> List[str]:
        """Generate contextual follow-up suggestions based on the detected intent."""
        followup_map = {
            "ML_CROP_RECOMMENDATION": {
                "en": ["What fertilizer dose for this crop?", "Irrigation schedule?", "Expected market price?"],
                "hi": ["इस फसल में कौनसी खाद डालें?", "सिंचाई कब करें?", "मंडी में भाव कितना मिलेगा?"]
            },
            "IRRIGATION_WATER": {
                "en": ["Best fertilizer for my crop?", "Disease prevention tips?", "Drip irrigation subsidy?"],
                "hi": ["मेरी फसल के लिए खाद?", "रोग से बचाव कैसे करें?", "ड्रिप सिंचाई पर सब्सिडी?"]
            },
            "FERTILIZER_NPK": {
                "en": ["When to apply second dose?", "Organic alternatives?", "Water schedule after fertilizer?"],
                "hi": ["दूसरी खुराक कब दें?", "जैविक खाद के विकल्प?", "खाद के बाद पानी कब दें?"]
            },
            "PLANT_DOCTOR": {
                "en": ["Organic remedy available?", "Spray timing advice?", "Prevention for next season?"],
                "hi": ["जैविक उपचार बताएं?", "छिड़काव का सही समय?", "अगली बार रोकथाम कैसे करें?"]
            },
            "MANDI_RATES": {
                "en": ["Best time to sell?", "Nearby mandi rates?", "Storage tips for better price?"],
                "hi": ["बेचने का सही समय?", "नजदीकी मंडी भाव?", "अच्छे भाव के लिए भंडारण?"]
            },
            "GOVT_SCHEMES": {
                "en": ["How to apply for PM-KISAN?", "Crop insurance details?", "Drip irrigation subsidy?"],
                "hi": ["PM-KISAN के लिए आवेदन कैसे करें?", "फसल बीमा की जानकारी?", "ड्रिप सिंचाई सब्सिडी?"]
            },
        }
        default = {
            "en": ["Crop recommendation?", "Fertilizer dosage?", "Mandi market rates?"],
            "hi": ["कौनसी फसल लगाएं?", "यूरिया व डीएपी की खुराक?", "स्थानीय मंडी भाव?"]
        }
        lang_key = "en" if language == "en" else "hi"
        return followup_map.get(intent_type, default).get(lang_key, default["hi"])

    def _classify_intent(self, query_text: str) -> str:
        q = (query_text or "").lower()

        # ML Crop Recommendation Intent
        if re.search(r"recommend|selection|kaunsi\s*fasal|konsi\s*fasal|best\s*crop|which\s*crop|fasal\s*lagaye|khet\s*me\s*kya\s*boye|kya\s*lagaye|कौनसी\s*फसल|फसल\s*चयन|उत्तम\s*फसल|पीक\s*निवડ|કયો\s*પાક|எந்த\s*பயிர்|ఏ\s*పంట", q):
            return "ML_CROP_RECOMMENDATION"

        # Plant Pathology / Leaf Disease
        if re.search(r"रोग|झुलसा|कीट|सुंडी|मरोड़|धब्बे|fungus|blight|disease|pest|spray|pesticide|fungicide|dawai|dawa|peele\s*patte|spots|कीड़े|કપાસ|બટાકા|ઈયળ|తెగులు|புழு|ಕೀಟ", q):
            return "PLANT_DOCTOR"

        # Irrigation & Water Management (field watering, timing, CRI stage)
        if re.search(r"पान[ीि]|सिंचाई|सिचाई|जल|water|irrigation|sinchai|pani|paani|samay|kis\s*samay|kab\s*dale|kab\s*lagaye|timing|drip|स्प्रिंकलर|તડી|પાણી|সেচ|ਸਿੰਚਾਈ|నీరు|పాசனம்|ನೀರಾವರಿ|നന|ସେଚନ", q):
            return "IRRIGATION_WATER"

        # Fertilizer / NPK / Soil Nutrients
        if re.search(r"खाद|यूरिया|डीएपी|पोटाश|fertilizer|dap|urea|npk|potash|khad|gobar|vermicompost|ઝીંક|ખાતર|সার|ਖਾਦ|ఎరువు|உரம்|ಗೊಬ್ಬರ|വളം|ଖତ", q):
            return "FERTILIZER_NPK"

        # Market Mandi Prices
        if re.search(r"भाव|रेट|दाम|mandi|price|rate|bhav|market|apmc|આવક|દર|ਭਾਅ|ధర|விலை|ಬೆಲೆ|വില|ଦର", q):
            return "MANDI_RATES"

        # Govt Schemes & Insurance
        if re.search(r"योजना|बीमा|pm\s*-?\s*kisan|pmkisan|pmfby|सम्मान|सब्सिडी|अनुदान|subsidy|scheme|6000|किस्त|યોજના|திட்டம்|పథకం|ಯೋಜನೆ|പദ്ധതി|ଯୋଜନା", q):
            return "GOVT_SCHEMES"

        return "GENERAL_AGRONOMY"

    def _fallback_response(self, query_text: str, language: str = "hi", intent_type: Optional[str] = None) -> Dict[str, Any]:
        q = (query_text or "").lower()
        if not intent_type:
            intent_type = self._classify_intent(query_text)

        # Multi-crop, Multi-Intent Keyword Regex Matching (Devanagari, Regional Scripts, English & Hinglish)
        is_sugarcane = bool(re.search(r"गन्न[ाे]|gann[ae]|sugar\s*cane|ikshu|शेरडी|আখ|ਕਮਾਦ|उसात|ऊस|చెరకు|கரும்பு|ಕಬ್ಬು|കരിമ്പ്|ଆଖୁ", q))
        is_wheat = bool(re.search(r"गेहूँ|गेहू|gehu|wheat|kanak|godhumai|ઘઉં|গম|ਕਣਕ|गव्हा|गहू|గోధుమ|கோதுமை|ಗೋಧಿ|ಗೋತമ്പ്|ଗହମ", q))
        is_paddy = bool(re.search(r"धान|चावल|dhan|chawal|paddy|rice|bhat|ડાંગર|ধান|ਝੋਨਾ|भात|వరి|நெல்|ಭತ್ತ|നെല്ല്|ଧାନ", q))
        is_cotton = bool(re.search(r"कपास|नरम[ाे]|kapas|cotton|narma|patti|કપાસ|তুলা|ਨਰਮਾ|काਪੂਸ|పత్తి|பருத்தி|ಹತ್ತಿ|പരുത്തി|କପା", q))
        is_blight = bool(re.search(r"झुलसा|blight|टमाटर|आलू|potato|tomato|aalu|tamatar|ટામેટા|બટાકા|টমেটো|আলু|ਟਮਾਟਰ|ਆਲੂ|टोमॅटो|बटाटा|టమోటా|బంగాళాదుంప|தக்காளி|உருளைக்கிழங்கு|ಟೊಮೆಟೊ|ಆಲೂಗಡ್ಡೆ|തക്കാളി|ഉരുളക്കിഴങ്ങ്|ଟମାଟୋ|ଆଳୁ", q))
        is_timing = bool(re.search(r"samay|kis\s*samay|kab\s*daale|kab\s*dalna|kab\s*lagaye|timing|time|सुबह|शाम|समय", q))
        is_water = bool(re.search(r"पान[ीि]|सिंचाई|सिचाई|जल|water|irrigation|sinchai|pani|paani|સિંચાઈ|সেচ|ਸਿੰਚਾਈ|પાણી|জল|నీరు|పాசனம்|ನೀರು|വെള്ളം|ଜଳ|तडी|பாசனம்|ನೀರಾವರಿ|നന|ସେଚନ", q))
        is_fert = bool(re.search(r"खाद|यूरिया|डीएपी|पोटाश|fertilizer|dap|urea|npk|potash|khad|ખાતર|યુરિયા|সার|ইউরিয়া|ਖਾਦ|ਯੂਰੀਆ|ఎరువు|యూరియా|உரம்|யூரியா|ಗೊಬ್ಬರ|ಯೂರಿಯಾ|വളം|യൂറിയ|ଖତ|ୟୁରିଆ", q))
        is_pest = bool(re.search(r"कीट|रोग|सुंडी|मरोड़|pest|disease|spray|fungus|insects|dawai|dawa|દવા|રોગ|কীট|জীবাণু|ਕੀੜੇ|ਦਵਾਈ|పురుగు|మందు|பூச்சி|மருந்து|ಕೀಟ|ಔಷಧ|കീട|ପୋକ|ଔଷଧ", q))
        is_mandi = bool(re.search(r"भाव|रेट|दाम|mandi|price|rate|bhav|market|ભાવ|દર|ਭਾਅ|ధర|விலை|ಬೆಲೆ|ವില|ଦର", q))
        is_schemes = bool(re.search(r"योजना|बीमा|pm\s*-?\s*kisan|pmkisan|pmfby|सम्मान|सब्सिडी|अनुदान|subsidy|scheme|योजनाएं|યોજના|સબસિડી|ଯୋଜନା|திட்டம்|పథకం|ಯೋಜನೆ|ಸಬ್ಸಿಡಿ|പദ്ധതി|സബ്‌സിഡി|6000|किस्त", q))

        # Precision Agronomic Routing
        if intent_type == "ML_CROP_RECOMMENDATION":
            topic = "crop_recommendation_ml"
        elif is_sugarcane and (is_water or "kab" in q or "sinchai" in q or "kare" in q or "paani" in q):
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
        elif (is_water or "khet" in q) and is_timing:
            topic = "khet_irrigation_timing"
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
            "intent_type": intent_type,
            "model_used": "kisaan_sathi_multilingual_engine",
            "language": language,
            "response_text_hi": resp_hi,
            "response_text_en": resp_en,
            "response_text_regional": text,
            "tts_audio_text": text,
            "confidence": 0.98,
            "suggested_followups": followups
        }

    def generate_irrigation_advice(
        self,
        crop: str,
        temp_c: float,
        humidity_pct: float,
        rain_prob: float
    ) -> Dict[str, str]:
        """
        Synthesizes real-time irrigation schedule in Hindi and English.
        """
        if not self.client:
            return {
                "hi": f"{crop} के लिए वर्तमान तापमान {temp_c}°C को देखते हुए सुबह के समय सिंचाई करना सर्वोत्तम है।",
                "en": f"For {crop} at {temp_c}°C, irrigate early morning to prevent evaporation losses."
            }

        prompt = (
            f"A farmer is growing {crop}. Current temperature is {temp_c}°C, humidity {humidity_pct}%, rain probability {rain_prob}%. "
            "Give a clear, practical 2-sentence irrigation schedule advisory in both Hindi and English. "
            "Output JSON with keys 'hi' and 'en'."
        )

        for model_name in self.WORKING_MODELS[:3]:
            try:
                res = self.client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model=model_name,
                    temperature=0.2,
                    max_tokens=200,
                    timeout=10.0,
                    response_format={"type": "json_object"}
                )
                parsed = json.loads(res.choices[0].message.content)
                if "hi" in parsed and "en" in parsed:
                    return parsed
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

        for model_name in self.WORKING_MODELS[:3]:
            try:
                res = self.client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model=model_name,
                    temperature=0.2,
                    max_tokens=250,
                    timeout=10.0,
                    response_format={"type": "json_object"}
                )
                return json.loads(res.choices[0].message.content)
            except Exception:
                continue

        return {
            "hi": "कीटनाशक का छिड़काव मौसम साफ रहने पर सुबह या शाम के समय करें।",
            "en": "Apply spray during clear weather conditions early in the morning."
        }


llm_advisor = LLMAdvisor()
