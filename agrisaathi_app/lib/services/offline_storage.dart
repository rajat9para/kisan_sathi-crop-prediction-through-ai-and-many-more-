import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/crop_recommendation.dart';
import '../models/soil_data.dart';
import '../models/weather_data.dart';
import '../models/market_price.dart';
import '../models/disease_result.dart';

class OfflineStorage {
  static const String keyLastRecommendation = 'agri_last_recommendation';
  static const String keyLastSoil = 'agri_last_soil';
  static const String keyLastWeather = 'agri_last_weather';
  static const String keyLastMarket = 'agri_last_market';
  static const String keyLastSyncTime = 'agri_last_sync_time';
  static const String keySimulatedOffline = 'agri_simulated_offline';
  static const String keyDiseaseHistory = 'agri_disease_history';

  static Future<void> saveRecommendation(RecommendationResult result) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(keyLastRecommendation, jsonEncode(result.toJson()));
    await prefs.setString(keyLastSyncTime, DateTime.now().toIso8601String());
  }

  static Future<RecommendationResult?> getCachedRecommendation() async {
    final prefs = await SharedPreferences.getInstance();
    final dataStr = prefs.getString(keyLastRecommendation);
    if (dataStr != null) {
      try {
        return RecommendationResult.fromJson(jsonDecode(dataStr));
      } catch (e) {
        print('Error decoding cached recommendation: $e');
      }
    }
    // Return pre-cached Nashik fallback if nothing stored yet
    return buildInitialDemoRecommendation();
  }

  static Future<void> saveSoil(SoilData soil) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(keyLastSoil, jsonEncode(soil.toJson()));
  }

  static Future<SoilData?> getCachedSoil() async {
    final prefs = await SharedPreferences.getInstance();
    final dataStr = prefs.getString(keyLastSoil);
    if (dataStr != null) {
      try {
        return SoilData.fromJson(jsonDecode(dataStr));
      } catch (e) {
        print('Error decoding cached soil: $e');
      }
    }
    return null;
  }

  static Future<void> saveWeather(WeatherData weather) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(keyLastWeather, jsonEncode(weather.toJson()));
  }

  static Future<WeatherData?> getCachedWeather() async {
    final prefs = await SharedPreferences.getInstance();
    final dataStr = prefs.getString(keyLastWeather);
    if (dataStr != null) {
      try {
        return WeatherData.fromJson(jsonDecode(dataStr));
      } catch (e) {
        print('Error decoding cached weather: $e');
      }
    }
    return null;
  }

  static Future<void> saveMarket(List<MarketPrice> prices) async {
    final prefs = await SharedPreferences.getInstance();
    final listJson = prices.map((p) => p.toJson()).toList();
    await prefs.setString(keyLastMarket, jsonEncode(listJson));
  }

  static Future<List<MarketPrice>> getCachedMarket() async {
    final prefs = await SharedPreferences.getInstance();
    final dataStr = prefs.getString(keyLastMarket);
    if (dataStr != null) {
      try {
        final list = jsonDecode(dataStr) as List;
        return list.map((e) => MarketPrice.fromJson(e)).toList();
      } catch (e) {
        print('Error decoding cached market: $e');
      }
    }
    return [];
  }

  static Future<String> getLastSyncTimeString() async {
    final prefs = await SharedPreferences.getInstance();
    final timeStr = prefs.getString(keyLastSyncTime);
    if (timeStr != null) {
      try {
        final dt = DateTime.parse(timeStr);
        return "${dt.day.toString().padLeft(2, '0')}/${dt.month.toString().padLeft(2, '0')} ${dt.hour.toString().padLeft(2, '0')}:${dt.minute.toString().padLeft(2, '0')}";
      } catch (_) {}
    }
    return "Today 12:45 PM (Cached)";
  }

  static Future<void> setSimulatedOffline(bool isOffline) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(keySimulatedOffline, isOffline);
  }

  static Future<bool> isSimulatedOffline() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getBool(keySimulatedOffline) ?? false;
  }

  static Future<void> saveDiseaseDiagnosis(DiseaseDiagnosis diag) async {
    final prefs = await SharedPreferences.getInstance();
    List<String> history = prefs.getStringList(keyDiseaseHistory) ?? [];
    history.insert(0, jsonEncode(diag.toJson()));
    if (history.length > 20) history = history.sublist(0, 20);
    await prefs.setStringList(keyDiseaseHistory, history);
  }

  static Future<List<DiseaseDiagnosis>> getDiseaseHistory() async {
    final prefs = await SharedPreferences.getInstance();
    List<String> history = prefs.getStringList(keyDiseaseHistory) ?? [];
    return history.map((e) => DiseaseDiagnosis.fromJson(jsonDecode(e))).toList();
  }

  static RecommendationResult buildInitialDemoRecommendation() {
    return RecommendationResult(
      timestamp: "2026-08-27 12:45:00",
      isCachedDemoLocation: true,
      location: {
        "latitude": 19.9975,
        "longitude": 73.7898,
        "state": "Maharashtra",
        "district": "Nashik",
        "farm_size_acres": 2.5,
        "irrigation_source": "Borewell"
      },
      soilSnapshot: {
        "ph": 6.8,
        "nitrogen": 85.0,
        "phosphorus": 48.0,
        "potassium": 190.0,
        "soil_type": "Black Cotton Loam",
        "source": "SoilGrids v2.0 Cached"
      },
      weatherSnapshot: {
        "current_temp_c": 26.5,
        "current_humidity_pct": 74.0,
        "rainfall_7d_total_mm": 68.0,
        "current_condition": "Partly Cloudy"
      },
      topRecommendations: [
        CropItem(
          rank: 1,
          cropName: "Grapes",
          cropNameHi: "अंगूर",
          scientificName: "Vitis vinifera",
          matchScorePct: 94.8,
          baseMlConfidencePct: 96.2,
          soilFitPct: 96.0,
          weatherFitPct: 92.5,
          marketProfitabilityPct: 94.0,
          rotationImpactPct: 85.0,
          expectedYield: "8 - 12 Tonnes",
          estimatedRevenue: "₹3,50,000 - ₹5,00,000",
          mandiPrice: "₹6,200 / Quintal",
          priceTrend: "up",
          waterRequirement: "Medium",
          sowingWindowEn: "October - November (Pruning)",
          sowingWindowHi: "अक्टूबर - नवंबर (छंटाई)",
          harvestDurationDays: 135,
          whyThisCropEn: "Grapes is ranked #1 with 94.8% suitability. High soil Potassium (190 kg/ha) and moderate climate in Nashik provide ideal sugar accumulation.",
          whyThisCropHi: "अंगूर को 94.8% मैच के साथ #1 रैंक प्राप्त है। मिट्टी में पोटाश की प्रचुरता (190 kg/ha) और नासिक की जलवायु मिठास व फल विकास के लिए उत्तम है।",
          shapContributions: [
            ShapFeature(feature: "K", featureNameHi: "पोटाश", impactScore: 0.28, explanationEn: "High soil Potash (190) strongly boosts berry size and sweetness.", explanationHi: "पोटाश की अधिक मात्रा अंगूर के आकार और मिठास को बढ़ाती है।", status: "positive"),
            ShapFeature(feature: "ph", featureNameHi: "पीएच मान", impactScore: 0.18, explanationEn: "Neutral pH 6.8 is ideal for grapevine root health.", explanationHi: "पीएच 6.8 जड़ों के विकास के लिए पूर्णतः अनुकूल है।", status: "positive"),
            ShapFeature(feature: "temperature", featureNameHi: "तापमान", impactScore: 0.12, explanationEn: "Moderate 26.5°C ensures stress-free vegetative growth.", explanationHi: "26.5°C का तापमान फसल वृद्धि के लिए अनुकूल है।", status: "positive"),
            ShapFeature(feature: "rainfall", featureNameHi: "मौसमी वर्षा", impactScore: 0.09, explanationEn: "68mm rainfall is manageable with regulated drip irrigation.", explanationHi: "68 मिमी वर्षा ड्रिप सिंचाई के साथ उपयुक्त है।", status: "positive"),
            ShapFeature(feature: "N", featureNameHi: "नाइट्रोजन", impactScore: 0.06, explanationEn: "Balanced nitrogen supports cane vigor.", explanationHi: "संतुलित नाइट्रोजन तनों को मजबूत बनाता है।", status: "positive"),
            ShapFeature(feature: "P", featureNameHi: "फास्फोरस", impactScore: 0.05, explanationEn: "Adequate phosphorus aids root establishment.", explanationHi: "फास्फोरस जड़ों की मजबूती में सहायक है।", status: "positive"),
            ShapFeature(feature: "humidity", featureNameHi: "हवा में नमी", impactScore: -0.04, explanationEn: "High humidity requires watchful downy mildew prevention.", explanationHi: "नमी अधिक होने पर फफूंद से बचाव का ध्यान रखें।", status: "negative"),
          ],
          fertilizerSchedule: [
            {"stage": "Basal / Pruning (छंटाई के समय)", "dosage": "Compost 10T + SSP 200kg + MOP 150kg/acre", "purpose": "Bud break & shoot initiation"},
            {"stage": "Berry Setting (फल बनने पर)", "dosage": "0:52:34 (MKP) via fertigation @ 4kg/acre", "purpose": "Berry elongation & cluster density"},
            {"stage": "Color Break / Veraison", "dosage": "0:0:50 (Potassium Sulphate) @ 5kg/acre", "purpose": "Sugar accumulation & uniform coloring"}
          ],
          irrigationSchedule: [
            {"stage": "Post-Pruning Stage", "timing": "Every 3 days (Drip)", "note": "Maintain 60% field capacity"},
            {"stage": "Flowering Stage", "timing": "Light irrigation", "note": "Avoid over-watering to prevent flower drop"},
            {"stage": "Berry Development", "timing": "Every 2 days (Drip)", "note": "Consistent moisture to prevent berry cracking"}
          ]
        ),
        CropItem(
          rank: 2,
          cropName: "Pomegranate",
          cropNameHi: "अनार (भगवा)",
          scientificName: "Punica granatum",
          matchScorePct: 91.2,
          baseMlConfidencePct: 89.4,
          soilFitPct: 94.0,
          weatherFitPct: 88.0,
          marketProfitabilityPct: 94.0,
          rotationImpactPct: 85.0,
          expectedYield: "4 - 6 Tonnes",
          estimatedRevenue: "₹2,80,000 - ₹4,20,000",
          mandiPrice: "₹8,400 / Quintal",
          priceTrend: "up",
          waterRequirement: "Low",
          sowingWindowEn: "June - July (Mrig Bahar)",
          sowingWindowHi: "जून - जुलाई (मृग बहार)",
          harvestDurationDays: 180,
          whyThisCropEn: "Bhagwa Pomegranate offers exceptional market returns (₹8,400/Qtl) with drought tolerance.",
          whyThisCropHi: "भगवा अनार सूखे के प्रति सहनशील है और मंडी में उच्चतम मुनाफा (₹8,400/क्विंटल) देता है।",
          shapContributions: [
            ShapFeature(feature: "ph", featureNameHi: "पीएच मान", impactScore: 0.22, explanationEn: "Soil pH 6.8 promotes deep rooting.", explanationHi: "पीएच 6.8 गहरी जड़ों के लिए आदर्श है।", status: "positive"),
            ShapFeature(feature: "K", featureNameHi: "पोटाश", impactScore: 0.19, explanationEn: "Enhances aril redness and fruit weight.", explanationHi: "दाने का लाल रंग और वजन बढ़ाता है।", status: "positive")
          ],
          fertilizerSchedule: [
            {"stage": "Bahar Treatment", "dosage": "FYM 20kg + Single Super Phosphate 500g/plant", "purpose": "Flower induction"},
            {"stage": "Fruit Growth", "dosage": "19:19:19 + Micronutrients @ 3g/L spray", "purpose": "Skin gloss and crack resistance"}
          ],
          irrigationSchedule: [
            {"stage": "Rest Period (तनाव काल)", "timing": "Stop water for 30 days", "note": "Induces heavy flowering"},
            {"stage": "Fruit Development", "timing": "Regular drip @ 20-25L/tree/day", "note": "Prevents fruit bursting"}
          ]
        ),
        CropItem(
          rank: 3,
          cropName: "Cotton",
          cropNameHi: "कपास",
          scientificName: "Gossypium hirsutum",
          matchScorePct: 86.4,
          baseMlConfidencePct: 82.0,
          soilFitPct: 91.0,
          weatherFitPct: 84.0,
          marketProfitabilityPct: 85.0,
          rotationImpactPct: 85.0,
          expectedYield: "10 - 14 Quintals",
          estimatedRevenue: "₹75,000 - ₹1,05,000",
          mandiPrice: "₹7,450 / Quintal",
          priceTrend: "stable",
          waterRequirement: "Medium",
          sowingWindowEn: "May - June (Kharif)",
          sowingWindowHi: "मई - जून (खरीफ)",
          harvestDurationDays: 160,
          whyThisCropEn: "Black cotton soil provides strong moisture retention for staple fiber elongation.",
          whyThisCropHi: "काली मिट्टी कपास की गहरी जड़ों और रेशे की गुणवत्ता के लिए उत्तम नमी धारण करती है।",
          shapContributions: [
            ShapFeature(feature: "N", featureNameHi: "नाइट्रोजन", impactScore: 0.16, explanationEn: "Supports vegetative branching and boll formation.", explanationHi: "शाखाओं और टिंडे के विकास में सहायक।", status: "positive")
          ],
          fertilizerSchedule: [
            {"stage": "Basal", "dosage": "DAP 50kg + MOP 25kg/acre", "purpose": "Early root vigor"},
            {"stage": "Squaring Stage", "dosage": "Urea top dress 30kg/acre", "purpose": "Boll retention"}
          ],
          irrigationSchedule: [
            {"stage": "Vegetative & Flowering", "timing": "Every 10-12 days (if rain absent)", "note": "Crucial during boll opening"}
          ]
        )
      ],
      advisoryWarnings: [
        {
          "title_en": "Optimal Spraying Window Today",
          "title_hi": "आज छिड़काव के लिए उत्तम समय",
          "desc_en": "Mild wind and clear sky. Safe for foliar bio-fertilizer spray.",
          "desc_hi": "हल्की हवा और साफ मौसम। जैविक पर्ण उर्वरक छिड़काव के लिए सुरक्षित।"
        }
      ]
    );
  }
}
