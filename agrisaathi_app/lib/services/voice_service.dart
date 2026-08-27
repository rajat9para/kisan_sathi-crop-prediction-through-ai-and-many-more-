import 'package:flutter/foundation.dart';
import 'package:flutter_tts/flutter_tts.dart';

class VoiceService extends ChangeNotifier {
  static final VoiceService _instance = VoiceService._internal();
  factory VoiceService() => _instance;
  VoiceService._internal() {
    _initTts();
  }

  FlutterTts? _flutterTts;
  bool _isSpeaking = false;
  bool _isListening = false;
  String _selectedLang = "hi-IN";

  bool get isSpeaking => _isSpeaking;
  bool get isListening => _isListening;
  String get selectedLang => _selectedLang;

  Future<void> _initTts() async {
    try {
      _flutterTts = FlutterTts();
      await _flutterTts?.setLanguage(_selectedLang);
      await _flutterTts?.setSpeechRate(0.48); // Natural, clear cadence for rural farmers
      await _flutterTts?.setVolume(1.0);
      await _flutterTts?.setPitch(1.0);

      _flutterTts?.setStartHandler(() {
        _isSpeaking = true;
        notifyListeners();
      });

      _flutterTts?.setCompletionHandler(() {
        _isSpeaking = false;
        notifyListeners();
      });

      _flutterTts?.setErrorHandler((msg) {
        _isSpeaking = false;
        notifyListeners();
      });
    } catch (e) {
      print('TTS Init error: $e');
    }
  }

  Future<void> setLanguage(String langCode) async {
    _selectedLang = langCode;
    await _flutterTts?.setLanguage(langCode);
    notifyListeners();
  }

  Future<void> speak(String text) async {
    if (text.isEmpty) return;
    try {
      if (_isSpeaking) {
        await stop();
      }
      await _flutterTts?.speak(text);
    } catch (e) {
      print('Speak error: $e');
    }
  }

  Future<void> stop() async {
    try {
      await _flutterTts?.stop();
      _isSpeaking = false;
      notifyListeners();
    } catch (e) {
      print('Stop error: $e');
    }
  }

  void startSimulatedListening({required Function(String) onRecognized}) {
    _isListening = true;
    notifyListeners();
  }

  void stopListening() {
    _isListening = false;
    notifyListeners();
  }

  @override
  void dispose() {
    _flutterTts?.stop();
    super.dispose();
  }
}
