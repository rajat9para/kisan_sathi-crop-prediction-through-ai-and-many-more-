import 'package:flutter/foundation.dart';
import '../models/weather_data.dart';
import '../services/api_service.dart';
import '../services/offline_storage.dart';

class WeatherProvider extends ChangeNotifier {
  WeatherData? _weather;
  bool _isLoading = false;

  WeatherData? get weather => _weather;
  bool get isLoading => _isLoading;

  WeatherProvider() {
    fetchWeather(19.9975, 73.7898);
  }

  Future<void> fetchWeather(double lat, double lon) async {
    _isLoading = true;
    notifyListeners();

    try {
      _weather = await ApiService.getWeatherData(lat, lon);
    } catch (e) {
      _weather = await OfflineStorage.getCachedWeather();
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }
}
