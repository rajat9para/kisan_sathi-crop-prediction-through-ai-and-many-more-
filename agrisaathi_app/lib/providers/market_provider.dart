import 'package:flutter/foundation.dart';
import '../models/market_price.dart';
import '../services/api_service.dart';
import '../services/offline_storage.dart';

class MarketProvider extends ChangeNotifier {
  List<MarketPrice> _prices = [];
  bool _isLoading = false;
  String _selectedState = "Maharashtra";

  List<MarketPrice> get prices => _prices;
  bool get isLoading => _isLoading;
  String get selectedState => _selectedState;

  MarketProvider() {
    fetchPrices("Maharashtra", "Nashik", 19.9975, 73.7898);
  }

  Future<void> fetchPrices(String state, String district, double lat, double lon) async {
    _isLoading = true;
    _selectedState = state;
    notifyListeners();

    try {
      _prices = await ApiService.getMarketPrices(state, district, lat, lon);
    } catch (e) {
      _prices = await OfflineStorage.getCachedMarket();
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }
}
