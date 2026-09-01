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
      "soil_type": "Deep Black Malwa Vertisol Clay",
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
      "soil_type": "Indo-Gangetic Alluvial Sandy Loam",
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
      "soil_type": "Coastal Red Clayey Sandy Loam",
      "primary_crops": ["Cotton", "Maize", "Rice", "Chilli"]
    },
    {
      "id": "rajkot",
      "name_en": "Rajkot / Junagadh, Gujarat",
      "name_hi": "राजकोट / जूनागढ़, गुजरात",
      "lat": 22.3039,
      "lon": 70.8022,
      "state": "Gujarat",
      "district": "Rajkot",
      "soil_type": "Saurashtra Medium Black Calcareous Loam",
      "primary_crops": ["Groundnut", "Cotton", "Sesame", "Cumin"]
    },
    {
      "id": "thanjavur",
      "name_en": "Thanjavur, Tamil Nadu",
      "name_hi": "तंजாவూర్, तमिलनाडु",
      "lat": 10.7870,
      "lon": 79.1378,
      "state": "Tamil Nadu",
      "district": "Thanjavur",
      "soil_type": "Cauvery Deltaic Alluvial Silt Clay",
      "primary_crops": ["Rice", "Blackgram", "Sugarcane", "Banana"]
    },
    {
      "id": "bardhaman",
      "name_en": "Bardhaman, West Bengal",
      "name_hi": "बर्धमान, पश्चिम बंगाल",
      "lat": 23.2324,
      "lon": 87.8615,
      "state": "West Bengal",
      "district": "Bardhaman",
      "soil_type": "Lower Gangetic Old Alluvial Clay Loam",
      "primary_crops": ["Rice", "Jute", "Potato", "Mustard"]
    },
    {
      "id": "jaipur",
      "name_en": "Jaipur, Rajasthan",
      "name_hi": "जयपुर, राजस्थान",
      "lat": 26.9124,
      "lon": 75.7873,
      "state": "Rajasthan",
      "district": "Jaipur",
      "soil_type": "Semi-Arid Desert Light Sandy Loam",
      "primary_crops": ["Mothbeans", "Bajra (Pearl Millet)", "Mustard", "Chickpea"]
    },
    {
      "id": "dharwad",
      "name_en": "Dharwad, Karnataka",
      "name_hi": "धारवाड़, कर्नाटक",
      "lat": 15.4589,
      "lon": 75.0078,
      "state": "Karnataka",
      "district": "Dharwad",
      "soil_type": "Western Ghats Red Laterite Loam",
      "primary_crops": ["Maize", "Cotton", "Groundnut", "Soybean"]
    },
    {
      "id": "varanasi",
      "name_en": "Varanasi, Uttar Pradesh",
      "name_hi": "वाराणसी, उत्तर प्रदेश",
      "lat": 25.3176,
      "lon": 82.9739,
      "state": "Uttar Pradesh",
      "district": "Varanasi",
      "soil_type": "Eastern Gangetic Silt Alluvial",
      "primary_crops": ["Wheat", "Rice", "Pigeonpeas", "Lentil"]
    },
    {
      "id": "palakkad",
      "name_en": "Palakkad, Kerala",
      "name_hi": "पालक्काड, केरल",
      "lat": 10.7867,
      "lon": 76.6548,
      "state": "Kerala",
      "district": "Palakkad",
      "soil_type": "High-Rainfall Acidic Peaty Laterite",
      "primary_crops": ["Rice", "Coconut", "Banana", "Black Pepper"]
    }
  ];

  static const List<Map<String, dynamic>> sampleSoilCards = [
    {
      "id": "sample_1_nashik",
      "title": "Nashik MahaSoil Health Card #MH-4012",
      "state": "Maharashtra",
      "card_id": "#SHC-MH-4012",
      "date": "18 May 2026",
      "n": 85.0,
      "p": 48.0,
      "k": 190.0,
      "ph": 6.8,
      "oc": 0.72,
      "texture": "Medium Black Cotton Clay Loam"
    },
    {
      "id": "sample_2_indore",
      "title": "MP Krishi Vigyan Soil Lab #MP-8830",
      "state": "Madhya Pradesh",
      "card_id": "#SHC-MP-8830",
      "date": "12 June 2026",
      "n": 45.0,
      "p": 62.0,
      "k": 82.0,
      "ph": 7.4,
      "oc": 0.58,
      "texture": "Deep Black Malwa Vertisol Clay"
    },
    {
      "id": "sample_3_ludhiana",
      "title": "PAU Ludhiana Testing Cell #PB-1049",
      "state": "Punjab",
      "card_id": "#SHC-PB-1049",
      "date": "22 April 2026",
      "n": 92.0,
      "p": 42.0,
      "k": 38.0,
      "ph": 7.2,
      "oc": 0.45,
      "texture": "Indo-Gangetic Alluvial Sandy Loam"
    },
    {
      "id": "sample_4_guntur",
      "title": "Andhra YSR Rythu Testing #AP-3190",
      "state": "Andhra Pradesh",
      "card_id": "#SHC-AP-3190",
      "date": "04 July 2026",
      "n": 70.0,
      "p": 55.0,
      "k": 140.0,
      "ph": 6.5,
      "oc": 0.65,
      "texture": "Coastal Red Clayey Sandy Loam"
    },
    {
      "id": "sample_5_rajkot",
      "title": "Gujarat Krishi Mahotsav Lab #GJ-5521",
      "state": "Gujarat",
      "card_id": "#SHC-GJ-5521",
      "date": "30 May 2026",
      "n": 58.0,
      "p": 64.0,
      "k": 165.0,
      "ph": 7.8,
      "oc": 0.52,
      "texture": "Saurashtra Medium Black Calcareous Loam"
    },
    {
      "id": "sample_6_thanjavur",
      "title": "TN Cauvery Delta Testing #TN-7204",
      "state": "Tamil Nadu",
      "card_id": "#SHC-TN-7204",
      "date": "18 June 2026",
      "n": 88.0,
      "p": 36.0,
      "k": 95.0,
      "ph": 6.7,
      "oc": 0.81,
      "texture": "Cauvery Deltaic Alluvial Silt Clay"
    },
    {
      "id": "sample_7_bardhaman",
      "title": "West Bengal Mati Tirtha Lab #WB-6112",
      "state": "West Bengal",
      "card_id": "#SHC-WB-6112",
      "date": "25 June 2026",
      "n": 95.0,
      "p": 32.0,
      "k": 88.0,
      "ph": 6.2,
      "oc": 0.78,
      "texture": "Lower Gangetic Old Alluvial Clay Loam"
    },
    {
      "id": "sample_8_jaipur",
      "title": "Rajasthan Semi-Arid Survey #RJ-2041",
      "state": "Rajasthan",
      "card_id": "#SHC-RJ-2041",
      "date": "10 May 2026",
      "n": 32.0,
      "p": 28.0,
      "k": 120.0,
      "ph": 8.2,
      "oc": 0.28,
      "texture": "Semi-Arid Desert Light Sandy Loam"
    },
    {
      "id": "sample_9_dharwad",
      "title": "Karnataka Raitha Mitra #KA-4418",
      "state": "Karnataka",
      "card_id": "#SHC-KA-4418",
      "date": "08 June 2026",
      "n": 75.0,
      "p": 46.0,
      "k": 115.0,
      "ph": 6.4,
      "oc": 0.69,
      "texture": "Western Ghats Red Laterite Loam"
    },
    {
      "id": "sample_10_varanasi",
      "title": "UP Krishi Bhawan Soil Hub #UP-9023",
      "state": "Uttar Pradesh",
      "card_id": "#SHC-UP-9023",
      "date": "22 May 2026",
      "n": 82.0,
      "p": 52.0,
      "k": 68.0,
      "ph": 7.1,
      "oc": 0.61,
      "texture": "Eastern Gangetic Silt Alluvial"
    },
    {
      "id": "sample_11_palakkad",
      "title": "Kerala Karshika Karma Sena #KL-1845",
      "state": "Kerala",
      "card_id": "#SHC-KL-1845",
      "date": "11 July 2026",
      "n": 68.0,
      "p": 24.0,
      "k": 75.0,
      "ph": 5.4,
      "oc": 1.15,
      "texture": "High-Rainfall Acidic Peaty Laterite"
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
