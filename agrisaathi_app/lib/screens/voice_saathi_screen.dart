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

  final List<Map<String, dynamic>> _messages = [
    {
      "isUser": false,
      "text_hi": "नमस्ते किसान भाई! मैं आपका एग्रीसाथी हूं। आप मुझसे फसल में पानी, खाद, मौसम या मंडी भाव के बारे में पूछ सकते हैं।",
      "text_en": "Hello farmer friend! I am your AgriSaathi. You can ask me about water needs, fertilizer dosage, weather forecasts, or mandi prices.",
      "tts": "नमस्ते किसान भाई! मैं आपका एग्रीसाथी हूं। आप मुझसे कोई भी प्रश्न पूछ सकते हैं।"
    }
  ];

  final List<String> _quickPrompts = [
    "इसके लिए पानी कितना चाहिए?",
    "खाद कब और कितनी डालनी है?",
    "अगले दिनों का मौसम कैसा रहेगा?",
    "मंडी में आज क्या भाव मिल रहा है?",
    "पत्तियों पर पीले धब्बे दिख रहे हैं"
  ];

  @override
  void initState() {
    super.initState();
    _voiceService.addListener(() {
      if (mounted) setState(() {});
    });
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

      setState(() {
        _messages.add({
          "isUser": false,
          "text_hi": res["response_text_hi"] ?? "",
          "text_en": res["response_text_en"] ?? "",
          "tts": ttsText,
          "followups": res["suggested_followups"]
        });
      });

      // Auto-speak response in Hindi
      await _voiceService.speak(ttsText);
    } finally {
      if (mounted) setState(() => _isLoading = false);
    }
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
        title: Text(
          AppStrings.voiceSaathi,
          style: const TextStyle(fontWeight: FontWeight.bold),
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

                return Align(
                  alignment: isUser ? Alignment.centerRight : Alignment.centerLeft,
                  child: Container(
                    margin: const EdgeInsets.only(bottom: 12),
                    constraints: BoxConstraints(maxWidth: MediaQuery.of(context).size.width * 0.82),
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(
                      color: isUser ? AppColors.primary : Colors.white,
                      borderRadius: BorderRadius.only(
                        topLeft: const Radius.circular(18),
                        topRight: const Radius.circular(18),
                        bottomLeft: Radius.circular(isUser ? 18 : 4),
                        bottomRight: Radius.circular(isUser ? 4 : 18),
                      ),
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
                        Text(
                          text,
                          style: TextStyle(
                            fontSize: 14,
                            color: isUser ? Colors.white : AppColors.textPrimary,
                            height: 1.35,
                          ),
                        ),
                        if (!isUser && msg["tts"] != null) ...[
                          const SizedBox(height: 8),
                          InkWell(
                            onTap: () => _voiceService.speak(msg["tts"]),
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
                                  AppStrings.isHindi ? "आवाज सुनें" : "Listen Audio",
                                  style: const TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: AppColors.primary),
                                ),
                              ],
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
            margin: const EdgeInsets.only(bottom: 12),
            child: ListView.separated(
              scrollDirection: Axis.horizontal,
              padding: const EdgeInsets.symmetric(horizontal: 16),
              itemCount: _quickPrompts.length,
              separatorBuilder: (_, __) => const SizedBox(width: 8),
              itemBuilder: (context, idx) {
                final prompt = _quickPrompts[idx];
                return ActionChip(
                  label: Text(prompt, style: const TextStyle(fontSize: 12, color: AppColors.primaryDark)),
                  backgroundColor: AppColors.surfaceElevated,
                  side: BorderSide(color: AppColors.primaryLight.withOpacity(0.3)),
                  onPressed: () => _handleQuery(prompt),
                );
              },
            ),
          ),

          // Bottom Voice Pulse & Input Bar
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
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
                  child: TextField(
                    controller: _textController,
                    decoration: InputDecoration(
                      hintText: AppStrings.askVoice,
                      hintStyle: const TextStyle(fontSize: 13, color: AppColors.textMuted),
                      contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                      filled: true,
                      fillColor: AppColors.background,
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(24),
                        borderSide: BorderSide.none,
                      ),
                    ),
                    onSubmitted: _handleQuery,
                  ),
                ),
                const SizedBox(width: 10),
                VoicePulseButton(
                  isListening: _voiceService.isSpeaking,
                  onTap: () {
                    // Tap voice button speaks or simulates recognized prompt for robust demo
                    _handleQuery(_quickPrompts[0]);
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
