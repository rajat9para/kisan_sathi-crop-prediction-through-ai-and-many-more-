import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../constants/app_colors.dart';
import 'home_dashboard_screen.dart';

class LanguageSelectionScreen extends StatefulWidget {
  final bool isModalMode;
  const LanguageSelectionScreen({super.key, this.isModalMode = false});

  @override
  State<LanguageSelectionScreen> createState() => _LanguageSelectionScreenState();
}

class _LanguageSelectionScreenState extends State<LanguageSelectionScreen> {
  String _selectedLangCode = 'hi';
  bool _isDefaultChecked = true;

  final List<Map<String, String>> _primaryLanguages = [
    {
      'code': 'hi',
      'name': 'हिन्दी',
      'sub': 'Hindi (राष्ट्रीय / उत्तर-मध्य भारत)',
      'flag': '🇮🇳',
    },
    {
      'code': 'en',
      'name': 'English',
      'sub': 'English (Standard / Global)',
      'flag': '🇬🇧',
    },
  ];

  final List<Map<String, String>> _regionalLanguages = [
    {'code': 'mr', 'name': 'मराठी', 'sub': 'Marathi (महाराष्ट्र)', 'flag': '🚩'},
    {'code': 'pa', 'name': 'ਪੰਜਾਬੀ', 'sub': 'Punjabi (ਪੰਜਾਬ)', 'flag': '🌾'},
    {'code': 'te', 'name': 'తెలుగు', 'sub': 'Telugu (ఆంధ్ర / తెలంగాణ)', 'flag': '🌶️'},
    {'code': 'ta', 'name': 'தமிழ்', 'sub': 'Tamil (தமிழ்நாடு)', 'flag': '🌴'},
    {'code': 'gu', 'name': 'ગુજરાતી', 'sub': 'Gujarati (ગુજરાત)', 'flag': '🥜'},
    {'code': 'bn', 'name': 'বাংলা', 'sub': 'Bengali (পশ্চিমবঙ্গ)', 'flag': '🌾'},
    {'code': 'kn', 'name': 'ಕನ್ನಡ', 'sub': 'Kannada (ಕರ್ನಾಟಕ)', 'flag': '☕'},
    {'code': 'ml', 'name': 'മലയാളം', 'sub': 'Malayalam (കേരളം)', 'flag': '🥥'},
    {'code': 'or', 'name': 'ଓଡ଼ିଆ', 'sub': 'Odia (ଓଡ଼ିଶା)', 'flag': '🌾'},
  ];

  @override
  void initState() {
    super.initState();
    _loadSavedLanguage();
  }

  Future<void> _loadSavedLanguage() async {
    final prefs = await SharedPreferences.getInstance();
    final saved = prefs.getString('kisaan_sathi_lang');
    if (saved != null) {
      setState(() {
        _selectedLangCode = saved;
      });
    }
  }

  Future<void> _applyAndProceed() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('kisaan_sathi_lang', _selectedLangCode);
    if (_isDefaultChecked) {
      await prefs.setBool('kisaan_sathi_lang_saved', true);
    } else {
      await prefs.remove('kisaan_sathi_lang_saved');
    }

    if (!mounted) return;

    if (widget.isModalMode) {
      Navigator.of(context).pop(_selectedLangCode);
    } else {
      Navigator.of(context).pushReplacement(
        PageRouteBuilder(
          pageBuilder: (_, __, ___) => const HomeDashboardScreen(),
          transitionsBuilder: (_, a, __, c) => FadeTransition(opacity: a, child: c),
          transitionDuration: const Duration(milliseconds: 400),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF8FAF7),
      appBar: AppBar(
        backgroundColor: AppColors.primaryDark,
        elevation: 0,
        title: const Text(
          'अपनी भाषा चुनें / Choose Language',
          style: TextStyle(fontSize: 18, fontWeight: FontWeight.w700, color: Colors.white),
        ),
        centerTitle: true,
        leading: widget.isModalMode
            ? IconButton(
                icon: const Icon(Icons.close, color: Colors.white),
                onPressed: () => Navigator.of(context).pop(),
              )
            : null,
      ),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Header Banner
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  gradient: const LinearGradient(
                    colors: [AppColors.primaryDark, AppColors.primary],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                  borderRadius: BorderRadius.circular(16),
                  boxShadow: [
                    BoxShadow(
                      color: AppColors.primary.withOpacity(0.2),
                      blurRadius: 10,
                      offset: const Offset(0, 4),
                    ),
                  ],
                ),
                child: Row(
                  children: [
                    Container(
                      padding: const EdgeInsets.all(10),
                      decoration: BoxDecoration(
                        color: Colors.white.withOpacity(0.15),
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: const Text('🌾', style: TextStyle(fontSize: 28)),
                    ),
                    const SizedBox(width: 14),
                    const Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            'Kisaan_Sathi • किसान साथी',
                            style: TextStyle(
                              color: Colors.white,
                              fontSize: 16,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          SizedBox(height: 4),
                          Text(
                            'भारत की 11 प्रमुख कृषि भाषाओं में उपलब्ध',
                            style: TextStyle(color: Colors.white70, fontSize: 12),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),

              const SizedBox(height: 20),

              // Section 1: Primary (Hindi & English)
              const Text(
                '🌟 प्राथमिक भाषाएँ / PRIMARY LANGUAGES',
                style: TextStyle(
                  fontSize: 12,
                  fontWeight: FontWeight.w800,
                  color: AppColors.primaryDark,
                  letterSpacing: 0.5,
                ),
              ),
              const SizedBox(height: 10),

              ..._primaryLanguages.map((lang) => _buildLanguageCard(lang)),

              const SizedBox(height: 20),

              // Section 2: Regional Indian Languages
              const Text(
                '🌾 क्षेत्रीय भाषाएँ / REGIONAL INDIAN LANGUAGES',
                style: TextStyle(
                  fontSize: 12,
                  fontWeight: FontWeight.w800,
                  color: AppColors.primaryDark,
                  letterSpacing: 0.5,
                ),
              ),
              const SizedBox(height: 10),

              GridView.builder(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: 2,
                  mainAxisSpacing: 10,
                  crossAxisSpacing: 10,
                  childAspectRatio: 2.2,
                ),
                itemCount: _regionalLanguages.length,
                itemBuilder: (context, index) {
                  final lang = _regionalLanguages[index];
                  final isSelected = _selectedLangCode == lang['code'];
                  return InkWell(
                    onTap: () {
                      setState(() {
                        _selectedLangCode = lang['code']!;
                      });
                    },
                    borderRadius: BorderRadius.circular(12),
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                      decoration: BoxDecoration(
                        color: isSelected ? const Color(0xFFE8F5E9) : Colors.white,
                        borderRadius: BorderRadius.circular(12),
                        border: Border.all(
                          color: isSelected ? AppColors.primary : Colors.grey.shade300,
                          width: isSelected ? 2 : 1,
                        ),
                        boxShadow: isSelected
                            ? [
                                BoxShadow(
                                  color: AppColors.primary.withOpacity(0.12),
                                  blurRadius: 6,
                                  offset: const Offset(0, 2),
                                ),
                              ]
                            : [],
                      ),
                      child: Row(
                        children: [
                          Text(lang['flag']!, style: const TextStyle(fontSize: 20)),
                          const SizedBox(width: 8),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Text(
                                  lang['name']!,
                                  style: TextStyle(
                                    fontSize: 14,
                                    fontWeight: FontWeight.bold,
                                    color: isSelected ? AppColors.primaryDark : Colors.black87,
                                  ),
                                ),
                                Text(
                                  lang['sub']!,
                                  style: TextStyle(
                                    fontSize: 10,
                                    color: Colors.grey.shade600,
                                  ),
                                  maxLines: 1,
                                  overflow: TextOverflow.ellipsis,
                                ),
                              ],
                            ),
                          ),
                          if (isSelected)
                            const Icon(Icons.check_circle, color: AppColors.primary, size: 18),
                        ],
                      ),
                    ),
                  );
                },
              ),

              const SizedBox(height: 20),

              // Set as default checkbox box
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                decoration: BoxDecoration(
                  color: const Color(0xFFFEF3C7),
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: const Color(0xFFFDE68A)),
                ),
                child: CheckboxListTile(
                  value: _isDefaultChecked,
                  onChanged: (val) {
                    setState(() {
                      _isDefaultChecked = val ?? true;
                    });
                  },
                  activeColor: AppColors.primary,
                  contentPadding: EdgeInsets.zero,
                  title: const Text(
                    'Make this my default language',
                    style: TextStyle(
                      fontSize: 13,
                      fontWeight: FontWeight.bold,
                      color: Color(0xFF78350F),
                    ),
                  ),
                  subtitle: const Text(
                    'इसे मेरी डिफ़ॉल्ट भाषा बनाएं (Don\'t ask on next launch)',
                    style: TextStyle(fontSize: 11, color: Color(0xFF92400E)),
                  ),
                  controlAffinity: ListTileControlAffinity.leading,
                ),
              ),

              const SizedBox(height: 24),

              // Continue Button
              SizedBox(
                width: double.infinity,
                height: 52,
                child: ElevatedButton(
                  onPressed: _applyAndProceed,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: AppColors.primary,
                    foregroundColor: Colors.white,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(14),
                    ),
                    elevation: 2,
                  ),
                  child: const Text(
                    '✓ Continue to Farm Advisory / आगे बढ़ें ➔',
                    style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold),
                  ),
                ),
              ),
              const SizedBox(height: 16),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildLanguageCard(Map<String, String> lang) {
    final isSelected = _selectedLangCode == lang['code'];
    return Padding(
      padding: const EdgeInsets.only(bottom: 10),
      child: InkWell(
        onTap: () {
          setState(() {
            _selectedLangCode = lang['code']!;
          });
        },
        borderRadius: BorderRadius.circular(14),
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
          decoration: BoxDecoration(
            color: isSelected ? const Color(0xFFE8F5E9) : Colors.white,
            borderRadius: BorderRadius.circular(14),
            border: Border.all(
              color: isSelected ? AppColors.primary : Colors.grey.shade300,
              width: isSelected ? 2.2 : 1,
            ),
            boxShadow: isSelected
                ? [
                    BoxShadow(
                      color: AppColors.primary.withOpacity(0.15),
                      blurRadius: 8,
                      offset: const Offset(0, 2),
                    ),
                  ]
                : [],
          ),
          child: Row(
            children: [
              Text(lang['flag']!, style: const TextStyle(fontSize: 26)),
              const SizedBox(width: 14),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      lang['name']!,
                      style: TextStyle(
                        fontSize: 17,
                        fontWeight: FontWeight.bold,
                        color: isSelected ? AppColors.primaryDark : Colors.black87,
                      ),
                    ),
                    const SizedBox(height: 2),
                    Text(
                      lang['sub']!,
                      style: TextStyle(fontSize: 12, color: Colors.grey.shade600),
                    ),
                  ],
                ),
              ),
              if (isSelected)
                const Icon(Icons.check_circle_rounded, color: AppColors.primary, size: 24),
            ],
          ),
        ),
      ),
    );
  }
}
