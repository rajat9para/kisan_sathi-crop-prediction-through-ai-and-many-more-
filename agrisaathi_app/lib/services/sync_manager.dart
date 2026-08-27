import 'dart:async';
import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import 'offline_storage.dart';
import '../constants/demo_constants.dart';

class SyncManager extends ChangeNotifier {
  static final SyncManager _instance = SyncManager._internal();
  factory SyncManager() => _instance;
  SyncManager._internal() {
    _init();
  }

  bool _isOnline = true;
  bool _isSimulatedAirplaneMode = false;
  bool _isSyncing = false;
  String _lastSyncTimestamp = "Just now";
  Timer? _healthCheckTimer;

  bool get isOnline => _isOnline && !_isSimulatedAirplaneMode;
  bool get isSimulatedAirplaneMode => _isSimulatedAirplaneMode;
  bool get isSyncing => _isSyncing;
  String get lastSyncTimestamp => _lastSyncTimestamp;

  Future<void> _init() async {
    _isSimulatedAirplaneMode = await OfflineStorage.isSimulatedOffline();
    _lastSyncTimestamp = await OfflineStorage.getLastSyncTimeString();
    await checkConnectivity();
    _healthCheckTimer = Timer.periodic(const Duration(seconds: 10), (_) => checkConnectivity());
  }

  Future<void> checkConnectivity() async {
    if (_isSimulatedAirplaneMode) {
      _isOnline = false;
      notifyListeners();
      return;
    }

    try {
      final response = await http
          .get(Uri.parse('${DemoConstants.backendBaseUrl}/health'))
          .timeout(const Duration(seconds: 2));
      _isOnline = response.statusCode == 200;
    } catch (_) {
      _isOnline = false;
    }
    notifyListeners();
  }

  Future<void> toggleAirplaneModeSimulation(bool enableAirplaneMode) async {
    _isSimulatedAirplaneMode = enableAirplaneMode;
    await OfflineStorage.setSimulatedOffline(enableAirplaneMode);
    
    if (!enableAirplaneMode) {
      // Reconnected! Trigger immediate live sync
      await triggerLiveSync();
    } else {
      _isOnline = false;
      notifyListeners();
    }
  }

  Future<void> triggerLiveSync({Function? onSyncCallback}) async {
    if (_isSimulatedAirplaneMode) return;

    _isSyncing = true;
    notifyListeners();

    // Simulate clean network sync transaction
    await Future.delayed(const Duration(milliseconds: 1200));

    try {
      if (onSyncCallback != null) {
        await onSyncCallback();
      }
      _isOnline = true;
      final now = DateTime.now();
      _lastSyncTimestamp = "${now.day.toString().padLeft(2, '0')}/${now.month.toString().padLeft(2, '0')} ${now.hour.toString().padLeft(2, '0')}:${now.minute.toString().padLeft(2, '0')}";
    } catch (e) {
      print('Sync error: $e');
    } finally {
      _isSyncing = false;
      notifyListeners();
    }
  }

  @override
  void dispose() {
    _healthCheckTimer?.cancel();
    super.dispose();
  }
}
