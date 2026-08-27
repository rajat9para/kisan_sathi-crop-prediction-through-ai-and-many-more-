import 'package:flutter/foundation.dart';
import '../models/crop_recommendation.dart';
import '../models/soil_data.dart';
import '../services/api_service.dart';
import '../services/offline_storage.dart';
import '../constants/demo_constants.dart';

class AdvisoryProvider extends ChangeNotifier {
  RecommendationResult? _recommendation;
  SoilData? _currentSoil;
  bool _isLoading = false;
  String _errorMessage = '';

  // Active farm configuration
  Map<String, dynamic> _selectedLocation = DemoConstants.demoLocations[0];
  double _farmSizeAcres = 2.5;
  String _irrigationSource = "Borewell";
  String? _previousCrop = "Cotton";
  
  // Custom / SHC soil overrides
  Map<String, dynamic>? _customSoilOverride;
  String? _scannedCardTitle;

  RecommendationResult? get recommendation => _recommendation;
  SoilData? get currentSoil => _currentSoil;
  bool get isLoading => _isLoading;
  String get errorMessage => _errorMessage;
  Map<String, dynamic> get selectedLocation => _selectedLocation;
  double get farmSizeAcres => _farmSizeAcres;
  String get irrigationSource => _irrigationSource;
  String? get previousCrop => _previousCrop;
  Map<String, dynamic>? get customSoilOverride => _customSoilOverride;
  String? get scannedCardTitle => _scannedCardTitle;

  AdvisoryProvider() {
    loadInitialData();
  }

  Future<void> loadInitialData() async {
    _isLoading = true;
    notifyListeners();

    try {
      _recommendation = await OfflineStorage.getCachedRecommendation();
      _currentSoil = await OfflineStorage.getCachedSoil();
      if (_recommendation == null) {
        await fetchRecommendations();
      }
    } catch (e) {
      _errorMessage = e.toString();
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  void setLocation(Map<String, dynamic> location) {
    _selectedLocation = location;
    _customSoilOverride = null;
    _scannedCardTitle = null;
    notifyListeners();
    fetchRecommendations();
  }

  void setFarmParameters({
    double? acres,
    String? irrigation,
    String? prevCrop,
  }) {
    if (acres != null) _farmSizeAcres = acres;
    if (irrigation != null) _irrigationSource = irrigation;
    if (prevCrop != null) _previousCrop = prevCrop;
    notifyListeners();
  }

  void setCustomSoil(Map<String, dynamic> soil, {String? cardTitle}) {
    _customSoilOverride = soil;
    _scannedCardTitle = cardTitle;
    notifyListeners();
    fetchRecommendations();
  }

  void clearCustomSoil() {
    _customSoilOverride = null;
    _scannedCardTitle = null;
    notifyListeners();
    fetchRecommendations();
  }

  Future<void> fetchRecommendations() async {
    _isLoading = true;
    _errorMessage = '';
    notifyListeners();

    try {
      final lat = (_selectedLocation['lat'] as num).toDouble();
      final lon = (_selectedLocation['lon'] as num).toDouble();
      final state = _selectedLocation['state'] ?? "Maharashtra";
      final district = _selectedLocation['district'] ?? "Nashik";

      _recommendation = await ApiService.getRecommendations(
        lat: lat,
        lon: lon,
        state: state,
        district: district,
        farmSizeAcres: _farmSizeAcres,
        irrigation: _irrigationSource,
        previousCrop: _previousCrop,
        customSoil: _customSoilOverride,
      );

      _currentSoil = await ApiService.getSoilData(lat, lon);
    } catch (e) {
      _errorMessage = e.toString();
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }
}
