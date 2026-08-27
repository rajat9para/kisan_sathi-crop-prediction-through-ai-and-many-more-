import 'package:flutter/material.dart';
import '../constants/app_colors.dart';
import '../constants/app_strings.dart';

class RoadmapSchemesScreen extends StatelessWidget {
  const RoadmapSchemesScreen({super.key});

  final List<Map<String, dynamic>> _schemes = const [
    {
      "name_hi": "प्रधानमंत्री किसान सम्मान निधि (PM-KISAN)",
      "name_en": "PM Kisan Samman Nidhi",
      "benefit": "₹6,000 / वर्ष प्रत्यक्ष लाभ हस्तांतरण (DBT)",
      "eligibility": "पात्र (सभी भूमिधारक किसान परिवार)",
      "status": "Active • Next Installment Due"
    },
    {
      "name_hi": "प्रधानमंत्री फसल बीमा योजना (PMFBY)",
      "name_en": "PM Fasal Bima Yojana",
      "benefit": "अतिवृष्टि व सूखे से फसल नुकसान का 100% क्लेम",
      "eligibility": "पात्र (अधिसूचित खरीफ व रबी फसलें)",
      "status": "Enrolled for Kharif Season"
    },
    {
      "name_hi": "मृदा स्वास्थ्य कार्ड योजना (Soil Health Scheme)",
      "name_en": "Soil Health Card Scheme",
      "benefit": "निःशुल्क पोषक तत्व जांच व सुधारक सिफारिश",
      "eligibility": "कार्ड जारी (MahaSoil Lab #MH-4012)",
      "status": "Valid until May 2029"
    },
    {
      "name_hi": "किसान क्रेडिट कार्ड (KCC)",
      "name_en": "Kisan Credit Card Scheme",
      "benefit": "4% रियायती ब्याज दर पर ₹3 लाख तक का कृषि ऋण",
      "eligibility": "पात्र (2.5 एकड़ भूमि पर ₹1.8 लाख सीमा)",
      "status": "Available via State Bank / APMC"
    }
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: AppBar(
        backgroundColor: AppColors.primary,
        title: Text(
          AppStrings.schemesRoadmap,
          style: const TextStyle(fontWeight: FontWeight.bold),
        ),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Government Schemes
            Text(
              AppStrings.isHindi ? "सरकारी कृषि योजनाएं व पात्रता" : "Government Schemes & Eligibility",
              style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
            ),
            const SizedBox(height: 12),
            ..._schemes.map((s) => _buildSchemeCard(s)).toList(),
            const SizedBox(height: 24),

            // Roadmap & Future Integrations (Pitch Card for Judges)
            Text(
              AppStrings.isHindi ? "एग्रीसाथी भविष्य का रोडमैप (Roadmap)" : "AgriSaathi Future Roadmap",
              style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
            ),
            const SizedBox(height: 12),
            _buildRoadmapCard(
              title: "1. ISRO Bhuvan Satellite Geo-Spatial Layer",
              subtitle: "Upgrading from SoilGrids to ISRO Bhuvan optical & SAR radar imagery for sub-meter NDVI moisture tracking.",
              badge: "Phase 2 Roadmap",
              icon: Icons.satellite_alt_rounded,
            ),
            _buildRoadmapCard(
              title: "2. KVK Extension Officer Cluster Dashboard",
              subtitle: "Village-level aggregate disease outbreak heatmaps and custom advisory broadcasts for Agriculture Officers.",
              badge: "Pilot Ready",
              icon: Icons.dashboard_customize_rounded,
            ),
            _buildRoadmapCard(
              title: "3. 12 Regional Indian Languages Voice Model",
              subtitle: "Expanding from Hindi to Marathi, Punjabi, Telugu, Tamil, Gujarati, Bengali, and Kannada with IndicWhisper.",
              badge: "Model Training",
              icon: Icons.translate_rounded,
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSchemeCard(Map<String, dynamic> s) {
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.black.withOpacity(0.06)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Expanded(
                child: Text(
                  AppStrings.isHindi ? s["name_hi"] : s["name_en"],
                  style: const TextStyle(fontSize: 14, fontWeight: FontWeight.bold, color: AppColors.primaryDark),
                ),
              ),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                decoration: BoxDecoration(
                  color: AppColors.success.withOpacity(0.1),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: const Text(
                  "Eligible",
                  style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: AppColors.success),
                ),
              ),
            ],
          ),
          const SizedBox(height: 6),
          Text(
            s["benefit"],
            style: const TextStyle(fontSize: 13, fontWeight: FontWeight.w600, color: AppColors.textPrimary),
          ),
          const SizedBox(height: 4),
          Text(
            s["eligibility"],
            style: const TextStyle(fontSize: 11, color: AppColors.textSecondary),
          ),
        ],
      ),
    );
  }

  Widget _buildRoadmapCard({
    required String title,
    required String subtitle,
    required String badge,
    required IconData icon,
  }) {
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: AppColors.surfaceElevated,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: AppColors.primaryLight.withOpacity(0.2)),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: AppColors.primary.withOpacity(0.12),
              shape: BoxShape.circle,
            ),
            child: Icon(icon, color: AppColors.primary, size: 22),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Expanded(
                      child: Text(
                        title,
                        style: const TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: AppColors.primaryDark),
                      ),
                    ),
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                      decoration: BoxDecoration(
                        color: AppColors.secondary,
                        borderRadius: BorderRadius.circular(6),
                      ),
                      child: Text(
                        badge,
                        style: const TextStyle(fontSize: 9, fontWeight: FontWeight.bold, color: Colors.white),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 4),
                Text(
                  subtitle,
                  style: const TextStyle(fontSize: 11, color: AppColors.textSecondary, height: 1.3),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
