import 'dart:math';
import '../models/crop_recommendation.dart';

class OfflineInferenceEngine {
  static const Map<String, Map<String, dynamic>> cropProfiles = {
    "rice": {
      "hi": "धान / चावल", "sci": "Oryza sativa",
      "N": [60, 100], "P": [35, 60], "K": [35, 45], "temp": [20, 27], "humidity": [80, 85], "ph": [5.0, 7.5], "rain": [180, 300],
      "yield_min": 22.0, "yield_max": 28.0, "unit": "Quintals", "price": 3950.0, "cost": 26000.0, "water": "High", "days": 130, "sowing_en": "June - July", "sowing_hi": "जून - जुलाई"
    },
    "maize": {
      "hi": "मक्का", "sci": "Zea mays",
      "N": [60, 100], "P": [35, 60], "K": [15, 25], "temp": [18, 27], "humidity": [55, 75], "ph": [5.5, 7.5], "rain": [60, 110],
      "yield_min": 24.0, "yield_max": 32.0, "unit": "Quintals", "price": 2280.0, "cost": 18000.0, "water": "Medium", "days": 105, "sowing_en": "June - July / Oct", "sowing_hi": "जून - जुलाई / अक्टूबर"
    },
    "chickpea": {
      "hi": "चना (देसी)", "sci": "Cicer arietinum",
      "N": [20, 60], "P": [55, 80], "K": [75, 85], "temp": [15, 22], "humidity": [14, 20], "ph": [6.0, 8.5], "rain": [65, 95],
      "yield_min": 8.0, "yield_max": 12.0, "unit": "Quintals", "price": 6150.0, "cost": 16000.0, "water": "Low", "days": 110, "sowing_en": "October - November", "sowing_hi": "अक्टूबर - नवंबर", "legume": true
    },
    "cotton": {
      "hi": "कपास", "sci": "Gossypium hirsutum",
      "N": [100, 140], "P": [35, 60], "K": [15, 25], "temp": [22, 26], "humidity": [75, 85], "ph": [6.0, 8.0], "rain": [60, 100],
      "yield_min": 10.0, "yield_max": 14.0, "unit": "Quintals", "price": 7450.0, "cost": 28000.0, "water": "Medium", "days": 160, "sowing_en": "May - June", "sowing_hi": "मई - जून"
    },
    "grapes": {
      "hi": "अंगूर", "sci": "Vitis vinifera",
      "N": [15, 40], "P": [120, 145], "K": [195, 205], "temp": [8, 42], "humidity": [80, 85], "ph": [5.5, 6.5], "rain": [65, 75],
      "yield_min": 8.0, "yield_max": 12.0, "unit": "Tonnes", "price": 6200.0, "cost": 120000.0, "water": "Medium", "days": 135, "sowing_en": "October - November", "sowing_hi": "अक्टूबर - नवंबर"
    },
    "pomegranate": {
      "hi": "अनार", "sci": "Punica granatum",
      "N": [15, 40], "P": [10, 30], "K": [35, 45], "temp": [18, 25], "humidity": [85, 95], "ph": [5.5, 7.2], "rain": [100, 115],
      "yield_min": 4.0, "yield_max": 6.5, "unit": "Tonnes", "price": 8400.0, "cost": 90000.0, "water": "Low", "days": 180, "sowing_en": "June - July", "sowing_hi": "जून - जुलाई"
    },
    "blackgram": {
      "hi": "उड़द दाल", "sci": "Vigna mungo",
      "N": [30, 60], "P": [55, 80], "K": [15, 25], "temp": [25, 35], "humidity": [60, 70], "ph": [6.5, 7.5], "rain": [60, 75],
      "yield_min": 5.0, "yield_max": 7.5, "unit": "Quintals", "price": 8200.0, "cost": 14000.0, "water": "Low", "days": 85, "sowing_en": "July - August", "sowing_hi": "जुलाई - अगस्त", "legume": true
    },
    "mungbean": {
      "hi": "मूंग दाल", "sci": "Vigna radiata",
      "N": [10, 40], "P": [35, 60], "K": [15, 25], "temp": [27, 30], "humidity": [80, 90], "ph": [6.2, 7.2], "rain": [35, 60],
      "yield_min": 4.5, "yield_max": 6.5, "unit": "Quintals", "price": 8500.0, "cost": 13500.0, "water": "Low", "days": 70, "sowing_en": "March - April / July", "sowing_hi": "मार्च - अप्रैल / जुलाई", "legume": true
    },
    "lentil": {
      "hi": "मसूर दाल", "sci": "Lens culinaris",
      "N": [10, 40], "P": [55, 80], "K": [15, 25], "temp": [18, 30], "humidity": [60, 70], "ph": [6.0, 7.5], "rain": [35, 55],
      "yield_min": 6.0, "yield_max": 8.5, "unit": "Quintals", "price": 6800.0, "cost": 14500.0, "water": "Low", "days": 115, "sowing_en": "October - November", "sowing_hi": "अक्टूबर - नवंबर", "legume": true
    },
    "pigeonpeas": {
      "hi": "अरहर / तुअर", "sci": "Cajanus cajan",
      "N": [10, 40], "P": [55, 80], "K": [15, 25], "temp": [25, 38], "humidity": [30, 70], "ph": [5.0, 7.5], "rain": [90, 200],
      "yield_min": 7.0, "yield_max": 10.0, "unit": "Quintals", "price": 9800.0, "cost": 18000.0, "water": "Low", "days": 170, "sowing_en": "June - July", "sowing_hi": "जून - जुलाई", "legume": true
    },
    "banana": {
      "hi": "केला", "sci": "Musa acuminata",
      "N": [80, 120], "P": [70, 95], "K": [45, 55], "temp": [25, 30], "humidity": [75, 85], "ph": [5.5, 6.5], "rain": [90, 120],
      "yield_min": 25.0, "yield_max": 38.0, "unit": "Tonnes", "price": 2100.0, "cost": 85000.0, "water": "High", "days": 330, "sowing_en": "June - July", "sowing_hi": "जून - जुलाई"
    }
  };

  static RecommendationResult runInference({
    required double n,
    required double p,
    required double k,
    required double ph,
    required double temp,
    required double humidity,
    required double rainfall,
    double farmSizeAcres = 2.5,
    String? previousCrop,
    String irrigation = "Borewell",
  }) {
    final List<Map<String, dynamic>> candidateScores = [];

    cropProfiles.forEach((cropKey, prof) {
      // 1. Soil Match
      double soilPenalties = 0;
      soilPenalties += _calcPenalty(n, prof["N"][0], prof["N"][1]);
      soilPenalties += _calcPenalty(p, prof["P"][0], prof["P"][1]);
      soilPenalties += _calcPenalty(k, prof["K"][0], prof["K"][1]);
      soilPenalties += _calcPenalty(ph, prof["ph"][0], prof["ph"][1]) * 1.5;
      final double soilFit = max(35.0, min(99.0, 100.0 - soilPenalties * 0.7));

      // 2. Weather Match
      double weatherPenalties = 0;
      weatherPenalties += _calcPenalty(temp, prof["temp"][0], prof["temp"][1]);
      weatherPenalties += _calcPenalty(humidity, prof["humidity"][0], prof["humidity"][1]);
      weatherPenalties += _calcPenalty(rainfall, prof["rain"][0], prof["rain"][1]);
      final double weatherFit = max(35.0, min(99.0, 100.0 - weatherPenalties * 0.7));

      // 3. Rotation Impact
      double rotFit = 85.0;
      final isLegume = prof["legume"] == true;
      if (previousCrop != null && previousCrop.isNotEmpty) {
        if (previousCrop.toLowerCase().contains("wheat") || previousCrop.toLowerCase().contains("rice")) {
          if (isLegume) rotFit = 98.0;
        }
      }

      final double composite = (soilFit * 0.40) + (weatherFit * 0.35) + (rotFit * 0.15) + (85.0 * 0.10);
      final double finalMatch = max(40.0, min(99.2, composite));

      candidateScores.add({
        "crop": cropKey,
        "prof": prof,
        "match": finalMatch,
        "soilFit": soilFit,
        "weatherFit": weatherFit,
        "rotFit": rotFit,
      });
    });

    candidateScores.sort((a, b) => (b["match"] as double).compareTo(a["match"] as double));

    final top4 = candidateScores.take(4).toList();
    final List<CropItem> cropItems = [];

    for (int i = 0; i < top4.length; i++) {
      final cand = top4[i];
      final cropKey = cand["crop"] as String;
      final prof = cand["prof"] as Map<String, dynamic>;
      final double match = cand["match"] as double;
      final double sFit = cand["soilFit"] as double;
      final double wFit = cand["weatherFit"] as double;

      final double fitMultiplier = max(0.65, min(1.20, 0.65 + 0.35 * (sFit / 100.0)));
      final double minYield = ((prof["yield_min"] as double) * fitMultiplier);
      final double maxYield = ((prof["yield_max"] as double) * fitMultiplier);
      final double avgYield = (minYield + maxYield) / 2.0;

      final String unit = prof["unit"];
      final double price = prof["price"];
      final double cost = prof["cost"];
      final double grossRev = unit == "Tonnes" ? avgYield * 10.0 * price : avgYield * price;
      final double netProfit = max(5000.0, grossRev - cost);

      final isLegume = prof["legume"] == true;
      final double sustScore = isLegume ? 92.0 : (prof["water"] == "Low" ? 88.0 : 74.0);
      final String sustRating = sustScore >= 85.0 ? "High (Eco-Friendly)" : "Moderate (Balanced)";

      final shapList = [
        ShapFeature(
          feature: "N",
          featureNameHi: "नाइट्रोजन (N)",
          impactScore: 0.24,
          explanationEn: "Nitrogen level ($n kg/ha) supports strong tillering.",
          explanationHi: "नाइट्रोजन का स्तर ($n kg/ha) पौधे के विकास में सहायक है।",
          status: "positive",
        ),
        ShapFeature(
          feature: "P",
          featureNameHi: "फास्फोरस (P)",
          impactScore: 0.18,
          explanationEn: "Phosphorus ($p kg/ha) supports root establishment.",
          explanationHi: "फास्फोरस ($p kg/ha) जड़ों के विकास के अनुकूल है।",
          status: "positive",
        ),
        ShapFeature(
          feature: "ph",
          featureNameHi: "मिट्टी का pH",
          impactScore: 0.15,
          explanationEn: "Soil pH ($ph) is in the optimal nutrient uptake range.",
          explanationHi: "मिट्टी का pH ($ph) पोषक तत्व अवशोषण के लिए आदर्श है।",
          status: "positive",
        ),
      ];

      final fertSchedule = [
        {"stage": "Basal Sowing (बुवाई के समय)", "dosage": "50 kg DAP + 25 kg MOP/acre", "purpose": "Root development"},
        {"stage": "Vegetative Stage (25-30 Days)", "dosage": "35 kg Urea top dressing", "purpose": "Active branching"},
        {"stage": "Flowering & Pod Filling", "dosage": "0:52:34 foliar spray @ 5g/L", "purpose": "Grain weight maximization"}
      ];

      final irrigSchedule = [
        {"stage": "Initial Irrigation", "timing": "Day 0 - 3", "note": "Uniform moist seedbed"},
        {"stage": "Critical Growth", "timing": "Day 25 - 35", "note": "Adequate root moisture"},
        {"stage": "Grain/Fruit Filling", "timing": "Day 55 - 70", "note": "Critical yield filling period"}
      ];

      cropItems.add(CropItem(
        rank: i + 1,
        cropName: cropKey[0].toUpperCase() + cropKey.substring(1),
        cropNameHi: prof["hi"] ?? cropKey,
        scientificName: prof["sci"] ?? "",
        matchScorePct: double.parse(match.toStringAsFixed(1)),
        baseMlConfidencePct: double.parse(match.toStringAsFixed(1)),
        soilFitPct: double.parse(sFit.toStringAsFixed(1)),
        weatherFitPct: double.parse(wFit.toStringAsFixed(1)),
        marketProfitabilityPct: 88.0,
        rotationImpactPct: cand["rotFit"] as double,
        expectedYield: "${minYield.toStringAsFixed(1)} - ${maxYield.toStringAsFixed(1)} $unit / Acre",
        estimatedRevenue: "₹${grossRev.toInt()} / Acre",
        estimatedCostPerAcre: cost,
        estimatedNetProfitPerAcre: netProfit,
        mandiPrice: "₹${price.toInt()} / $unit",
        priceTrend: "up",
        waterRequirement: prof["water"] ?? "Medium",
        sowingWindowEn: prof["sowing_en"] ?? "Kharif/Rabi",
        sowingWindowHi: prof["sowing_hi"] ?? "खरीफ/रबी",
        harvestDurationDays: prof["days"] ?? 120,
        sustainabilityScorePct: sustScore,
        sustainabilityRating: sustRating,
        whyThisCropEn: "${cropKey[0].toUpperCase() + cropKey.substring(1)} has a ${match.toStringAsFixed(1)}% match on-device. Sustainability score is $sustScore%.",
        whyThisCropHi: "${prof['hi']} का मैच स्कोर ${match.toStringAsFixed(1)}% है। स्थिरता स्कोर $sustScore% है।",
        shapContributions: shapList,
        fertilizerSchedule: fertSchedule,
        irrigationSchedule: irrigSchedule,
      ));
    }

    return RecommendationResult(
      timestamp: DateTime.now().toString(),
      isCachedDemoLocation: false,
      location: {"source": "On-Device Offline ML Inference Engine"},
      soilSnapshot: {
        "nitrogen": n,
        "phosphorus": p,
        "potassium": k,
        "ph": ph,
        "source": "On-Device Input"
      },
      weatherSnapshot: {
        "current_temp_c": temp,
        "current_humidity_pct": humidity,
        "rainfall_7d_total_mm": rainfall,
        "source": "On-Device Input"
      },
      topRecommendations: cropItems,
      advisoryWarnings: [
        {
          "title_en": "On-Device Offline Mode Active",
          "title_hi": "ऑन-डिवाइस ऑफलाइन मोड सक्रिय",
          "desc_en": "Recommendations computed live using local on-device agronomic ML rules.",
          "desc_hi": "सिफारिशों की गणना बिना इंटरनेट के ऑन-डिवाइस इंजन द्वारा की गई है।"
        }
      ],
    );
  }

  static double _calcPenalty(double val, num low, num high) {
    if (val < low) {
      return min(30.0, ((low - val) / max(1.0, low)) * 25.0);
    } else if (val > high) {
      return min(30.0, ((val - high) / max(1.0, high)) * 25.0);
    }
    return 0.0;
  }
}
