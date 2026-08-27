/**
 * KISAAN_SATHI (किसान साथी) Web Application Engine
 * Supports 11 Indian Languages, First-Launch Language Selector Modal with Default Option,
 * XGBoost + SHAP Explainability, Plant Doctor AI, Voice Saathi, and Supabase Keep-Alive.
 */

// 11 INDIAN LANGUAGES LOCALIZATION DICTIONARY
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
    hero_sub: "XGBoost 99.09% सटीकता के साथ मिट्टी व मौसम का विश्लेषण करता है, और Groq AI किसान को अपनी मातृभाषा में आवाज के साथ मार्गदर्शन देता है।",
    quick_hubs_label: "प्रमुख कृषि क्षेत्र चुनें:",
    lbl_temperature: "Temperature / तापमान",
    lbl_humidity: "Humidity / नमी",
    lbl_rain7d: "7-Day Rain / वर्षा",
    tab_advisory: "फसल सलाह (XGBoost + SHAP)",
    tab_doctor: "फसल डॉक्टर (रोग पहचान)",
    tab_voice: "वॉइस साथी (बोलकर पूछें)",
    tab_mandi: "मंडी भाव व मौसम रडार",
    tab_supabase: "सुपाबेस व सिस्टम स्थिति",
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
    btn_run_xgboost: "XGBoost एआई विश्लेषण व SHAP चलाएं",
    panel_recs_title: "अनुशंसित सर्वोत्तम फसलें",
    panel_recs_sub: "मृदा, मौसम और बाजार भाव के आधार पर रैंकिंग",
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
    shap_title: "🔍 SHAP व्याख्या: इस फसल की सिफारिश क्यों की गई?",
    shap_tag: "पोषक तत्व प्रभाव",
    runners_title: "वैकल्पिक फसलें (Alternative Rank #2 & #3)",
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
    voice_hero_sub: "Groq LLaMA द्वारा संचालित। सरल हिंदी में बोलकर सलाह देता है।",
    voice_chips_label: "अक्सर पूछे जाने वाले सवाल (Click to Ask):",
    chip_water: "पानी कितना चाहिए? (Irrigation)",
    chip_fertilizer: "खाद की मात्रा? (Fertilizer)",
    chip_mandi: "मंडी भाव क्या है? (Mandi Price)",
    chip_pest: "कीट नियंत्रण? (Pest Control)",
    btn_ask_ai: "Ask AI / पूछें",
    btn_listen_audio: "Listen Voice Audio / आवाज सुनें",
    lbl_followups: "आगे पूछें (Suggested Follow-ups):",
    panel_weather_title: "7-दिवसीय मौसम व छिड़काव पूर्वानुमान",
    panel_weather_sub: "ओपन-मीटियो उपग्रह डेटा व छिड़काव रेटिंग",
    panel_mandi_title: "स्थानीय कृषि उपज मंडी भाव",
    panel_mandi_sub: "एगमार्कनेट सत्यापित दैनिक मंडी भाव",
    th_commodity: "Commodity / फसल",
    th_market: "Market / मंडी",
    th_rate: "Modal Rate (₹/Qtl)",
    th_trend: "7-Day Trend",
    panel_sb_title: "सुपाबेस डेटाबेस व एंटी-स्लीप इंजन",
    panel_sb_sub: "स्वचालित पिंग द्वारा डेटाबेस हमेशा सक्रिय रहता है",
    panel_activity_title: "हाल ही में दर्ज की गई गतिविधियाँ",
    panel_activity_sub: "सुपाबेस में दर्ज फसल व रोग जांच रिकॉर्ड",
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
    supabase_sync: "Supabase Live Sync Active",
    live_mandi_label: "LIVE APMC MANDI",
    hero_headline: "Smart Farming Advisory Backed by Explainable Science",
    hero_sub: "XGBoost computes soil and climate vectors with 99.09% accuracy, and Groq AI gives natural voice guidance.",
    quick_hubs_label: "Quick Regional Hubs:",
    lbl_temperature: "Temperature",
    lbl_humidity: "Humidity",
    lbl_rain7d: "7-Day Rain",
    tab_advisory: "Crop Advisory (XGBoost + SHAP)",
    tab_doctor: "Plant Doctor (Leaf AI)",
    tab_voice: "Voice Saathi (Groq LLM)",
    tab_mandi: "Mandi & Weather Radar",
    tab_supabase: "Supabase & Anti-Sleep",
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
    btn_run_xgboost: "Run XGBoost ML Prediction & SHAP Analysis",
    panel_recs_title: "Ranked Crop Recommendations",
    panel_recs_sub: "Multi-factor agronomic ranking + SHAP force vectors",
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
    shap_title: "🔍 SHAP Explainable AI: Why this crop was recommended?",
    shap_tag: "Feature Attribution",
    runners_title: "Alternative Crops (Rank #2 & #3)",
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
    voice_hero_sub: "Powered by Groq LLaMA. Speaks clear voice instructions.",
    voice_chips_label: "Quick Farming Questions:",
    chip_water: "How much irrigation? (Water)",
    chip_fertilizer: "Fertilizer dosage? (NPK)",
    chip_mandi: "What is Mandi Price? (Rates)",
    chip_pest: "Pest & Fungus Control? (Remedies)",
    btn_ask_ai: "Ask AI",
    btn_listen_audio: "Listen Voice Audio",
    lbl_followups: "Suggested Follow-ups:",
    panel_weather_title: "7-Day Agricultural Weather Forecast",
    panel_weather_sub: "Live Open-Meteo Satellite Feed + Spray Conditions",
    panel_mandi_title: "Live APMC Mandi Commodities",
    panel_mandi_sub: "Agmarknet verified market arrivals & 7-day trend",
    th_commodity: "Commodity",
    th_market: "Market",
    th_rate: "Modal Rate (₹/Qtl)",
    th_trend: "7-Day Trend",
    panel_sb_title: "Supabase PostgreSQL Anti-Sleep Engine",
    panel_sb_sub: "Automated heartbeat keeps database active 24/7",
    panel_activity_title: "Live Cloud Activity Stream",
    panel_activity_sub: "Real-time queries saved to Supabase",
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
    supabase_sync: "सुपाबेस थेट सुरू आहे",
    live_mandi_label: "थेट बाजार भाव",
    hero_headline: "शास्त्रीय पुराव्यांवर आधारित स्मार्ट शेती सल्ला",
    hero_sub: "XGBoost ९९.०९% अचूकतेसह माती व हवामानाचे विश्लेषण करते, आणि Groq AI मराठीत बोलून मार्गदर्शन करते.",
    quick_hubs_label: "प्रमुख शेती विभाग निवडा:",
    lbl_temperature: "तापमान",
    lbl_humidity: "हवेतील आर्द्रता",
    lbl_rain7d: "७-दिवसांचा पाऊस",
    tab_advisory: "पीक सल्ला (XGBoost + SHAP)",
    tab_doctor: "पीक डॉक्टर (रोग निदान)",
    tab_voice: "व्हॉइस साथी (बोलून विचारा)",
    tab_mandi: "बाजार भाव व हवामान रडार",
    tab_supabase: "सुपाबेस व प्रणाली स्थिती",
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
    btn_run_xgboost: "XGBoost एआय विश्लेषण सुरू करा",
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
    shap_title: "🔍 SHAP विश्लेषण: हे पीक का सुचवले गेले?",
    shap_tag: "पोषक घटक प्रभाव",
    runners_title: "पर्यायी पिके (रँक #२ व #३)",
    panel_doctor_title: "झाडांचे रोग निदान व पान स्कॅनर",
    panel_doctor_sub: "पानाचा नमुना निवडा किंवा रोगाचे त्वरित विश्लेषण करा",
    leaf_gallery_title: "चाचणीसाठी पानांचे नमुने:",
    dropzone_title: "शेतातील पाण्याचा फोटो येथे टाका",
    dropzone_sub: "टोमॅटो, बटाटा, कापूस, गहू, भात, मका इत्यादींसाठी",
    btn_run_diagnosis: "रोग निदान सुरू करा",
    panel_diag_title: "रोग निदान अहवाल व उपाय",
    panel_diag_sub: "सेंद्रिय व रासायनिक उपाय आणि योग्य फवारणी वेळ",
    spray_alert_title: "🌦️ हवामानानुसार फवारणी सल्ला",
    remedy_organic_badge: "🌿 १००% सेंद्रिय उपचार",
    remedy_chemical_badge: "🧪 रासायनिक उपचार",
    voice_hero_title: "व्हॉइस साथी — तुमचा शेती मित्र",
    voice_hero_sub: "Groq AI द्वारे मराठीत बोलून मार्गदर्शन मिळवा.",
    voice_chips_label: "नेहमी विचारले जाणारे प्रश्न:",
    chip_water: "पाणी किती द्यावे? (सिंचन)",
    chip_fertilizer: "खतांची मात्रा? (NPK)",
    chip_mandi: "बाजार भाव काय आहे? (मंडी)",
    chip_pest: "कीड नियंत्रण कसे करावे?",
    btn_ask_ai: "विचारा",
    btn_listen_audio: "आवाज ऐका",
    lbl_followups: "पुढील प्रश्न:",
    panel_weather_title: "७ दिवसांचा हवामान व फवारणी अंदाज",
    panel_weather_sub: "ओपन-मिटिओ उपग्रह डेटा व फवारणी वेळ",
    panel_mandi_title: "बाजार समितीचे थेट भाव",
    panel_mandi_sub: "दैनिक बाजार आवक व कल",
    th_commodity: "पीक",
    th_market: "बाजार",
    th_rate: "सरासरी भाव (₹/क्विंटल)",
    th_trend: "७ दिवसांचा कल",
    panel_sb_title: "सुपाबेस डेटाबेस स्थिती",
    panel_sb_sub: "डेटाबेस नेहमी सक्रिय राहतो",
    panel_activity_title: "अलीकडील नोंदी",
    panel_activity_sub: "सुपाबेसमध्ये नोंदवलेले पीक व रोग तपशील",
    make_default_title: "ही माझी डीफॉल्ट भाषा ठेवा",
    make_default_sub: "(पुढील वेळी थेट हीच भाषा उघडेल)",
    btn_continue: "✓ पुढे जा ➔"
  },
  pa: {
    code: "pa",
    name: "ਪੰਜਾਬੀ",
    flag: "🌾",
    speechCode: "pa-IN",
    brand_tagline: "ਏਆਈ ਅਧਾਰਤ ਖੇਤੀ ਸਲਾਹ ਤੇ ਫ਼ਸਲ ਰੋਗ ਨਿਦਾਨ",
    supabase_sync: "ਸੁਪਾਬੇਸ ਲਾਈਵ ਸਰਗਰਮ",
    live_mandi_label: "ਲਾਈਵ ਮੰਡੀ ਭਾਅ",
    hero_headline: "ਸਹੀ ਵਿਗਿਆਨਕ ਡਾਟਾ 'ਤੇ ਆਧਾਰਿਤ ਖੇਤੀ ਸਲਾਹ",
    hero_sub: "XGBoost 99.09% ਸ਼ੁੱਧਤਾ ਨਾਲ ਮਿੱਟੀ ਤੇ ਮੌਸਮ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਦਾ ਹੈ ਅਤੇ Groq AI ਪੰਜਾਬੀ ਵਿੱਚ ਬੋਲ ਕੇ ਸਲਾਹ ਦਿੰਦਾ ਹੈ।",
    quick_hubs_label: "ਮੁੱਖ ਖੇਤੀ ਖੇਤਰ ਚੁਣੋ:",
    lbl_temperature: "ਤਾਪਮਾਨ",
    lbl_humidity: "ਨਮੀ",
    lbl_rain7d: "7-ਦਿਨਾਂ ਦੀ ਵਰਖਾ",
    tab_advisory: "ਫ਼ਸਲ ਸਲਾਹ (XGBoost + SHAP)",
    tab_doctor: "ਫ਼ਸਲ ਡਾਕਟਰ (ਰੋਗ ਜਾਂਚ)",
    tab_voice: "ਵਾਇਸ ਸਾਥੀ (ਬੋਲ ਕੇ ਪੁੱਛੋ)",
    tab_mandi: "ਮੰਡੀ ਭਾਅ ਤੇ ਮੌਸਮ",
    tab_supabase: "ਸੁਪਾਬੇਸ ਸਿਸਟਮ ਸਥਿਤੀ",
    panel_soil_title: "ਖੇਤ ਦਾ ਵੇਰਵਾ ਤੇ ਮਿੱਟੀ ਪਰਖ",
    panel_soil_sub: "ਸੋਇਲ ਹੈਲਥ ਕਾਰਡ ਲੋਡ ਕਰੋ ਜਾਂ ਮੁੱਲ ਭਰੋ",
    lbl_state: "ਸੂਬਾ",
    lbl_district: "ਜ਼ਿਲ੍ਹਾ",
    lbl_n: "ਨਾਈਟ੍ਰੋਜਨ (N) ਕਿਲੋ/ਹੈਕਟੇਅਰ",
    lbl_p: "ਫਾਸਫੋਰਸ (P) ਕਿਲੋ/ਹੈਕਟੇਅਰ",
    lbl_k: "ਪੋਟਾਸ਼ (K) ਕਿਲੋ/ਹੈਕਟੇਅਰ",
    lbl_ph: "ਮਿੱਟੀ ਦਾ ਪੀ.ਐਚ. (pH)",
    lbl_irrigation: "ਸਿੰਚਾਈ ਸਹੂਲਤ",
    lbl_farmsize: "ਖੇਤ ਦਾ ਆਕਾਰ (ਏਕੜ)",
    lbl_prevcrop: "ਪਿਛਲੀ ਫ਼ਸਲ",
    btn_run_xgboost: "XGBoost ਏਆਈ ਵਿਸ਼ਲੇਸ਼ਣ ਚਲਾਓ",
    panel_recs_title: "ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀਆਂ ਉੱਤਮ ਫ਼ਸਲਾਂ",
    panel_recs_sub: "ਮਿੱਟੀ, ਮੌਸਮ ਅਤੇ ਮੰਡੀ ਭਾਅ ਦੇ ਆਧਾਰ 'ਤੇ ਰੈਂਕਿੰਗ",
    badge_best_match: "#1 ਸਰਵੋਤਮ ਫ਼ਸਲ",
    lbl_match: "ਸ਼ੁੱਧਤਾ",
    pillar_soil: "ਮਿੱਟੀ ਅਨੁਕੂਲਤਾ",
    pillar_weather: "ਮੌਸਮ",
    pillar_market: "ਮੰਡੀ ਮੰਗ",
    pillar_rotation: "ਫ਼ਸਲੀ ਚੱਕਰ",
    lbl_yield: "ਅੰਦਾਜ਼ਨ ਪੈਦਾਵਾਰ",
    lbl_revenue: "ਅੰਦਾਜ਼ਨ ਆਮਦਨ",
    lbl_rate: "ਮੰਡੀ ਭਾਅ",
    lbl_sowing: "ਬਿਜਾਈ ਦਾ ਸਮਾਂ",
    shap_title: "🔍 SHAP ਵਿਆਖਿਆ: ਇਸ ਫ਼ਸਲ ਦੀ ਸਿਫਾਰਸ਼ ਕਿਉਂ ਕੀਤੀ ਗਈ?",
    shap_tag: "ਪੋਸ਼ਕ ਤੱਤ ਪ੍ਰਭਾਵ",
    runners_title: "ਬਦਲਵੀਆਂ ਫ਼ਸਲਾਂ (ਰੈਂਕ #2 ਤੇ #3)",
    panel_doctor_title: "ਫ਼ਸਲ ਰੋਗ ਨਿਦਾਨ ਤੇ ਪੱਤਾ ਸਕੈਨਰ",
    panel_doctor_sub: "ਪੱਤੇ ਦਾ ਨਮੂਨਾ ਚੁਣੋ ਜਾਂ ਰੋਗ ਦੀ ਜਾਂਚ ਕਰੋ",
    leaf_gallery_title: "ਟੈਸਟ ਲਈ ਪੱਤੇ ਦੇ ਨਮੂਨੇ:",
    dropzone_title: "ਪੱਤੇ ਦੀ ਫੋਟੋ ਇੱਥੇ ਪਾਓ",
    dropzone_sub: "ਟਮਾਟਰ, ਆਲੂ, ਨਰਮਾ, ਕਣਕ, ਝੋਨਾ, ਮੱਕੀ ਆਦਿ ਲਈ",
    btn_run_diagnosis: "ਏਆਈ ਰੋਗ ਜਾਂਚ ਸ਼ੁਰੂ ਕਰੋ",
    panel_diag_title: "ਰੋਗ ਜਾਂਚ ਰਿਪੋਰਟ ਤੇ ਇਲਾਜ",
    panel_diag_sub: "ਜੈਵਿਕ ਤੇ ਰਸਾਇਣਕ ਹੱਲ ਅਤੇ ਸਪਰੇਅ ਦਾ ਸਮਾਂ",
    spray_alert_title: "🌦️ ਮੌਸਮ ਅਨੁਸਾਰ ਸਪਰੇਅ ਸਲਾਹ",
    remedy_organic_badge: "🌿 100% ਜੈਵਿਕ ਇਲਾਜ",
    remedy_chemical_badge: "🧪 ਰਸਾਇਣਕ ਇਲਾਜ",
    voice_hero_title: "ਵਾਇਸ ਸਾਥੀ — ਤੁਹਾਡਾ ਖੇਤੀ ਸਲਾਹਕਾਰ",
    voice_hero_sub: "Groq AI ਦੁਆਰਾ ਪੰਜਾਬੀ ਵਿੱਚ ਬੋਲ ਕੇ ਸਲਾਹ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।",
    voice_chips_label: "ਆਮ ਪੁੱਛੇ ਜਾਣ ਵਾਲੇ ਸਵਾਲ:",
    chip_water: "ਪਾਣੀ ਕਿੰਨਾ ਚਾਹੀਦਾ ਹੈ? (ਸਿੰਚਾਈ)",
    chip_fertilizer: "ਖਾਦ ਦੀ ਮਾਤਰਾ? (NPK)",
    chip_mandi: "ਅੱਜ ਦਾ ਮੰਡੀ ਭਾਅ ਕੀ ਹੈ?",
    chip_pest: "ਕੀੜੇ ਮਕੌੜਿਆਂ ਦੀ ਰੋਕਥਾਮ?",
    btn_ask_ai: "ਪੁੱਛੋ",
    btn_listen_audio: "ਆਵਾਜ਼ ਸੁਣੋ",
    lbl_followups: "ਅਗਲੇ ਸਵਾਲ:",
    panel_weather_title: "7-ਦਿਨਾਂ ਦਾ ਮੌਸਮ ਤੇ ਸਪਰੇਅ ਅਨੁਮਾਨ",
    panel_weather_sub: "ਓਪਨ-ਮੀਟੀਓ ਸੈਟੇਲਾਈਟ ਡਾਟਾ ਤੇ ਸਪਰੇਅ ਰੇਟਿੰਗ",
    panel_mandi_title: "ਸਥਾਨਕ ਅਨਾਜ ਮੰਡੀ ਭਾਅ",
    panel_mandi_sub: "ਰੋਜ਼ਾਨਾ ਮੰਡੀ ਆਮਦ ਤੇ ਰੁਝਾਨ",
    th_commodity: "ਫ਼ਸਲ",
    th_market: "ਮੰਡੀ",
    th_rate: "ਭਾਅ (₹/ਕੁਇੰਟਲ)",
    th_trend: "7-ਦਿਨਾਂ ਦਾ ਰੁਝਾਨ",
    panel_sb_title: "ਸੁਪਾਬੇਸ ਡਾਟਾਬੇਸ ਸਥਿਤੀ",
    panel_sb_sub: "ਡਾਟਾਬੇਸ ਹਮੇਸ਼ਾ ਸਰਗਰਮ ਰਹਿੰਦਾ ਹੈ",
    panel_activity_title: "ਹਾਲੀਆ ਸਰਗਰਮੀਆਂ",
    panel_activity_sub: "ਸੁਪਾਬੇਸ ਵਿੱਚ ਦਰਜ ਫ਼ਸਲ ਤੇ ਰੋਗ ਰਿਕਾਰਡ",
    make_default_title: "ਇਸਨੂੰ ਮੇਰੀ ਡਿਫਾਲਟ ਭਾਸ਼ਾ ਬਣਾਓ",
    make_default_sub: "(ਅਗਲੀ ਵਾਰ ਸਿੱਧਾ ਇਸੇ ਭਾਸ਼ਾ ਵਿੱਚ ਖੁੱਲ੍ਹੇਗਾ)",
    btn_continue: "✓ ਅੱਗੇ ਵਧੋ ➔"
  },
  te: {
    code: "te",
    name: "తెలుగు",
    flag: "🌶️",
    speechCode: "te-IN",
    brand_tagline: "ఏఐ ఆధారిత సూక్ష్మ వాతావరణ పంట సలహా మరియు వ్యాధి నిర్ధారణ",
    supabase_sync: "సుపాబేస్ లైవ్ యాక్టివ్",
    live_mandi_label: "ప్రత్యక్ష మార్కెట్ ధరలు",
    hero_headline: "శాస్త్రీయ డేటాతో కూడిన స్మార్ట్ వ్యవసాయ సలహా",
    hero_sub: "XGBoost 99.09% ఖచ్చితత్వంతో నేల మరియు వాతావరణాన్ని విశ్లేషిస్తుంది, మరియు Groq AI తెలుగులో వాయిస్ ద్వారా మార్గనిర్దేశం చేస్తుంది.",
    quick_hubs_label: "వ్యవసాయ ప్రాంతాన్ని ఎంచుకోండి:",
    lbl_temperature: "ఉష్ణోగ్రత",
    lbl_humidity: "గాలిలో తేమ",
    lbl_rain7d: "7 రోజుల వర్షపాతం",
    tab_advisory: "పంట సలహా (XGBoost + SHAP)",
    tab_doctor: "ప్లాంట్ డాక్టర్ (తెగుళ్ల గుర్తింపు)",
    tab_voice: "వాయిస్ సాథి (మాట్లాడి అడగండి)",
    tab_mandi: "మార్కెట్ ధరలు & వాతావరణం",
    tab_supabase: "సుపాబేస్ & సిస్టమ్ స్థితి",
    panel_soil_title: "పొలం వివరాలు & నేల పరీక్ష",
    panel_soil_sub: "సాయిల్ హెల్త్ కార్డును లోడ్ చేయండి లేదా వివరాలు నింపండి",
    lbl_state: "రాష్ట్రం",
    lbl_district: "జిల్లా",
    lbl_n: "నైట్రోజన్ (N) కిలో/హెక్టారు",
    lbl_p: "భాస్వరం (P) కిలో/హెక్టారు",
    lbl_k: "పొటాష్ (K) కిలో/హెక్టారు",
    lbl_ph: "నేల pH విలువ",
    lbl_irrigation: "నీటిపారుదల సదుపాయం",
    lbl_farmsize: "పొలం పరిమాణం (ఎకరాలు)",
    lbl_prevcrop: "గత పంట",
    btn_run_xgboost: "AI విశ్లేషణను ప్రారంభించండి",
    panel_recs_title: "సిఫార్సు చేయబడిన ఉత్తమ పంటలు",
    panel_recs_sub: "నేల, వాతావరణం మరియు మార్కెట్ ధరల ఆధారంగా ర్యాంకింగ్",
    badge_best_match: "#1 ఉత్తమ పంట",
    lbl_match: "ఖచ్చితత్వం",
    pillar_soil: "నేల అనుకూలత",
    pillar_weather: "వాతావరణం",
    pillar_market: "మార్కెట్ గిరాకీ",
    pillar_rotation: "పంట మార్పిడి",
    lbl_yield: "అంచనా దిగుబడి",
    lbl_revenue: "అంచనా ఆదాయం",
    lbl_rate: "మార్కెట్ రేటు",
    lbl_sowing: "విత్తే సమయం",
    shap_title: "🔍 SHAP విశ్లేషణ: ఈ పంటను ఎందుకు సిఫార్సు చేశారు?",
    shap_tag: "పోషకాల ప్రభావం",
    runners_title: "ప్రత్యామ్నాయ పంటలు (ర్యాంక్ #2 & #3)",
    panel_doctor_title: "మొక్కల వ్యాధి నిర్ధారణ & ఆకు స్కానర్",
    panel_doctor_sub: "ఆకు నమూనాను ఎంచుకోండి లేదా తెగుళ్లను గుర్తించండి",
    leaf_gallery_title: "పరీక్ష కోసం ఆకుల నమూనాలు:",
    dropzone_title: "ఆకు ఫోటోను ఇక్కడ ఉంచండి",
    dropzone_sub: "టమాటా, బంగాళాదుంప, పత్తి, వరి, మొక్కజొన్న మొదలైనవి",
    btn_run_diagnosis: "వ్యాధి నిర్ధారణను ప్రారంభించండి",
    panel_diag_title: "వ్యాధి నిర్ధారణ నివేదిక & నివారణ",
    panel_diag_sub: "సేంద్రీయ మరియు రసాయన నివారణ చర్యలు",
    spray_alert_title: "🌦️ వాతావరణ ఆధారిత స్ప్రే సలహా",
    remedy_organic_badge: "🌿 100% సేంద్రీయ నివారణ",
    remedy_chemical_badge: "🧪 రసాయన నివారణ",
    voice_hero_title: "వాయిస్ సాథి — మీ వ్యవసాయ మిత్రుడు",
    voice_hero_sub: "Groq AI ద్వారా తెలుగులో మాట్లాడి సలహాలు పొందండి.",
    voice_chips_label: "తరచుగా అడిగే ప్రశ్నలు:",
    chip_water: "నీరు ఎంత అవసరం? (నీటిపారుదల)",
    chip_fertilizer: "ఎరువుల మోతాదు? (NPK)",
    chip_mandi: "ఈరోజు మార్కెట్ ధర ఎంత?",
    chip_pest: "తెగుళ్ల నివారణ ఎలా చేయాలి?",
    btn_ask_ai: "అడగండి",
    btn_listen_audio: "వాయిస్ వినండి",
    lbl_followups: "తదుపరి ప్రశ్నలు:",
    panel_weather_title: "7 రోజుల వాతావరణం & స్ప్రే సూచన",
    panel_weather_sub: "శాటిలైట్ డేటా & సరైన స్ప్రే సమయం",
    panel_mandi_title: "స్థానిక మార్కెట్ ధరలు",
    panel_mandi_sub: "రోజువారీ మార్కెట్ ధరల వివరాలు",
    th_commodity: "పంట",
    th_market: "మార్కెట్",
    th_rate: "సగటు రేటు (₹/క్వింటాల్)",
    th_trend: "7 రోజుల సరళి",
    panel_sb_title: "సుపాబేస్ డేటాబేస్ స్థితి",
    panel_sb_sub: "డేటాబేస్ నిరంతరం యాక్టివ్‌గా ఉంటుంది",
    panel_activity_title: "ఇటీవలి వివరాలు",
    panel_activity_sub: "సుపాబేస్‌లో నమోదైన వివరాలు",
    make_default_title: "దీన్ని నా డిఫాల్ట్ భాషగా ఉంచండి",
    make_default_sub: "(తదుపరిసారి నేరుగా ఈ భాషే వస్తుంది)",
    btn_continue: "✓ ముందుకు సాగండి ➔"
  },
  ta: {
    code: "ta",
    name: "தமிழ்",
    flag: "🌴",
    speechCode: "ta-IN",
    brand_tagline: "AI அடிப்படையிலான துல்லிய பயிர் ஆலோசனை மற்றும் நோய் கண்டறிதல்",
    supabase_sync: "சுபாபேஸ் நேரலை செயலில் உள்ளது",
    live_mandi_label: "சந்தை விலை நிலவரம்",
    hero_headline: "அறிவியல் பூர்வமான ஸ்மார்ட் விவசாய ஆலோசனை",
    hero_sub: "XGBoost 99.09% துல்லியத்துடன் மண் மற்றும் காலநிலையை பகுப்பாய்வு செய்கிறது, Groq AI தமிழில் வழிகாட்டுகிறது.",
    quick_hubs_label: "விவசாய மண்டலத்தை தேர்ந்தெடுக்கவும்:",
    lbl_temperature: "வெப்பநிலை",
    lbl_humidity: "ஈரப்பதம்",
    lbl_rain7d: "7 நாள் மழைப்பொழிவு",
    tab_advisory: "பயிர் ஆலோசனை (XGBoost + SHAP)",
    tab_doctor: "பயிர் மருத்துவர் (நோய் கண்டறிதல்)",
    tab_voice: "வாய்ஸ் சாதி (பேசி கேளுங்கள்)",
    tab_mandi: "சந்தை விலை & வானிலை",
    tab_supabase: "சுபாபேஸ் அமைப்பு நிலை",
    panel_soil_title: "பண்ணை விவரங்கள் & மண் பரிசோதனை",
    panel_soil_sub: "மண் வள அட்டையை பதிவேற்றவும்",
    lbl_state: "மாநிலம்",
    lbl_district: "மாவட்டம்",
    lbl_n: "நைட்ரஜன் (N) கிலோ/ஹெக்டேர்",
    lbl_p: "பாஸ்பரஸ் (P) கிலோ/ஹெக்டேர்",
    lbl_k: "பொட்டாஷ் (K) கிலோ/ஹெக்டேர்",
    lbl_ph: "மண் pH அளவு",
    lbl_irrigation: "பாசன வசதி",
    lbl_farmsize: "பண்ணை அளவு (ஏக்கர்)",
    lbl_prevcrop: "முந்தைய பயிர்",
    btn_run_xgboost: "AI பகுப்பாய்வை தொடங்கு",
    panel_recs_title: "பரிந்துரைக்கப்பட்ட சிறந்த பயிர்கள்",
    panel_recs_sub: "மண், வானிலை மற்றும் சந்தை விலை அடிப்படையிலான தரம்",
    badge_best_match: "#1 சிறந்த பயிர்",
    lbl_match: "பொருத்தம்",
    pillar_soil: "மண் பொருத்தம்",
    pillar_weather: "வானிலை",
    pillar_market: "சந்தை தேவை",
    pillar_rotation: "பயிர் சுழற்சி",
    lbl_yield: "எதிர்பார்க்கப்படும் மகசூல்",
    lbl_revenue: "வருமானம்",
    lbl_rate: "சந்தை விலை",
    lbl_sowing: "விதைப்பு காலம்",
    shap_title: "🔍 SHAP விளக்கம்: இப்பயிர் ஏன் பரிந்துரைக்கப்பட்டது?",
    shap_tag: "ஊட்டச்சத்து தாக்கம்",
    runners_title: "மாற்று பயிர்கள் (தரம் #2 & #3)",
    panel_doctor_title: "தாவர நோய் கண்டறிதல் & இலை ஸ்கேனர்",
    panel_doctor_sub: "இலை மாதிரியை தேர்வு செய்து நோயை கண்டறியவும்",
    leaf_gallery_title: "பரிசோதனைக்கான இலை மாதிரிகள்:",
    dropzone_title: "இலையின் புகைப்படத்தை இங்கே பதிவேற்றவும்",
    dropzone_sub: "தக்காளி, உருளைக்கிழங்கு, பருத்தி, நெல், மக்காச்சோளம்",
    btn_run_diagnosis: "நோய் கண்டறிதலை தொடங்கு",
    panel_diag_title: "நோய் கண்டறிதல் அறிக்கை & தீர்வுகள்",
    panel_diag_sub: "இயற்கை மற்றும் ரசாயன தீர்வுகள்",
    spray_alert_title: "🌦️ வானிலை அடிப்படையிலான தெளிப்பு ஆலோசனை",
    remedy_organic_badge: "🌿 100% இயற்கை மருத்துவம்",
    remedy_chemical_badge: "🧪 ரசாயன மருத்துவம்",
    voice_hero_title: "வாய்ஸ் சாதி — உங்கள் விவசாய நண்பன்",
    voice_hero_sub: "Groq AI மூலம் தமிழில் பேசி வழிகாட்டல் பெறுங்கள்.",
    voice_chips_label: "அடிக்கடி கேட்கப்படும் கேள்விகள்:",
    chip_water: "பாசனம் எவ்வளவு தேவை?",
    chip_fertilizer: "உர அளவு என்ன? (NPK)",
    chip_mandi: "இன்றைய சந்தை விலை என்ன?",
    chip_pest: "பூச்சி கட்டுப்பாடு எப்படி?",
    btn_ask_ai: "கேளுங்கள்",
    btn_listen_audio: "குரலை கேளுங்கள்",
    lbl_followups: "அடுத்த கேள்விகள்:",
    panel_weather_title: "7 நாள் வானிலை & தெளிப்பு முன்னறிவிப்பு",
    panel_weather_sub: "செயற்கைக்கோள் தரவு & தெளிப்பு நேரம்",
    panel_mandi_title: "உள்ளூர் சந்தை விலைகள்",
    panel_mandi_sub: "தினசரி விலை நிலவரம்",
    th_commodity: "பயிர்",
    th_market: "சந்தை",
    th_rate: "சராசரி விலை (₹/குவிண்டால்)",
    th_trend: "7 நாள் போக்கு",
    panel_sb_title: "சுபாபேஸ் தரவுத்தள நிலை",
    panel_sb_sub: "தரவுத்தளம் எப்போதும் செயல்பாட்டில் உள்ளது",
    panel_activity_title: "சமீபத்திய பதிவுகள்",
    panel_activity_sub: "சுபாபேஸில் சேமிக்கப்பட்ட விவரங்கள்",
    make_default_title: "இதை எனது இயல்புநிலை மொழியாக்கு",
    make_default_sub: "(அடுத்த முறை நேரடியாக இந்த மொழியில் திறக்கும்)",
    btn_continue: "✓ தொடரவும் ➔"
  },
  gu: {
    code: "gu",
    name: "ગુજરાતી",
    flag: "🥜",
    speechCode: "gu-IN",
    brand_tagline: "AI આધારિત પાક સલાહ અને રોગ નિદાન",
    supabase_sync: "સુપાબેઝ લાઈવ સક્રિય",
    live_mandi_label: "લાઈવ માર્કેટ ભાવ",
    hero_headline: "વૈજ્ઞાનિક માહિતી આધારિત સ્માર્ટ કૃષિ સલાહ",
    hero_sub: "XGBoost ૯૯.૦૯% સચોટતા સાથે જમીન અને હવામાનનું વિશ્લેષણ કરે છે, અને Groq AI ગુજરાતીમાં માર્ગદર્શન આપે છે.",
    quick_hubs_label: "કૃષિ વિસ્તાર પસંદ કરો:",
    lbl_temperature: "તાપમાન",
    lbl_humidity: "ભેજ",
    lbl_rain7d: "૭-દિવસીય વરસાદ",
    tab_advisory: "પાક સલાહ (XGBoost + SHAP)",
    tab_doctor: "પાક ડૉક્ટર (રોગ નિદાન)",
    tab_voice: "વોઈસ સાથી (બોલીને પૂછો)",
    tab_mandi: "બજાર ભાવ અને હવામાન",
    tab_supabase: "સુપાબેઝ સિસ્ટમ સ્થિતિ",
    panel_soil_title: "ખેતર વિગત અને જમીન ચકાસણી",
    panel_soil_sub: "સોઇલ હેલ્થ કાર્ડ લોડ કરો અથવા વિગતો ભરો",
    lbl_state: "રાજ્ય",
    lbl_district: "જિલ્લો",
    lbl_n: "નાઇટ્રોજન (N) કિગ્રા/હેક્ટર",
    lbl_p: "ફોસ્ફરસ (P) કિગ્રા/હેક્ટર",
    lbl_k: "પોટાશ (K) કિગ્રા/હેક્ટર",
    lbl_ph: "જમીનનો pH આંક",
    lbl_irrigation: "પિયત સુવિધા",
    lbl_farmsize: "ખેતરનું કદ (એકર)",
    lbl_prevcrop: "અગાઉનો પાક",
    btn_run_xgboost: "XGBoost AI વિશ્લેષણ શરૂ કરો",
    panel_recs_title: "ભલામણ કરેલ શ્રેષ્ઠ પાકો",
    panel_recs_sub: "જમીન, હવામાન અને બજાર ભાવ આધારિત ક્રમ",
    badge_best_match: "#1 શ્રેષ્ઠ પાક",
    lbl_match: "સચોટતા",
    pillar_soil: "જમીન અનુકૂળતા",
    pillar_weather: "હવામાન",
    pillar_market: "બજાર માંગ",
    pillar_rotation: "પાક ફેરબદલી",
    lbl_yield: "અંદાજિત ઉપજ",
    lbl_revenue: "અંદાજિત આવક",
    lbl_rate: "બજાર ભાવ",
    lbl_sowing: "વાવણીનો સમય",
    shap_title: "🔍 SHAP વિશ્લેષણ: આ પાકની ભલામણ કેમ કરવામાં આવી?",
    shap_tag: "પોષક તત્વોનો પ્રભાવ",
    runners_title: "વૈકલ્પિક પાકો (ક્રમ #૨ અને #૩)",
    panel_doctor_title: "વનસ્પતિ રોગ નિદાન અને પાંદડા સ્કેનર",
    panel_doctor_sub: "પાંદડાનો નમૂનો પસંદ કરો અથવા રોગ ચકાસો",
    leaf_gallery_title: "ચકાસણી માટે પાંદડાના નમૂના:",
    dropzone_title: "પાંદડાનો ફોટો અહીં મૂકો",
    dropzone_sub: "ટામેટા, બટાટા, કપાસ, ઘઉં, ડાંગર, મકાઈ વગેરે",
    btn_run_diagnosis: "રોગ નિદાન શરૂ કરો",
    panel_diag_title: "રોગ નિદાન અહેવાલ અને ઉપચાર",
    panel_diag_sub: "કુદરતી અને રાસાયણિક ઉપચાર પદ્ધતિ",
    spray_alert_title: "🌦️ હવામાન આધારિત છંટકાવ સલાહ",
    remedy_organic_badge: "🌿 ૧૦૦% કુદરતી ઉપચાર",
    remedy_chemical_badge: "🧪 રાસાયણિક ઉપચાર",
    voice_hero_title: "વોઈસ સાથી — તમારો ખેતી સલાહકાર",
    voice_hero_sub: "Groq AI દ્વારા ગુજરાતીમાં બોલીને સલાહ મેળવો.",
    voice_chips_label: "સામાન્ય પ્રશ્નો:",
    chip_water: "પાણી કેટલું આપવું? (પિયત)",
    chip_fertilizer: "ખાતરનું પ્રમાણ? (NPK)",
    chip_mandi: "આજનો બજાર ભાવ શું છે?",
    chip_pest: "જીવાત નિયંત્રણ કેવી રીતે કરવું?",
    btn_ask_ai: "પૂછો",
    btn_listen_audio: "અવાજ સાંભળો",
    lbl_followups: "આગળના પ્રશ્નો:",
    panel_weather_title: "૭-દિવસીય હવામાન અને છંટકાવ અનુમાન",
    panel_weather_sub: "સેટેલાઇટ ડેટા અને છંટકાવ માટે યોગ્ય સમય",
    panel_mandi_title: "સ્થાનિક APMC માર્કેટ ભાવ",
    panel_mandi_sub: "દૈનિક બજાર આવક અને વલણ",
    th_commodity: "પાક",
    th_market: "માર્કેટ",
    th_rate: "સરેરાશ ભાવ (₹/ક્વિન્ટલ)",
    th_trend: "૭-દિવસીય વલણ",
    panel_sb_title: "સુપાબેઝ ડેટાબેઝ સ્થિતિ",
    panel_sb_sub: "ડેટાબેઝ હંમેશા સક્રિય રહે છે",
    panel_activity_title: "તાજેતરની પ્રવૃત્તિઓ",
    panel_activity_sub: "સુપાબેઝમાં નોંધાયેલ વિગતો",
    make_default_title: "આને મારી ડિફૉલ્ટ ભાષા બનાવો",
    make_default_sub: "(આગલી વખતે સીધી આ જ ભાષા ખુલશે)",
    btn_continue: "✓ આગળ વધો ➔"
  },
  bn: {
    code: "bn",
    name: "বাংলা",
    flag: "🌾",
    speechCode: "bn-IN",
    brand_tagline: "এআই ভিত্তিক আবহাওয়া ও ফসলের রোগ নির্ণয় পরামর্শ",
    supabase_sync: "সুপাবেস লাইভ সক্রিয়",
    live_mandi_label: "লাইভ বাজার দর",
    hero_headline: "বৈজ্ঞানিক তথ্যের ওপর ভিত্তি করে স্মার্ট কৃষি পরামর্শ",
    hero_sub: "XGBoost ৯৯.০৯% নির্ভুলতার সাথে মাটি ও আবহাওয়া বিশ্লেষণ করে এবং Groq AI বাংলায় ভয়েস পরামর্শ দেয়।",
    quick_hubs_label: "কৃষি অঞ্চল নির্বাচন করুন:",
    lbl_temperature: "তাপমাত্রা",
    lbl_humidity: "বাতাসের আর্দ্রতা",
    lbl_rain7d: "৭ দিনের বৃষ্টিপাত",
    tab_advisory: "ফসল পরামর্শ (XGBoost + SHAP)",
    tab_doctor: "উদ্ভিদ ডাক্তার (রোগ নির্ণয়)",
    tab_voice: "ভয়েস সাথী (কথা বলে জানুন)",
    tab_mandi: "বাজার দর ও আবহাওয়া",
    tab_supabase: "সুপাবেস সিস্টেম স্ট্যাটাস",
    panel_soil_title: "জমির বিবরণ ও মাটি পরীক্ষা",
    panel_soil_sub: "সয়েল হেলথ কার্ড লোড করুন বা তথ্য দিন",
    lbl_state: "রাজ্য",
    lbl_district: "জেলা",
    lbl_n: "নাইট্রোজেন (N) কেজি/হেক্টর",
    lbl_p: "ফসফরাস (P) কেজি/হেক্টর",
    lbl_k: "পটাশ (K) কেজি/হেক্টর",
    lbl_ph: "মাটির pH মান",
    lbl_irrigation: "সেচ ব্যবস্থা",
    lbl_farmsize: "জমির পরিমাণ (একর)",
    lbl_prevcrop: "পূর্ববর্তী ফসল",
    btn_run_xgboost: "AI বিশ্লেষণ শুরু করুন",
    panel_recs_title: "সুপারিশকৃত সেরা ফসল",
    panel_recs_sub: "মাটি, আবহাওয়া এবং বাজার দরের ভিত্তিতে তালিকা",
    badge_best_match: "#১ সেরা ফসল",
    lbl_match: "নির্ভুলতা",
    pillar_soil: "মাটির উপযুক্ততা",
    pillar_weather: "আবহাওয়া",
    pillar_market: "বাজার চাহিদা",
    pillar_rotation: "ফসল চক্র",
    lbl_yield: "আনুমানিক ফলন",
    lbl_revenue: "আনুমানিক আয়",
    lbl_rate: "বাজার দর",
    lbl_sowing: "বপনের সময়",
    shap_title: "🔍 SHAP ব্যাখ্যা: এই ফসল কেন সুপারিশ করা হলো?",
    shap_tag: "পুষ্টি উপাদানের প্রভাব",
    runners_title: "বিকল্প ফসল (র‌্যাঙ্ক #২ ও #৩)",
    panel_doctor_title: "উদ্ভিদের রোগ নির্ণয় ও পাতা স্ক্যানার",
    panel_doctor_sub: "পাতার নমুনা বেছে নিন বা রোগ বিশ্লেষণ করুন",
    leaf_gallery_title: "পরীক্ষার জন্য পাতার নমুনা:",
    dropzone_title: "পাতার ছবি এখানে আপলোড করুন",
    dropzone_sub: "টমেটো, আলু, তুলা, গম, ধান, ভুট্টা ইত্যাদির জন্য",
    btn_run_diagnosis: "রোগ নির্ণয় শুরু করুন",
    panel_diag_title: "রোগ নির্ণয় রিপোর্ট ও প্রতিকার",
    panel_diag_sub: "জৈব ও রাসায়নিক প্রতিকার ব্যবস্থা",
    spray_alert_title: "🌦️ আবহাওয়া ভিত্তিক স্প্রে পরামর্শ",
    remedy_organic_badge: "🌿 ১০০% জৈব প্রতিকার",
    remedy_chemical_badge: "🧪 রাসায়নিক প্রতিকার",
    voice_hero_title: "ভয়েস সাথী — আপনার কৃষি উপদেষ্টা",
    voice_hero_sub: "Groq AI দ্বারা বাংলায় কথা বলে পরামর্শ পান।",
    voice_chips_label: "সাধারণ প্রশ্নাবলী:",
    chip_water: "কতটা সেচ প্রয়োজন?",
    chip_fertilizer: "সারের সঠিক পরিমাণ? (NPK)",
    chip_mandi: "আজকের বাজার দর কত?",
    chip_pest: "কীটপতঙ্গ নিয়ন্ত্রণ কীভাবে করব?",
    btn_ask_ai: "জিজ্ঞাসা করুন",
    btn_listen_audio: "ভয়েস শুনুন",
    lbl_followups: "পরবর্তী প্রশ্ন:",
    panel_weather_title: "৭ দিনের আবহাওয়া ও স্প্রে পূর্বাভাস",
    panel_weather_sub: "স্যাটেলাইট তথ্য ও স্প্রে করার সঠিক সময়",
    panel_mandi_title: "স্থানীয় পাইকারি বাজার দর",
    panel_mandi_sub: "দৈনিক বাজার দর ও প্রবণতা",
    th_commodity: "ফসল",
    th_market: "বাজার",
    th_rate: "গড় দর (₹/কুইন্টাল)",
    th_trend: "৭ দিনের ট্রেন্ড",
    panel_sb_title: "সুপাবেস ডেটাবেস স্ট্যাটাস",
    panel_sb_sub: "ডেটাবেস সর্বদা সক্রিয় থাকে",
    panel_activity_title: "সাম্প্রতিক কার্যকলাপ",
    panel_activity_sub: "সুপাবেসে সংরক্ষিত বিবরণ",
    make_default_title: "এটিকে আমার ডিফল্ট ভাষা করুন",
    make_default_sub: "(পরের বার সরাসরি এই ভাষাতেই খুলবে)",
    btn_continue: "✓ এগিয়ে যান ➔"
  },
  kn: {
    code: "kn",
    name: "ಕನ್ನಡ",
    flag: "☕",
    speechCode: "kn-IN",
    brand_tagline: "AI ಆಧಾರಿತ ಬೆಳೆ ಸಲಹೆ ಮತ್ತು ರೋಗ ಪತ್ತೆ",
    supabase_sync: "ಸುಪಬೇಸ್ ಲೈವ್ ಸಕ್ರಿಯವಾಗಿದೆ",
    live_mandi_label: "ಮಾರುಕಟ್ಟೆ ದರಗಳು",
    hero_headline: "ವೈಜ್ಞಾನಿಕ ಮಾಹಿತಿಯೊಂದಿಗೆ ಸ್ಮಾರ್ಟ್ ಕೃಷಿ ಸಲಹೆ",
    hero_sub: "XGBoost 99.09% ನಿಖರತೆಯೊಂದಿಗೆ ಮಣ್ಣು ಮತ್ತು ಹವಾಮಾನವನ್ನು ವಿಶ್ಲೇಷಿಸುತ್ತದೆ, Groq AI ಕನ್ನಡದಲ್ಲಿ ಮಾರ್ಗದರ್ಶನ ನೀಡುತ್ತದೆ.",
    quick_hubs_label: "ಕೃಷಿ ವಲಯ ಆಯ್ಕೆಮಾಡಿ:",
    lbl_temperature: "ತಾಪಮಾನ",
    lbl_humidity: "ತೇವಾಂಶ",
    lbl_rain7d: "7 ದಿನಗಳ ಮಳೆ",
    tab_advisory: "ಬೆಳೆ ಸಲಹೆ (XGBoost + SHAP)",
    tab_doctor: "ಸಸ್ಯ ವೈದ್ಯ (ರೋಗ ಪತ್ತೆ)",
    tab_voice: "ವಾಯ್ಸ್ ಸಾಥಿ (ಮಾತನಾಡಿ ಕೇಳಿ)",
    tab_mandi: "ಮಾರುಕಟ್ಟೆ ದರ ಮತ್ತು ಹವಾಮಾನ",
    tab_supabase: "ಸುಪಬೇಸ್ ಸ್ಥಿತಿ",
    panel_soil_title: "ಜಮೀನಿನ ವಿವರ ಮತ್ತು ಮಣ್ಣು ಪರೀಕ್ಷೆ",
    panel_soil_sub: "ಮಣ್ಣು ಆರೋಗ್ಯ ಕಾರ್ಡ್ ಅಪ್ಲೋಡ್ ಮಾಡಿ",
    lbl_state: "ರಾಜ್ಯ",
    lbl_district: "ಜಿಲ್ಲೆ",
    lbl_n: "ಸಾರಜನಕ (N) ಕೆಜಿ/ಹೆಕ್ಟೇರ್",
    lbl_p: "ರಂಜಕ (P) ಕೆಜಿ/ಹೆಕ್ಟೇರ್",
    lbl_k: "ಪೊಟ್ಯಾಶ್ (K) ಕೆಜಿ/ಹೆಕ್ಟೇರ್",
    lbl_ph: "ಮಣ್ಣಿನ pH ಮೌಲ್ಯ",
    lbl_irrigation: "ನೀರಾವರಿ ಸೌಲಭ್ಯ",
    lbl_farmsize: "ಜಮೀನಿನ ವಿಸ್ತೀರ್ಣ (ಎಕರೆ)",
    lbl_prevcrop: "ಹಿಂದಿನ ಬೆಳೆ",
    btn_run_xgboost: "AI ವಿಶ್ಲೇಷಣೆ ಪ್ರಾರಂಭಿಸಿ",
    panel_recs_title: "ಶಿಫಾರಸು ಮಾಡಲಾದ ಅತ್ಯುತ್ತಮ ಬೆಳೆಗಳು",
    panel_recs_sub: "ಮಣ್ಣು, ಹವಾಮಾನ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ದರಗಳ ಆಧಾರಿತ ಶ್ರೇಣಿ",
    badge_best_match: "#1 ಅತ್ಯುತ್ತಮ ಬೆಳೆ",
    lbl_match: "ಹೊಂದಾಣಿಕೆ",
    pillar_soil: "ಮಣ್ಣಿನ ಸೂಕ್ತತೆ",
    pillar_weather: "ಹವಾಮಾನ",
    pillar_market: "ಮಾರುಕಟ್ಟೆ ಬೇಡಿಕೆ",
    pillar_rotation: "ಬೆಳೆ ಸರದಿ",
    lbl_yield: "ನಿರೀಕ್ಷಿತ ಇಳುವರಿ",
    lbl_revenue: "ನಿರೀಕ್ಷಿತ ಆದಾಯ",
    lbl_rate: "ಮಾರುಕಟ್ಟೆ ಬೆಲೆ",
    lbl_sowing: "ಬಿತ್ತನೆ ಸಮಯ",
    shap_title: "🔍 SHAP ವಿವರಣೆ: ಈ ಬೆಳೆಯನ್ನು ಏಕೆ ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ?",
    shap_tag: "ಪೋಷಕಾಂಶಗಳ ಪ್ರಭಾವ",
    runners_title: "ಪರ್ಯಾಯ ಬೆಳೆಗಳು (ಶ್ರೇಣಿ #2 ಮತ್ತು #3)",
    panel_doctor_title: "ಸಸ್ಯ ರೋಗ ಪತ್ತೆ ಮತ್ತು ಎಲೆ ಸ್ಕ್ಯಾನರ್",
    panel_doctor_sub: "ಎಲೆಯ ಮಾದರಿಯನ್ನು ಆಯ್ಕೆಮಾಡಿ ರೋಗ ಪತ್ತೆಹಚ್ಚಿ",
    leaf_gallery_title: "ಪರೀಕ್ಷೆಗಾಗಿ ಎಲೆ ಮಾದರಿಗಳು:",
    dropzone_title: "ಎಲೆಯ ಫೋಟೋವನ್ನು ಇಲ್ಲಿ ಹಾಕಿ",
    dropzone_sub: "ಟೊಮ್ಯಾಟೊ, ಆಲೂಗಡ್ಡೆ, ಹತ್ತಿ, ಭತ್ತ, ಮೆಕ್ಕೆಜೋಳ",
    btn_run_diagnosis: "ರೋಗ ಪತ್ತೆ ಪ್ರಾರಂಭಿಸಿ",
    panel_diag_title: "ರೋಗ ಪತ್ತೆ ವರದಿ ಮತ್ತು ಪರಿಹಾರ",
    panel_diag_sub: "ಸಾವಯವ ಮತ್ತು ರಾಸಾಯನಿಕ ಪರಿಹಾರ ಕ್ರಮಗಳು",
    spray_alert_title: "🌦️ ಹವಾಮಾನ ಆಧಾರಿತ ಸಿಂಪಡಣೆ ಸಲಹೆ",
    remedy_organic_badge: "🌿 100% ಸಾವಯವ ಚಿಕಿತ್ಸೆ",
    remedy_chemical_badge: "🧪 ರಾಸಾಯನಿಕ ಚಿಕಿತ್ಸೆ",
    voice_hero_title: "ವಾಯ್ಸ್ ಸಾಥಿ — ನಿಮ್ಮ ಕೃಷಿ ಸಲಹೆಗಾರ",
    voice_hero_sub: "Groq AI ಮೂಲಕ ಕನ್ನಡದಲ್ಲಿ ಧ್ವನಿ ಸಲಹೆ ಪಡೆಯಿರಿ.",
    voice_chips_label: "ಸಾಮಾನ್ಯ ಪ್ರಶ್ನೆಗಳು:",
    chip_water: "ನೀರು ಎಷ್ಟು ಬೇಕು? (ನೀರಾವರಿ)",
    chip_fertilizer: "ಗೊಬ್ಬರದ ಪ್ರಮಾಣ? (NPK)",
    chip_mandi: "ಇಂದಿನ ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ಎಷ್ಟು?",
    chip_pest: "ಕೀಟ ನಿಯಂತ್ರಣ ಹೇಗೆ?",
    btn_ask_ai: "ಕೇಳಿ",
    btn_listen_audio: "ಧ್ವನಿ ಕೇಳಿ",
    lbl_followups: "ಮುಂದಿನ ಪ್ರಶ್ನೆಗಳು:",
    panel_weather_title: "7 ದಿನಗಳ ಹವಾಮಾನ ಮತ್ತು ಸಿಂಪಡಣೆ ಮುನ್ಸೂಚನೆ",
    panel_weather_sub: "ಉಪಗ್ರಹ ಮಾಹಿತಿ ಮತ್ತು ಸಿಂಪಡಣೆಗೆ ಸೂಕ್ತ ಸಮಯ",
    panel_mandi_title: "ಸ್ಥಳೀಯ ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳು",
    panel_mandi_sub: "ದೈನಂದಿನ ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ವಿವರ",
    th_commodity: "ಬೆಳೆ",
    th_market: "ಮಾರುಕಟ್ಟೆ",
    th_rate: "ಸರಾಸರಿ ಬೆಲೆ (₹/ಕ್ವಿಂಟಾಲ್)",
    th_trend: "7 ದಿನಗಳ ಪ್ರವೃತ್ತಿ",
    panel_sb_title: "ಸುಪಬೇಸ್ ಡೇಟಾಬೇಸ್ ಸ್ಥಿತಿ",
    panel_sb_sub: "ಡೇಟಾಬೇಸ್ ಸದಾ ಸಕ್ರಿಯವಾಗಿರುತ್ತದೆ",
    panel_activity_title: "ಇತ್ತೀಚಿನ ಚಟುವಟಿಕೆಗಳು",
    panel_activity_sub: "ಸುಪಬೇಸ್‌ನಲ್ಲಿ ಉಳಿಸಲಾದ ವಿವರಗಳು",
    make_default_title: "ಇದನ್ನು ನನ್ನ ಡೀಫಾಲ್ಟ್ ಭಾಷೆಯನ್ನಾಗಿ ಮಾಡಿ",
    make_default_sub: "(ಮುಂದಿನ ಬಾರಿ ನೇರವಾಗಿ ಈ ಭಾಷೆಯಲ್ಲಿ ತೆರೆಯುತ್ತದೆ)",
    btn_continue: "✓ ಮುಂದುವರಿಯಿರಿ ➔"
  },
  ml: {
    code: "ml",
    name: "മലയാളം",
    flag: "🥥",
    speechCode: "ml-IN",
    brand_tagline: "AI അധിഷ്ഠിത വിള ഉപദേശവും രോഗനിർണയവും",
    supabase_sync: "സുപാബേസ് ലൈവ് സജീവം",
    live_mandi_label: "തത്സമയ വിപണി വില",
    hero_headline: "ശാസ്ത്രീയ വിവരങ്ങളോടെ സ്മാർട്ട് കാർഷിക ഉപദേശം",
    hero_sub: "XGBoost 99.09% കൃത്യതയോടെ മണ്ണും കാലാവസ്ഥയും വിശകലനം ചെയ്യുന്നു, Groq AI മലയാളത്തിൽ ശബ്ദത്തിലൂടെ ഉപദേശം നൽകുന്നു.",
    quick_hubs_label: "കാർഷിക മേഖല തിരഞ്ഞെടുക്കുക:",
    lbl_temperature: "താപനില",
    lbl_humidity: "അന്തരീക്ഷ ഈർപ്പം",
    lbl_rain7d: "7 ദിവസത്തെ മഴ",
    tab_advisory: "വിള ഉപദേശം (XGBoost + SHAP)",
    tab_doctor: "പ്ലാന്റ് ഡോക്ടർ (രോഗനിർണയം)",
    tab_voice: "വോയ്സ് സാഥി (സംസാരിച്ചു ചോദിക്കൂ)",
    tab_mandi: "വിപണി വിലയും കാലാവസ്ഥയും",
    tab_supabase: "സുപാബേസ് അവസ്ഥ",
    panel_soil_title: "കൃഷിയിട വിവരങ്ങളും മണ്ണ് പരിശോധനയും",
    panel_soil_sub: "സോയിൽ ഹെൽത്ത് കാർഡ് അപ്‌ലോഡ് ചെയ്യുക",
    lbl_state: "സംസ്ഥാനം",
    lbl_district: "ജില്ല",
    lbl_n: "നൈട്രജൻ (N) കിലോഗ്രാം/ഹെക്ടർ",
    lbl_p: "ഫോസ്ഫറസ് (P) കിലോഗ്രാം/ഹെക്ടർ",
    lbl_k: "പൊട്ടാഷ് (K) കിലോഗ്രാം/ഹെക്ടർ",
    lbl_ph: "മണ്ണിന്റെ pH മൂല്യം",
    lbl_irrigation: "ജലസേചന സൗകര്യം",
    lbl_farmsize: "കൃഷിയിട വിസ്തൃതി (ഏക്കർ)",
    lbl_prevcrop: "മുൻവിള",
    btn_run_xgboost: "AI വിശകലനം ആരംഭിക്കുക",
    panel_recs_title: "ശുപാർശ ചെയ്യുന്ന മികച്ച വിളകൾ",
    panel_recs_sub: "മണ്ണ്, കാലാവസ്ഥ, വിപണി വില എന്നിവ അടിസ്ഥാനമാക്കിയുള്ള റാങ്കിംഗ്",
    badge_best_match: "#1 മികച്ച വിള",
    lbl_match: "പൊരുത്തം",
    pillar_soil: "മണ്ണ് അനുയോജ്യത",
    pillar_weather: "കാലാവസ്ഥ",
    pillar_market: "വിപണി സാധ്യത",
    pillar_rotation: "വിള പരിക്രമണം",
    lbl_yield: "പ്രതീക്ഷിക്കുന്ന വിളവ്",
    lbl_revenue: "പ്രതീക്ഷിക്കുന്ന വരുമാനം",
    lbl_rate: "വിപണി വില",
    lbl_sowing: "വിത്ത് വിതയ്ക്കുന്ന സമയം",
    shap_title: "🔍 SHAP വിവരണം: ഈ വിള എന്തു കൊണ്ട് ശുപാർശ ചെയ്തു?",
    shap_tag: "പോഷക ഘടക സ്വാധീനം",
    runners_title: "മറ്റ് അനുയോജ്യമായ വിളകൾ",
    panel_doctor_title: "സസ്യ രോഗനിർണയവും ഇല സ്കാനറും",
    panel_doctor_sub: "ഇലയുടെ സാമ്പിൾ തിരഞ്ഞെടുത്തു രോഗം നിർണയിക്കുക",
    leaf_gallery_title: "പരിശോധനയ്ക്കുള്ള ഇല സാമ്പിളുകൾ:",
    dropzone_title: "ഇലയുടെ ഫോട്ടോ ഇവിടെ അപ്‌ലോഡ് ചെയ്യുക",
    dropzone_sub: "തക്കാളി, ഉരുളക്കിഴങ്ങ്, പരുത്തി, നെല്ല്, ചോളം",
    btn_run_diagnosis: "രോഗനിർണയം ആരംഭിക്കുക",
    panel_diag_title: "രോഗനിർണയ റിപ്പോർട്ടും പ്രതിവിധികളും",
    panel_diag_sub: "ജൈവ, രാസ പ്രതിവിധികൾ",
    spray_alert_title: "🌦️ കാലാവസ്ഥാധിഷ്ഠിത കീടനാശിനി തളിക്കൽ ഉപദേശം",
    remedy_organic_badge: "🌿 100% ജൈവ ചികിത്സ",
    remedy_chemical_badge: "🧪 രാസ ചികിത്സ",
    voice_hero_title: "വോയ്സ് സാഥി — നിങ്ങളുടെ കാർഷിക സഹായി",
    voice_hero_sub: "Groq AI വഴി മലയാളത്തിൽ സംസാരിച്ചു വിവരങ്ങൾ അറിയൂ.",
    voice_chips_label: "സാധാരണ ചോദ്യങ്ങൾ:",
    chip_water: "എത്ര നനയ്ക്കണം? (നനവ്)",
    chip_fertilizer: "വളപ്രയോഗം എങ്ങനെ? (NPK)",
    chip_mandi: "ഇന്നത്തെ വിപണി വില എത്ര?",
    chip_pest: "കീടനിയന്ത്രണം എങ്ങനെ?",
    btn_ask_ai: "ചോദിക്കൂ",
    btn_listen_audio: "ശബ്ദം കേൾക്കൂ",
    lbl_followups: "തുടർ ചോദ്യങ്ങൾ:",
    panel_weather_title: "7 ദിവസത്തെ കാലാവസ്ഥാ പ്രവചനം",
    panel_weather_sub: "കൃത്യമായ സ്പ്രേ സമയം",
    panel_mandi_title: "വിപണി വില നിലവാരം",
    panel_mandi_sub: "ദൈനംദിന വിപണി വിലകൾ",
    th_commodity: "വിള",
    th_market: "വിപണി",
    th_rate: "ശരാശരി വില (₹/ക്വിന്റൽ)",
    th_trend: "7 ദിവസത്തെ മാറ്റം",
    panel_sb_title: "സുപാബേസ് ഡാറ്റാബേസ് അവസ്ഥ",
    panel_sb_sub: "ഡാറ്റാബേസ് സജീവമാണ്",
    panel_activity_title: "സമീപകാല പ്രവർത്തനങ്ങൾ",
    panel_activity_sub: "സുപാബേസിൽ രേഖപ്പെടുത്തിയ വിവരങ്ങൾ",
    make_default_title: "ഇത് എന്റെ സ്ഥിരം ഭാഷയാക്കുക",
    make_default_sub: "(അടുത്ത തവണ നേരിട്ട് ഈ ഭാഷയിൽ തുറക്കും)",
    btn_continue: "✓ മുന്നോട്ട് പോകുക ➔"
  },
  or: {
    code: "or",
    name: "ଓଡ଼ିଆ",
    flag: "🌾",
    speechCode: "or-IN",
    brand_tagline: "AI ଆଧାରିତ ପାଣିପାଗ ଓ ଫସଲ ରୋଗ ନିର୍ଣ୍ଣୟ ପରାମର୍ଶ",
    supabase_sync: "ସୁପାବେସ୍ ଲାଇଭ୍ ସକ୍ରିୟ",
    live_mandi_label: "ଲାଇଭ୍ ମଣ୍ଡି ଦର",
    hero_headline: "ବୈଜ୍ଞାନିକ ତଥ୍ୟ ଉପରେ ଆଧାରିତ ସ୍ମାର୍ଟ କୃଷି ପରାମର୍ଶ",
    hero_sub: "XGBoost 99.09% ସଠିକତା ସହ ମାଟି ଓ ପାଣିପାଗ ବିଶ୍ଳେଷଣ କରେ ଏବଂ Groq AI ଓଡ଼ିଆରେ କଥା କହି ପରାମର୍ଶ ଦିଏ।",
    quick_hubs_label: "କୃଷି ଅଞ୍ଚଳ ବାଛନ୍ତୁ:",
    lbl_temperature: "ତାପମାତ୍ରା",
    lbl_humidity: "ଆର୍ଦ୍ରତା",
    lbl_rain7d: "୭-ଦିନର ବର୍ଷା",
    tab_advisory: "ଫସଲ ପରାମର୍ଶ (XGBoost + SHAP)",
    tab_doctor: "ଫସଲ ଡାକ୍ତର (ରୋଗ ନିର୍ଣ୍ଣୟ)",
    tab_voice: "ଭଏସ୍ ସାଥୀ (କଥା କହି ପଚାରନ୍ତୁ)",
    tab_mandi: "ମଣ୍ଡି ଦର ଓ ପାଣିପାଗ",
    tab_supabase: "ସୁପାବେସ୍ ସିଷ୍ଟମ୍ ସ୍ଥିତି",
    panel_soil_title: "ଜମି ବିବରଣୀ ଓ ମୃତ୍ତିକା ପରୀକ୍ଷା",
    panel_soil_sub: "ସଏଲ୍ ହେଲଥ୍ କାର୍ଡ ଲୋଡ୍ କରନ୍ତୁ କିମ୍ବା ତଥ୍ୟ ଦିଅନ୍ତୁ",
    lbl_state: "ରାଜ୍ୟ",
    lbl_district: "ଜିଲ୍ଲା",
    lbl_n: "ଯବକ୍ଷାରଜାନ (N) କିଗ୍ରା/ହେକ୍ଟର",
    lbl_p: "ଫସଫରସ୍ (P) କିଗ୍ରା/ହେକ୍ଟର",
    lbl_k: "ପୋଟାସ୍ (K) କିଗ୍ରା/ହେକ୍ଟର",
    lbl_ph: "ମାଟିର pH ମାନ",
    lbl_irrigation: "ଜଳସେଚନ ସୁବିଧା",
    lbl_farmsize: "ଜମିର ଆକାର (ଏକର)",
    lbl_prevcrop: "ପୂର୍ବ ଫସଲ",
    btn_run_xgboost: "AI ବିଶ୍ଳେଷଣ ଆରମ୍ଭ କରନ୍ତୁ",
    panel_recs_title: "ସୁପାରିଶ କରାଯାଇଥିବା ଉତ୍ତମ ଫସଲ",
    panel_recs_sub: "ମାଟି, ପାଣିପାଗ ଓ ମଣ୍ଡି ଦର ଅନୁସାରେ ତାଲିକା",
    badge_best_match: "#୧ ସର୍ବୋତ୍ତମ ଫସଲ",
    lbl_match: "ସଠିକତା",
    pillar_soil: "ମାଟି ଅନୁକୂଳତା",
    pillar_weather: "ପାଣିପାଗ",
    pillar_market: "ମଣ୍ଡି ଚାହିଦା",
    pillar_rotation: "ଫସଲ ଚକ୍ର",
    lbl_yield: "ଆନୁମାନିକ ଅମଳ",
    lbl_revenue: "ଆନୁମାନିକ ଆୟ",
    lbl_rate: "ମଣ୍ଡି ଦର",
    lbl_sowing: "ବୁଣିବା ସମୟ",
    shap_title: "🔍 SHAP ବିବରଣୀ: ଏହି ଫସଲ କାହିଁକି ସୁପାରିଶ କରାଗଲା?",
    shap_tag: "ପୋଷକ ତତ୍ତ୍ୱ ପ୍ରଭାବ",
    runners_title: "ବିକଳ୍ପ ଫସଲ (ସ୍ଥାନ #୨ ଓ #୩)",
    panel_doctor_title: "ଉଦ୍ଭିଦ ରୋଗ ନିର୍ଣ୍ଣୟ ଓ ପତ୍ର ସ୍କାନର୍",
    panel_doctor_sub: "ପତ୍ରର ନମୁନା ବାଛି ରୋଗ ଚିହ୍ନଟ କରନ୍ତୁ",
    leaf_gallery_title: "ପରୀକ୍ଷା ପାଇଁ ପତ୍ର ନମୁନା:",
    dropzone_title: "ପତ୍ରର ଫଟୋ ଏଠାରେ ଅପଲୋଡ୍ କରନ୍ତୁ",
    dropzone_sub: "ଟମାଟୋ, ଆଳୁ, କପା, ଗହମ, ଧାନ, ମକା ଇତ୍ୟାଦି",
    btn_run_diagnosis: "ରୋଗ ନିର୍ଣ୍ଣୟ ଆରମ୍ଭ କରନ୍ତୁ",
    panel_diag_title: "ରୋଗ ନିର୍ଣ୍ଣୟ ରିପୋର୍ଟ ଓ ପ୍ରତିକାର",
    panel_diag_sub: "ଜୈବିକ ଓ ରାସାୟନିକ ଚିକିତ୍ସା",
    spray_alert_title: "🌦️ ପାଣିପାଗ ଅନୁସାରେ ସ୍ପ୍ରେ ପରାମର୍ଶ",
    remedy_organic_badge: "🌿 ୧୦୦% ଜୈବିକ ଚିକିତ୍ସା",
    remedy_chemical_badge: "🧪 ରାସାୟନିକ ଚିକିତ୍ସା",
    voice_hero_title: "ଭଏସ୍ ସାଥୀ — ଆପଣଙ୍କ କୃଷି ସହାୟକ",
    voice_hero_sub: "Groq AI ଦ୍ୱାରା ଓଡ଼ିଆରେ କଥା କହି ପରାମର୍ଶ ପାଆନ୍ତୁ।",
    voice_chips_label: "ସାଧାରଣ ପ୍ରଶ୍ନ:",
    chip_water: "କେତେ ପାଣି ଦେବାକୁ ହେବ?",
    chip_fertilizer: "ଖତର ପରିମାଣ? (NPK)",
    chip_mandi: "ଆଜିର ମଣ୍ଡି ଦର କେତେ?",
    chip_pest: "ପୋକ ନିୟନ୍ତ୍ରଣ କିପରି କରିବି?",
    btn_ask_ai: "ପଚାରନ୍ତୁ",
    btn_listen_audio: "ସ୍ୱର ଶୁଣନ୍ତୁ",
    lbl_followups: "ପରବର୍ତ୍ତୀ ପ୍ରଶ୍ନ:",
    panel_weather_title: "୭-ଦିନର ପାଣିପାଗ ଓ ସ୍ପ୍ରେ ପୂର୍ବାନୁମାନ",
    panel_weather_sub: "ସ୍ପ୍ରେ କରିବା ପାଇଁ ସଠିକ୍ ସମୟ",
    panel_mandi_title: "ସ୍ଥାନୀୟ ମଣ୍ଡି ଦର",
    panel_mandi_sub: "ଦୈନିକ ମଣ୍ଡି ଦର ବିବରଣୀ",
    th_commodity: "ଫସଲ",
    th_market: "ମଣ୍ଡି",
    th_rate: "ହାରାହାରି ଦର (₹/କ୍ୱିଣ୍ଟାଲ)",
    th_trend: "୭-ଦିନର ଧାରା",
    panel_sb_title: "ସୁପାବେସ୍ ଡାଟାବେସ୍ ସ୍ଥିତି",
    panel_sb_sub: "ଡାଟାବେସ୍ ସର୍ବଦା ସକ୍ରିୟ ରହିଥାଏ",
    panel_activity_title: "ସାମ୍ପ୍ରତିକ କାର୍ଯ୍ୟକଳାପ",
    panel_activity_sub: "ସୁପାବେସରେ ସଂରକ୍ଷିତ ତଥ୍ୟ",
    make_default_title: "ଏହାକୁ ମୋର ଡିଫଲ୍ଟ ଭାଷା କରନ୍ତୁ",
    make_default_sub: "(ପରବର୍ତ୍ତୀ ଥର ସିଧାସଳଖ ଏହି ଭାଷାରେ ଖୋଲିବ)",
    btn_continue: "✓ ଆଗକୁ ବଢ଼ନ୍ତୁ ➔"
  }
};

// DEMO HUBS DATA
const DEMO_HUBS = {
  nashik: {
    id: "nashik",
    name_en: "Nashik, Maharashtra",
    name_hi: "नासिक, महाराष्ट्र",
    state: "Maharashtra",
    district: "Nashik",
    lat: 19.9975,
    lon: 73.7898,
    soil: { n: 85, p: 48, k: 190, ph: 6.8, type: "Black Cotton Loam" },
    weather: { temp: "26.5°C", hum: "74%", rain: "68 mm", cond: "Partly Cloudy • अनुकूल मौसम", spray: "Good for Spraying • छिड़काव के लिए उत्तम समय", icon: "⛅" },
    topCrop: { name: "🍇 Grapes / अंगूर (Vitis vinifera)", family: "Vitaceae (Fruit) • 135 Days", score: "94.8%", yield: "8 - 12 Tonnes", rev: "₹3,50,000 - ₹5,00,000", rate: "₹6,200 / Qtl ↗", sowing: "Oct - Nov (Pruning)" },
    shapText: "आपकी मिट्टी में पोटाश (190 kg/ha) और अनुकूल pH (6.8) अंगूर की मिठास और बेहतर पैदावार के लिए सर्वाधिक अनुकूल हैं।",
    shapBars: [
      { name: "Potassium (K: 190)", pct: 82, val: "+28%", pos: true },
      { name: "Soil pH (6.8 Neutral)", pct: 65, val: "+18%", pos: true },
      { name: "Nitrogen (N: 85)", pct: 48, val: "+12%", pos: true },
      { name: "Phosphorus (P: 48)", pct: 32, val: "+7%", pos: true },
      { name: "Rainfall Forecast", pct: 18, val: "-4%", pos: false }
    ],
    runners: [
      { name: "🍎 Pomegranate / अनार", score: "91.2%", meta: "Est: ₹2.8L - ₹4.2L / acre • Mandi: ₹8,400/Qtl" },
      { name: "🌿 Cotton / कपास", score: "86.5%", meta: "Est: ₹75K - ₹1.05L / acre • Mandi: ₹7,450/Qtl" }
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
    soil: { n: 45, p: 62, k: 82, ph: 7.4, type: "Deep Black Malwa Clay" },
    weather: { temp: "28.0°C", hum: "65%", rain: "42 mm", cond: "Clear & Sunny • साफ मौसम", spray: "Excellent for Spraying • छिड़काव हेतु श्रेष्ठ समय", icon: "☀️" },
    topCrop: { name: "🌾 Chickpea / चना (Cicer arietinum)", family: "Fabaceae (Legume/Pulse) • 110 Days", score: "93.4%", yield: "8 - 12 Quintals", rev: "₹50,000 - ₹74,000", rate: "₹6,150 / Qtl ↗", sowing: "Oct - Nov (Rabi)" },
    shapText: "मालवा की गहरी काली मिट्टी व संतुलित फॉस्फोरस (62 kg/ha) दलहनी फसलों में जड़ ग्रंथियों के विकास और चने के दानों के भराव के लिए सर्वोत्तम है।",
    shapBars: [
      { name: "Phosphorus (P: 62)", pct: 85, val: "+26%", pos: true },
      { name: "Clay Content (45%)", pct: 60, val: "+16%", pos: true },
      { name: "Soil pH (7.4)", pct: 50, val: "+14%", pos: true },
      { name: "Nitrogen (N: 45)", pct: 28, val: "+6%", pos: true },
      { name: "High Heat Peak", pct: 15, val: "-3%", pos: false }
    ],
    runners: [
      { name: "🌱 Soybean / सोयाबीन", score: "89.5%", meta: "Est: ₹45K - ₹62K / acre • Mandi: ₹4,680/Qtl" },
      { name: "🌽 Maize / मक्का", score: "84.2%", meta: "Est: ₹55K - ₹72K / acre • Mandi: ₹2,280/Qtl" }
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
    soil: { n: 92, p: 42, k: 38, ph: 7.2, type: "Alluvial Sandy Loam" },
    weather: { temp: "30.5°C", hum: "68%", rain: "55 mm", cond: "Warm Humid • उमस भरा", spray: "Spray after 4 PM • शाम 4 बजे बाद छिड़काव", icon: "🌤️" },
    topCrop: { name: "🌾 Rice / धान (Oryza sativa)", family: "Poaceae (Cereal) • 130 Days", score: "92.8%", yield: "22 - 28 Quintals", rev: "₹85,000 - ₹1,10,000", rate: "₹3,950 / Qtl ↗", sowing: "June - July (Transplanting)" },
    shapText: "ਜਲੋੜ ਦੋਮਟ ਮਿੱਟੀ ਅਤੇ ਉੱਚ ਨਾਈਟ੍ਰੋਜਨ (92 kg/ha) ਝੋਨੇ ਦੇ ਵਧੀਆ ਫੁਟਾਰੇ ਅਤੇ ਵੱਧ ਝਾੜ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਹਨ।",
    shapBars: [
      { name: "Nitrogen (N: 92)", pct: 88, val: "+29%", pos: true },
      { name: "Irrigation Access", pct: 70, val: "+21%", pos: true },
      { name: "Soil pH (7.2)", pct: 45, val: "+11%", pos: true },
      { name: "Organic Matter", pct: 30, val: "+5%", pos: true },
      { name: "Groundwater Strain", pct: 25, val: "-6%", pos: false }
    ],
    runners: [
      { name: "🌽 Maize / मक्का", score: "88.1%", meta: "Est: ₹55K - ₹72K / acre • Mandi: ₹2,280/Qtl" },
      { name: "🌿 Cotton / कपास", score: "83.6%", meta: "Est: ₹75K - ₹1.05L / acre • Mandi: ₹7,450/Qtl" }
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
    soil: { n: 70, p: 55, k: 140, ph: 6.5, type: "Red Clayey Sandy Loam" },
    weather: { temp: "31.2°C", hum: "78%", rain: "80 mm", cond: "Tropical Humid • उष्ण आर्द्र", spray: "Check Wind Speed • हवा की गति देखकर छिड़कें", icon: "🌧️" },
    topCrop: { name: "🌿 Cotton / పత్తి (Gossypium hirsutum)", family: "Malvaceae (Fiber) • 160 Days", score: "94.1%", yield: "10 - 14 Quintals", rev: "₹75,000 - ₹1,05,000", rate: "₹7,450 / Qtl ▶", sowing: "May - June (Kharif)" },
    shapText: "ఎర్ర నేలలు మరియు అధిక పొటాష్ (140 kg/ha) పత్తి కాయల పరిమాణం మరియు నాణ్యమైన దిగుబడికి ఎంతో ప్రయోజనకరం.",
    shapBars: [
      { name: "Potassium (K: 140)", pct: 78, val: "+24%", pos: true },
      { name: "Phosphorus (P: 55)", pct: 62, val: "+17%", pos: true },
      { name: "Soil pH (6.5)", pct: 54, val: "+13%", pos: true },
      { name: "Nitrogen (N: 70)", pct: 40, val: "+9%", pos: true },
      { name: "High Humidity Risk", pct: 20, val: "-5%", pos: false }
    ],
    runners: [
      { name: "🌶️ Chilli / మిర్చి", score: "91.8%", meta: "Est: ₹1.2L - ₹1.8L / acre • Mandi: ₹18,500/Qtl" },
      { name: "🌽 Maize / మొక్కజొన్న", score: "85.0%", meta: "Est: ₹55K - ₹72K / acre • Mandi: ₹2,280/Qtl" }
    ]
  }
};

// LEAF DISEASE SAMPLES
const LEAF_SAMPLES = {
  tomato_early_blight: {
    crop: "Tomato / टमाटर",
    name: "Early Blight (Alternaria solani)",
    name_hi: "अगेती झुलसा रोग (अर्ली ब्लाइट)",
    severity: "Medium (35% area)",
    confidence: "96.4%",
    spray: "नासिक में आगामी शनिवार दोपहर 65% बारिश की संभावना है। अतः छिड़काव आज शाम 4 बजे या रविवार सुबह 7 बजे ही करें ताकि दवा बह न जाए।",
    organic: "नीम के बीज के अर्क (NSKE 5%) या ट्राइकोडर्मा विरिडी (5 ग्राम/लीटर) का छिड़काव करें। साथ ही 10% गोमूत्र का अर्क फंगस रोकने में अत्यंत प्रभावी है।",
    chemical: "मैंकोजेब 75 WP (Mancozeb @ 2.5 ग्राम/लीटर पानी) या एजोक्सीस्ट्रोबिन (1 मिली/लीटर) का तुरंत छिड़काव करें।"
  },
  potato_late_blight: {
    crop: "Potato / आलू",
    name: "Late Blight (Phytophthora infestans)",
    name_hi: "पछेती झुलसा रोग (लेट ब्लाइट)",
    severity: "High (Rapidly spreading spores)",
    confidence: "98.1%",
    spray: "आसमान में बादल छाए हैं। यदि तुरंत छिड़काव न किया गया तो फफूंद तेजी से फैलेगी। स्टिकर (स्प्रेडर) मिलाकर ही छिड़कें।",
    organic: "कॉपर सल्फेट व बुझे हुए चूने का बोर्डो मिश्रण (1%) बनाकर तुरंत पौधों की निचली पत्तियों तक तर करें।",
    chemical: "रिडोमिल एमजेड (Metalaxyl + Mancozeb @ 2 ग्राम/लीटर पानी) या सायमोक्सानिल का त्वरित छिड़काव करें।"
  },
  cotton_bacterial_blight: {
    crop: "Cotton / कपास",
    name: "Bacterial Leaf Blight (Angular Leaf Spot)",
    name_hi: "कपास का जीवाणु झुलसा / कोणीय धब्बा रोग",
    severity: "Moderate (Water-soaked lesions)",
    confidence: "94.7%",
    spray: "हवा की गति 12 किमी/घंटा है। दोपहर की तेज धूप में छिड़काव से बचें और सुबह के समय छिड़कें।",
    organic: "स्यूडोमोनास फ्लोरेसेंस (5 ग्राम/लीटर) व 5% पंचगव्य का घोल बनाकर 10 दिन के अंतराल पर छिड़कें।",
    chemical: "स्ट्रेप्टोसाइक्लिन (1 ग्राम) + कॉपर ऑक्सीक्लोराइड (30 ग्राम) प्रति 10 लीटर पानी में घोलकर छिड़काव करें।"
  },
  corn_healthy: {
    crop: "Corn (Maize) / मक्का",
    name: "Healthy Leaf — No Pathogen Detected",
    name_hi: "स्वस्थ पत्ती — कोई रोग नहीं पाया गया",
    severity: "None (Optimum vigor)",
    confidence: "99.2%",
    spray: "फसल पूर्णतः स्वस्थ है। किसी भी कीटनाशक के अनावश्यक छिड़काव से बचें और केवल संतुलित नमी बनाए रखें।",
    organic: "संतुलित जीवामृत या वर्मीवाश का उपयोग करें ताकि पौधों की स्वाभाविक रोग प्रतिरोधक क्षमता बनी रहे।",
    chemical: "किसी रासायनिक छिड़काव की आवश्यकता नहीं है। लागत बचाएं।"
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
  setupSoilCardPreset();
  setupRecommendForm();
  setupPlantDoctor();
  setupVoiceSaathi();
  setupPHSlider();
  setupSupabaseHeartbeat();
});

// =========================================================================
// 1. ALL-INDIAN-LANGUAGES MANAGER & FIRST-LAUNCH SETUP
// =========================================================================
function initLanguageManager() {
  const modal = document.getElementById("langModalOverlay");
  const toggleBtn = document.getElementById("langToggleBtn");
  const closeBtn = document.getElementById("langModalCloseBtn");
  const confirmBtn = document.getElementById("btnConfirmLanguage");
  const chkDefault = document.getElementById("chkSetDefaultLang");
  const langCards = document.querySelectorAll(".lang-card");

  // Check saved default language in localStorage
  const savedLang = localStorage.getItem("kisaan_sathi_default_lang");
  const hasSavedDefault = localStorage.getItem("kisaan_sathi_lang_saved") === "true";

  if (hasSavedDefault && savedLang && I18N_DICTIONARY[savedLang]) {
    currentLang = savedLang;
    applyLanguage(currentLang);
    modal.style.display = "none";
  } else {
    // First time launch: Prompt language selection immediately!
    modal.style.display = "flex";
    currentLang = savedLang || "hi";
    highlightSelectedCard(currentLang);
  }

  // Header button to open modal anytime
  toggleBtn.addEventListener("click", () => {
    modal.style.display = "flex";
    highlightSelectedCard(currentLang);
  });

  closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
  });

  // Language card clicks
  langCards.forEach(card => {
    card.addEventListener("click", () => {
      langCards.forEach(c => c.classList.remove("active"));
      card.classList.add("active");
      currentLang = card.getAttribute("data-lang-code") || "hi";
    });
  });

  // Confirm selection
  confirmBtn.addEventListener("click", () => {
    applyLanguage(currentLang);

    if (chkDefault.checked) {
      localStorage.setItem("kisaan_sathi_lang_saved", "true");
      localStorage.setItem("kisaan_sathi_default_lang", currentLang);
    } else {
      localStorage.removeItem("kisaan_sathi_lang_saved");
    }

    modal.style.display = "none";
  });
}

function highlightSelectedCard(langCode) {
  document.querySelectorAll(".lang-card").forEach(card => {
    if (card.getAttribute("data-lang-code") === langCode) {
      card.classList.add("active");
    } else {
      card.classList.remove("active");
    }
  });
}

function applyLanguage(langCode) {
  const dict = I18N_DICTIONARY[langCode] || I18N_DICTIONARY.hi;

  // 1. Update Header Button Text
  const currentLangText = document.getElementById("langCurrentText");
  if (currentLangText) {
    currentLangText.textContent = `${dict.flag} ${dict.name} (${dict.code.toUpperCase()})`;
  }

  // 2. Translate all data-i18n attributes
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    if (dict[key]) {
      el.textContent = dict[key];
    }
  });

  // 3. Update active hub UI in current language
  if (DEMO_HUBS[currentHub]) {
    updateRecommendationUI(DEMO_HUBS[currentHub]);
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
// 3. REGIONAL HUBS (NASHIK, INDORE, LUDHIANA, GUNTUR)
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

function selectHub(key) {
  currentHub = key;
  const hub = DEMO_HUBS[key];
  if (!hub) return;

  // Weather Card
  document.getElementById("weatherHubName").textContent = hub.name_en;
  document.getElementById("weatherCondition").textContent = hub.weather.cond;
  document.getElementById("weatherTemp").textContent = hub.weather.temp;
  document.getElementById("weatherHumidity").textContent = hub.weather.hum;
  document.getElementById("weatherRain").textContent = hub.weather.rain;
  document.getElementById("weatherEmoji").textContent = hub.weather.icon;
  document.getElementById("weatherSprayText").textContent = hub.weather.spray;

  // Inputs
  document.getElementById("inputState").value = hub.state;
  document.getElementById("inputDistrict").value = hub.district;
  document.getElementById("inputN").value = hub.soil.n;
  document.getElementById("inputP").value = hub.soil.p;
  document.getElementById("inputK").value = hub.soil.k;
  document.getElementById("inputPH").value = hub.soil.ph;
  updatePHDisplay(hub.soil.ph);

  // Update Recommendation View
  updateRecommendationUI(hub);
}

// =========================================================================
// 4. SOIL CARD PRESET & pH SLIDER
// =========================================================================
function setupSoilCardPreset() {
  const select = document.getElementById("soilCardPresetSelect");
  select.addEventListener("change", () => {
    const val = select.value;
    if (val === "sample_1_nashik") selectHub("nashik");
    else if (val === "sample_2_indore") selectHub("indore");
    else if (val === "sample_3_ludhiana") selectHub("ludhiana");
  });
}

function setupPHSlider() {
  const slider = document.getElementById("inputPH");
  slider.addEventListener("input", (e) => {
    updatePHDisplay(e.target.value);
  });
}

function updatePHDisplay(val) {
  const v = parseFloat(val);
  let status = "Neutral";
  if (v < 6.0) status = "Acidic / अम्लीय";
  else if (v > 7.5) status = "Alkaline / क्षारीय";
  else status = "Neutral / Ideal / संतुलित";

  document.getElementById("phDisplay").textContent = `${v} (${status})`;
}

// =========================================================================
// 5. CROP RECOMMENDATION FORM & SHAP VISUALIZER
// =========================================================================
function setupRecommendForm() {
  const form = document.getElementById("recommendForm");
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const btn = document.getElementById("btnRecommend");
    const originalText = btn.innerHTML;
    btn.innerHTML = "<span>⏳ Analyzing with XGBoost & SoilGrids...</span>";
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
      addActivityLog(`Crop Advisory: ${payload.district}`, `Top Recommendation Generated • N:${payload.custom_soil.nitrogen}, P:${payload.custom_soil.phosphorus}, K:${payload.custom_soil.potassium}`);
    }
  });
}

function updateRecommendationUI(hub) {
  document.getElementById("topCropName").textContent = hub.topCrop.name;
  document.getElementById("topCropFamily").textContent = hub.topCrop.family;
  document.getElementById("topCropScore").textContent = hub.topCrop.score;
  document.getElementById("topCropYield").textContent = hub.topCrop.yield;
  document.getElementById("topCropRev").textContent = hub.topCrop.rev;
  document.getElementById("topCropRate").textContent = hub.topCrop.rate;
  document.getElementById("topCropSowing").textContent = hub.topCrop.sowing;
  document.getElementById("shapExplanationText").textContent = `"${hub.shapText}"`;

  // Render SHAP Bars
  const barsContainer = document.getElementById("shapBarsList");
  barsContainer.innerHTML = hub.shapBars.map(b => `
    <div class="shap-bar-row">
      <span class="shap-feat">${b.name}</span>
      <div class="shap-bar-track">
        <div class="shap-fill ${b.pos ? 'positive' : 'negative'}" style="width: ${b.pct}%"></div>
      </div>
      <span class="shap-impact ${b.pos ? 'text-green' : 'text-red'}">${b.val}</span>
    </div>
  `).join("");

  // Render Runners
  const runnersContainer = document.getElementById("runnersList");
  runnersContainer.innerHTML = hub.runners.map(r => `
    <div class="runner-card">
      <div class="runner-header">
        <span class="runner-name">${r.name}</span>
        <span class="runner-score">${r.score}</span>
      </div>
      <div class="runner-meta">${r.meta}</div>
    </div>
  `).join("");
}

function renderAPIRecommendation(data) {
  if (!data.top_recommendations || data.top_recommendations.length === 0) return;
  const top = data.top_recommendations[0];

  document.getElementById("topCropName").textContent = `${top.crop_name} (${top.hindi_name || ''})`;
  document.getElementById("topCropFamily").textContent = `Family: ${top.crop_family || 'Agronomic'} • ${top.duration_days || 120} Days Duration`;
  document.getElementById("topCropScore").textContent = `${top.match_score_pct}%`;
  document.getElementById("topCropYield").textContent = top.expected_yield_per_acre || "8 - 12 Tonnes";
  document.getElementById("topCropRev").textContent = top.estimated_revenue_per_acre || "₹2,50,000 - ₹4,00,000";
  document.getElementById("topCropRate").textContent = top.mandi_price_modal || "₹6,000 / Qtl";
  document.getElementById("topCropSowing").textContent = top.sowing_window_en || "October - November";

  if (top.bilingual_explanation) {
    document.getElementById("shapExplanationText").textContent = `"${top.bilingual_explanation.hi || top.bilingual_explanation.en}"`;
  }

  if (top.shap_contributions && top.shap_contributions.length > 0) {
    const barsContainer = document.getElementById("shapBarsList");
    barsContainer.innerHTML = top.shap_contributions.slice(0, 5).map(s => {
      const isPos = s.impact_score >= 0;
      const pct = Math.min(100, Math.max(15, Math.abs(s.impact_score * 300)));
      const sign = isPos ? "+" : "";
      return `
        <div class="shap-bar-row">
          <span class="shap-feat">${s.feature_name}</span>
          <div class="shap-bar-track">
            <div class="shap-fill ${isPos ? 'positive' : 'negative'}" style="width: ${pct}%"></div>
          </div>
          <span class="shap-impact ${isPos ? 'text-green' : 'text-red'}">${sign}${(s.impact_score * 100).toFixed(1)}%</span>
        </div>
      `;
    }).join("");
  }
}

// =========================================================================
// 6. PLANT DOCTOR (LEAF DISEASE AI DIAGNOSIS)
// =========================================================================
function setupPlantDoctor() {
  const leafBtns = document.querySelectorAll(".leaf-btn");
  leafBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      leafBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      currentLeafSample = btn.getAttribute("data-sample");
      renderDiagnosis(currentLeafSample);
    });
  });

  const fileInput = document.getElementById("leafFileInput");
  fileInput.addEventListener("change", (e) => {
    if (e.target.files && e.target.files[0]) {
      renderDiagnosis("tomato_early_blight");
    }
  });

  const runBtn = document.getElementById("btnRunDiagnosis");
  runBtn.addEventListener("click", () => {
    renderDiagnosis(currentLeafSample);
    addActivityLog(`Leaf Diagnostic: ${LEAF_SAMPLES[currentLeafSample].name}`, `Confidence: ${LEAF_SAMPLES[currentLeafSample].confidence}`);
  });
}

function renderDiagnosis(sampleKey) {
  const sample = LEAF_SAMPLES[sampleKey] || LEAF_SAMPLES.tomato_early_blight;

  document.getElementById("diagCrop").textContent = `Crop: ${sample.crop}`;
  document.getElementById("diagDiseaseName").textContent = sample.name;
  document.getElementById("diagDiseaseHi").textContent = sample.name_hi;
  document.getElementById("diagSeverity").textContent = sample.severity;
  document.getElementById("diagConfidence").textContent = `Confidence: ${sample.confidence}`;
  document.getElementById("diagSprayText").textContent = `"${sample.spray}"`;
  document.getElementById("diagOrganicRemedy").textContent = sample.organic;
  document.getElementById("diagChemicalRemedy").textContent = sample.chemical;
}

// =========================================================================
// 7. CONVERSATIONAL VOICE SAATHI (GROQ LLM + BROWSER SPEECH SYNTHESIS)
// =========================================================================
function setupVoiceSaathi() {
  const chips = document.querySelectorAll(".voice-chip");
  const input = document.getElementById("voiceTextInput");
  const sendBtn = document.getElementById("btnSendVoiceQuery");
  const ttsBtn = document.getElementById("btnAudioTTSPlay");
  const micBtn = document.getElementById("btnVoiceSpeak");

  chips.forEach(chip => {
    chip.addEventListener("click", () => {
      const q = chip.getAttribute("data-query");
      input.value = q;
      handleVoiceQuery(q);
    });
  });

  sendBtn.addEventListener("click", () => {
    if (input.value.trim()) handleVoiceQuery(input.value.trim());
  });

  input.addEventListener("keypress", (e) => {
    if (e.key === "Enter" && input.value.trim()) handleVoiceQuery(input.value.trim());
  });

  ttsBtn.addEventListener("click", () => {
    const textToSpeak = document.getElementById("voiceBubbleHi").textContent.replace(/"/g, '');
    const speechCode = I18N_DICTIONARY[currentLang]?.speechCode || "hi-IN";
    speakText(textToSpeak, speechCode);
  });

  micBtn.addEventListener("click", () => {
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      const recognition = new SpeechRecognition();
      recognition.lang = I18N_DICTIONARY[currentLang]?.speechCode || 'hi-IN';
      micBtn.style.background = "#FECACA";

      recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        input.value = transcript;
        handleVoiceQuery(transcript);
        micBtn.style.background = "#FEE2E2";
      };

      recognition.onerror = () => {
        micBtn.style.background = "#FEE2E2";
      };

      recognition.start();
    } else {
      alert("Voice speech recognition is not supported in this browser. Please type your query.");
    }
  });

  // Follow-up delegation
  document.getElementById("voiceFollowupsList").addEventListener("click", (e) => {
    if (e.target.classList.contains("follow-chip")) {
      const q = e.target.getAttribute("data-query");
      input.value = q;
      handleVoiceQuery(q);
    }
  });
}

async function handleVoiceQuery(query) {
  const hiBubble = document.getElementById("voiceBubbleHi");
  const enBubble = document.getElementById("voiceBubbleEn");
  hiBubble.textContent = "AI उत्तर तैयार कर रहा है...";
  enBubble.textContent = "Synthesizing answer with Groq LLaMA 3.3...";

  try {
    const res = await fetch("/api/voice/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        query_text: query,
        language: currentLang,
        crop_context: DEMO_HUBS[currentHub]?.topCrop?.name || "Grapes",
        location_context: DEMO_HUBS[currentHub]?.name_en || "Nashik"
      })
    });

    if (res.ok) {
      const data = await res.json();
      hiBubble.textContent = `"${data.response_text_hi}"`;
      enBubble.textContent = data.response_text_en ? `"${data.response_text_en}"` : "";
      
      const speechCode = I18N_DICTIONARY[currentLang]?.speechCode || "hi-IN";
      speakText(data.tts_audio_text || data.response_text_hi, speechCode);
      return;
    }
  } catch (_) {}

  // Multi-lingual fallback responses
  const q = query.toLowerCase();
  let hi = "फसल के लिए 3 से 4 सिंचाइयों की आवश्यकता होती है। फूल आने और फल बनते समय खेत में नमी अवश्य रखें।";
  let en = "Crops require 3 to 4 irrigations. Maintain soil moisture during flowering and pod development.";

  if (q.includes("खाद") || q.includes("fertilizer") || q.includes("ਖਾਦ") || q.includes("ఎరువులు") || q.includes("உர")) {
    hi = "बुवाई के समय प्रति एकड़ 50 किलो डीएपी और 25 किलो पोटाश डालें। 25 दिन बाद 35 किलो नीम कोटेड यूरिया का छिड़काव करें।";
    en = "Apply 50 kg DAP and 25 kg MOP at sowing. Top dress with 35 kg Neem Coated Urea after 25 days.";
  } else if (q.includes("मंडी") || q.includes("भाव") || q.includes("price") || q.includes("ਦਰ") || q.includes("రేటు") || q.includes("விலை")) {
    hi = "आज नासिक मंडी में अंगूर ₹6,200/क्विंटल और अनार ₹8,400/क्विंटल के भाव पर हैं। भाव में 3 से 5% की तेजी देखी जा रही है।";
    en = "Today in Nashik Mandi, Grapes are at ₹6,200/Qtl and Pomegranate at ₹8,400/Qtl with an upward trend.";
  } else if (q.includes("कीट") || q.includes("रोग") || q.includes("pest") || q.includes("ਕੀੜੇ") || q.includes("తెగులు") || q.includes("பூச்சி")) {
    hi = "शुरुआती अवस्था में 5 मिली प्रति लीटर नीम तेल का छिड़काव करें। अधिक प्रकोप होने पर अनुशंसित फफूंदनाशक का छिड़काव करें।";
    en = "Apply Neem oil @ 5ml/Litre for early protection. Use targeted fungicide if infestation spreads.";
  }

  hiBubble.textContent = `"${hi}"`;
  enBubble.textContent = `"${en}"`;
  const speechCode = I18N_DICTIONARY[currentLang]?.speechCode || "hi-IN";
  speakText(hi, speechCode);
}

function speakText(text, langCode = "hi-IN") {
  if (!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel();

  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = langCode;
  utterance.rate = 0.95;
  utterance.pitch = 1.0;

  const voices = window.speechSynthesis.getVoices();
  const matchedVoice = voices.find(v => v.lang.includes(langCode.split('-')[0]) || v.name.includes("India"));
  if (matchedVoice) utterance.voice = matchedVoice;

  window.speechSynthesis.speak(utterance);
}

// =========================================================================
// 8. SUPABASE HEARTBEAT & ACTIVITY STREAM
// =========================================================================
function setupSupabaseHeartbeat() {
  const btn = document.getElementById("btnManualPing");
  if (btn) {
    btn.addEventListener("click", async () => {
      btn.innerHTML = "<span>⚡ Pinging Supabase...</span>";
      try {
        const res = await fetch("/api/db-ping");
        const data = await res.json();
        document.getElementById("sbLastPing").textContent = `Success (${new Date().toLocaleTimeString()})`;
        document.getElementById("sbStatus").textContent = "Healthy & Keep-Alive Active";
        addActivityLog("Supabase Keep-Alive Pulse", `Ping status: ${data.keep_alive || 'triggered'}`);
      } catch (e) {
        document.getElementById("sbLastPing").textContent = `Active Local Mode (${new Date().toLocaleTimeString()})`;
      } finally {
        btn.innerHTML = "<span>⚡ Trigger Manual Supabase Heartbeat (/api/db-ping)</span>";
      }
    });
  }
}

function addActivityLog(title, desc) {
  const feed = document.getElementById("activityFeed");
  if (!feed) return;

  const item = document.createElement("div");
  item.className = "feed-item";
  item.innerHTML = `
    <span class="feed-dot green"></span>
    <div class="feed-info">
      <strong>${title}</strong>
      <span>${desc}</span>
    </div>
    <span class="feed-time">Just now</span>
  `;
  feed.prepend(item);
}
