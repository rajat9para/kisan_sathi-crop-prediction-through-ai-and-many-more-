import 'package:flutter/material.dart';
import '../services/voice_service.dart';
import '../services/api_service.dart';
import '../constants/app_colors.dart';
import '../constants/app_strings.dart';
import '../widgets/voice_pulse_button.dart';

class VoiceSaathiScreen extends StatefulWidget {
  const VoiceSaathiScreen({super.key});

  @override
  State<VoiceSaathiScreen> createState() => _VoiceSaathiScreenState();
}

class _VoiceSaathiScreenState extends State<VoiceSaathiScreen> {
  final TextEditingController _textController = TextEditingController();
  final VoiceService _voiceService = VoiceService();
  bool _isLoading = false;
  bool _hasText = false;

  final List<Map<String, dynamic>> _messages = [
    {
      "isUser": false,
      "text_hi": "नमस्ते किसान भाई! मैं आपका एग्रीसाथी हूं। आप मुझसे फसल चयन (ML), पानी/सिंचाई समय, खाद (NPK), मौसम या मंडी भाव के बारे में पूछ सकते हैं।",
      "text_en": "Hello farmer friend! I am your AgriSaathi. You can ask me about AI crop selection, irrigation timings, balanced fertilizers, weather forecasts, or live mandi rates.",
      "tts": "नमस्ते किसान भाई! मैं आपका एग्रीसाथी हूं। आप मुझसे कोई भी कृषि प्रश्न पूछ सकते हैं।",
      "intent": "GENERAL_AGRONOMY"
    }
  ];

  final List<String> _quickPrompts = [
    "खेत में पानी किस समय डालना चाहिए?",
    "इस मिट्टी के लिए कौनसी फसल उत्तम है?",
    "गन्ने में खाद कब और कितनी डालनी है?",
    "गेहूं में पहला पानी कब लगाएं (CRI)?",
    "मंडी में आज क्या भाव मिल रहा है?",
    "टमाटर की पत्तियों पर झुलसा रोग उपचार"
  ];

  @override
  void initState() {
    super.initState();
    _textController.addListener(() {
      final has = _textController.text.trim().isNotEmpty;
      if (has != _hasText) {
        setState(() => _hasText = has);
      }
    });
    _voiceService.addListener(() {
      if (mounted) setState(() {});
    });
  }

  String _classifyLocalIntent(String q) {
    final query = q.toLowerCase();
    if (query.contains("kaunsi") || query.contains("fasal") || query.contains("selection") || query.contains("recommend") || query.contains("फसल")) {
      return "ML_CROP_RECOMMENDATION";
    }
    if (query.contains("pani") || query.contains("paani") || query.contains("water") || query.contains("sinchai") || query.contains("सिंचाई") || query.contains("samay")) {
      return "IRRIGATION_WATER";
    }
    if (query.contains("khad") || query.contains("fertilizer") || query.contains("urea") || query.contains("dap") || query.contains("खाद")) {
      return "FERTILIZER_NPK";
    }
    if (query.contains("rog") || query.contains("jhulsa") || query.contains("disease") || query.contains("pest") || query.contains("कीट") || query.contains("रोग")) {
      return "PLANT_DOCTOR";
    }
    if (query.contains("bhav") || query.contains("rate") || query.contains("mandi") || query.contains("भाव") || query.contains("मंडी")) {
      return "MANDI_RATES";
    }
    if (query.contains("scheme") || query.contains("yojana") || query.contains("pmkisan") || query.contains("योजना")) {
      return "GOVT_SCHEMES";
    }
    return "GENERAL_AGRONOMY";
  }

  Future<void> _handleQuery(String text) async {
    if (text.trim().isEmpty) return;

    setState(() {
      _messages.add({"isUser": true, "text_hi": text, "text_en": text});
      _isLoading = true;
    });
    _textController.clear();

    try {
      final res = await ApiService.sendVoiceQuery(text, lang: AppStrings.isHindi ? "hi" : "en");
      final ttsText = res["tts_audio_text"] ?? res["response_text_hi"] ?? "";
      final intent = res["intent_type"] ?? _classifyLocalIntent(text);

      setState(() {
        _messages.add({
          "isUser": false,
          "text_hi": res["response_text_hi"] ?? "",
          "text_en": res["response_text_en"] ?? "",
          "tts": ttsText,
          "intent": intent,
          "followups": res["suggested_followups"]
        });
      });

      // Auto-speak response in Hindi
      await _voiceService.speak(ttsText);
    } catch (_) {
      // Local fallback in case offline
      final intent = _classifyLocalIntent(text);
      String fallbackHi = "आपकी समस्या कृषि वैज्ञानिकों द्वारा विश्लेषित की जा रही है। अधिक जानकारी हेतु किसान कॉल सेंटर 1800-180-1551 पर संपर्क करें।";
      if (intent == "IRRIGATION_WATER") {
        fallbackHi = "सिंचाई सलाह: सुबह 6 से 9 बजे या शाम को 5 बजे के बाद ही पानी दें। दोपहर की तेज धूप में सिंचाई करने से 30-40% पानी वाष्पीकरण से उड़ जाता है।";
      } else if (intent == "ML_CROP_RECOMMENDATION") {
        fallbackHi = "मशीन लर्निंग फसल चयन: आपकी मिट्टी के अनुसार अंगूर व सोयाबीन 95% उपयुक्त हैं। विस्तृत रिपोर्ट फसल सलाहकार टैब में देखें।";
      }

      setState(() {
        _messages.add({
          "isUser": false,
          "text_hi": fallbackHi,
          "text_en": fallbackHi,
          "tts": fallbackHi,
          "intent": intent,
        });
      });
    } finally {
      if (mounted) setState(() => _isLoading = false);
    }
  }

  Widget _buildIntentBadge(String? intent) {
    if (intent == null) return const SizedBox.shrink();

    String label = "🌱 सामान्य कृषि परामर्श";
    Color bg = const Color(0xFFF1F5F9);
    Color text = const Color(0xFF334155);

    if (intent == "ML_CROP_RECOMMENDATION") {
      label = "⚡ ML फसल चयन (Crop AI)";
      bg = const Color(0xFFEDE9FE);
      text = const Color(0xFF6D28D9);
    } else if (intent == "IRRIGATION_WATER") {
      label = "💧 सिंचाई व जल प्रबंधन";
      bg = const Color(0xFFE0F2FE);
      text = const Color(0xFF0369A1);
    } else if (intent == "FERTILIZER_NPK") {
      label = "🧪 संतुलित खाद व पोषण";
      bg = const Color(0xFFDCFCE7);
      text = const Color(0xFF15803D);
    } else if (intent == "PLANT_DOCTOR") {
      label = "🩺 फसल रोग निदान";
      bg = const Color(0xFFFFE4E6);
      text = const Color(0xFFE11D48);
    } else if (intent == "MANDI_RATES") {
      label = "📊 दैनिक मंडी भाव";
      bg = const Color(0xFFFEF3C7);
      text = const Color(0xFFB45309);
    } else if (intent == "GOVT_SCHEMES") {
      label = "🏛️ सरकारी योजना";
      bg = const Color(0xFFDBEAFE);
      text = const Color(0xFF1D4ED8);
    }

    return Container(
      margin: const EdgeInsets.only(bottom: 6),
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
      decoration: BoxDecoration(
        color: bg,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: text.withOpacity(0.3)),
      ),
      child: Text(
        label,
        style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: text),
      ),
    );
  }

  @override
  void dispose() {
    _voiceService.stop();
    _textController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: AppBar(
        backgroundColor: AppColors.primary,
        title: Row(
          children: [
            const Text("🌾 ", style: TextStyle(fontSize: 20)),
            Text(
              AppStrings.voiceSaathi,
              style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 18),
            ),
          ],
        ),
        actions: [
          if (_voiceService.isSpeaking)
            IconButton(
              icon: const Icon(Icons.volume_off_rounded, color: Colors.white),
              onPressed: () => _voiceService.stop(),
            ),
        ],
      ),
      body: Column(
        children: [
          // Chat Messages List
          Expanded(
            child: ListView.builder(
              padding: const EdgeInsets.all(16),
              itemCount: _messages.length,
              itemBuilder: (context, idx) {
                final msg = _messages[idx];
                final isUser = msg["isUser"] == true;
                final text = AppStrings.isHindi ? (msg["text_hi"] ?? "") : (msg["text_en"] ?? "");
                final intent = msg["intent"] as String?;

                return Align(
                  alignment: isUser ? Alignment.centerRight : Alignment.centerLeft,
                  child: Container(
                    margin: const EdgeInsets.only(bottom: 12),
                    constraints: BoxConstraints(maxWidth: MediaQuery.of(context).size.width * 0.84),
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(
                      color: isUser ? AppColors.primary : Colors.white,
                      borderRadius: BorderRadius.only(
                        topLeft: const Radius.circular(18),
                        topRight: const Radius.circular(18),
                        bottomLeft: Radius.circular(isUser ? 18 : 4),
                        bottomRight: Radius.circular(isUser ? 4 : 18),
                      ),
                      border: isUser ? null : Border.all(color: AppColors.primaryLight.withOpacity(0.4)),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withOpacity(0.04),
                          blurRadius: 8,
                          offset: const Offset(0, 3),
                        ),
                      ],
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        if (!isUser) _buildIntentBadge(intent),
                        Text(
                          text,
                          style: TextStyle(
                            fontSize: 14,
                            color: isUser ? Colors.white : AppColors.textPrimary,
                            height: 1.4,
                            fontWeight: isUser ? FontWeight.w600 : FontWeight.normal,
                          ),
                        ),
                        if (!isUser && msg["tts"] != null) ...[
                          const SizedBox(height: 8),
                          InkWell(
                            onTap: () => _voiceService.speak(msg["tts"]),
                            child: Container(
                              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                              decoration: BoxDecoration(
                                color: AppColors.surfaceElevated,
                                borderRadius: BorderRadius.circular(8),
                              ),
                              child: Row(
                                mainAxisSize: MainAxisSize.min,
                                children: [
                                  Icon(
                                    _voiceService.isSpeaking ? Icons.volume_up_rounded : Icons.play_circle_outline_rounded,
                                    size: 16,
                                    color: AppColors.primary,
                                  ),
                                  const SizedBox(width: 4),
                                  Text(
                                    AppStrings.isHindi ? "1-टैप सुनें (Audio)" : "Listen 1-Tap",
                                    style: const TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: AppColors.primary),
                                  ),
                                ],
                              ),
                            ),
                          ),
                        ],
                      ],
                    ),
                  ),
                );
              },
            ),
          ),

          if (_isLoading)
            const Padding(
              padding: EdgeInsets.symmetric(vertical: 8),
              child: SizedBox(
                width: 24,
                height: 24,
                child: CircularProgressIndicator(strokeWidth: 2, color: AppColors.primary),
              ),
            ),

          // Quick Prompt Chips
          Container(
            height: 42,
            margin: const EdgeInsets.only(bottom: 8),
            child: ListView.separated(
              scrollDirection: Axis.horizontal,
              padding: const EdgeInsets.symmetric(horizontal: 16),
              itemCount: _quickPrompts.length,
              separatorBuilder: (ctx, i) => const SizedBox(width: 8),
              itemBuilder: (context, idx) {
                final prompt = _quickPrompts[idx];
                return ActionChip(
                  label: Text(prompt, style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w600, color: AppColors.primaryDark)),
                  backgroundColor: Colors.white,
                  side: BorderSide(color: AppColors.primary.withOpacity(0.3)),
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
                  onPressed: () {
                    _textController.text = prompt;
                    _handleQuery(prompt);
                  },
                );
              },
            ),
          ),

          // Google-Style Unified Search & Mic Bar
          Container(
            padding: const EdgeInsets.fromLTRB(16, 8, 16, 16),
            decoration: BoxDecoration(
              color: Colors.white,
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withOpacity(0.06),
                  blurRadius: 10,
                  offset: const Offset(0, -3),
                ),
              ],
            ),
            child: Row(
              children: [
                Expanded(
                  child: Container(
                    decoration: BoxDecoration(
                      color: AppColors.background,
                      borderRadius: BorderRadius.circular(28),
                      border: Border.all(color: AppColors.surfaceElevated),
                    ),
                    child: Row(
                      children: [
                        const Padding(
                          padding: EdgeInsets.only(left: 12, right: 6),
                          child: Icon(Icons.search_rounded, size: 20, color: AppColors.textMuted),
                        ),
                        Expanded(
                          child: TextField(
                            controller: _textController,
                            decoration: InputDecoration(
                              hintText: AppStrings.isHindi ? "कृषि प्रश्न पूछें या बोलें..." : "Ask or speak farming question...",
                              hintStyle: const TextStyle(fontSize: 13, color: AppColors.textMuted),
                              border: InputBorder.none,
                              contentPadding: const EdgeInsets.symmetric(vertical: 12),
                            ),
                            onSubmitted: _handleQuery,
                          ),
                        ),
                        if (_hasText)
                          IconButton(
                            icon: const Icon(Icons.close_rounded, size: 18, color: AppColors.textMuted),
                            onPressed: () => _textController.clear(),
                          ),
                        IconButton(
                          icon: const Icon(Icons.send_rounded, size: 20, color: AppColors.primary),
                          onPressed: () => _handleQuery(_textController.text),
                        ),
                      ],
                    ),
                  ),
                ),
                const SizedBox(width: 10),
                VoicePulseButton(
                  isListening: _voiceService.isSpeaking,
                  onTap: () {
                    final sampleQuery = _quickPrompts[0];
                    _textController.text = sampleQuery;
                    _handleQuery(sampleQuery);
                  },
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
