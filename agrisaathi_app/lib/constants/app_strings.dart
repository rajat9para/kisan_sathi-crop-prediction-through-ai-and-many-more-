class AppStrings {
  static bool isHindi = true;

  static String get appName => isHindi ? "एग्रीसाथी" : "AgriSaathi";
  static String get appTagline => isHindi ? "स्मार्ट एआई कृषि व फसल सलाहकार" : "AI Hyper-Local Crop Advisory";
  
  // Dashboard & Navigation
  static String get home => isHindi ? "मुख्य पृष्ठ" : "Home";
  static String get advisory => isHindi ? "फसल सलाह" : "Crop Advisory";
  static String get voiceSaathi => isHindi ? "आवाज साथी" : "Voice Saathi";
  static String get leafDoctor => isHindi ? "पत्ती डॉक्टर" : "Leaf Doctor";
  static String get marketMandi => isHindi ? "मंडी भाव" : "Mandi Rates";
  static String get offlineProof => isHindi ? "ऑफलाइन जांच" : "Offline Demo";
  static String get schemesRoadmap => isHindi ? "सरकारी योजनाएं" : "Govt Schemes";

  // Status & Sync
  static String get liveOnline => isHindi ? "लाइव सिंक चालू" : "Live Sync Active";
  static String get offlineMode => isHindi ? "ऑफलाइन मोड (कैश डेटा)" : "Offline Mode (Cached Data)";
  static String get lastUpdated => isHindi ? "अंतिम अपडेट:" : "Last Updated:";
  static String get syncNow => isHindi ? "अभी सिंक करें" : "Sync Now";
  static String get toggleOfflineSim => isHindi ? "एरोप्लेन मोड सिमुलेशन" : "Simulate Airplane Mode";

  // Actions
  static String get getRecommendations => isHindi ? "फसल सिफारिश प्राप्त करें" : "Generate Crop Advisory";
  static String get whyThisCrop => isHindi ? "यही फसल क्यों? (AI विश्लेषण)" : "Why this Crop? (AI Breakdown)";
  static String get scanSoilCard => isHindi ? "मृदा स्वास्थ्य कार्ड स्कैन करें" : "Scan Soil Health Card";
  static String get takeLeafPhoto => isHindi ? "पत्ती की फोटो लें" : "Take Leaf Photo";
  static String get askVoice => isHindi ? "माइक दबाकर पूछें..." : "Tap mic and speak...";

  // Explainability
  static String get explainabilityTitle => isHindi ? "पारदर्शी एआई सिफारिश विश्लेषण" : "Explainable AI Decision Breakdown";
  static String get soilFit => isHindi ? "मिट्टी पोषक अनुकूलता" : "Soil Nutrient Fit";
  static String get weatherFit => isHindi ? "मौसम व जलवायु अनुकूलता" : "Weather & Climate Fit";
  static String get marketProfit => isHindi ? "मंडी लाभप्रदता व रुझान" : "Market Profitability Trend";
  static String get rotationImpact => isHindi ? "फसल चक्र (रोटेशन) प्रभाव" : "Crop Rotation Impact";
  static String get shapDrivers => isHindi ? "निर्णय को प्रभावित करने वाले मुख्य कारक" : "Key Scientific Decision Drivers (SHAP)";
  static String get fertilizerPlan => isHindi ? "उर्वरक प्रबंधन अनुसूची" : "Fertilizer Schedule";
  static String get irrigationPlan => isHindi ? "सिंचाई प्रबंधन" : "Irrigation Plan";
}
