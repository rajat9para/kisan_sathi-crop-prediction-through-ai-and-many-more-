import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/crop_recommendation.dart';
import '../models/soil_data.dart';
import '../models/weather_data.dart';
import '../models/market_price.dart';
import '../constants/demo_constants.dart';
import 'offline_storage.dart';
import 'sync_manager.dart';

class ApiService {
  static const String baseUrl = DemoConstants.backendBaseUrl;
  static const Duration timeoutDuration = Duration(seconds: 4);

  static Future<RecommendationResult> getRecommendations({
    required double lat,
    required double lon,
    String state = "Maharashtra",
    String district = "Nashik",
    double farmSizeAcres = 2.5,
    String irrigation = "Borewell",
    String? previousCrop,
    Map<String, dynamic>? customSoil,
    Map<String, dynamic>? customWeather,
  }) async {
    final syncMgr = SyncManager();

    // If in offline mode, return cached recommendation
    if (!syncMgr.isOnline) {
      final cached = await OfflineStorage.getCachedRecommendation();
      if (cached != null) return cached;
    }

    try {
      final body = {
        "latitude": lat,
        "longitude": lon,
        "state": state,
        "district": district,
        "farm_size_acres": farmSizeAcres,
        "irrigation_source": irrigation,
        "previous_crop": previousCrop,
        "custom_soil": customSoil,
        "custom_weather": customWeather,
      };

      final response = await http
          .post(
            Uri.parse('$baseUrl/api/recommend'),
            headers: {'Content-Type': 'application/json'},
            body: jsonEncode(body),
          )
          .timeout(timeoutDuration);

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        final result = RecommendationResult.fromJson(data);
        await OfflineStorage.saveRecommendation(result);
        return result;
      }
    } catch (e) {
      print('API Error in recommend: $e. Using offline cache.');
    }

    // Offline fallback
    final cached = await OfflineStorage.getCachedRecommendation();
    return cached ?? OfflineStorage.buildInitialDemoRecommendation();
  }

  static Future<SoilData> getSoilData(double lat, double lon) async {
    final syncMgr = SyncManager();
    if (!syncMgr.isOnline) {
      final cached = await OfflineStorage.getCachedSoil();
      if (cached != null) return cached;
    }

    try {
      final response = await http
          .get(Uri.parse('$baseUrl/api/soil?lat=$lat&lon=$lon'))
          .timeout(timeoutDuration);
      if (response.statusCode == 200) {
        final soil = SoilData.fromJson(jsonDecode(response.body));
        await OfflineStorage.saveSoil(soil);
        return soil;
      }
    } catch (e) {
      print('API Error in soil: $e');
    }

    final cached = await OfflineStorage.getCachedSoil();
    if (cached != null) return cached;

    return SoilData(
      latitude: lat,
      longitude: lon,
      source: "SoilGrids v2.0 (Offline Cache)",
      ph: 6.8,
      nitrogen: 85.0,
      phosphorus: 48.0,
      potassium: 190.0,
      organicCarbonPct: 0.72,
      clayContentPct: 42.0,
      sandContentPct: 24.0,
      soilType: "Black Cotton Loam",
    );
  }

  static Future<WeatherData> getWeatherData(double lat, double lon) async {
    final syncMgr = SyncManager();
    if (!syncMgr.isOnline) {
      final cached = await OfflineStorage.getCachedWeather();
      if (cached != null) return cached;
    }

    try {
      final response = await http
          .get(Uri.parse('$baseUrl/api/weather?lat=$lat&lon=$lon'))
          .timeout(timeoutDuration);
      if (response.statusCode == 200) {
        final weather = WeatherData.fromJson(jsonDecode(response.body));
        await OfflineStorage.saveWeather(weather);
        return weather;
      }
    } catch (e) {
      print('API Error in weather: $e');
    }

    final cached = await OfflineStorage.getCachedWeather();
    if (cached != null) return cached;

    return WeatherData(
      latitude: lat,
      longitude: lon,
      currentTempC: 26.5,
      currentHumidityPct: 74.0,
      currentCondition: "Partly Cloudy",
      windSpeedKmh: 12.0,
      rainfall7dTotalMm: 68.0,
      forecast7d: [
        WeatherDay(date: "2026-08-28", dayName: "Friday", tempMax: 28.5, tempMin: 21.0, humidityAvg: 78.0, precipitationProb: 35.0, weatherDesc: "Light Showers", sprayConditionRating: "Moderate - Spray after 4 PM"),
        WeatherDay(date: "2026-08-29", dayName: "Saturday", tempMax: 29.0, tempMin: 21.5, humidityAvg: 72.0, precipitationProb: 15.0, weatherDesc: "Clear", sprayConditionRating: "Good for Spraying"),
        WeatherDay(date: "2026-08-30", dayName: "Sunday", tempMax: 30.0, tempMin: 22.0, humidityAvg: 68.0, precipitationProb: 10.0, weatherDesc: "Sunny", sprayConditionRating: "Good for Spraying"),
      ],
      alerts: [
        {"type": "spray", "title_en": "Good Spraying Conditions", "title_hi": "छिड़काव के लिए उत्तम समय", "message_en": "Clear skies and moderate humidity today.", "message_hi": "आज आसमान साफ और नमी अनुकूल है।"}
      ],
    );
  }

  static Future<List<MarketPrice>> getMarketPrices(String state, String district, double lat, double lon) async {
    final syncMgr = SyncManager();
    if (!syncMgr.isOnline) {
      final cached = await OfflineStorage.getCachedMarket();
      if (cached.isNotEmpty) return cached;
    }

    try {
      final response = await http
          .get(Uri.parse('$baseUrl/api/market-prices?state=$state&district=$district&lat=$lat&lon=$lon'))
          .timeout(timeoutDuration);
      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        final list = (data['prices'] as List).map((e) => MarketPrice.fromJson(e)).toList();
        await OfflineStorage.saveMarket(list);
        return list;
      }
    } catch (e) {
      print('API Error in market: $e');
    }

    final cached = await OfflineStorage.getCachedMarket();
    if (cached.isNotEmpty) return cached;

    return [
      MarketPrice(commodity: "Grapes", commodityHi: "अंगूर", variety: "Thompson", marketName: "Nashik APMC", state: "Maharashtra", modalPriceRsQuintal: 6200.0, minPriceRsQuintal: 5400.0, maxPriceRsQuintal: 7100.0, trendPct7d: 5.4, trendDirection: "up", arrivalDate: "2026-08-27"),
      MarketPrice(commodity: "Pomegranate", commodityHi: "अनार", variety: "Bhagwa", marketName: "Nashik APMC", state: "Maharashtra", modalPriceRsQuintal: 8400.0, minPriceRsQuintal: 7200.0, maxPriceRsQuintal: 9600.0, trendPct7d: 3.8, trendDirection: "up", arrivalDate: "2026-08-27"),
      MarketPrice(commodity: "Cotton", commodityHi: "कपास", variety: "Medium", marketName: "Malegaon APMC", state: "Maharashtra", modalPriceRsQuintal: 7450.0, minPriceRsQuintal: 6900.0, maxPriceRsQuintal: 7800.0, trendPct7d: -1.2, trendDirection: "stable", arrivalDate: "2026-08-27"),
    ];
  }

  static Future<Map<String, dynamic>> sendVoiceQuery(String text, {String lang = "hi"}) async {
    final syncMgr = SyncManager();
    if (syncMgr.isOnline) {
      try {
        final response = await http
            .post(
              Uri.parse('$baseUrl/api/voice/query'),
              headers: {'Content-Type': 'application/json'},
              body: jsonEncode({"query_text": text, "language": lang}),
            )
            .timeout(timeoutDuration);
        if (response.statusCode == 200) {
          return jsonDecode(response.body);
        }
      } catch (e) {
        print('Voice query network error: $e');
      }
    }

    // On-device / Offline NLP Intent Response
    final q = text.toLowerCase();
    if (q.contains("पानी") || q.contains("water") || q.contains("सिंचाई")) {
      return {
        "query": text,
        "detected_intent": "water",
        "response_text_hi": "सोयाबीन व मक्का के लिए 3 से 4 सिंचाई की आवश्यकता होती है। फूल आने और फल बनते समय खेत में नमी अवश्य रखें।",
        "response_text_en": "Crops like Soybean require 3 to 4 irrigations. Maintain soil moisture during flowering and pod development.",
        "tts_audio_text": "सोयाबीन और मक्का के लिए तीन से चार सिंचाई की आवश्यकता होती है। फूल आने के समय खेत में नमी अवश्य रखें।",
        "suggested_followups": ["खाद की मात्रा?", "मंडी भाव क्या है?"]
      };
    } else if (q.contains("खाद") || q.contains("fertilizer") || q.contains("यूरिया")) {
      return {
        "query": text,
        "detected_intent": "fertilizer",
        "response_text_hi": "बुवाई के समय प्रति एकड़ 50 किलो डीएपी और 25 किलो पोटाश डालें। 25 दिन बाद 35 किलो नीम कोटेड यूरिया छिड़कें।",
        "response_text_en": "Apply 50 kg DAP and 25 kg MOP at sowing. Top dress with 35 kg Neem Coated Urea after 25 days.",
        "tts_audio_text": "बुवाई के समय पचास किलो डीएपी डालें। पच्चीस दिन बाद पैंतीस किलो यूरिया का छिड़काव करें।",
        "suggested_followups": ["सिंचाई कब करनी है?", "कीट नियंत्रण कैसे करें?"]
      };
    } else if (q.contains("मंडी") || q.contains("भाव") || q.contains("price") || q.contains("रेट")) {
      return {
        "query": text,
        "detected_intent": "mandi",
        "response_text_hi": "आज मंडी में अंगूर ₹6,200/क्विंटल और अनार ₹8,400/क्विंटल बिक रहा है। भाव में 3 से 5% की तेजी है।",
        "response_text_en": "Today in APMC Mandi, Grapes are at ₹6,200/Qtl and Pomegranate at ₹8,400/Qtl with an upward trend.",
        "tts_audio_text": "आज मंडी में अंगूर बासठ सौ रुपये और अनार चौरासी सौ रुपये प्रति क्विंटल के भाव पर है।",
        "suggested_followups": ["आने वाले हफ्तों का भाव?", "फसल भंडारण सलाह"]
      };
    } else {
      return {
        "query": text,
        "detected_intent": "general",
        "response_text_hi": "एग्रीसाथी आपके खेत के लिए सर्वश्रेष्ठ फसल व कृषि सलाह प्रदान करता है। आप खाद, पानी, मौसम या मंडी भाव के बारे में पूछ सकते हैं।",
        "response_text_en": "AgriSaathi provides AI crop advisory. You can ask about irrigation, fertilizer dosage, weather, or mandi prices.",
        "tts_audio_text": "नमस्ते किसान भाई। आप खाद, पानी, मौसम या मंडी भाव से जुड़ा कोई भी प्रश्न पूछ सकते हैं।",
        "suggested_followups": ["पानी कितना चाहिए?", "खाद की मात्रा?", "मंडी भाव?"]
      };
    }
  }

  static Future<Map<String, dynamic>> parseSoilCardPreset(String preset) async {
    try {
      final response = await http
          .post(
            Uri.parse('$baseUrl/api/ocr/soil-card'),
            headers: {'Content-Type': 'application/json'},
            body: jsonEncode({"sample_preset": preset}),
          )
          .timeout(timeoutDuration);
      if (response.statusCode == 200) {
        return jsonDecode(response.body);
      }
    } catch (_) {}

    // Offline fallback for Soil Health Card
    return {
      "detected_scheme": "Soil Health Card Scheme (MahaSoil)",
      "farmer_name": "Ramesh Kisan Patil",
      "lab_id": "Nashik District Agri Lab #MH-4012",
      "sample_date": "2026-05-18",
      "parameters": {
        "nitrogen": 85.0,
        "phosphorus": 48.0,
        "potassium": 190.0,
        "ph": 6.8,
        "organic_carbon_pct": 0.72,
        "texture": "Medium Black Clay Loam"
      },
      "health_status": {
        "nitrogen": "Medium",
        "phosphorus": "Medium",
        "potassium": "High",
        "ph": "Neutral (Ideal)"
      }
    };
  }
}
