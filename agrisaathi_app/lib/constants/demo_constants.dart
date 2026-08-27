class DemoConstants {
  static const String backendBaseUrl = "http://127.0.0.1:8000";

  static const List<Map<String, dynamic>> demoLocations = [
    {
      "id": "nashik",
      "name_en": "Nashik, Maharashtra",
      "name_hi": "नासिक, महाराष्ट्र",
      "lat": 19.9975,
      "lon": 73.7898,
      "state": "Maharashtra",
      "district": "Nashik",
      "soil_type": "Black Cotton (Regur) Loam",
      "primary_crops": ["Grapes", "Pomegranate", "Cotton", "Maize"]
    },
    {
      "id": "indore",
      "name_en": "Indore, Madhya Pradesh",
      "name_hi": "इंदौर, मध्य प्रदेश",
      "lat": 22.7196,
      "lon": 75.8577,
      "state": "Madhya Pradesh",
      "district": "Indore",
      "soil_type": "Deep Black Malwa Clay",
      "primary_crops": ["Chickpea", "Soybean", "Maize", "Blackgram"]
    },
    {
      "id": "ludhiana",
      "name_en": "Ludhiana, Punjab",
      "name_hi": "लुधियाना, पंजाब",
      "lat": 30.9010,
      "lon": 75.8573,
      "state": "Punjab",
      "district": "Ludhiana",
      "soil_type": "Alluvial Sandy Loam",
      "primary_crops": ["Rice", "Maize", "Cotton", "Wheat"]
    },
    {
      "id": "guntur",
      "name_en": "Guntur, Andhra Pradesh",
      "name_hi": "गुंटूर, आंध्र प्रदेश",
      "lat": 16.3067,
      "lon": 80.4365,
      "state": "Andhra Pradesh",
      "district": "Guntur",
      "soil_type": "Red Clayey Sandy Loam",
      "primary_crops": ["Cotton", "Maize", "Rice", "Chilli"]
    }
  ];

  static const List<Map<String, dynamic>> sampleSoilCards = [
    {
      "id": "sample_1_nashik",
      "title": "Nashik MahaSoil Health Card #MH-4012",
      "farmer": "Ramesh Kisan Patil",
      "date": "18 May 2026",
      "n": 85.0,
      "p": 48.0,
      "k": 190.0,
      "ph": 6.8,
      "oc": 0.72,
      "texture": "Medium Black Clay Loam"
    },
    {
      "id": "sample_2_indore",
      "title": "MP Krishi Vigyan Soil Lab #MP-8830",
      "farmer": "Vikram Singh Chouhan",
      "date": "12 June 2026",
      "n": 45.0,
      "p": 62.0,
      "k": 82.0,
      "ph": 7.4,
      "oc": 0.58,
      "texture": "Deep Black Malwa Clay"
    },
    {
      "id": "sample_3_ludhiana",
      "title": "PAU Ludhiana Testing Cell #PB-1049",
      "farmer": "Gurpreet Singh Dhillon",
      "date": "22 April 2026",
      "n": 92.0,
      "p": 42.0,
      "k": 38.0,
      "ph": 7.2,
      "oc": 0.45,
      "texture": "Alluvial Sandy Loam"
    }
  ];

  static const List<Map<String, dynamic>> leafDiseaseSamples = [
    {
      "crop": "Tomato / आलू-टमाटर",
      "disease_name_en": "Early Blight (Alternaria solani)",
      "disease_name_hi": "अगेती झुलसा रोग (अर्ली ब्लाइट)",
      "severity": "Medium (35% area affected)",
      "confidence": 96.4,
      "organic_remedy_en": "Spray 5ml/L Neem Seed Kernel Extract (NSKE 5%) or Trichoderma viride.",
      "organic_remedy_hi": "नीम के तेल का 5 मिली/लीटर घोल या ट्राइकोडर्मा विरिडी का छिड़काव करें।",
      "chemical_remedy_en": "Spray Mancozeb 75 WP @ 2.5g/Litre or Azoxystrobin @ 1ml/Litre.",
      "chemical_remedy_hi": "मैंकोजेब 75 WP (2.5 ग्राम/लीटर) या एजोक्सीस्ट्रोबिन (1 मिली/लीटर) का छिड़काव करें।"
    },
    {
      "crop": "Potato / आलू",
      "disease_name_en": "Late Blight (Phytophthora infestans)",
      "disease_name_hi": "पछेती झुलसा रोग (लेट ब्लाइट)",
      "severity": "High (Rapidly spreading fungal spores)",
      "confidence": 98.1,
      "organic_remedy_en": "Apply copper hydroxide bio-formulation and ensure adequate sunlight penetration.",
      "organic_remedy_hi": "कॉपर सल्फेट व चूने का बोर्डो मिश्रण (1%) छिड़कें तथा खेत में जल न भरने दें।",
      "chemical_remedy_en": "Spray Metalaxyl + Mancozeb (Ridomil MZ) @ 2g/Litre water.",
      "chemical_remedy_hi": "रिडोमिल (2 ग्राम/लीटर पानी) का तुरंत छिड़काव करें।"
    },
    {
      "crop": "Cotton / कपास",
      "disease_name_en": "Bacterial Leaf Blight / Angular Leaf Spot",
      "disease_name_hi": "कपास का जीवाणु झुलसा / कोणीय धब्बा रोग",
      "severity": "Moderate (Water-soaked angular lesions)",
      "confidence": 94.7,
      "organic_remedy_en": "Spray Pseudomonas fluorescens @ 5g/Litre + Panchagavya.",
      "organic_remedy_hi": "स्यूडोमोनास फ्लोरेसेंस (5 ग्राम/लीटर) का छिड़काव करें।",
      "chemical_remedy_en": "Spray Streptocycline (100 ppm) + Copper Oxychloride @ 3g/Litre.",
      "chemical_remedy_hi": "स्ट्रेप्टोसाइक्लिन (1 ग्राम) + कॉपर ऑक्सीक्लोराइड (30 ग्राम) प्रति 10 लीटर पानी में मिलाकर छिड़कें।"
    },
    {
      "crop": "Corn (Maize) / मक्का",
      "disease_name_en": "Healthy Leaf — No Pathogen Detected",
      "disease_name_hi": "स्वस्थ पत्ती — कोई रोग नहीं पाया गया",
      "severity": "None (Optimum vigor)",
      "confidence": 99.2,
      "organic_remedy_en": "Maintain balanced NPK fertilization and monitor regularly.",
      "organic_remedy_hi": "संतुलित पोषण बनाए रखें और समय पर हल्की सिंचाई करें।",
      "chemical_remedy_en": "No chemical application required.",
      "chemical_remedy_hi": "किसी रासायनिक छिड़काव की आवश्यकता नहीं है।"
    }
  ];
}
