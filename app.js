/**
 * KISAAN_SATHI (किसान साथी) Web Application Engine
 * Supports 11 Indian Languages, 11 Regional Agro-Ecological Hubs, 11 Soil Health Cards,
 * GPS Auto-Location Detection, First-Launch Language Selector Modal with Default Persistence,
 * Explainable Crop Advisory, Plant Doctor AI, Voice Saathi, and Supabase Live Sync.
 */

// 11 INDIAN LANGUAGES LOCALIZATION DICTIONARY (FARMER-FIRST TERMINOLOGY)
const I18N_DICTIONARY = {
  hi: {
    code: "hi",
    name: "हिन्दी",
    flag: "🇮🇳",
    speechCode: "hi-IN",
    brand_tagline: "एआई आधारित सूक्ष्म-जलवायु फसल सलाह व रोग निदान",
    supabase_sync: "सुपाबेस लाइव सक्रिय",
    live_mandi_label: "लाइव मंडी भाव",
    hero_headline: "वैज्ञानिक प्रमाणों और सटीक डेटा पर आधारित स्मार्ट कृषि सलाह",
    hero_sub: "आपकी मिट्टी के पोषक तत्वों और उपग्रह मौसम का विश्लेषण कर आपकी मातृभाषा में सही फसल और वैज्ञानिक सलाह।",
    btn_detect_location: "📍 मेरा खेत स्थान खोजें (GPS)",
    quick_hubs_label: "प्रमुख कृषि क्षेत्र व मृदा प्रकार:",
    lbl_temperature: "Temperature / तापमान",
    lbl_humidity: "Humidity / नमी",
    lbl_rain7d: "7-Day Rain / वर्षा",
    tab_advisory: "फसल सलाह (Crop Advisory)",
    tab_doctor: "फसल डॉक्टर (रोग पहचान)",
    tab_voice: "वॉइस साथी (बोलकर पूछें)",
    tab_mandi: "मंडी भाव व मौसम रडार",
    tab_supabase: "क्लाउड सिंक व स्थिति",
    panel_soil_title: "खेत का विवरण व मृदा परीक्षण",
    panel_soil_sub: "मृदा स्वास्थ्य कार्ड लोड करें या सीधे मान भरें",
    lbl_state: "State / राज्य",
    lbl_district: "District / जिला",
    lbl_n: "Nitrogen (N) kg/ha",
    lbl_p: "Phosphorus (P) kg/ha",
    lbl_k: "Potassium (K) kg/ha",
    lbl_ph: "Soil pH Level / मिट्टी का pH मान",
    lbl_irrigation: "Irrigation Facility / सिंचाई सुविधा",
    lbl_farmsize: "Farm Size (Acres) / खेत का आकार",
    lbl_prevcrop: "Previous Crop / पिछली फसल",
    btn_run_advisory: "🌱 खेत का विश्लेषण करें और फसल सलाह पाएं",
    panel_recs_title: "अनुशंसित सर्वोत्तम फसलें",
    panel_recs_sub: "मृदा उर्वरता, मौसम और बाजार भाव के आधार पर रैंकिंग",
    badge_best_match: "#1 BEST MATCH / सर्वोत्तम",
    lbl_match: "सटीकता",
    pillar_soil: "Soil Fit / मृदा",
    pillar_weather: "Weather Fit / मौसम",
    pillar_market: "Market Fit / मंडी",
    pillar_rotation: "Rotation / चक्र",
    lbl_yield: "Est. Yield / पैदावार",
    lbl_revenue: "Est. Revenue / आय",
    lbl_rate: "Mandi Rate / भाव",
    lbl_sowing: "Sowing / बुवाई",
    shap_title: "🌱 यह फसल आपके खेत के लिए सबसे उत्तम क्यों है?",
    shap_tag: "पोषक तत्व व मौसम अनुकूलता",
    runners_title: "वैकल्पिक फसलें (Alternative Crops)",
    panel_doctor_title: "पौधा रोग निदान व पत्ती स्कैनर",
    panel_doctor_sub: "पत्ती का नमूना चुनें या रोग का तुरंत विश्लेषण करें",
    leaf_gallery_title: "परीक्षण हेतु पत्तियों के नमूने (क्लिक करें):",
    dropzone_title: "खेत से खींची पत्ती की फोटो यहां डालें",
    dropzone_sub: "टमाटर, आलू, कपास, गेहूं, धान, मक्का आदि के लिए उपयुक्त",
    btn_run_diagnosis: "एआई रोग निदान चलाएं",
    panel_diag_title: "रोग निदान रिपोर्ट व उपचार",
    panel_diag_sub: "जैविक व रासायनिक समाधान और मौसम अनुकूल छिड़काव",
    spray_alert_title: "🌦️ मौसम आधारित छिड़काव सलाह",
    remedy_organic_badge: "🌿 100% Organic / प्राकृतिक उपचार",
    remedy_chemical_badge: "🧪 Scientific Chemical / रासायनिक उपचार",
    voice_hero_title: "वॉइस साथी — आपका अपना कृषि सलाहकार",
    voice_hero_sub: "सरल हिंदी और क्षेत्रीय भाषाओं में बोलकर सटीक सलाह देता है।",
    voice_chips_label: "अक्सर पूछे जाने वाले सवाल (Click to Ask):",
    chip_water: "पानी कितना चाहिए? (Irrigation)",
    chip_fertilizer: "खाद की मात्रा? (Fertilizer)",
    chip_mandi: "मंडी भाव क्या है? (Mandi Price)",
    chip_pest: "कीट नियंत्रण? (Pest Control)",
    btn_ask_ai: "Ask AI / पूछें",
    btn_listen_audio: "Listen Voice Audio / आवाज सुनें",
    lbl_followups: "आगे पूछें (Suggested Follow-ups):",
    panel_weather_title: "7-दिवसीय मौसम व छिड़काव पूर्वानुमान",
    panel_weather_sub: "उपग्रह डेटा व छिड़काव रेटिंग",
    panel_mandi_title: "स्थानीय कृषि उपज मंडी भाव",
    panel_mandi_sub: "दैनिक मंडी भाव व 7-दिवसीय रुझान",
    th_commodity: "Commodity / फसल",
    th_market: "Market / मंडी",
    th_rate: "Modal Rate (₹/Qtl)",
    th_trend: "7-Day Trend",
    panel_sb_title: "कृषि क्लाउड सिंक व प्रणाली स्थिति",
    panel_sb_sub: "डेटाबेस हमेशा सुरक्षित और लाइव सिंक रहता है",
    panel_activity_title: "हाल ही में दर्ज की गई गतिविधियाँ",
    panel_activity_sub: "क्लाउड में दर्ज फसल व रोग जांच रिकॉर्ड",
    make_default_title: "Set as my default language",
    make_default_sub: "(Don't ask on startup, can switch anytime in top bar)",
    btn_continue: "✓ Continue to Farm Advisory / आगे बढ़ें ➔"
  },
  en: {
    code: "en",
    name: "English",
    flag: "🇬🇧",
    speechCode: "en-IN",
    brand_tagline: "AI-Powered Hyper-Local Crop Advisory & Diagnostics",
    supabase_sync: "Live Cloud Sync Active",
    live_mandi_label: "LIVE APMC MANDI",
    hero_headline: "Smart Farming Advisory Backed by Scientific Evidence",
    hero_sub: "Analyzes your soil nutrients and live satellite weather to recommend the best crops and remedies in clear language.",
    btn_detect_location: "📍 Detect My Farm Location (GPS)",
    quick_hubs_label: "Quick Regional Soil Hubs:",
    lbl_temperature: "Temperature",
    lbl_humidity: "Humidity",
    lbl_rain7d: "7-Day Rain",
    tab_advisory: "Crop Advisory",
    tab_doctor: "Plant Doctor",
    tab_voice: "Voice Saathi",
    tab_mandi: "Mandi & Weather Radar",
    tab_supabase: "Cloud Sync & Status",
    panel_soil_title: "Farm Parameters & Soil Health",
    panel_soil_sub: "Load Soil Health Card or enter parameters manually",
    lbl_state: "State",
    lbl_district: "District",
    lbl_n: "Nitrogen (N) kg/ha",
    lbl_p: "Phosphorus (P) kg/ha",
    lbl_k: "Potassium (K) kg/ha",
    lbl_ph: "Soil pH Level",
    lbl_irrigation: "Irrigation Facility",
    lbl_farmsize: "Farm Size (Acres)",
    lbl_prevcrop: "Previous Season Crop",
    btn_run_advisory: "🌱 Analyze Land & Recommend Crops",
    panel_recs_title: "Top Recommended Crops for Your Land",
    panel_recs_sub: "Ranked by soil fertility, live weather, and APMC market prices",
    badge_best_match: "#1 BEST MATCH",
    lbl_match: "Match",
    pillar_soil: "Soil Fit",
    pillar_weather: "Weather Fit",
    pillar_market: "Market Fit",
    pillar_rotation: "Rotation Fit",
    lbl_yield: "Est. Yield",
    lbl_revenue: "Est. Revenue",
    lbl_rate: "Mandi Rate",
    lbl_sowing: "Sowing Window",
    shap_title: "🌱 Why this crop is best for your land",
    shap_tag: "Soil & Climate Fit Factor",
    runners_title: "Alternative Crops",
    panel_doctor_title: "Plant Pathology & Leaf Disease AI",
    panel_doctor_sub: "Select sample leaf pathogen or test diagnosis",
    leaf_gallery_title: "Sample Crop Pathogens (Click to Test):",
    dropzone_title: "Drag & Drop Crop Photo or Click to Browse",
    dropzone_sub: "Supports Tomato, Potato, Cotton, Wheat, Rice, Corn, Apple",
    btn_run_diagnosis: "Run Instant AI Pathology Diagnosis",
    panel_diag_title: "Diagnostic Scan Report",
    panel_diag_sub: "Zero-budget organic + Scientific chemical remedies",
    spray_alert_title: "🌦️ Weather-Grounded Spray Timing",
    remedy_organic_badge: "🌿 100% Organic Treatment",
    remedy_chemical_badge: "🧪 Scientific Chemical Treatment",
    voice_hero_title: "Voice Saathi — AI Farmer Advisor",
    voice_hero_sub: "Speaks clear, practical farming instructions in your language.",
    voice_chips_label: "Quick Farming Questions:",
    chip_water: "How much irrigation? (Water)",
    chip_fertilizer: "Fertilizer dosage? (NPK)",
    chip_mandi: "What is Mandi Price? (Rates)",
    chip_pest: "Pest & Fungus Control? (Remedies)",
    btn_ask_ai: "Ask AI",
    btn_listen_audio: "Listen Voice Audio",
    lbl_followups: "Suggested Follow-ups:",
    panel_weather_title: "7-Day Agricultural Weather Forecast",
    panel_weather_sub: "Live Satellite Feed + Spray Conditions",
    panel_mandi_title: "Live APMC Mandi Commodities",
    panel_mandi_sub: "Verified market arrivals & 7-day price trends",
    th_commodity: "Commodity",
    th_market: "Market",
    th_rate: "Modal Rate (₹/Qtl)",
    th_trend: "7-Day Trend",
    panel_sb_title: "Live Agricultural Cloud Sync & Status",
    panel_sb_sub: "Real-time records and secure synchronization",
    panel_activity_title: "Recent Farm Advisory Activity",
    panel_activity_sub: "Saved crop and disease diagnostic queries",
    make_default_title: "Set as my default language",
    make_default_sub: "(Don't ask on startup, can switch anytime in top bar)",
    btn_continue: "✓ Continue to Farm Advisory ➔"
  },
  mr: {
    code: "mr",
    name: "मराठी",
    flag: "🚩",
    speechCode: "mr-IN",
    brand_tagline: "एआय आधारित सूक्ष्म-हवामान पीक सल्ला व रोग निदान",
    supabase_sync: "थेट क्लाउड सिंक सुरू आहे",
    live_mandi_label: "थेट बाजार भाव",
    hero_headline: "शास्त्रीय पुराव्यांवर आधारित स्मार्ट शेती सल्ला",
    hero_sub: "तुमच्या मातीचे घटक व उपग्रह हवामानाचे विश्लेषण करून मराठीत अचूक पीक व कीड मार्गदर्शन.",
    btn_detect_location: "📍 माझे शेत शोधा (GPS)",
    quick_hubs_label: "प्रमुख शेती विभाग व मातीचे प्रकार:",
    lbl_temperature: "तापमान",
    lbl_humidity: "हवेतील आर्द्रता",
    lbl_rain7d: "७-दिवसांचा पाऊस",
    tab_advisory: "पीक सल्ला",
    tab_doctor: "पीक डॉक्टर",
    tab_voice: "व्हॉइस साथी",
    tab_mandi: "बाजार भाव व हवामान",
    tab_supabase: "क्लाउड स्थिती",
    panel_soil_title: "शेताचा तपशील व माती परीक्षण",
    panel_soil_sub: "मृदा आरोग्य पत्रिका लोड करा किंवा माहिती भरा",
    lbl_state: "राज्य",
    lbl_district: "जिल्हा",
    lbl_n: "नायट्रोजन (N) किलो/हेक्टर",
    lbl_p: "फॉस्फरस (P) किलो/हेक्टर",
    lbl_k: "पोटॅश (K) किलो/हेक्टर",
    lbl_ph: "मातीचा सामू (pH)",
    lbl_irrigation: "सिंचन सुविधा",
    lbl_farmsize: "शेताचे क्षेत्र (एकर)",
    lbl_prevcrop: "मागील हंगामातील पीक",
    btn_run_advisory: "🌱 शेताचे विश्लेषण करा व पीक सल्ला मिळवा",
    panel_recs_title: "शिफारस केलेली सर्वोत्तम पिके",
    panel_recs_sub: "माती, हवामान आणि बाजार भावावर आधारित क्रमवारी",
    badge_best_match: "#1 सर्वोत्तम पीक",
    lbl_match: "अचूकता",
    pillar_soil: "माती अनुकूलता",
    pillar_weather: "हवामान",
    pillar_market: "बाजार भाव",
    pillar_rotation: "पीक फेरपालट",
    lbl_yield: "अंदाजे उत्पादन",
    lbl_revenue: "अंदाजे उत्पन्न",
    lbl_rate: "बाजार भाव",
    lbl_sowing: "पेरणीची वेळ",
    shap_title: "🌱 हे पीक तुमच्या शेतासाठी सर्वोत्तम का आहे?",
    shap_tag: "पोषक घटक व हवामान अनुकूलता",
    runners_title: "पर्यायी पिके",
    panel_doctor_title: "झाडांचे रोग निदान व पान स्कॅनर",
    panel_doctor_sub: "पानाचा नमुना निवडा किंवा रोगाचे त्वरित विश्लेषण करा",
    leaf_gallery_title: "चाचणीसाठी पानांचे नमुने:",
    dropzone_title: "शेतातील पानाचा फोटो येथे टाका",
    dropzone_sub: "टोमॅटो, बटाटा, कापूस, गहू, भात, मका इत्यादींसाठी",
    btn_run_diagnosis: "रोग निदान सुरू करा",
    panel_diag_title: "रोग निदान अहवाल व उपाय",
    panel_diag_sub: "सेंद्रिय व रासायनिक उपाय आणि योग्य फवारणी वेळ",
    spray_alert_title: "🌦️ हवामानानुसार फवारणी सल्ला",
    remedy_organic_badge: "🌿 १००% सेंद्रिय उपचार",
    remedy_chemical_badge: "🧪 रासायनिक उपचार",
    voice_hero_title: "व्हॉइस साथी — तुमचा शेती मित्र",
    voice_hero_sub: "मराठीत बोलून अचूक शेती मार्गदर्शन मिळवा.",
    voice_chips_label: "नेहमी विचारले जाणारे प्रश्न:",
    chip_water: "पाणी किती द्यावे? (सिंचन)",
    chip_fertilizer: "खतांची मात्रा? (NPK)",
    chip_mandi: "बाजार भाव काय आहे? (मंडी)",
    chip_pest: "कीड नियंत्रण कसे करावे?",
    btn_ask_ai: "विचारा",
    btn_listen_audio: "आवाज ऐका",
    lbl_followups: "पुढील प्रश्न:",
    panel_weather_title: "७ दिवसांचा हवामान अंदाज",
    panel_weather_sub: "उपग्रह डेटा व फवारणी वेळ",
    panel_mandi_title: "बाजार समितीचे थेट भाव",
    panel_mandi_sub: "दैनिक बाजार आवक व कल",
    th_commodity: "पीक",
    th_market: "बाजार",
    th_rate: "सरासरी भाव (₹/क्विंटल)",
    th_trend: "७ दिवसांचा कल",
    panel_sb_title: "क्लाउड डेटा सिंक व स्थिती",
    panel_sb_sub: "डेटा सुरक्षित व अद्ययावत राहतो",
    panel_activity_title: "नोंदवलेली माहिती",
    panel_activity_sub: "पीक व रोग तपासणी नोंदी",
    make_default_title: "ही माझी पूर्वनिर्धारित भाषा करा",
    make_default_sub: "(दरवेळी विचारू नका)",
    btn_continue: "✓ पुढे जा ➔"
  },
  pa: {
    code: "pa",
    name: "ਪੰਜਾਬੀ",
    flag: "🌾",
    speechCode: "pa-IN",
    brand_tagline: "ਏਆਈ ਅਧਾਰਤ ਮਾਈਕ੍ਰੋ-ਕਲਾਈਮੇਟ ਫਸਲ ਸਲਾਹ ਤੇ ਬਿਮਾਰੀ ਜਾਂਚ",
    supabase_sync: "ਲਾਈਵ ਕਲਾਊਡ ਸਿੰਕ ਐਕਟਿਵ",
    live_mandi_label: "ਲਾਈਵ ਮੰਡੀ ਭਾਅ",
    hero_headline: "ਵਿਗਿਆਨਕ ਸਬੂਤਾਂ 'ਤੇ ਆਧਾਰਿਤ ਸਮਾਰਟ ਖੇਤੀ ਸਲਾਹ",
    hero_sub: "ਮਿੱਟੀ ਦੇ ਪੋਸ਼ਕ ਤੱਤਾਂ ਅਤੇ ਮੌਸਮ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਕੇ ਪੰਜਾਬੀ ਵਿੱਚ ਸਹੀ ਫਸਲ ਤੇ ਕੀੜੇ-ਮਕੌੜਿਆਂ ਦੀ ਰੋਕਥਾਮ ਦੀ ਸਲਾਹ।",
    btn_detect_location: "📍 ਮੇਰਾ ਖੇਤ ਲੱਭੋ (GPS)",
    quick_hubs_label: "ਮੁੱਖ ਖੇਤੀ ਖੇਤਰ ਅਤੇ ਮਿੱਟੀ ਦੀਆਂ ਕਿਸਮਾਂ:",
    lbl_temperature: "ਤਾਪਮਾਨ",
    lbl_humidity: "ਨਮੀ",
    lbl_rain7d: "7-ਦਿਨਾਂ ਦਾ ਮੀਂਹ",
    tab_advisory: "ਫਸਲ ਸਲਾਹ",
    tab_doctor: "ਫਸਲ ਡਾਕਟਰ",
    tab_voice: "ਵਾਇਸ ਸਾਥੀ",
    tab_mandi: "ਮੰਡੀ ਭਾਅ",
    tab_supabase: "ਕਲਾਊਡ ਸਥਿਤੀ",
    panel_soil_title: "ਖੇਤ ਦਾ ਵੇਰਵਾ ਤੇ ਮਿੱਟੀ ਪਰਖ",
    panel_soil_sub: "ਸੋਇਲ ਹੈਲਥ ਕਾਰਡ ਲੋਡ ਕਰੋ ਜਾਂ ਵੇਰਵੇ ਭਰੋ",
    lbl_state: "ਰਾਜ",
    lbl_district: "ਜ਼ਿਲ੍ਹਾ",
    lbl_n: "ਨਾਈਟ੍ਰੋਜਨ (N) ਕਿਲੋ/ਹੈਕਟੇਅਰ",
    lbl_p: "ਫਾਸਫੋਰਸ (P) ਕਿਲੋ/ਹੈਕਟੇਅਰ",
    lbl_k: "ਪੋਟਾਸ਼ (K) ਕਿਲੋ/ਹੈਕਟੇਅਰ",
    lbl_ph: "ਮਿੱਟੀ ਦਾ pH",
    lbl_irrigation: "ਸਿੰਚਾਈ ਸਾਧਨ",
    lbl_farmsize: "ਖੇਤ ਦਾ ਰਕਬਾ (ਏਕੜ)",
    lbl_prevcrop: "ਪਿਛਲੇ ਸੀਜ਼ਨ ਦੀ ਫਸਲ",
    btn_run_advisory: "🌱 ਖੇਤ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੋ ਤੇ ਫਸਲ ਸਲਾਹ ਲਵੋ",
    panel_recs_title: "ਸਭ ਤੋਂ ਵਧੀਆ ਸਿਫਾਰਸ਼ ਕੀਤੀਆਂ ਫਸਲਾਂ",
    panel_recs_sub: "ਮਿੱਟੀ, ਮੌਸਮ ਅਤੇ ਮੰਡੀ ਭਾਅ ਅਨੁਸਾਰ",
    badge_best_match: "#1 ਸਭ ਤੋਂ ਵਧੀਆ",
    lbl_match: "ਸਟੀਕਤਾ",
    pillar_soil: "ਮਿੱਟੀ ਅਨੁਕੂਲਤਾ",
    pillar_weather: "ਮੌਸਮ",
    pillar_market: "ਮੰਡੀ ਭਾਅ",
    pillar_rotation: "ਫਸਲੀ ਚੱਕਰ",
    lbl_yield: "ਅੰਦਾਜ਼ਨ ਝਾੜ",
    lbl_revenue: "ਅੰਦਾਜ਼ਨ ਕਮਾਈ",
    lbl_rate: "ਮੰਡੀ ਰੇਟ",
    lbl_sowing: "ਬਿਜਾਈ ਸਮਾਂ",
    shap_title: "🌱 ਇਹ ਫਸਲ ਤੁਹਾਡੇ ਖੇਤ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਕਿਉਂ ਹੈ?",
    shap_tag: "ਪੋਸ਼ਕ ਤੱਤ ਤੇ ਮੌਸਮ ਅਨੁਕੂਲਤਾ",
    runners_title: "ਹੋਰ ਬਦਲਵੀਆਂ ਫਸਲਾਂ",
    panel_doctor_title: "ਫਸਲ ਬਿਮਾਰੀ ਜਾਂਚ ਤੇ ਪੱਤਾ ਸਕੈਨਰ",
    panel_doctor_sub: "ਪੱਤੇ ਦੀ ਫੋਟੋ ਲਗਾਓ ਜਾਂ ਬਿਮਾਰੀ ਦੀ ਜਾਂਚ ਕਰੋ",
    leaf_gallery_title: "ਜਾਂਚ ਲਈ ਪੱਤਿਆਂ ਦੇ ਨਮੂਨੇ:",
    dropzone_title: "ਪੱਤੇ ਦੀ ਫੋਟੋ ਇੱਥੇ ਅੱਪਲੋਡ ਕਰੋ",
    dropzone_sub: "ਟਮਾਟਰ, ਆਲੂ, ਕਪਾਹ, ਕਣਕ, ਝੋਨਾ, ਮੱਕੀ ਲਈ",
    btn_run_diagnosis: "ਬਿਮਾਰੀ ਦੀ ਜਾਂਚ ਸ਼ੁਰੂ ਕਰੋ",
    panel_diag_title: "ਬਿਮਾਰੀ ਰਿਪੋਰਟ ਤੇ ਇਲਾਜ",
    panel_diag_sub: "ਜੈਵਿਕ ਤੇ ਰਸਾਇਣਕ ਹੱਲ ਅਤੇ ਸਪਰੇਅ ਦਾ ਸਹੀ ਸਮਾਂ",
    spray_alert_title: "🌦️ ਮੌਸਮ ਅਨੁਸਾਰ ਸਪਰੇਅ ਸਲਾਹ",
    remedy_organic_badge: "🌿 100% ਕੁਦਰਤੀ ਇਲਾਜ",
    remedy_chemical_badge: "🧪 ਰਸਾਇਣਕ ਇਲਾਜ",
    voice_hero_title: "ਵਾਇਸ ਸਾਥੀ — ਤੁਹਾਡਾ ਆਪਣਾ ਖੇਤੀ ਮਿੱਤਰ",
    voice_hero_sub: "ਪੰਜਾਬੀ ਵਿੱਚ ਬੋਲ ਕੇ ਸਵਾਲ ਪੁੱਛੋ ਤੇ ਸਲਾਹ ਪ੍ਰਾਪਤ ਕਰੋ।",
    voice_chips_label: "ਆਮ ਪੁੱਛੇ ਜਾਣ ਵਾਲੇ ਸਵਾਲ:",
    chip_water: "ਪਾਣੀ ਕਿੰਨਾ ਲਾਉਣਾ ਹੈ?",
    chip_fertilizer: "ਖਾਦ ਦੀ ਮਾਤਰਾ?",
    chip_mandi: "ਮੰਡੀ ਦਾ ਭਾਅ ਕੀ ਹੈ?",
    chip_pest: "ਕੀੜੇ ਦੀ ਰੋਕਥਾਮ?",
    btn_ask_ai: "ਪੁੱਛੋ",
    btn_listen_audio: "ਆਵਾਜ਼ ਸੁਣੋ",
    lbl_followups: "ਹੋਰ ਸਵਾਲ:",
    panel_weather_title: "7 ਦਿਨਾਂ ਦਾ ਮੌਸਮ ਪੂਰਵ ਅਨੁਮਾਨ",
    panel_weather_sub: "ਸੈਟੇਲਾਈਟ ਡਾਟਾ ਤੇ ਸਪਰੇਅ ਹਾਲਤਾਂ",
    panel_mandi_title: "ਮੰਡੀ ਦੇ ਤਾਜ਼ਾ ਭਾਅ",
    panel_mandi_sub: "ਰੋਜ਼ਾਨਾ ਮੰਡੀ ਆਮਦ ਤੇ ਰੁਝਾਨ",
    th_commodity: "ਫਸਲ",
    th_market: "ਮੰਡੀ",
    th_rate: "ਔਸਤ ਰੇਟ (₹/ਕੁਇੰਟਲ)",
    th_trend: "7 ਦਿਨਾਂ ਦਾ ਰੁਝਾਨ",
    panel_sb_title: "ਕਲਾਊਡ ਡਾਟਾ ਸਿੰਕ",
    panel_sb_sub: "ਡਾਟਾਬੇਸ ਹਮੇਸ਼ਾ ਐਕਟਿਵ ਰਹਿੰਦਾ ਹੈ",
    panel_activity_title: "ਤਾਜ਼ਾ ਗਤੀਵਿਧੀਆਂ",
    panel_activity_sub: "ਕਲਾਊਡ ਵਿੱਚ ਸੇਵ ਹੋਏ ਰਿਕਾਰਡ",
    make_default_title: "ਇਸ ਨੂੰ ਮੇਰੀ ਡਿਫਾਲਟ ਭਾਸ਼ਾ ਬਣਾਓ",
    make_default_sub: "(ਅਗਲੀ ਵਾਰ ਸਿੱਧਾ ਇਸੇ ਵਿੱਚ ਖੁੱਲ੍ਹੇਗਾ)",
    btn_continue: "✓ ਅੱਗੇ ਵਧੋ ➔"
  },
  te: {
    code: "te",
    name: "తెలుగు",
    flag: "🌶️",
    speechCode: "te-IN",
    brand_tagline: "ఏఐ ఆధారిత సూక్ష్మ వాతావరణ పంట సలహా మరియు వ్యాధి నిర్ధారణ",
    supabase_sync: "లైవ్ క్లౌడ్ సింక్ యాక్టివ్",
    live_mandi_label: "లైవ్ మార్కెట్ ధరలు",
    hero_headline: "శాస్త్రీయ ఆధారాలతో కూడిన స్మార్ట్ వ్యవసాయ సలహా",
    hero_sub: "మీ నేల పోషకాలు మరియు ఉపగ్రహ వాతావరణాన్ని విశ్లేషించి తెలుగులో సరైన పంట సలహాలు.",
    btn_detect_location: "📍 నా పొలం లొకేషన్ గుర్తించు (GPS)",
    quick_hubs_label: "ప్రాంతీయ వ్యవసాయ కేంద్రాలు మరియు నేల రకాలు:",
    lbl_temperature: "ఉష్ణోగ్రత",
    lbl_humidity: "తేమ",
    lbl_rain7d: "7 రోజుల వర్షం",
    tab_advisory: "పంట సలహా",
    tab_doctor: "మొక్కల డాక్టర్",
    tab_voice: "వాయిస్ సాథీ",
    tab_mandi: "మార్కెట్ ధరలు",
    tab_supabase: "సిస్టమ్ స్థితి",
    panel_soil_title: "పొలం వివరాలు మరియు నేల పరీక్ష",
    panel_soil_sub: "సాయిల్ హెల్త్ కార్డ్ లోడ్ చేయండి లేదా వివరాలు నమోదు చేయండి",
    lbl_state: "రాష్ట్రం",
    lbl_district: "జిల్లా",
    lbl_n: "నత్రజని (N) కేజీ/హెక్టారు",
    lbl_p: "భాస్వరం (P) కేజీ/హెక్టారు",
    lbl_k: "పొటాష్ (K) కేజీ/హెక్టారు",
    lbl_ph: "నేల pH విలువ",
    lbl_irrigation: "నీటిపారుదల సదుపాయం",
    lbl_farmsize: "పొలం పరిమాణం (ఎకరాలు)",
    lbl_prevcrop: "గత పంట",
    btn_run_advisory: "🌱 నేలను విశ్లేషించి పంట సలహా పొందండి",
    panel_recs_title: "సిఫార్సు చేయబడిన ఉత్తమ పంటలు",
    panel_recs_sub: "నేల సారం, వాతావరణం మరియు మార్కెట్ ధరల ఆధారంగా",
    badge_best_match: "#1 ఉత్తమ పంట",
    lbl_match: "ఖచ్చితత్వం",
    pillar_soil: "నేల అనుకూలత",
    pillar_weather: "వాతావరణం",
    pillar_market: "మార్కెట్ ధర",
    pillar_rotation: "పంట మార్పిడి",
    lbl_yield: "అంచనా దిగుబడి",
    lbl_revenue: "అంచనా ఆదాయం",
    lbl_rate: "మార్కెట్ ధర",
    lbl_sowing: "విత్తే సమయం",
    shap_title: "🌱 ఈ పంట మీ పొలానికి ఎందుకు ఉత్తమమైనది?",
    shap_tag: "పోషకాలు మరియు వాతావరణ అనుకూలత",
    runners_title: "ప్రత్యామ్నాయ పంటలు",
    panel_doctor_title: "మొక్కల వ్యాధి నిర్ధారణ మరియు ఆకు స్కానర్",
    panel_doctor_sub: "ఆకు ఫోటోను ఎంచుకోండి లేదా రోగ నిర్ధారణ చేయండి",
    leaf_gallery_title: "పరీక్ష కోసం ఆకుల నమూనాలు:",
    dropzone_title: "ఆకు ఫోటోను ఇక్కడ అప్‌లోడ్ చేయండి",
    dropzone_sub: "టమోటా, బంగాళాదుంప, పత్తి, వరి, మొక్కజొన్న మొదలైనవి",
    btn_run_diagnosis: "వ్యాధి నిర్ధారణ ప్రారంభించండి",
    panel_diag_title: "వ్యాధి నివేదిక మరియు నివారణ",
    panel_diag_sub: "సేంద్రీయ మరియు రసాయన నివారణ చర్యలు",
    spray_alert_title: "🌦️ వాతావరణ ఆధారిత స్ప్రే సలహా",
    remedy_organic_badge: "🌿 100% సేంద్రీయ నివారణ",
    remedy_chemical_badge: "🧪 రసాయన నివారణ",
    voice_hero_title: "వాయిస్ సాథీ — మీ వ్యవసాయ మిత్రుడు",
    voice_hero_sub: "తెలుగులో మాట్లాడి సరైన వ్యవసాయ సలహాలు పొందండి.",
    voice_chips_label: "తరచుగా అడిగే ప్రశ్నలు:",
    chip_water: "నీరు ఎంత అవసరం?",
    chip_fertilizer: "ఎరువుల మోతాదు?",
    chip_mandi: "మార్కెట్ ధర ఎంత?",
    chip_pest: "పురుగు నివారణ ఎలా?",
    btn_ask_ai: "అడగండి",
    btn_listen_audio: "వాయిస్ వినండి",
    lbl_followups: "తదుపరి ప్రశ్నలు:",
    panel_weather_title: "7 రోజుల వాతావరణ సూచన",
    panel_weather_sub: "ఉపగ్రహ సమాచారం మరియు స్ప్రే పరిస్థితులు",
    panel_mandi_title: "తాజా మార్కెట్ ధరలు",
    panel_mandi_sub: "రోజువారీ మార్కెట్ రాబడులు",
    th_commodity: "పంట",
    th_market: "మార్కెట్",
    th_rate: "సగటు ధర (₹/క్వింటాల్)",
    th_trend: "7 రోజుల ధోరణి",
    panel_sb_title: "క్లౌడ్ డేటా సింక్",
    panel_sb_sub: "డేటాబేస్ ఎల్లప్పుడూ సక్రియంగా ఉంటుంది",
    panel_activity_title: "ఇటీవలి కార్యకలాపాలు",
    panel_activity_sub: "క్లౌడ్‌లో భద్రపరచబడిన రికార్డులు",
    make_default_title: "దీన్ని నా ప్రామాణిక భాషగా సెట్ చేయండి",
    make_default_sub: "(తదుపరిసారి నేరుగా ఇందులో ఓపెన్ అవుతుంది)",
    btn_continue: "✓ కొనసాగించండి ➔"
  },
  ta: {
    code: "ta",
    name: "தமிழ்",
    flag: "🌴",
    speechCode: "ta-IN",
    brand_tagline: "செயற்கை நுண்ணறிவு அடிப்படையிலான பயிர் ஆலோசனை மற்றும் நோய் கண்டறிதல்",
    supabase_sync: "நேரடி கிளவுட் ஒத்திசைவு",
    live_mandi_label: "சந்தை விலை நிலவரம்",
    hero_headline: "அறிவியல் ஆதாரங்களுடன் கூடிய ஸ்மார்ட் விவசாய ஆலோசனை",
    hero_sub: "உங்கள் மண் ஊட்டச்சத்துக்கள் மற்றும் வானிலையை பகுப்பாய்வு செய்து தமிழில் சிறந்த ஆலோசனை.",
    btn_detect_location: "📍 எனது பண்ணை இருப்பிடத்தை கண்டறி (GPS)",
    quick_hubs_label: "மண் மற்றும் வேளாண் மண்டலங்கள்:",
    lbl_temperature: "வெப்பநிலை",
    lbl_humidity: "ஈரப்பதம்",
    lbl_rain7d: "7-நாள் மழை",
    tab_advisory: "பயிர் ஆலோசனை",
    tab_doctor: "பயிர் மருத்துவர்",
    tab_voice: "வாய்ஸ் சாதி",
    tab_mandi: "சந்தை நிலவரம்",
    tab_supabase: "கிளவுட் நிலை",
    panel_soil_title: "நில விவரங்கள் மற்றும் மண் பரிசோதனை",
    panel_soil_sub: "மண் வள அட்டை ஏற்றவும் அல்லது விவரங்களை உள்ளிடவும்",
    lbl_state: "மாநிலம்",
    lbl_district: "மாவட்டம்",
    lbl_n: "நைட்ரஜன் (N) கிலோ/ஹெக்டேர்",
    lbl_p: "பாஸ்பரஸ் (P) கிலோ/ஹெக்டேர்",
    lbl_k: "பொட்டாஷ் (K) கிலோ/ஹெக்டேர்",
    lbl_ph: "மண் pH அளவு",
    lbl_irrigation: "பாசன வசதி",
    lbl_farmsize: "பண்ணை அளவு (ஏக்கர்)",
    lbl_prevcrop: "முந்தைய பயிர்",
    btn_run_advisory: "🌱 நிலத்தை பகுப்பாய்வு செய்து பயிர் ஆலோசனை பெறுங்கள்",
    panel_recs_title: "பரிந்துரைக்கப்படும் சிறந்த பயிர்கள்",
    panel_recs_sub: "மண் வளம் மற்றும் சந்தை விலையின் அடிப்படையில்",
    badge_best_match: "#1 சிறந்த தேர்வு",
    lbl_match: "பொருத்தம்",
    pillar_soil: "மண் பொருத்தம்",
    pillar_weather: "வானிலை",
    pillar_market: "சந்தை விலை",
    pillar_rotation: "பயிர் சுழற்சி",
    lbl_yield: "எதிர்பார்க்கப்படும் மகசூல்",
    lbl_revenue: "எதிர்பார்க்கப்படும் வருமானம்",
    lbl_rate: "சந்தை விலை",
    lbl_sowing: "விதைப்பு காலம்",
    shap_title: "🌱 இந்த பயிர் உங்கள் நிலத்திற்கு ஏன் சிறந்தது?",
    shap_tag: "ஊட்டச்சத்து மற்றும் வானிலை பொருத்தம்",
    runners_title: "மாற்று பயிர்கள்",
    panel_doctor_title: "பயிர் நோய் கண்டறிதல் மற்றும் இலை ஸ்கேனர்",
    panel_doctor_sub: "இலை படத்தை தேர்ந்தெடுத்து உடனடியாக நோய் கண்டறியவும்",
    leaf_gallery_title: "பரிசோதனைக்கான இலை மாதிரிகள்:",
    dropzone_title: "இலை புகைப்படத்தை பதிவேற்றவும்",
    dropzone_sub: "தக்காளி, உருளைக்கிழங்கு, பருத்தி, நெல், சோளம் போன்றவற்றிற்கு",
    btn_run_diagnosis: "நோய் கண்டறிதலை தொடங்கு",
    panel_diag_title: "நோய் கண்டறிதல் அறிக்கை மற்றும் தீர்வு",
    panel_diag_sub: "இயற்கை மற்றும் ரசாயன சிகிச்சை முறைகள்",
    spray_alert_title: "🌦️ வானிலை அடிப்படையிலான தெளிப்பு ஆலோசனை",
    remedy_organic_badge: "🌿 100% இயற்கை மருத்துவம்",
    remedy_chemical_badge: "🧪 ரசாயன சிகிச்சை",
    voice_hero_title: "வாய்ஸ் சாதி — உங்கள் விவசாய நண்பன்",
    voice_hero_sub: "தமிழில் பேசி விவசாய ஆலோசனைகளை பெறுங்கள்.",
    voice_chips_label: "அடிக்கடி கேட்கப்படும் கேள்விகள்:",
    chip_water: "பாசனம் எவ்வளவு தேவை?",
    chip_fertilizer: "உர அளவு என்ன?",
    chip_mandi: "சந்தை விலை என்ன?",
    chip_pest: "பூச்சி கட்டுப்பாடு எப்படி?",
    btn_ask_ai: "கேளுங்கள்",
    btn_listen_audio: "குரலைக் கேளுங்கள்",
    lbl_followups: "அடுத்த கேள்விகள்:",
    panel_weather_title: "7 நாள் வானிலை முன்னறிவிப்பு",
    panel_weather_sub: "செயற்கைக்கோள் தரவு மற்றும் தெளிப்பு சூழல்",
    panel_mandi_title: "நேரடி சந்தை விலை",
    panel_mandi_sub: "தினசரி சந்தை வரத்து",
    th_commodity: "பயிர்",
    th_market: "சந்தை",
    th_rate: "சராசரி விலை (₹/குவிண்டால்)",
    th_trend: "7 நாள் போக்கு",
    panel_sb_title: "கிளவுட் தரவு ஒத்திசைவு",
    panel_sb_sub: "தரவுத்தளம் எப்போதும் செயல்பாட்டில் உள்ளது",
    panel_activity_title: "சமீபத்திய செயல்பாடுகள்",
    panel_activity_sub: "சேமிக்கப்பட்ட பதிவுகள்",
    make_default_title: "இதை எனது முதன்மை மொழியாக அமைக்கவும்",
    make_default_sub: "(அடுத்த முறை நேரடியாக இதில் திறக்கும்)",
    btn_continue: "✓ தொடரவும் ➔"
  },
  gu: {
    code: "gu",
    name: "ગુજરાતી",
    flag: "🥜",
    speechCode: "gu-IN",
    brand_tagline: "એઆઈ આધારિત સૂક્ષ્મ આબોહવા પાક સલાહ અને રોગ નિદાન",
    supabase_sync: "લાઈવ ક્લાઉડ સિંક સક્રિય",
    live_mandi_label: "લાઈવ માર્કેટ યાર્ડ ભાવ",
    hero_headline: "વૈજ્ઞાનિક પુરાવા આધારિત સ્માર્ટ ખેતી સલાહ",
    hero_sub: "તમારી જમીનના પોષક તત્વો અને હવામાનનું વિશ્લેષણ કરીને ગુજરાતીમાં સચોટ પાક માર્ગદર્શન.",
    btn_detect_location: "📍 મારું ખેતર સ્થાન શોધો (GPS)",
    quick_hubs_label: "મુખ્ય કૃષિ વિસ્તારો અને જમીનના પ્રકારો:",
    lbl_temperature: "તાપમાન",
    lbl_humidity: "ભેજ",
    lbl_rain7d: "૭ દિવસનો વરસાદ",
    tab_advisory: "પાક સલાહ",
    tab_doctor: "પાક ડૉક્ટર",
    tab_voice: "વોઇસ સાથી",
    tab_mandi: "બજાર ભાવ",
    tab_supabase: "સિસ્ટમ સ્થિતિ",
    panel_soil_title: "ખેતરની વિગતો અને જમીન ચકાસણી",
    panel_soil_sub: "સોઈલ હેલ્થ કાર્ડ લોડ કરો અથવા વિગતો ભરો",
    lbl_state: "રાજ્ય",
    lbl_district: "જિલ્લો",
    lbl_n: "નાઇટ્રોજન (N) કિગ્રા/હેક્ટર",
    lbl_p: "ફોસ્ફરસ (P) કિગ્રા/હેક્ટર",
    lbl_k: "પોટાશ (K) કિગ્રા/હેક્ટર",
    lbl_ph: "જમીનનો pH",
    lbl_irrigation: "પિયત સુવિધા",
    lbl_farmsize: "ખેતરનું કદ (એકર)",
    lbl_prevcrop: "પાછલા વર્ષનો પાક",
    btn_run_advisory: "🌱 જમીનનું વિશ્લેષણ કરો અને પાક સલાહ મેળવો",
    panel_recs_title: "ભલામણ કરેલ શ્રેષ્ઠ પાકો",
    panel_recs_sub: "જમીન, આબોહવા અને બજાર ભાવોના આધારે",
    badge_best_match: "#1 શ્રેષ્ઠ પાક",
    lbl_match: "સચોટતા",
    pillar_soil: "જમીન અનુકૂળતા",
    pillar_weather: "હવામાન",
    pillar_market: "બજાર ભાવ",
    pillar_rotation: "પાક ફેરબદલ",
    lbl_yield: "અંદાજિત ઉત્પાદન",
    lbl_revenue: "અંદાજિત આવક",
    lbl_rate: "બજાર ભાવ",
    lbl_sowing: "વાવણી સમય",
    shap_title: "🌱 આ પાક તમારા ખેતર માટે શા માટે ઉત્તમ છે?",
    shap_tag: "પોષક તત્વો અને આબોહવા અનુકૂળતા",
    runners_title: "વૈકલ્પિક પાકો",
    panel_doctor_title: "છોડના રોગનું નિદાન અને પાન સ્કેનર",
    panel_doctor_sub: "પાનનો ફોટો પસંદ કરો અને રોગનું નિદાન મેળવો",
    leaf_gallery_title: "પરીક્ષણ માટે પાનના નમૂના:",
    dropzone_title: "પાનનો ફોટો અહીં અપલોડ કરો",
    dropzone_sub: "ટામેટાં, બટાકા, કપાસ, ઘઉં, ડાંગર, મકાઈ માટે",
    btn_run_diagnosis: "રોગ નિદાન શરૂ કરો",
    panel_diag_title: "રોગ નિદાન રિપોર્ટ અને ઉપાય",
    panel_diag_sub: "કુદરતી અને રાસાયણિક ઉપાયો",
    spray_alert_title: "🌦️ હવામાન મુજબ છંટકાવ સલાહ",
    remedy_organic_badge: "🌿 ૧૦૦% કુદરતી ઉપચાર",
    remedy_chemical_badge: "🧪 રાસાયણિક ઉપચાર",
    voice_hero_title: "વોઇસ સાથી — તમારો ખેતી મિત્ર",
    voice_hero_sub: "ગુજરાતીમાં બોલીને સલાહ મેળવો.",
    voice_chips_label: "વારંવાર પૂછાતા પ્રશ્નો:",
    chip_water: "પાણી કેટલું આપવું?",
    chip_fertilizer: "ખાતરની માત્રા કેટલી?",
    chip_mandi: "બજાર ભાવ શું છે?",
    chip_pest: "જીવાત નિયંત્રણ કેવી રીતે કરવું?",
    btn_ask_ai: "પૂછો",
    btn_listen_audio: "અવાજ સાંભળો",
    lbl_followups: "આગળના પ્રશ્નો:",
    panel_weather_title: "૭ દિવસનું હવામાન પૂર્વાનુમાન",
    panel_weather_sub: "સેટેલાઇટ ડેટા અને છંટકાવ સ્થિતિ",
    panel_mandi_title: "માર્કેટ યાર્ડના તાજા ભાવો",
    panel_mandi_sub: "દૈનિક આવક અને ભાવ વલણ",
    th_commodity: "પાક",
    th_market: "યાર્ડ",
    th_rate: "સરેરાશ ભાવ (₹/ક્વિન્ટલ)",
    th_trend: "૭ દિવસનું વલણ",
    panel_sb_title: "ક્લાઉડ ડેટા સિંક",
    panel_sb_sub: "ડેટાબેઝ હંમેશા સક્રિય રહે છે",
    panel_activity_title: "તાજેતરની પ્રવૃત્તિઓ",
    panel_activity_sub: "ક્લાઉડમાં સંગ્રહિત વિગતો",
    make_default_title: "આને મારી ડિફૉલ્ટ ભાષા બનાવો",
    make_default_sub: "(આગલી વખતે સીધું આમાં જ ખૂલશે)",
    btn_continue: "✓ આગળ વધો ➔"
  },
  bn: {
    code: "bn",
    name: "বাংলা",
    flag: "🌾",
    speechCode: "bn-IN",
    brand_tagline: "কৃত্রিম বুদ্ধিমত্তা ভিত্তিক আবহাওয়া ও শস্য পরামর্শ",
    supabase_sync: "লাইভ ক্লাউড সিঙ্ক সক্রিয়",
    live_mandi_label: "লাইভ মান্ডি দর",
    hero_headline: "বৈজ্ঞানিক তথ্যের ওপর ভিত্তি করে স্মার্ট কৃষি পরামর্শ",
    hero_sub: "মাটির পুষ্টি উপাদান ও আবহাওয়া বিশ্লেষণ করে বাংলায় সঠিক শস্য ও রোগ নিরাময় পরামর্শ।",
    btn_detect_location: "📍 আমার খামার অবস্থান খুঁজুন (GPS)",
    quick_hubs_label: "প্রধান কৃষি অঞ্চল ও মাটির ধরন:",
    lbl_temperature: "তাপমাত্রা",
    lbl_humidity: "আর্দ্রতা",
    lbl_rain7d: "৭ দিনের বৃষ্টিপাত",
    tab_advisory: "শস্য পরামর্শ",
    tab_doctor: "শস্য ডাক্তার",
    tab_voice: "ভয়েস সাথী",
    tab_mandi: "বাজার দর",
    tab_supabase: "সিস্টেম স্থিতি",
    panel_soil_title: "জমির বিবরণ ও মাটি পরীক্ষা",
    panel_soil_sub: "সয়েল হেলথ কার্ড লোড করুন অথবা মান লিখুন",
    lbl_state: "রাজ্য",
    lbl_district: "জেলা",
    lbl_n: "নাইট্রোজেন (N) কেজি/হেক্টর",
    lbl_p: "ফসফরাস (P) কেজি/হেক্টর",
    lbl_k: "পটাশ (K) কেজি/হেক্টর",
    lbl_ph: "মাটির pH মাত্রা",
    lbl_irrigation: "সেচ সুবিধা",
    lbl_farmsize: "জমির আয়তন (একর)",
    lbl_prevcrop: "পূর্ববর্তী ফসল",
    btn_run_advisory: "🌱 জমি বিশ্লেষণ করুন ও শস্য পরামর্শ পান",
    panel_recs_title: "সুপারিশকৃত সেরা ফসলসমূহ",
    panel_recs_sub: "মাটির উর্বরতা ও বাজার দরের ভিত্তিতে",
    badge_best_match: "#১ সেরা ফসল",
    lbl_match: "নির্ভুলতা",
    pillar_soil: "মাটি উপযোগিতা",
    pillar_weather: "আবহাওয়া",
    pillar_market: "বাজার দর",
    pillar_rotation: "ফসল চক্র",
    lbl_yield: "আনুমানিক ফলন",
    lbl_revenue: "আনুমানিক আয়",
    lbl_rate: "বাজার দর",
    lbl_sowing: "বপনের সময়",
    shap_title: "🌱 কেন এই ফসলটি আপনার জমির জন্য সেরা?",
    shap_tag: "পুষ্টি ও আবহাওয়া উপযোগিতা",
    runners_title: "বিকল্প ফসলসমূহ",
    panel_doctor_title: "গাছের রোগ নির্ণয় ও পাতা স্ক্যানার",
    panel_doctor_sub: "পাতার নমুনা বেছে নিন বা সরাসরি রোগ নির্ণয় করুন",
    leaf_gallery_title: "পরীক্ষার জন্য পাতার নমুনা:",
    dropzone_title: "পাতার ছবি এখানে আপলোড করুন",
    dropzone_sub: "টমেটো, আলু, তুলা, গম, ধান, ভুট্টার জন্য",
    btn_run_diagnosis: "রোগ নির্ণয় শুরু করুন",
    panel_diag_title: "রোগ নির্ণয় রিপোর্ট ও প্রতিকার",
    panel_diag_sub: "জৈব ও রাসায়নিক প্রতিকার ব্যবস্থা",
    spray_alert_title: "🌦️ আবহাওয়া ভিত্তিক স্প্রে পরামর্শ",
    remedy_organic_badge: "🌿 ১০০% জৈব প্রতিকার",
    remedy_chemical_badge: "🧪 রাসায়নিক প্রতিকার",
    voice_hero_title: "ভয়েস সাথী — আপনার কৃষি বন্ধু",
    voice_hero_sub: "বাংলায় কথা বলে নির্ভুল পরামর্শ পান।",
    voice_chips_label: "সাধারণ প্রশ্নাবলী:",
    chip_water: "কতটা জল সেচ দিতে হবে?",
    chip_fertilizer: "সারের সঠিক মাত্রা?",
    chip_mandi: "বাজার দর কত চলছে?",
    chip_pest: "কীটপতঙ্গ দমন কীভাবে করবেন?",
    btn_ask_ai: "জিজ্ঞাসা করুন",
    btn_listen_audio: "ভয়েস শুনুন",
    lbl_followups: "পরবর্তী প্রশ্ন:",
    panel_weather_title: "৭ দিনের আবহাওয়া পূর্বাভাস",
    panel_weather_sub: "স্যাটেলাইট তথ্য ও স্প্রে পরিস্থিতি",
    panel_mandi_title: "তাজা মান্ডি বাজার দর",
    panel_mandi_sub: "দৈনিক শস্য আমদানি ও দর",
    th_commodity: "ফসল",
    th_market: "মান্ডি",
    th_rate: "গড় দর (₹/কুইন্টাল)",
    th_trend: "৭ দিনের ধারা",
    panel_sb_title: "ক্লাউড ডেটা সিঙ্ক",
    panel_sb_sub: "ডেটাবেস সর্বদা সক্রিয় থাকে",
    panel_activity_title: "সাম্প্রতিক কার্যকলাপ",
    panel_activity_sub: "সংরক্ষিত তথ্যসমূহ",
    make_default_title: "এটিকে আমার ডিফল্ট ভাষা হিসেবে সেট করুন",
    make_default_sub: "(পরের বার সরাসরি এই ভাষায় খুলবে)",
    btn_continue: "✓ এগিয়ে যান ➔"
  },
  kn: {
    code: "kn",
    name: "ಕನ್ನಡ",
    flag: "☕",
    speechCode: "kn-IN",
    brand_tagline: "ಎಐ ಆಧಾರಿತ ಬೆಳೆ ಸಲಹೆ ಮತ್ತು ರೋಗ ಪತ್ತೆ",
    supabase_sync: "ಲೈವ್ ಕ್ಲೌಡ್ ಸಿಂಕ್ ಸಕ್ರಿಯ",
    live_mandi_label: "ಲೈವ್ ಮಾರುಕಟ್ಟೆ ದರಗಳು",
    hero_headline: "ವೈಜ್ಞಾನಿಕ ಆಧಾರಿತ ಸ್ಮಾರ್ಟ್ ಕೃಷಿ ಸಲಹೆ",
    hero_sub: "ನಿಮ್ಮ ಮಣ್ಣಿನ ಪೋಷಕಾಂಶಗಳು ಮತ್ತು ಹವಾಮಾನವನ್ನು ವಿಶ್ಲೇಷಿಸಿ ಕನ್ನಡದಲ್ಲಿ ಸೂಕ್ತ ಬೆಳೆ ಮಾಹಿತಿ.",
    btn_detect_location: "📍 ನನ್ನ ಜಮೀನಿನ ಸ್ಥಳ ಪತ್ತೆ ಮಾಡಿ (GPS)",
    quick_hubs_label: "ಪ್ರಮುಖ ಕೃಷಿ ವಲಯಗಳು ಮತ್ತು ಮಣ್ಣಿನ ಪ್ರಕಾರಗಳು:",
    lbl_temperature: "ತಾಪಮಾನ",
    lbl_humidity: "ತೇವಾಂಶ",
    lbl_rain7d: "7-ದಿನಗಳ ಮಳೆ",
    tab_advisory: "ಬೆಳೆ ಸಲಹೆ",
    tab_doctor: "ಸಸ್ಯ ವೈದ್ಯ",
    tab_voice: "ವಾಯ್ಸ್ ಸಾಥಿ",
    tab_mandi: "ಮಾರುಕಟ್ಟೆ ದರ",
    tab_supabase: "ಕ್ಲೌಡ್ ಸ್ಥಿತಿ",
    panel_soil_title: "ಜಮೀನಿನ ವಿವರ ಮತ್ತು ಮಣ್ಣು ಪರೀಕ್ಷೆ",
    panel_soil_sub: "ಮಣ್ಣಿನ ಆರೋಗ್ಯ ಕಾರ್ಡ್ ಲೋಡ್ ಮಾಡಿ",
    lbl_state: "ರಾಜ್ಯ",
    lbl_district: "ಜಿಲ್ಲೆ",
    lbl_n: "ಸಾರಜನಕ (N) ಕೆಜಿ/ಹೆಕ್ಟೇರ್",
    lbl_p: "ರಂಜಕ (P) ಕೆಜಿ/ಹೆಕ್ಟೇರ್",
    lbl_k: "ಪೊಟ್ಯಾಶ್ (K) ಕೆಜಿ/ಹೆಕ್ಟೇರ್",
    lbl_ph: "ಮಣ್ಣಿನ pH ಮೌಲ್ಯ",
    lbl_irrigation: "ನೀರಾವರಿ ಸೌಲಭ್ಯ",
    lbl_farmsize: "ಜಮೀನಿನ ವಿಸ್ತೀರ್ಣ (ಎಕರೆ)",
    lbl_prevcrop: "ಹಿಂದಿನ ಬೆಳೆ",
    btn_run_advisory: "🌱 ಜಮೀನು ವಿಶ್ಲೇಷಿಸಿ ಬೆಳೆ ಸಲಹೆ ಪಡೆಯಿರಿ",
    panel_recs_title: "ಶಿಫಾರಸು ಮಾಡಿದ ಅತ್ಯುತ್ತಮ ಬೆಳೆಗಳು",
    panel_recs_sub: "ಮಣ್ಣಿನ ಫಲವತ್ತತೆ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ದರದ ಆಧಾರದ ಮೇಲೆ",
    badge_best_match: "#1 ಅತ್ಯುತ್ತಮ ಬೆಳೆ",
    lbl_match: "ಹೊಂದಾಣಿಕೆ",
    pillar_soil: "ಮಣ್ಣಿನ ಹೊಂದಾಣಿಕೆ",
    pillar_weather: "ಹವಾಮಾನ",
    pillar_market: "ಮಾರುಕಟ್ಟೆ ದರ",
    pillar_rotation: "ಬೆಳೆ ಪರಿವರ್ತನೆ",
    lbl_yield: "ನಿರೀಕ್ಷಿತ ಇಳುವರಿ",
    lbl_revenue: "ನಿರೀಕ್ಷಿತ ಆದಾಯ",
    lbl_rate: "ಮಾರುಕಟ್ಟೆ ದರ",
    lbl_sowing: "ಬಿತ್ತನೆ ಸಮಯ",
    shap_title: "🌱 ಈ ಬೆಳೆ ನಿಮ್ಮ ಜಮೀನಿಗೆ ಏಕೆ ಅತ್ಯುತ್ತಮವಾಗಿದೆ?",
    shap_tag: "ಪೋಷಕಾಂಶ ಮತ್ತು ಹವಾಮಾನ ಹೊಂದಾಣಿಕೆ",
    runners_title: "ಪರ್ಯಾಯ ಬೆಳೆಗಳು",
    panel_doctor_title: "ಸಸ್ಯ ರೋಗ ಪತ್ತೆ ಮತ್ತು ಎಲೆ ಸ್ಕ್ಯಾನರ್",
    panel_doctor_sub: "ಎಲೆಯ ಮಾದರಿಯನ್ನು ಆಯ್ಕೆಮಾಡಿ ರೋಗ ಪತ್ತೆ ಹಚ್ಚಿ",
    leaf_gallery_title: "ಪರೀಕ್ಷೆಗಾಗಿ ಎಲೆಗಳ ಮಾದರಿಗಳು:",
    dropzone_title: "ಎಲೆಯ ಫೋಟೋವನ್ನು ಇಲ್ಲಿ ಅಪ್ಲೋಡ್ ಮಾಡಿ",
    dropzone_sub: "ಟೊಮ್ಯಾಟೊ, ಆಲೂಗಡ್ಡೆ, ಹತ್ತಿ, ಗೋಧಿ, ಭತ್ತ, ಮೆಕ್ಕೆಜೋಳ ಇತ್ಯಾದಿಗಳಿಗೆ",
    btn_run_diagnosis: "ರೋಗ ಪತ್ತೆ ಆರಂಭಿಸಿ",
    panel_diag_title: "ರೋಗ ವರದಿ ಮತ್ತು ಪರಿಹಾರ",
    panel_diag_sub: "ನೈಸರ್ಗಿಕ ಮತ್ತು ರಾಸಾಯನಿಕ ಪರಿಹಾರ ಕ್ರಮಗಳು",
    spray_alert_title: "🌦️ ಹವಾಮಾನ ಆಧಾರಿತ ಸಿಂಪಡಣೆ ಸಲಹೆ",
    remedy_organic_badge: "🌿 100% ಸಾವಯವ ಚಿಕಿತ್ಸೆ",
    remedy_chemical_badge: "🧪 ರಾಸಾಯನಿಕ ಚಿಕಿತ್ಸೆ",
    voice_hero_title: "ವಾಯ್ಸ್ ಸಾಥಿ — ನಿಮ್ಮ ಕೃಷಿ ಮಿತ್ರ",
    voice_hero_sub: "ಕನ್ನಡದಲ್ಲಿ ಮಾತನಾಡಿ ಕೃಷಿ ಸಲಹೆಗಳನ್ನು ಪಡೆಯಿರಿ.",
    voice_chips_label: "ಸಾಮಾನ್ಯ ಪ್ರಶ್ನೆಗಳು:",
    chip_water: "ನೀರಾವರಿ ಎಷ್ಟು ಬೇಕು?",
    chip_fertilizer: "ಗೊಬ್ಬರದ ಪ್ರಮಾಣ ಎಷ್ಟು?",
    chip_mandi: "ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ಎಷ್ಟಿದೆ?",
    chip_pest: "ಕೀಟ ನಿಯಂತ್ರಣ ಹೇಗೆ?",
    btn_ask_ai: "ಕೇಳಿ",
    btn_listen_audio: "ಧ್ವನಿ ಆಲಿಸಿ",
    lbl_followups: "ಮುಂದಿನ ಪ್ರಶ್ನೆಗಳು:",
    panel_weather_title: "7 ದಿನಗಳ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ",
    panel_weather_sub: "ಉಪಗ್ರಹ ಮಾಹಿತಿ ಮತ್ತು ಸಿಂಪಡಣೆ ಪರಿಸ್ಥಿತಿ",
    panel_mandi_title: "ತಾಜಾ ಮಾರುಕಟ್ಟೆ ದರಗಳು",
    panel_mandi_sub: "ದೈನಂದಿನ ಮಾರುಕಟ್ಟೆ ದರ ವಿವರ",
    th_commodity: "ಬೆಳೆ",
    th_market: "ಮಾರುಕಟ್ಟೆ",
    th_rate: "ಸರಾಸರಿ ದರ (₹/ಕ್ವಿಂಟಾಲ್)",
    th_trend: "7 ದಿನಗಳ ಪ್ರವೃತ್ತಿ",
    panel_sb_title: "ಕ್ಲೌಡ್ ಡೇಟಾ ಸಿಂಕ್",
    panel_sb_sub: "ಡೇಟಾಬೇಸ್ ಸದಾ ಸಕ್ರಿಯವಾಗಿರುತ್ತದೆ",
    panel_activity_title: "ಇತ್ತೀಚಿನ ಚಟುವಟಿಕೆಗಳು",
    panel_activity_sub: "ಕ್ಲೌಡ್‌ನಲ್ಲಿ ಸಂಗ್ರಹಿಸಲಾದ ವಿವರಗಳು",
    make_default_title: "ಇದನ್ನು ನನ್ನ ಡೀಫಾಲ್ಟ್ ಭಾಷೆಯಾಗಿ ಹೊಂದಿಸಿ",
    make_default_sub: "(ಮುಂದಿನ ಬಾರಿ ನೇರವಾಗಿ ಇದರಲ್ಲಿ ತೆರೆಯುತ್ತದೆ)",
    btn_continue: "✓ ಮುಂದುವರಿಯಿರಿ ➔"
  },
  ml: {
    code: "ml",
    name: "മലയാളം",
    flag: "🥥",
    speechCode: "ml-IN",
    brand_tagline: "എഐ അധിഷ്ഠിത വിള ഉപദേശവും രോഗനിർണയവും",
    supabase_sync: "ലൈവ് ക്ലൗഡ് സമന്వയം സജീവം",
    live_mandi_label: "ലൈവ് മാർക്കറ്റ് നിരക്കുകൾ",
    hero_headline: "ശാസ്ത്രീയ അടിസ്ഥാനത്തിലുള്ള സ്മാർട്ട് കാർഷിക ഉപദേശം",
    hero_sub: "മണ്ണിലെ പോഷകങ്ങളും ഉപഗ്രഹ കാലാവസ്ഥയും വിശകലനം ചെയ്ത് മലയാളത്തിൽ മികച്ച കാർഷിക മാർഗ്ഗനിർദ്ദേശം.",
    btn_detect_location: "📍 എന്റെ കൃഷിസ്ഥലം കണ്ടെത്തുക (GPS)",
    quick_hubs_label: "കാർഷിക മേഖലകളും മണ്ണിന്റെ തരങ്ങളും:",
    lbl_temperature: "താപനില",
    lbl_humidity: "ഈർപ്പം",
    lbl_rain7d: "7-ദിവസത്തെ മഴ",
    tab_advisory: "വിള ഉപദേശം",
    tab_doctor: "സസ്യ ഡോക്ടർ",
    tab_voice: "വോയ്‌സ് സാഥി",
    tab_mandi: "മാർക്കറ്റ് നിരക്ക്",
    tab_supabase: "ക്ലൗഡ് നില",
    panel_soil_title: "കൃഷിയിട വിവരങ്ങളും മണ്ണ് പരിശോധനയും",
    panel_soil_sub: "സോയിൽ ഹെൽത്ത് കാർഡ് വിവരങ്ങൾ നൽകുക",
    lbl_state: "സംസ്ഥാനം",
    lbl_district: "ജില്ല",
    lbl_n: "നൈട്രജൻ (N) കിലോ/ഹെക്ടർ",
    lbl_p: "ഫോസ്ഫറസ് (P) കിലോ/ഹെക്ടർ",
    lbl_k: "പൊട്ടാഷ് (K) കിലോ/ഹെക്ടർ",
    lbl_ph: "മണ്ണിന്റെ pH മൂല്യം",
    lbl_irrigation: "ജലസേചന സൗകര്യം",
    lbl_farmsize: "കൃഷിയിട വിസ്തൃതി (ഏക്കർ)",
    lbl_prevcrop: "മുൻവിള",
    btn_run_advisory: "🌱 മണ്ണ് വിശകലനം ചെയ്ത് വിള ഉപദേശം നേടുക",
    panel_recs_title: "ശുപാർശ ചെയ്യുന്ന മികച്ച വിളകൾ",
    panel_recs_sub: "മണ്ണിന്റെ ഫലഭൂയിഷ്ഠതയുടെ അടിസ്ഥാനത്തിൽ",
    badge_best_match: "#1 മികച്ച വിള",
    lbl_match: "കൃത്യത",
    pillar_soil: "മണ്ണ് അനുയോജ്യത",
    pillar_weather: "കാലാവസ്ഥ",
    pillar_market: "വിപണി വില",
    pillar_rotation: "വിള പരിക്രമണം",
    lbl_yield: "പ്രതീക്ഷിക്കുന്ന വിളവ്",
    lbl_revenue: "പ്രതീക്ഷിക്കുന്ന വരുമാനം",
    lbl_rate: "മാർക്കറ്റ് നിരക്ക്",
    lbl_sowing: "വിത്ത് വിതയ്ക്കൽ സമയം",
    shap_title: "🌱 ഈ വിള നിങ്ങളുടെ കൃഷിയിടത്തിന് ഏറ്റവും അനുയോജ്യമാകുന്നത് എന്തുകൊണ്ട്?",
    shap_tag: "പോഷക ഘടകങ്ങളും കാലാവസ്ഥയും",
    runners_title: "മറ്റ് ഇതര വിളകൾ",
    panel_doctor_title: "സസ്യരോഗ നിർണയവും ഇല സ്കാനറും",
    panel_doctor_sub: "ഇലയുടെ ചിത്രം നൽകി രോഗം വേഗത്തിൽ കണ്ടെത്തുക",
    leaf_gallery_title: "പരിശോധനയ്ക്കുള്ള ഇല സാമ്പിളുകൾ:",
    dropzone_title: "ഇലയുടെ ഫോട്ടോ ഇവിടെ അപ്‌ലോഡ് ചെയ്യുക",
    dropzone_sub: "തക്കാളി, ഉരുളക്കിഴങ്ങ്, പരുത്തി, നെല്ല്, ചോളം എന്നിവയ്ക്ക്",
    btn_run_diagnosis: "രോഗനിർണയം ആരംഭിക്കുക",
    panel_diag_title: "രോഗനിർണയ റിപ്പോർട്ടും പരിഹാരങ്ങളും",
    panel_diag_sub: "ജൈവ, രാസ പ്രതിവിധികൾ",
    spray_alert_title: "🌦️ കാലാവസ്ഥാ അധിഷ്ഠിത കീടനാശിനി തളിക്കൽ ഉപദേശം",
    remedy_organic_badge: "🌿 100% ജൈവ ചികിത്സ",
    remedy_chemical_badge: "🧪 രാസ ചികിത്സ",
    voice_hero_title: "വോയ്‌സ് സാഥി — നിങ്ങളുടെ കാർഷിക സുഹൃത്ത്",
    voice_hero_sub: "മലയാളത്തിൽ സംസാരിച്ച് കൃഷി ഉപദേശങ്ങൾ നേടുക.",
    voice_chips_label: "സാധാരണ ചോദ്യങ്ങൾ:",
    chip_water: "എത്ര ജലസേചനം വേണം?",
    chip_fertilizer: "വളത്തിന്റെ അളവ് എത്ര?",
    chip_mandi: "മാർക്കറ്റ് നിരക്ക് എത്രയാണ്?",
    chip_pest: "കീടനിയന്ത്രണം എങ്ങനെ?",
    btn_ask_ai: "ചോദിക്കുക",
    btn_listen_audio: "ശബ്ദം കേൾക്കുക",
    lbl_followups: "തുടർ ചോദ്യങ്ങൾ:",
    panel_weather_title: "7 ദിവസത്തെ കാലാവസ്ഥ പ്രവചനം",
    panel_weather_sub: "ഉപഗ്രഹ വിവരങ്ങളും സ്പ്രേ സാഹചര്യങ്ങളും",
    panel_mandi_title: "തത്സമയ വിപണി വിലകൾ",
    panel_mandi_sub: "ദൈനംദിന മാർക്കറ്റ് നിരക്കുകൾ",
    th_commodity: "വിള",
    th_market: "വിപണി",
    th_rate: "ശരാശരി നിരക്ക് (₹/ക്വിന്റൽ)",
    th_trend: "7 ദിവസത്തെ പ്രവണത",
    panel_sb_title: "ക്ലൗഡ് ഡാറ്റ സമന്വയം",
    panel_sb_sub: "വിവരങ്ങൾ സുരക്ഷിതമായി സൂക്ഷിക്കുന്നു",
    panel_activity_title: "സമീപകാല പ്രവർത്തനങ്ങൾ",
    panel_activity_sub: "സംരക്ഷിച്ച വിവരങ്ങൾ",
    make_default_title: "ഇത് എന്റെ സ്ഥിരം ഭാഷയായി ക്രമീകരിക്കുക",
    make_default_sub: "(അടുത്ത തവണ നേരിട്ട് ഇതിൽ തുറക്കും)",
    btn_continue: "✓ മുന്നോട്ട് പോകുക ➔"
  },
  or: {
    code: "or",
    name: "ଓଡ଼ିଆ",
    flag: "🌾",
    speechCode: "or-IN",
    brand_tagline: "ଏଆଇ ଆଧାରିତ ପାଣିପାଗ ଓ ଫସଲ ପରାମର୍ଶ",
    supabase_sync: "ଲାଇଭ୍ କ୍ଲାଉଡ୍ ସିଙ୍କ୍ ସକ୍ରିୟ",
    live_mandi_label: "ଲାଇଭ୍ ମଣ୍ଡି ଦର",
    hero_headline: "ବୈଜ୍ଞାନିକ ତଥ୍ୟ ଆଧାରିତ ସ୍ମାର୍ଟ କୃଷି ପରାମର୍ଶ",
    hero_sub: "ମାଟିର ପୋଷକ ତତ୍ତ୍ୱ ଏବଂ ପାଣିପାଗ ବିଶ୍ଳେଷଣ କରି ଓଡ଼ିଆରେ ସଠିକ୍ ଫସଲ ଓ ରୋଗ ନିରାକରଣ ପରାମର୍ଶ।",
    btn_detect_location: "📍 ମୋର ଜମି ଅବସ୍ଥିତି ଖୋଜନ୍ତୁ (GPS)",
    quick_hubs_label: "ମୁଖ୍ୟ କୃଷି ଅଞ୍ଚଳ ଏବଂ ମୃତ୍ତିକା ପ୍ରକାର:",
    lbl_temperature: "ତାପମାତ୍ରା",
    lbl_humidity: "ଆର୍ଦ୍ରତା",
    lbl_rain7d: "୭-ଦିନର ବର୍ଷା",
    tab_advisory: "ଫସଲ ପରାମର୍ଶ",
    tab_doctor: "ଫସଲ ଡାକ୍ତର",
    tab_voice: "ଭଏସ୍ ସାଥୀ",
    tab_mandi: "ମଣ୍ଡି ଦର",
    tab_supabase: "କ୍ଲାଉଡ୍ ସ୍ଥିତି",
    panel_soil_title: "ଜମିର ବିବରଣୀ ଓ ମାଟି ପରୀକ୍ଷା",
    panel_soil_sub: "ସଏଲ୍ ହେଲଥ କାର୍ଡ ଲୋଡ୍ କରନ୍ତୁ",
    lbl_state: "ରାଜ୍ୟ",
    lbl_district: "ଜିଲ୍ଲା",
    lbl_n: "ଯବକ୍ଷାରଜାନ (N) କିଗ୍ରା/ହେକ୍ଟର",
    lbl_p: "ଫସଫରସ୍ (P) କିଗ୍ରା/ହେକ୍ଟର",
    lbl_k: "ପଟାସ୍ (K) କିଗ୍ରା/ହେକ୍ଟର",
    lbl_ph: "ମାଟିର pH ମୂଲ୍ୟ",
    lbl_irrigation: "ଜଳସେଚନ ସୁବିଧା",
    lbl_farmsize: "ଜମିର ଆକାର (ଏକର)",
    lbl_prevcrop: "ପୂର୍ବବର୍ତ୍ତୀ ଫସଲ",
    btn_run_advisory: "🌱 ଜମି ପରୀକ୍ଷା କରି ଫସଲ ପରାମର୍ଶ ପାଆନ୍ତୁ",
    panel_recs_title: "ସର୍ବୋତ୍ତମ ପରାମର୍ଶିତ ଫସଲ",
    panel_recs_sub: "ମାଟିର ଉର୍ବରତା ଓ ବଜାର ଦର ଅନୁସାରେ",
    badge_best_match: "#୧ ସର୍ବୋତ୍ତମ ଫସଲ",
    lbl_match: "ସଠିକତା",
    pillar_soil: "ମାଟି ଅନୁକୂଳତା",
    pillar_weather: "ପାଣିପାଗ",
    pillar_market: "ମଣ୍ଡି ଦର",
    pillar_rotation: "ଫସଲ ଚକ୍ର",
    lbl_yield: "ଆକଳିତ ଅମଳ",
    lbl_revenue: "ଆକଳିତ ଆୟ",
    lbl_rate: "ମଣ୍ଡି ଦର",
    lbl_sowing: "ବୁଣିବା ସମୟ",
    shap_title: "🌱 ଏହି ଫସଲ ଆପଣଙ୍କ ଜମି ପାଇଁ କାହିଁକି ସର୍ବୋତ୍ତମ?",
    shap_tag: "ପୋଷକ ତତ୍ତ୍ୱ ଓ ପାଣିପାଗ ଅନୁକୂଳତା",
    runners_title: "ଅନ୍ୟାନ୍ୟ ବିକଳ୍ପ ଫସଲ",
    panel_doctor_title: "ଫସଲ ରୋଗ ନିରାକରଣ ଓ ପତ୍ର ସ୍କାନର୍",
    panel_doctor_sub: "ପତ୍ରର ଫଟୋ ବାଛି ରୋଗ ଚିହ୍ନଟ କରନ୍ତୁ",
    leaf_gallery_title: "ପରୀକ୍ଷା ପାଇଁ ପତ୍ର ନମୁନା:",
    dropzone_title: "ପତ୍ରର ଫଟୋ ଏଠାରେ ଅପଲୋଡ୍ କରନ୍ତୁ",
    dropzone_sub: "ଟମାଟୋ, ଆଳୁ, କପା, ଗହମ, ଧାନ, ମକା ଇତ୍ୟାଦି",
    btn_run_diagnosis: "ରୋଗ ଚିହ୍ନଟ ଆରମ୍ଭ କରନ୍ତୁ",
    panel_diag_title: "ରୋଗ ବିବରଣୀ ଓ ପ୍ରତିକାର",
    panel_diag_sub: "ଜୈବିକ ଏବଂ ରାସାୟନିକ ପ୍ରତିକାର",
    spray_alert_title: "🌦️ ପାଣିପାଗ ଅନୁସାରେ ସ୍ପ୍ରେ ପରାମର୍ଶ",
    remedy_organic_badge: "🌿 ୧୦୦% ପ୍ରାକୃତିକ ଚିକିତ୍ସା",
    remedy_chemical_badge: "🧪 ରାସାୟନିକ ଚିକିତ୍ସା",
    voice_hero_title: "ଭଏସ୍ ସାଥୀ — ଆପଣଙ୍କ କୃଷି ମିତ୍ର",
    voice_hero_sub: "ଓଡ଼ିଆରେ କହି କୃଷି ପରାମର୍ଶ ପାଆନ୍ତୁ।",
    voice_chips_label: "ସାଧାରଣ ପ୍ରଶ୍ନ:",
    chip_water: "କେତେ ପାଣି ଦେବା ଆବଶ୍ୟକ?",
    chip_fertilizer: "ଖତ ଓ ସାରର ପରିମାଣ?",
    chip_mandi: "ମଣ୍ଡି ଦର କେତେ ଚାଲିଛି?",
    chip_pest: "ପୋକ ନିୟନ୍ତ୍ରଣ କିପରି କରିବେ?",
    btn_ask_ai: "ପଚାରନ୍ତୁ",
    btn_listen_audio: "ଭଏସ୍ ଶୁଣନ୍ତୁ",
    lbl_followups: "ପରବର୍ତ୍ତୀ ପ୍ରଶ୍ନ:",
    panel_weather_title: "୭ ଦିନର ପାଣିପାଗ ପୂର୍ବାନୁମାନ",
    panel_weather_sub: "ସାଟେଲାଇଟ୍ ତଥ୍ୟ ଓ ସ୍ପ୍ରେ ସ୍ଥିତି",
    panel_mandi_title: "ତାଜା ମଣ୍ଡି ଦର",
    panel_mandi_sub: "ଦୈନିକ ମଣ୍ଡି ଦର ବିବରଣୀ",
    th_commodity: "ଫସଲ",
    th_market: "ମଣ୍ଡି",
    th_rate: "ହାରାହାରି ଦର (₹/କ୍ୱିଣ୍ଟାଲ)",
    th_trend: "୭-ଦିନର ଧାରା",
    panel_sb_title: "କ୍ଲାଉଡ୍ ଡାଟା ସିଙ୍କ୍",
    panel_sb_sub: "ଡାଟାବେସ୍ ସର୍ବଦା ସକ୍ରିୟ ରହିଥାଏ",
    panel_activity_title: "ସାମ୍ପ୍ରତିକ କାର୍ଯ୍ୟକଳାପ",
    panel_activity_sub: "ସଂରକ୍ଷିତ ତଥ୍ୟ",
    make_default_title: "ଏହାକୁ ମୋର ଡିଫଲ୍ଟ ଭାଷା କରନ୍ତୁ",
    make_default_sub: "(ପରବର୍ତ୍ତୀ ଥର ସିଧାସଳଖ ଏହି ଭାଷାରେ ଖୋଲିବ)",
    btn_continue: "✓ ଆଗକୁ ବଢ଼ନ୍ତୁ ➔"
  }
};

// 11 INDIAN REGIONAL AGRO-ECOLOGICAL HUBS DATA (CLEAN BILINGUAL FIELDS)
const DEMO_HUBS = {
  nashik: {
    id: "nashik",
    name_en: "Nashik, Maharashtra",
    name_hi: "नासिक, महाराष्ट्र",
    state: "Maharashtra",
    district: "Nashik",
    lat: 19.9975,
    lon: 73.7898,
    soil: { n: 85, p: 48, k: 190, ph: 6.8, oc: 0.72, type: "Medium Black Cotton (Regur) Loam", farmer: "Ramesh Kisan Patil" },
    weather: {
      temp: "26.5°C",
      hum: "74%",
      rain: "68 mm",
      cond_en: "Partly Cloudy • Favorable Weather",
      cond_hi: "आंशिक बादल • अनुकूल मौसम",
      spray_en: "Good for Spraying • Clear Window",
      spray_hi: "छिड़काव के लिए उत्तम समय",
      icon: "⛅"
    },
    topCrop: {
      name_en: "🍇 Grapes (Vitis vinifera)",
      name_hi: "🍇 अंगूर (Vitis vinifera)",
      family: "Vitaceae (Fruit) • 135 Days Duration",
      score: "94.8%",
      yield: "8 - 12 Tonnes",
      rev: "₹3,50,000 - ₹5,00,000",
      rate: "₹6,200 / Qtl ↗",
      sowing: "Oct - Nov (Pruning)"
    },
    shap_en: "High Potassium (190 kg/ha) combined with neutral soil pH (6.8) provides the ideal nutrient balance for superior grape berry sweetness and cluster yield.",
    shap_hi: "आपकी मिट्टी में पोटाश (190 kg/ha) और अनुकूल pH (6.8) अंगूर की मिठास और बेहतर पैदावार के लिए सर्वाधिक अनुकूल हैं।",
    shapBars: [
      { name: "Potassium (K: 190)", pct: 82, val: "+28%", pos: true },
      { name: "Soil pH (6.8 Neutral)", pct: 65, val: "+18%", pos: true },
      { name: "Nitrogen (N: 85)", pct: 48, val: "+12%", pos: true },
      { name: "Phosphorus (P: 48)", pct: 32, val: "+7%", pos: true },
      { name: "Rainfall Forecast", pct: 18, val: "-4%", pos: false }
    ],
    runners: [
      { name_en: "🍎 Pomegranate", name_hi: "🍎 अनार", score: "91.2%", meta: "Est: ₹2.8L - ₹4.2L / acre • Mandi: ₹8,400/Qtl" },
      { name_en: "🌿 Cotton", name_hi: "🌿 कपास", score: "86.5%", meta: "Est: ₹75K - ₹1.05L / acre • Mandi: ₹7,450/Qtl" }
    ]
  },
  indore: {
    id: "indore",
    name_en: "Indore, Madhya Pradesh",
    name_hi: "इंदौर, मध्य प्रदेश",
    state: "Madhya Pradesh",
    district: "Indore",
    lat: 22.7196,
    lon: 75.8577,
    soil: { n: 45, p: 62, k: 82, ph: 7.4, oc: 0.58, type: "Deep Black Malwa Vertisol Clay", farmer: "Vikram Singh Chouhan" },
    weather: {
      temp: "28.0°C",
      hum: "65%",
      rain: "42 mm",
      cond_en: "Clear & Sunny • Dry Conditions",
      cond_hi: "साफ मौसम • शुष्क हवा",
      spray_en: "Excellent for Spraying • No Rain Expected",
      spray_hi: "छिड़काव हेतु श्रेष्ठ समय • बारिश नहीं",
      icon: "☀️"
    },
    topCrop: {
      name_en: "🌾 Chickpea (Cicer arietinum)",
      name_hi: "🌾 चना (Cicer arietinum)",
      family: "Fabaceae (Legume/Pulse) • 110 Days",
      score: "93.4%",
      yield: "8 - 12 Quintals",
      rev: "₹50,000 - ₹74,000",
      rate: "₹6,150 / Qtl ↗",
      sowing: "Oct - Nov (Rabi)"
    },
    shap_en: "Deep black vertisol clay with high available phosphorus (62 kg/ha) stimulates nodulation and pod development for high-yield chickpea cultivation.",
    shap_hi: "मालवा की गहरी काली मिट्टी व संतुलित फॉस्फोरस (62 kg/ha) दलहनी फसलों में जड़ ग्रंथियों के विकास और चने के दानों के भराव के लिए सर्वोत्तम है।",
    shapBars: [
      { name: "Phosphorus (P: 62)", pct: 85, val: "+26%", pos: true },
      { name: "Clay Content (45%)", pct: 60, val: "+16%", pos: true },
      { name: "Soil pH (7.4)", pct: 50, val: "+14%", pos: true },
      { name: "Nitrogen (N: 45)", pct: 28, val: "+6%", pos: true },
      { name: "High Heat Peak", pct: 15, val: "-3%", pos: false }
    ],
    runners: [
      { name_en: "🌱 Soybean", name_hi: "🌱 सोयाबीन", score: "89.5%", meta: "Est: ₹45K - ₹62K / acre • Mandi: ₹4,680/Qtl" },
      { name_en: "🌽 Maize", name_hi: "🌽 मक्का", score: "84.2%", meta: "Est: ₹55K - ₹72K / acre • Mandi: ₹2,280/Qtl" }
    ]
  },
  ludhiana: {
    id: "ludhiana",
    name_en: "Ludhiana, Punjab",
    name_hi: "लुधियाना, पंजाब",
    state: "Punjab",
    district: "Ludhiana",
    lat: 30.9010,
    lon: 75.8573,
    soil: { n: 92, p: 42, k: 38, ph: 7.2, oc: 0.45, type: "Indo-Gangetic Alluvial Sandy Loam", farmer: "Gurpreet Singh Dhillon" },
    weather: {
      temp: "30.5°C",
      hum: "68%",
      rain: "55 mm",
      cond_en: "Warm & Humid • Moderate Breeze",
      cond_hi: "उमस भरा मौसम • हल्की हवा",
      spray_en: "Spray after 4 PM to avoid heat evaporation",
      spray_hi: "शाम 4 बजे बाद छिड़काव करें",
      icon: "🌤️"
    },
    topCrop: {
      name_en: "🌾 Rice (Oryza sativa)",
      name_hi: "🌾 धान (Oryza sativa)",
      family: "Poaceae (Cereal) • 130 Days",
      score: "92.8%",
      yield: "22 - 28 Quintals",
      rev: "₹85,000 - ₹1,10,000",
      rate: "₹3,950 / Qtl ↗",
      sowing: "June - July (Transplanting)"
    },
    shap_en: "Fertile alluvial sandy loam soil with high nitrogen availability (92 kg/ha) accelerates tillering and maximizes panicle grains in paddy crops.",
    shap_hi: "जलोढ़ दोमट मिट्टी और उच्च नाइट्रोजन (92 kg/ha) धान के कल्ले फूटने और भरपूर पैदावार के लिए सर्वोत्तम हैं।",
    shapBars: [
      { name: "Nitrogen (N: 92)", pct: 88, val: "+29%", pos: true },
      { name: "Irrigation Access", pct: 70, val: "+21%", pos: true },
      { name: "Soil pH (7.2)", pct: 45, val: "+11%", pos: true },
      { name: "Organic Matter", pct: 30, val: "+5%", pos: true },
      { name: "Groundwater Strain", pct: 25, val: "-6%", pos: false }
    ],
    runners: [
      { name_en: "🌽 Maize", name_hi: "🌽 मक्का", score: "88.1%", meta: "Est: ₹55K - ₹72K / acre • Mandi: ₹2,280/Qtl" },
      { name_en: "🌿 Cotton", name_hi: "🌿 कपास", score: "83.6%", meta: "Est: ₹75K - ₹1.05L / acre • Mandi: ₹7,450/Qtl" }
    ]
  },
  guntur: {
    id: "guntur",
    name_en: "Guntur, Andhra Pradesh",
    name_hi: "गुंटूर, आंध्र प्रदेश",
    state: "Andhra Pradesh",
    district: "Guntur",
    lat: 16.3067,
    lon: 80.4365,
    soil: { n: 70, p: 55, k: 140, ph: 6.5, oc: 0.65, type: "Coastal Red Clayey Sandy Loam", farmer: "Venkat Ramanayya" },
    weather: {
      temp: "31.2°C",
      hum: "78%",
      rain: "80 mm",
      cond_en: "Tropical Humid • Breezy",
      cond_hi: "उष्ण आर्द्र मौसम • तेज हवा",
      spray_en: "Check wind speed before spraying",
      spray_hi: "हवा की गति देखकर छिड़काव करें",
      icon: "🌧️"
    },
    topCrop: {
      name_en: "🌿 Cotton (Gossypium hirsutum)",
      name_hi: "🌿 कपास (Gossypium hirsutum)",
      family: "Malvaceae (Fiber) • 160 Days",
      score: "94.1%",
      yield: "10 - 14 Quintals",
      rev: "₹75,000 - ₹1,05,000",
      rate: "₹7,450 / Qtl ▶",
      sowing: "May - June (Kharif)"
    },
    shap_en: "Red loam soil with rich potassium (140 kg/ha) promotes strong boll formation, fiber elongation, and pest tolerance in cotton crops.",
    shap_hi: "लाल दोमट मिट्टी और पर्याप्त पोटाश (140 kg/ha) कपास के टिंडों के विकास और उत्कृष्ट रेशे की गुणवत्ता के लिए अत्यंत लाभकारी हैं।",
    shapBars: [
      { name: "Potassium (K: 140)", pct: 78, val: "+24%", pos: true },
      { name: "Phosphorus (P: 55)", pct: 62, val: "+17%", pos: true },
      { name: "Soil pH (6.5)", pct: 54, val: "+13%", pos: true },
      { name: "Nitrogen (N: 70)", pct: 40, val: "+9%", pos: true },
      { name: "High Humidity Risk", pct: 20, val: "-5%", pos: false }
    ],
    runners: [
      { name_en: "🌶️ Chilli", name_hi: "🌶️ मिर्च", score: "91.8%", meta: "Est: ₹1.2L - ₹1.8L / acre • Mandi: ₹18,500/Qtl" },
      { name_en: "🌽 Maize", name_hi: "🌽 मक्का", score: "85.0%", meta: "Est: ₹55K - ₹72K / acre • Mandi: ₹2,280/Qtl" }
    ]
  },
  rajkot: {
    id: "rajkot",
    name_en: "Rajkot, Gujarat",
    name_hi: "राजकोट, गुजरात",
    state: "Gujarat",
    district: "Rajkot",
    lat: 22.3039,
    lon: 70.8022,
    soil: { n: 58, p: 64, k: 165, ph: 7.8, oc: 0.52, type: "Saurashtra Calcareous Loam", farmer: "Mansukhbhai Patel" },
    weather: {
      temp: "29.8°C",
      hum: "62%",
      rain: "35 mm",
      cond_en: "Sunny & Dry • Mild Breeze",
      cond_hi: "धूप व शुष्क मौसम",
      spray_en: "Excellent for Spraying • Clear Sky",
      spray_hi: "छिड़काव के लिए उत्तम समय",
      icon: "☀️"
    },
    topCrop: {
      name_en: "🥜 Groundnut (Arachis hypogaea)",
      name_hi: "🥜 मूंगफली (Arachis hypogaea)",
      family: "Fabaceae (Oilseed) • 105 Days",
      score: "93.8%",
      yield: "12 - 16 Quintals",
      rev: "₹72,000 - ₹96,000",
      rate: "₹6,800 / Qtl ↗",
      sowing: "June - July"
    },
    shap_en: "Calcareous medium loam with balanced calcium and phosphorus supports excellent pod filling, shell hardness, and oil content in groundnut.",
    shap_hi: "कैल्शियम युक्त दोमट मिट्टी मूंगफली के दानों के भराव और तेल की उच्च मात्रा के लिए सबसे उपयुक्त है।",
    shapBars: [
      { name: "Phosphorus (P: 64)", pct: 80, val: "+25%", pos: true },
      { name: "Potassium (K: 165)", pct: 75, val: "+22%", pos: true },
      { name: "Soil Calcium", pct: 60, val: "+15%", pos: true }
    ],
    runners: [
      { name_en: "🌿 Cotton", name_hi: "🌿 कपास", score: "90.2%", meta: "Est: ₹75K - ₹1.05L / acre • Mandi: ₹7,450/Qtl" },
      { name_en: "🌾 Sesame", name_hi: "🌾 तिल", score: "86.4%", meta: "Est: ₹45K - ₹65K / acre • Mandi: ₹11,200/Qtl" }
    ]
  },
  thanjavur: {
    id: "thanjavur",
    name_en: "Thanjavur, Tamil Nadu",
    name_hi: "तंजावूर, तमिलनाडु",
    state: "Tamil Nadu",
    district: "Thanjavur",
    lat: 10.7870,
    lon: 79.1378,
    soil: { n: 88, p: 36, k: 95, ph: 6.7, oc: 0.81, type: "Cauvery Deltaic Silt Clay", farmer: "Muthusamy Sundaram" },
    weather: {
      temp: "31.5°C",
      hum: "76%",
      rain: "95 mm",
      cond_en: "Delta Rain Showers • Humid",
      cond_hi: "डेल्टा वर्षा • उमस भरा मौसम",
      spray_en: "Spray after rain clears",
      spray_hi: "बारिश रुकने के बाद ही छिड़काव करें",
      icon: "🌦️"
    },
    topCrop: {
      name_en: "🌾 Rice (Oryza sativa)",
      name_hi: "🌾 धान (Oryza sativa)",
      family: "Poaceae (Cereal) • 120 Days",
      score: "95.2%",
      yield: "24 - 30 Quintals",
      rev: "₹95,000 - ₹1,20,000",
      rate: "₹3,950 / Qtl ↗",
      sowing: "Kuruvai / Samba"
    },
    shap_en: "Rich Cauvery delta silt clay with high organic carbon (0.81%) provides superior water retention and root nutrition for paddy.",
    shap_hi: "कावेरी डेल्टा की उपजाऊ जलोढ़ मिट्टी और उच्च जैविक कार्बन (0.81%) धान की बंपर पैदावार सुनिश्चित करते हैं।",
    shapBars: [
      { name: "Organic Carbon (0.81%)", pct: 86, val: "+27%", pos: true },
      { name: "Nitrogen (N: 88)", pct: 78, val: "+23%", pos: true }
    ],
    runners: [
      { name_en: "🌾 Blackgram", name_hi: "🌾 उड़द", score: "89.4%", meta: "Est: ₹35K - ₹50K / acre • Mandi: ₹7,800/Qtl" },
      { name_en: "🍌 Banana", name_hi: "🍌 केला", score: "87.1%", meta: "Est: ₹1.8L - ₹2.5L / acre • Mandi: ₹2,400/Qtl" }
    ]
  },
  bardhaman: {
    id: "bardhaman",
    name_en: "Bardhaman, West Bengal",
    name_hi: "बर्धमान, पश्चिम बंगाल",
    state: "West Bengal",
    district: "Bardhaman",
    lat: 23.2324,
    lon: 87.8615,
    soil: { n: 95, p: 32, k: 88, ph: 6.2, oc: 0.78, type: "Gangetic Old Alluvial Clay Loam", farmer: "Subrata Mukherjee" },
    weather: {
      temp: "30.0°C",
      hum: "82%",
      rain: "110 mm",
      cond_en: "Monsoon Showers • High Humidity",
      cond_hi: "मानसूनी फुहारें • अधिक नमी",
      spray_en: "Hold spraying for 24h due to rainfall",
      spray_hi: "बारिश के कारण छिड़काव 24 घंटे टालें",
      icon: "🌧️"
    },
    topCrop: {
      name_en: "🌾 Rice (Oryza sativa)",
      name_hi: "🌾 धान (Aman Rice)",
      family: "Poaceae (Cereal) • 135 Days",
      score: "94.6%",
      yield: "25 - 32 Quintals",
      rev: "₹90,000 - ₹1,15,000",
      rate: "₹3,800 / Qtl ↗",
      sowing: "Aman / Boro Season"
    },
    shap_en: "Gangetic clay loam with high nitrogen (95 kg/ha) supports vigorous vegetative growth and high grain density in paddy.",
    shap_hi: "गांगेय जलोढ़ मिट्टी और भरपूर नाइट्रोजन धान की फसल के तेजी से विकास और स्वस्थ बालियों के लिए अत्यंत उपयोगी हैं।",
    shapBars: [
      { name: "Nitrogen (N: 95)", pct: 88, val: "+28%", pos: true },
      { name: "Soil Organic Carbon", pct: 72, val: "+20%", pos: true }
    ],
    runners: [
      { name_en: "🥔 Potato", name_hi: "🥔 आलू", score: "91.5%", meta: "Est: ₹65K - ₹95K / acre • Mandi: ₹1,450/Qtl" },
      { name_en: "🌿 Jute", name_hi: "🌿 जूट", score: "86.8%", meta: "Est: ₹45K - ₹68K / acre • Mandi: ₹5,400/Qtl" }
    ]
  },
  jaipur: {
    id: "jaipur",
    name_en: "Jaipur, Rajasthan",
    name_hi: "जयपुर, राजस्थान",
    state: "Rajasthan",
    district: "Jaipur",
    lat: 26.9124,
    lon: 75.7873,
    soil: { n: 32, p: 28, k: 120, ph: 8.2, oc: 0.28, type: "Desert Light Sandy Loam", farmer: "Ramkishan Gurjar" },
    weather: {
      temp: "34.5°C",
      hum: "42%",
      rain: "18 mm",
      cond_en: "Dry & Sunny • Strong Sun",
      cond_hi: "तेज धूप • शुष्क हवा",
      spray_en: "Spray Early Morning (6-8 AM)",
      spray_hi: "सुबह 6 से 8 बजे के बीच ही छिड़कें",
      icon: "☀️"
    },
    topCrop: {
      name_en: "🌾 Mothbeans (Vigna aconitifolia)",
      name_hi: "🌾 मोठ (Vigna aconitifolia)",
      family: "Fabaceae (Drought Pulse) • 75 Days",
      score: "93.1%",
      yield: "5 - 8 Quintals",
      rev: "₹38,000 - ₹58,000",
      rate: "₹7,200 / Qtl ↗",
      sowing: "July (Kharif)"
    },
    shap_en: "Light sandy loam soil with low water requirement makes drought-hardy mothbeans and pearl millet the lowest-risk, highest-profit crop.",
    shap_hi: "रेतीली दोमट मिट्टी और कम पानी की आवश्यकता में मोठ व बाजरा की फसल न्यूनतम जोखिम में सर्वोत्तम लाभ देती है।",
    shapBars: [
      { name: "Drought Resilience", pct: 92, val: "+32%", pos: true },
      { name: "Potassium (K: 120)", pct: 60, val: "+16%", pos: true },
      { name: "Low Rain Requirement", pct: 55, val: "+14%", pos: true }
    ],
    runners: [
      { name_en: "🌾 Chickpea", name_hi: "🌾 चना", score: "88.7%", meta: "Est: ₹45K - ₹68K / acre • Mandi: ₹6,150/Qtl" },
      { name_en: "🌱 Mustard", name_hi: "🌱 सरसों", score: "85.3%", meta: "Est: ₹42K - ₹62K / acre • Mandi: ₹5,650/Qtl" }
    ]
  },
  dharwad: {
    id: "dharwad",
    name_en: "Dharwad, Karnataka",
    name_hi: "धारवाड़, कर्नाटक",
    state: "Karnataka",
    district: "Dharwad",
    lat: 15.4589,
    lon: 75.0078,
    soil: { n: 75, p: 46, k: 115, ph: 6.4, oc: 0.69, type: "Western Ghats Red Laterite Loam", farmer: "Basavaraj Bommai Gowda" },
    weather: {
      temp: "27.5°C",
      hum: "72%",
      rain: "75 mm",
      cond_en: "Pleasant & Breezy",
      cond_hi: "सुहावना मौसम • हल्की हवा",
      spray_en: "Good for Spraying • Clear Window",
      spray_hi: "छिड़काव के लिए उत्तम समय",
      icon: "⛅"
    },
    topCrop: {
      name_en: "🌽 Maize (Zea mays)",
      name_hi: "🌽 मक्का (Zea mays)",
      family: "Poaceae (Cereal) • 105 Days",
      score: "93.7%",
      yield: "25 - 32 Quintals",
      rev: "₹60,000 - ₹82,000",
      rate: "₹2,280 / Qtl ↗",
      sowing: "June - July"
    },
    shap_en: "Red laterite loam provides excellent drainage and nutrient availability, ensuring robust cob development and high maize yield.",
    shap_hi: "लाल लेटराइट मिट्टी मक्का और कपास की फसलों में अच्छी जल निकासी और मजबूत भुट्टों के विकास के लिए सबसे उपयुक्त है।",
    shapBars: [
      { name: "Soil Drainage", pct: 82, val: "+25%", pos: true },
      { name: "Potassium (K: 115)", pct: 68, val: "+19%", pos: true }
    ],
    runners: [
      { name_en: "🌿 Cotton", name_hi: "🌿 कपास", score: "89.8%", meta: "Est: ₹75K - ₹1.05L / acre • Mandi: ₹7,450/Qtl" },
      { name_en: "🌱 Soybean", name_hi: "🌱 सोयाबीन", score: "85.6%", meta: "Est: ₹45K - ₹62K / acre • Mandi: ₹4,680/Qtl" }
    ]
  },
  varanasi: {
    id: "varanasi",
    name_en: "Varanasi, Uttar Pradesh",
    name_hi: "वाराणसी, उत्तर प्रदेश",
    state: "Uttar Pradesh",
    district: "Varanasi",
    lat: 25.3176,
    lon: 82.9739,
    soil: { n: 82, p: 52, k: 68, ph: 7.1, oc: 0.61, type: "Eastern Gangetic Silt Alluvial", farmer: "Chandrabhan Tiwari" },
    weather: {
      temp: "29.2°C",
      hum: "69%",
      rain: "60 mm",
      cond_en: "Scattered Clouds • Warm",
      cond_hi: "हल्के बादल • सामान्य मौसम",
      spray_en: "Spray in afternoon hours",
      spray_hi: "दोपहर के समय छिड़काव करें",
      icon: "🌤️"
    },
    topCrop: {
      name_en: "🌾 Wheat (Triticum aestivum)",
      name_hi: "🌾 गेहूं (Triticum aestivum)",
      family: "Poaceae (Rabi Cereal) • 125 Days",
      score: "94.2%",
      yield: "18 - 24 Quintals",
      rev: "₹75,000 - ₹98,000",
      rate: "₹2,550 / Qtl ↗",
      sowing: "Nov - Dec"
    },
    shap_en: "Gangetic alluvial silt soil with balanced phosphorus (52 kg/ha) maximizes root depth, tiller numbers, and grain weight in wheat.",
    shap_hi: "गंगा के मैदानों की दोमट जलोढ़ मिट्टी गेहूं के कल्ले फूटने और दाने के भराव के लिए अत्यंत उपजाऊ है।",
    shapBars: [
      { name: "Phosphorus (P: 52)", pct: 84, val: "+26%", pos: true },
      { name: "Soil Silt Content", pct: 75, val: "+21%", pos: true }
    ],
    runners: [
      { name_en: "🌾 Pigeonpeas", name_hi: "🌾 अरहर", score: "90.1%", meta: "Est: ₹55K - ₹78K / acre • Mandi: ₹10,200/Qtl" },
      { name_en: "🌱 Mustard", name_hi: "🌱 सरसों", score: "87.4%", meta: "Est: ₹42K - ₹62K / acre • Mandi: ₹5,650/Qtl" }
    ]
  },
  palakkad: {
    id: "palakkad",
    name_en: "Palakkad, Kerala",
    name_hi: "पालक्काड, केरल",
    state: "Kerala",
    district: "Palakkad",
    lat: 10.7867,
    lon: 76.6548,
    soil: { n: 68, p: 24, k: 75, ph: 5.4, oc: 1.15, type: "High-Rainfall Acidic Peaty Laterite", farmer: "Gopalakrishnan Nair" },
    weather: {
      temp: "28.5°C",
      hum: "85%",
      rain: "140 mm",
      cond_en: "Monsoon Rains • Overcast",
      cond_hi: "मानसूनी बारिश • घने बादल",
      spray_en: "Do not spray during heavy rain",
      spray_hi: "भारी बारिश में छिड़काव न करें",
      icon: "🌧️"
    },
    topCrop: {
      name_en: "🥥 Coconut (Cocos nucifera)",
      name_hi: "🥥 नारियल (Cocos nucifera)",
      family: "Arecaceae (Palm) • Perennial",
      score: "95.5%",
      yield: "80 - 100 Nuts/Palm",
      rev: "₹1,20,000 - ₹1,80,000",
      rate: "₹3,400 / 100 Nuts ↗",
      sowing: "May - June"
    },
    shap_en: "High organic matter (1.15%) and tropical rainfall support sustained root vitality and high copra nut yield in coconut plantations.",
    shap_hi: "अम्लीय व उच्च जैविक पदार्थ (1.15%) युक्त मिट्टी नारियल और बागवानी फसलों के निरंतर उत्पादन के लिए सर्वोत्तम है।",
    shapBars: [
      { name: "High Organic Matter (1.15%)", pct: 90, val: "+30%", pos: true },
      { name: "High Rainfall Adaptation", pct: 85, val: "+26%", pos: true }
    ],
    runners: [
      { name_en: "🍌 Banana", name_hi: "🍌 केला", score: "91.0%", meta: "Est: ₹1.5L - ₹2.2L / acre • Mandi: ₹3,800/Qtl" },
      { name_en: "🌾 Rice", name_hi: "🌾 धान", score: "88.2%", meta: "Est: ₹60K - ₹85K / acre • Mandi: ₹3,950/Qtl" }
    ]
  }
};

// 11 INDIAN SOIL HEALTH CARDS
const SAMPLE_SOIL_CARDS_MAP = {
  sample_1_nashik: { hub: "nashik", n: 85, p: 48, k: 190, ph: 6.8, oc: 0.72, texture: "Medium Black Cotton (Regur) Loam", farmer: "Ramesh Kisan Patil", state: "Maharashtra", district: "Nashik" },
  sample_2_indore: { hub: "indore", n: 45, p: 62, k: 82, ph: 7.4, oc: 0.58, texture: "Deep Black Malwa Vertisol Clay", farmer: "Vikram Singh Chouhan", state: "Madhya Pradesh", district: "Indore" },
  sample_3_ludhiana: { hub: "ludhiana", n: 92, p: 42, k: 38, ph: 7.2, oc: 0.45, texture: "Indo-Gangetic Alluvial Sandy Loam", farmer: "Gurpreet Singh Dhillon", state: "Punjab", district: "Ludhiana" },
  sample_4_guntur: { hub: "guntur", n: 70, p: 55, k: 140, ph: 6.5, oc: 0.65, texture: "Coastal Red Clayey Sandy Loam", farmer: "Venkat Ramanayya", state: "Andhra Pradesh", district: "Guntur" },
  sample_5_rajkot: { hub: "rajkot", n: 58, p: 64, k: 165, ph: 7.8, oc: 0.52, texture: "Saurashtra Calcareous Loam", farmer: "Mansukhbhai Patel", state: "Gujarat", district: "Rajkot" },
  sample_6_thanjavur: { hub: "thanjavur", n: 88, p: 36, k: 95, ph: 6.7, oc: 0.81, texture: "Cauvery Deltaic Silt Clay", farmer: "Muthusamy Sundaram", state: "Tamil Nadu", district: "Thanjavur" },
  sample_7_bardhaman: { hub: "bardhaman", n: 95, p: 32, k: 88, ph: 6.2, oc: 0.78, texture: "Gangetic Old Alluvial Clay Loam", farmer: "Subrata Mukherjee", state: "West Bengal", district: "Bardhaman" },
  sample_8_jaipur: { hub: "jaipur", n: 32, p: 28, k: 120, ph: 8.2, oc: 0.28, texture: "Desert Light Sandy Loam", farmer: "Ramkishan Gurjar", state: "Rajasthan", district: "Jaipur" },
  sample_9_dharwad: { hub: "dharwad", n: 75, p: 46, k: 115, ph: 6.4, oc: 0.69, texture: "Western Ghats Red Laterite Loam", farmer: "Basavaraj Bommai Gowda", state: "Karnataka", district: "Dharwad" },
  sample_10_varanasi: { hub: "varanasi", n: 82, p: 52, k: 68, ph: 7.1, oc: 0.61, texture: "Eastern Gangetic Silt Alluvial", farmer: "Chandrabhan Tiwari", state: "Uttar Pradesh", district: "Varanasi" },
  sample_11_palakkad: { hub: "palakkad", n: 68, p: 24, k: 75, ph: 5.4, oc: 1.15, texture: "High-Rainfall Acidic Peaty Laterite", farmer: "Gopalakrishnan Nair", state: "Kerala", district: "Palakkad" }
};

// LEAF DISEASE SAMPLES
const LEAF_SAMPLES = {
  tomato_early_blight: {
    crop_en: "Tomato",
    crop_hi: "टमाटर",
    name_en: "Early Blight (Alternaria solani)",
    name_hi: "अगेती झुलसा रोग (अर्ली ब्लाइट)",
    severity_en: "Medium (35% area)",
    severity_hi: "मध्यम (35% क्षेत्र)",
    confidence: "96.4%",
    spray_en: "Chance of afternoon showers. Spray early in the morning (6-8 AM) or in late evening with a sticker.",
    spray_hi: "दोपहर बाद बारिश की संभावना है। अतः छिड़काव सुबह 6 से 8 बजे या शाम को स्टिकर मिलाकर ही करें।",
    organic_en: "Spray Neem Seed Kernel Extract (NSKE 5%) or Trichoderma viride (@ 5g/L water). Fermented 10% cow urine spray prevents fungal spore expansion.",
    organic_hi: "नीम के बीज के अर्क (NSKE 5%) या ट्राइकोडर्मा विरिडी (5 ग्राम/लीटर) का छिड़काव करें। साथ ही 10% गोमूत्र का अर्क फंगस रोकने में अत्यंत प्रभावी है।",
    chemical_en: "Apply Mancozeb 75 WP (@ 2.5g/L water) or Azoxystrobin 23 SC (@ 1ml/L water) for fast curative action.",
    chemical_hi: "मैंकोजेब 75 WP (Mancozeb @ 2.5 ग्राम/लीटर पानी) या एजोक्सीस्ट्रोबिन (1 मिली/लीटर) का तुरंत छिड़काव करें।"
  },
  potato_late_blight: {
    crop_en: "Potato",
    crop_hi: "आलू",
    name_en: "Late Blight (Phytophthora infestans)",
    name_hi: "पछेती झुलसा रोग (लेट ब्लाइट)",
    severity_en: "High (Rapidly spreading spores)",
    severity_hi: "गंभीर (तेजी से फैलने वाले बीजाणु)",
    confidence: "98.1%",
    spray_en: "Overcast conditions detected. Immediate spray required to prevent spore germination.",
    spray_hi: "आसमान में बादल छाए हैं। यदि तुरंत छिड़काव न किया गया तो फफूंद तेजी से फैलेगी।",
    organic_en: "Apply 1% Bordeaux mixture thoroughly covering lower leaf surfaces. Repeat after 7 days.",
    organic_hi: "कॉपर सल्फेट व बुझे हुए चूने का बोर्डो मिश्रण (1%) बनाकर तुरंत पौधों की निचली पत्तियों तक तर करें।",
    chemical_en: "Spray Ridomil Gold (Metalaxyl-M + Mancozeb @ 2g/L water) or Cymoxanil 8% + Mancozeb 64% WP.",
    chemical_hi: "रिडोमिल एमजेड (Metalaxyl + Mancozeb @ 2 ग्राम/लीटर पानी) या सायमोक्सानिल का त्वरित छिड़काव करें।"
  },
  cotton_bacterial_blight: {
    crop_en: "Cotton",
    crop_hi: "कपास",
    name_en: "Bacterial Leaf Blight (Angular Leaf Spot)",
    name_hi: "कपास का जीवाणु झुलसा / कोणीय धब्बा रोग",
    severity_en: "Moderate (Water-soaked lesions)",
    severity_hi: "मध्यम (पानी जैसे धब्बे)",
    confidence: "94.7%",
    spray_en: "Wind speed is moderate. Avoid noon hours; spray during calm morning hours.",
    spray_hi: "हवा की गति सामान्य है। दोपहर की तेज धूप में छिड़काव से बचें और सुबह के समय छिड़कें।",
    organic_en: "Spray Pseudomonas fluorescens (@ 5g/L) and 5% Panchagavya solution at 10-day intervals.",
    organic_hi: "स्यूडोमोनास फ्लोरेसेंस (5 ग्राम/लीटर) व 5% पंचगव्य का घोल बनाकर 10 दिन के अंतराल पर छिड़कें।",
    chemical_en: "Spray Streptocycline (1g) + Copper Oxychloride (30g) dissolved in 10 liters of clean water.",
    chemical_hi: "स्ट्रेप्टोसाइक्लिन (1 ग्राम) + कॉपर ऑक्सीक्लोराइड (30 ग्राम) प्रति 10 लीटर पानी में घोलकर छिड़काव करें।"
  },
  corn_healthy: {
    crop_en: "Corn (Maize)",
    crop_hi: "मक्का",
    name_en: "Healthy Leaf — No Pathogen Detected",
    name_hi: "स्वस्थ पत्ती — कोई रोग नहीं पाया गया",
    severity_en: "None (Optimum vigor)",
    severity_hi: "शून्य (उत्कृष्ट स्वास्थ्य)",
    confidence: "99.2%",
    spray_en: "Crop is completely healthy. Avoid unnecessary chemical sprays to save cost.",
    spray_hi: "फसल पूर्णतः स्वस्थ है। किसी भी कीटनाशक के अनावश्यक छिड़काव से बचें और केवल संतुलित नमी बनाए रखें।",
    organic_en: "Apply Jeevamrutha or vermiwash periodically to maintain natural plant vigor and immunity.",
    organic_hi: "संतुलित जीवामृत या वर्मीवाश का उपयोग करें ताकि पौधों की स्वाभाविक रोग प्रतिरोधक क्षमता बनी रहे।",
    chemical_en: "No chemical sprays required. Protect natural beneficial insects.",
    chemical_hi: "किसी रासायनिक छिड़काव की आवश्यकता नहीं है। लागत बचाएं।"
  }
};

// CURRENT APP STATE
let currentLang = "hi";
let currentHub = "nashik";
let currentLeafSample = "tomato_early_blight";

// APP INITIALIZATION
document.addEventListener("DOMContentLoaded", () => {
  initLanguageManager();
  setupTabs();
  setupHubSelector();
  setupLocationAutoDetect();
  setupSoilCardPreset();
  setupRecommendForm();
  setupPlantDoctor();
  setupVoiceSaathi();
  setupPHSlider();
  setupSupabaseHeartbeat();
});

// =========================================================================
// 1. LANGUAGE SELECTION & PERSISTENCE
// =========================================================================
function initLanguageManager() {
  const modal = document.getElementById("langModalBackdrop");
  const btnConfirm = document.getElementById("btnConfirmLanguage");
  const chkDefault = document.getElementById("chkSetDefaultLang");
  const topLangSelect = document.getElementById("topLanguageSelect");
  const btnOpenLangModal = document.getElementById("btnOpenLangModal");

  const savedLang = localStorage.getItem("kisaan_sathi_lang");
  const isDefaultSaved = localStorage.getItem("kisaan_sathi_is_default_lang") === "true";

  let tempSelectedLang = savedLang || "hi";

  if (savedLang && isDefaultSaved) {
    if (modal) modal.style.display = "none";
    setLanguage(savedLang);
    if (topLangSelect) topLangSelect.value = savedLang;
  } else {
    if (modal) modal.style.display = "flex";
    highlightModalCard(tempSelectedLang);
  }

  const langCards = document.querySelectorAll(".lang-card");
  langCards.forEach(card => {
    card.addEventListener("click", () => {
      tempSelectedLang = card.getAttribute("data-lang-code");
      highlightModalCard(tempSelectedLang);
    });
  });

  if (btnConfirm) {
    btnConfirm.addEventListener("click", () => {
      setLanguage(tempSelectedLang);
      localStorage.setItem("kisaan_sathi_lang", tempSelectedLang);
      if (chkDefault && chkDefault.checked) {
        localStorage.setItem("kisaan_sathi_is_default_lang", "true");
      } else {
        localStorage.removeItem("kisaan_sathi_is_default_lang");
      }
      if (topLangSelect) topLangSelect.value = tempSelectedLang;
      if (modal) modal.style.display = "none";
    });
  }

  if (topLangSelect) {
    topLangSelect.addEventListener("change", (e) => {
      setLanguage(e.target.value);
      localStorage.setItem("kisaan_sathi_lang", e.target.value);
    });
  }

  if (btnOpenLangModal && modal) {
    btnOpenLangModal.addEventListener("click", () => {
      tempSelectedLang = currentLang;
      highlightModalCard(tempSelectedLang);
      modal.style.display = "flex";
    });
  }
}

function highlightModalCard(langCode) {
  const cards = document.querySelectorAll(".lang-card");
  cards.forEach(c => {
    if (c.getAttribute("data-lang-code") === langCode) {
      c.classList.add("selected");
    } else {
      c.classList.remove("selected");
    }
  });
}

function setLanguage(lang) {
  currentLang = lang;
  const dict = I18N_DICTIONARY[lang] || I18N_DICTIONARY.hi;

  // Translate all [data-i18n] elements
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    if (dict[key]) {
      el.textContent = dict[key];
    }
  });

  // Re-render Hub, Weather, and Soil Preview in the new language
  if (DEMO_HUBS[currentHub]) {
    selectHub(currentHub);
  }

  // Re-render Plant Doctor
  if (LEAF_SAMPLES[currentLeafSample]) {
    renderLeafDiagnosis(LEAF_SAMPLES[currentLeafSample]);
  }
}

// =========================================================================
// 2. NAVIGATION TABS
// =========================================================================
function setupTabs() {
  const btns = document.querySelectorAll(".tab-btn");
  const panes = document.querySelectorAll(".tab-pane");

  btns.forEach(btn => {
    btn.addEventListener("click", () => {
      btns.forEach(b => b.classList.remove("active"));
      panes.forEach(p => p.classList.remove("active"));

      btn.classList.add("active");
      const target = btn.getAttribute("data-tab");
      const pane = document.getElementById(target);
      if (pane) pane.classList.add("active");
    });
  });
}

// =========================================================================
// 3. REGIONAL HUBS & AUTO-LOCATION (GPS)
// =========================================================================
function setupHubSelector() {
  const chips = document.querySelectorAll(".hub-chip");
  chips.forEach(chip => {
    chip.addEventListener("click", () => {
      chips.forEach(c => c.classList.remove("active"));
      chip.classList.add("active");

      const hubKey = chip.getAttribute("data-hub");
      selectHub(hubKey);
    });
  });
}

function setupLocationAutoDetect() {
  const btn = document.getElementById("btnAutoDetectLocation");
  if (btn) {
    btn.addEventListener("click", detectUserLocation);
  }
}

function detectUserLocation() {
  const statusEl = document.getElementById("locationDetectStatus");
  const btn = document.getElementById("btnAutoDetectLocation");
  if (!navigator.geolocation) {
    alert("Geolocation is not supported by your browser / जीपीएस उपलब्ध नहीं है");
    return;
  }

  statusEl.style.display = "inline-flex";
  statusEl.className = "location-status-badge detecting";
  statusEl.textContent = currentLang === "hi" ? "📡 स्थान खोजा जा रहा है..." : "📡 Detecting farm location...";
  if (btn) btn.disabled = true;

  navigator.geolocation.getCurrentPosition(
    (pos) => {
      if (btn) btn.disabled = false;
      const userLat = pos.coords.latitude;
      const userLon = pos.coords.longitude;

      // Find closest regional hub using Haversine formula
      let closestHub = "nashik";
      let minDistance = Infinity;

      for (const [key, hub] of Object.entries(DEMO_HUBS)) {
        const d = calculateDistance(userLat, userLon, hub.lat, hub.lon);
        if (d < minDistance) {
          minDistance = d;
          closestHub = key;
        }
      }

      if (closestHub) {
        const chips = document.querySelectorAll(".hub-chip");
        chips.forEach(c => {
          if (c.getAttribute("data-hub") === closestHub) {
            c.classList.add("active");
          } else {
            c.classList.remove("active");
          }
        });

        selectHub(closestHub);

        statusEl.className = "location-status-badge success";
        const h = DEMO_HUBS[closestHub];
        const hubName = (currentLang === "en") ? h.name_en : h.name_hi;
        statusEl.textContent = (currentLang === "en")
          ? `📍 Detected: ${hubName} (GPS: ${userLat.toFixed(2)}°, ${userLon.toFixed(2)}°)`
          : `📍 पाया गया: ${hubName} (GPS: ${userLat.toFixed(2)}°, ${userLon.toFixed(2)}°)`;
      }
    },
    (err) => {
      if (btn) btn.disabled = false;
      statusEl.className = "location-status-badge error";
      statusEl.textContent = (currentLang === "en")
        ? "⚠️ Location permission denied"
        : "⚠️ स्थान की अनुमति नहीं मिली";
      setTimeout(() => { statusEl.style.display = "none"; }, 4000);
    },
    { enableHighAccuracy: true, timeout: 10000 }
  );
}

function calculateDistance(lat1, lon1, lat2, lon2) {
  const R = 6371; // Earth radius in km
  const dLat = (lat2 - lat1) * Math.PI / 180;
  const dLon = (lon2 - lon1) * Math.PI / 180;
  const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
            Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
            Math.sin(dLon / 2) * Math.sin(dLon / 2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  return R * c;
}

function selectHub(key) {
  currentHub = key;
  const hub = DEMO_HUBS[key];
  if (!hub) return;

  const isEn = (currentLang === "en");

  // Weather Card
  document.getElementById("weatherHubName").textContent = isEn ? hub.name_en : hub.name_hi;
  document.getElementById("weatherCondition").textContent = isEn ? hub.weather.cond_en : hub.weather.cond_hi;
  document.getElementById("weatherTemp").textContent = hub.weather.temp;
  document.getElementById("weatherHumidity").textContent = hub.weather.hum;
  document.getElementById("weatherRain").textContent = hub.weather.rain;
  document.getElementById("weatherEmoji").textContent = hub.weather.icon;
  document.getElementById("weatherSprayText").textContent = isEn ? hub.weather.spray_en : hub.weather.spray_hi;

  // Form Inputs
  document.getElementById("inputState").value = hub.state;
  document.getElementById("inputDistrict").value = hub.district;
  document.getElementById("inputN").value = hub.soil.n;
  document.getElementById("inputP").value = hub.soil.p;
  document.getElementById("inputK").value = hub.soil.k;
  document.getElementById("inputPH").value = hub.soil.ph;
  updatePHDisplay(hub.soil.ph);

  // Update Soil Card Preview Box
  updateSoilCardPreviewBox({
    texture: hub.soil.type,
    farmer: hub.soil.farmer,
    n: hub.soil.n,
    p: hub.soil.p,
    k: hub.soil.k,
    ph: hub.soil.ph,
    oc: hub.soil.oc || 0.65
  });

  // Update Recommendation View in Selected Language
  updateRecommendationUI(hub);
}

// =========================================================================
// 4. SOIL HEALTH CARD PRESETS & LIVE PREVIEW BOX
// =========================================================================
function setupSoilCardPreset() {
  const select = document.getElementById("soilCardPresetSelect");
  if (!select) return;

  select.addEventListener("change", () => {
    const val = select.value;
    const card = SAMPLE_SOIL_CARDS_MAP[val];
    if (card) {
      selectHub(card.hub);
      updateSoilCardPreviewBox(card);
    }
  });

  if (DEMO_HUBS[currentHub]) {
    const h = DEMO_HUBS[currentHub];
    updateSoilCardPreviewBox({
      texture: h.soil.type,
      farmer: h.soil.farmer,
      n: h.soil.n,
      p: h.soil.p,
      k: h.soil.k,
      ph: h.soil.ph,
      oc: h.soil.oc || 0.72
    });
  }
}

function updateSoilCardPreviewBox(card) {
  const badge = document.getElementById("soilTextureBadge");
  const farmer = document.getElementById("soilFarmerName");
  const pillN = document.getElementById("soilPillN");
  const pillP = document.getElementById("soilPillP");
  const pillK = document.getElementById("soilPillK");
  const pillPH = document.getElementById("soilPillPH");
  const pillOC = document.getElementById("soilPillOC");

  if (badge) badge.textContent = `🪨 ${card.texture}`;
  if (farmer) farmer.textContent = `Farmer: ${card.farmer}`;
  if (pillN) pillN.textContent = `N: ${card.n} (${card.n > 80 ? 'High' : (card.n < 40 ? 'Low' : 'Med')})`;
  if (pillP) pillP.textContent = `P: ${card.p} (${card.p > 55 ? 'High' : (card.p < 30 ? 'Low' : 'Med')})`;
  if (pillK) pillK.textContent = `K: ${card.k} (${card.k > 150 ? 'High' : (card.k < 60 ? 'Low' : 'Med')})`;
  if (pillPH) pillPH.textContent = `pH: ${card.ph} (${card.ph < 6.0 ? 'Acidic' : (card.ph > 7.5 ? 'Alkaline' : 'Neutral')})`;
  if (pillOC) pillOC.textContent = `OC: ${card.oc}% (${card.oc > 0.7 ? 'Good' : 'Moderate'})`;
}

function setupPHSlider() {
  const slider = document.getElementById("inputPH");
  if (slider) {
    slider.addEventListener("input", (e) => {
      updatePHDisplay(e.target.value);
    });
  }
}

function updatePHDisplay(val) {
  const v = parseFloat(val);
  let status = "Neutral";
  const isEn = (currentLang === "en");
  if (v < 6.0) status = isEn ? "Acidic" : "अम्लीय";
  else if (v > 7.5) status = isEn ? "Alkaline" : "क्षारीय";
  else status = isEn ? "Neutral / Ideal" : "संतुलित / उत्तम";

  const el = document.getElementById("phDisplay");
  if (el) el.textContent = `${v} (${status})`;
}

// =========================================================================
// 5. CROP RECOMMENDATION & EXPLAINABILITY ENGINE
// =========================================================================
function setupRecommendForm() {
  const form = document.getElementById("recommendForm");
  if (!form) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const btn = document.getElementById("btnRecommend");
    const originalText = btn.innerHTML;
    btn.innerHTML = (currentLang === "en")
      ? "<span>⏳ Analyzing Farm Parameters...</span>"
      : "<span>⏳ खेत का विश्लेषण हो रहा है...</span>";
    btn.disabled = true;

    const payload = {
      latitude: DEMO_HUBS[currentHub]?.lat || 19.9975,
      longitude: DEMO_HUBS[currentHub]?.lon || 73.7898,
      state: document.getElementById("inputState").value,
      district: document.getElementById("inputDistrict").value,
      farm_size_acres: parseFloat(document.getElementById("inputFarmSize").value) || 2.5,
      irrigation_source: document.getElementById("inputIrrigation").value,
      previous_crop: document.getElementById("inputPrevCrop").value,
      custom_soil: {
        nitrogen: parseFloat(document.getElementById("inputN").value),
        phosphorus: parseFloat(document.getElementById("inputP").value),
        potassium: parseFloat(document.getElementById("inputK").value),
        ph: parseFloat(document.getElementById("inputPH").value)
      }
    };

    try {
      const res = await fetch("/api/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      if (res.ok) {
        const data = await res.json();
        renderAPIRecommendation(data);
      } else {
        updateRecommendationUI(DEMO_HUBS[currentHub]);
      }
    } catch (_) {
      updateRecommendationUI(DEMO_HUBS[currentHub]);
    } finally {
      btn.innerHTML = originalText;
      btn.disabled = false;
      addActivityLog(`Crop Advisory: ${payload.district}`, `Recommendation Generated • N:${payload.custom_soil.nitrogen}, P:${payload.custom_soil.phosphorus}, K:${payload.custom_soil.potassium}`);
    }
  });
}

function updateRecommendationUI(hub) {
  const isEn = (currentLang === "en");

  const topCropName = isEn ? hub.topCrop.name_en : hub.topCrop.name_hi;
  document.getElementById("topCropName").textContent = topCropName;
  document.getElementById("topCropFamily").textContent = hub.topCrop.family;
  document.getElementById("topCropScore").textContent = hub.topCrop.score;
  document.getElementById("topCropYield").textContent = hub.topCrop.yield;
  document.getElementById("topCropRev").textContent = hub.topCrop.rev;
  document.getElementById("topCropRate").textContent = hub.topCrop.rate;
  document.getElementById("topCropSowing").textContent = hub.topCrop.sowing;

  // Localized Explanation Text
  const shapText = isEn ? hub.shap_en : hub.shap_hi;
  document.getElementById("shapExplanationText").textContent = `"${shapText}"`;

  // Bars
  const barsContainer = document.getElementById("shapBarsList");
  if (barsContainer && hub.shapBars) {
    barsContainer.innerHTML = hub.shapBars.map(b => `
      <div class="shap-bar-row">
        <span class="shap-feat">${b.name}</span>
        <div class="shap-bar-track">
          <div class="shap-fill ${b.pos ? 'positive' : 'negative'}" style="width: ${b.pct}%"></div>
        </div>
        <span class="shap-impact ${b.pos ? 'text-green' : 'text-red'}">${b.val}</span>
      </div>
    `).join("");
  }

  // Runners up
  const runnersContainer = document.getElementById("runnersList");
  if (runnersContainer && hub.runners) {
    runnersContainer.innerHTML = hub.runners.map(r => `
      <div class="runner-card">
        <div class="runner-header">
          <span class="runner-name">${isEn ? r.name_en : r.name_hi}</span>
          <span class="runner-score">${r.score}</span>
        </div>
        <div class="runner-meta">${r.meta}</div>
      </div>
    `).join("");
  }
}

function renderAPIRecommendation(data) {
  const isEn = (currentLang === "en");
  const rec = data.top_recommendation || data.ranked_crops?.[0];
  if (!rec) return;

  const cropTitle = isEn
    ? (rec.crop_name_en || rec.crop || "Recommended Crop")
    : (rec.crop_name_hi || rec.crop_hindi || rec.crop || "अनुशंसित फसल");

  document.getElementById("topCropName").textContent = `🌾 ${cropTitle}`;
  document.getElementById("topCropScore").textContent = `${Math.round((rec.confidence || rec.final_score || 0.92) * 100)}%`;

  if (rec.estimated_yield) {
    document.getElementById("topCropYield").textContent = rec.estimated_yield;
  }
  if (rec.estimated_revenue) {
    document.getElementById("topCropRev").textContent = rec.estimated_revenue;
  }
  if (rec.mandi_price) {
    document.getElementById("topCropRate").textContent = `₹${rec.mandi_price} / Qtl`;
  }

  const expText = isEn
    ? (rec.farmer_explanation_en || rec.explanation || "This crop matches your regional soil and weather profile.")
    : (rec.farmer_explanation_hi || rec.explanation || "यह फसल आपकी मिट्टी के पोषक तत्वों और मौसम के लिए सबसे उपयुक्त है।");
  document.getElementById("shapExplanationText").textContent = `"${expText}"`;
}

// =========================================================================
// 6. PLANT DOCTOR & LEAF PATHOLOGY
// =========================================================================
function setupPlantDoctor() {
  const chips = document.querySelectorAll(".leaf-thumb-btn");
  chips.forEach(chip => {
    chip.addEventListener("click", () => {
      chips.forEach(c => c.classList.remove("active"));
      chip.classList.add("active");

      const key = chip.getAttribute("data-sample");
      currentLeafSample = key;
      const sample = LEAF_SAMPLES[key];
      if (sample) {
        renderLeafDiagnosis(sample);
      }
    });
  });

  const btnDiagnose = document.getElementById("btnDiagnose");
  if (btnDiagnose) {
    btnDiagnose.addEventListener("click", () => {
      const sample = LEAF_SAMPLES[currentLeafSample];
      if (sample) {
        renderLeafDiagnosis(sample);
        addActivityLog(`Plant Doctor: ${sample.crop_en}`, `Diagnosis Completed • ${sample.name_en} (${sample.confidence})`);
      }
    });
  }

  // Init default sample
  if (LEAF_SAMPLES[currentLeafSample]) {
    renderLeafDiagnosis(LEAF_SAMPLES[currentLeafSample]);
  }
}

function renderLeafDiagnosis(sample) {
  const isEn = (currentLang === "en");

  const cropEl = document.getElementById("diagCrop");
  const nameEl = document.getElementById("diagDiseaseName");
  const confEl = document.getElementById("diagConfidence");
  const sprayEl = document.getElementById("diagSprayTiming");
  const orgEl = document.getElementById("diagOrganicRemedy");
  const chemEl = document.getElementById("diagChemicalRemedy");

  if (cropEl) cropEl.textContent = isEn ? sample.crop_en : sample.crop_hi;
  if (nameEl) nameEl.textContent = isEn ? sample.name_en : sample.name_hi;
  if (confEl) confEl.textContent = `${sample.confidence} Reliability`;
  if (sprayEl) sprayEl.textContent = isEn ? sample.spray_en : sample.spray_hi;
  if (orgEl) orgEl.textContent = isEn ? sample.organic_en : sample.organic_hi;
  if (chemEl) chemEl.textContent = isEn ? sample.chemical_en : sample.chemical_hi;
}

// =========================================================================
// 7. VOICE SAATHI (AI VOICE ADVISOR)
// =========================================================================
function setupVoiceSaathi() {
  const input = document.getElementById("voiceInputText");
  const btnAsk = document.getElementById("btnAskVoice");
  const btnListen = document.getElementById("btnListenVoice");
  const chips = document.querySelectorAll(".voice-chip");

  chips.forEach(chip => {
    chip.addEventListener("click", () => {
      const q = chip.getAttribute("data-q");
      if (input) {
        input.value = q;
        sendVoiceQuery(q);
      }
    });
  });

  if (btnAsk) {
    btnAsk.addEventListener("click", () => {
      const q = input?.value?.trim();
      if (q) sendVoiceQuery(q);
    });
  }

  if (btnListen) {
    btnListen.addEventListener("click", () => {
      const resp = document.getElementById("voiceResponseText")?.textContent;
      if (resp && 'speechSynthesis' in window) {
        window.speechSynthesis.cancel();
        const utter = new SpeechSynthesisUtterance(resp);
        const dict = I18N_DICTIONARY[currentLang] || I18N_DICTIONARY.hi;
        utter.lang = dict.speechCode || 'hi-IN';
        window.speechSynthesis.speak(utter);
      }
    });
  }
}

async function sendVoiceQuery(query) {
  const respBox = document.getElementById("voiceResponseText");
  const followupsBox = document.getElementById("voiceFollowups");
  if (!respBox) return;

  respBox.textContent = (currentLang === "en") ? "Thinking & formulating farming advice..." : "सलाह तैयार की जा रही है...";

  try {
    const res = await fetch("/api/voice/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        query: query,
        language: currentLang,
        district: DEMO_HUBS[currentHub]?.district || "Nashik",
        state: DEMO_HUBS[currentHub]?.state || "Maharashtra",
        crop: DEMO_HUBS[currentHub]?.topCrop?.name_en || "Crop"
      })
    });

    if (res.ok) {
      const data = await res.json();
      respBox.textContent = data.response_text || data.answer || "सलाह प्राप्त हुई।";

      if (data.followup_questions && followupsBox) {
        followupsBox.innerHTML = data.followup_questions.map(q => `
          <button class="voice-chip followup" onclick="sendVoiceQuery('${q.replace(/'/g, "\\'")}')">💬 ${q}</button>
        `).join("");
      }
    } else {
      respBox.textContent = getLocalVoiceFallback(query);
    }
  } catch (_) {
    respBox.textContent = getLocalVoiceFallback(query);
  } finally {
    addActivityLog(`Voice Advisory: ${query.slice(0, 25)}...`, `Response Generated in ${currentLang.toUpperCase()}`);
  }
}

function getLocalVoiceFallback(q) {
  const isEn = (currentLang === "en");
  if (q.includes("पानी") || q.includes("water") || q.includes("irrigation")) {
    return isEn
      ? "Maintain 65-75% soil moisture. Irrigate through drip or furrow every 4-5 days during fruit development."
      : "मिट्टी में 65-75% नमी बनाए रखें। फल व दाना बनते समय हर 4-5 दिन में ड्रिप या क्यारियों द्वारा सिंचाई करें।";
  }
  if (q.includes("खाद") || q.includes("fertilizer") || q.includes("NPK")) {
    return isEn
      ? "Apply recommended NPK dosage with 5 tonnes of well-rotted FYM per acre before sowing. Top-dress nitrogen in split doses."
      : "बुवाई से पहले प्रति एकड़ 5 टन गोबर की खाद डालें और अनुशंसित NPK मात्रा को 2-3 खुराकों में दें।";
  }
  return isEn
    ? "Maintain regular crop scouting, weed control, and consult local Krishi Vigyan Kendra for certified seeds."
    : "नियमित खेत निरीक्षण करें, खरपतवार नियंत्रण रखें और प्रमाणित बीजों का ही उपयोग करें।";
}

// =========================================================================
// 8. SUPABASE LIVE SYNC & ACTIVITY LOGGER
// =========================================================================
function setupSupabaseHeartbeat() {
  const btnPing = document.getElementById("btnPingSupabase");
  if (btnPing) {
    btnPing.addEventListener("click", async () => {
      const original = btnPing.innerHTML;
      btnPing.innerHTML = "<span>⏳ Syncing...</span>";
      try {
        const res = await fetch("/api/db-ping");
        if (res.ok) {
          addActivityLog("Supabase Database Sync", "Ping Success • Database active & connected");
          alert(currentLang === "en" ? "✓ Cloud Database Active & Synchronized!" : "✓ क्लाउड डेटाबेस सक्रिय व सिंक है!");
        }
      } finally {
        btnPing.innerHTML = original;
      }
    });
  }
}

function addActivityLog(title, desc) {
  const stream = document.getElementById("activityStream");
  if (!stream) return;

  const now = new Date().toLocaleTimeString();
  const item = document.createElement("div");
  item.className = "activity-item";
  item.innerHTML = `
    <div class="activity-dot"></div>
    <div class="activity-content">
      <div class="activity-title">${title} <span class="activity-time">${now}</span></div>
      <div class="activity-desc">${desc}</div>
    </div>
  `;
  stream.insertBefore(item, stream.firstChild);

  // Keep max 8 items
  while (stream.children.length > 8) {
    stream.removeChild(stream.lastChild);
  }
}
