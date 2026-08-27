import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/advisory_provider.dart';
import '../models/crop_recommendation.dart';
import '../constants/app_colors.dart';
import '../constants/app_strings.dart';
import 'explainability_detail_screen.dart';
import 'location_soil_input_screen.dart';

class RecommendationScreen extends StatelessWidget {
  const RecommendationScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final advisory = context.watch<AdvisoryProvider>();
    final rec = advisory.recommendation;

    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: AppBar(
        backgroundColor: AppColors.primary,
        title: Text(
          AppStrings.advisory,
          style: const TextStyle(fontWeight: FontWeight.bold),
        ),
        actions: [
          IconButton(
            tooltip: "Modify Soil / Location",
            icon: const Icon(Icons.tune_rounded),
            onPressed: () {
              Navigator.push(context, MaterialPageRoute(builder: (_) => const LocationSoilInputScreen()));
            },
          ),
        ],
      ),
      body: advisory.isLoading
          ? const Center(child: CircularProgressIndicator())
          : (rec == null || rec.topRecommendations.isEmpty)
              ? Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      const Icon(Icons.psychology_outlined, size: 64, color: Colors.grey),
                      const SizedBox(height: 16),
                      Text(AppStrings.isHindi ? "कोई सिफारिश उपलब्ध नहीं है" : "No recommendations found."),
                      const SizedBox(height: 12),
                      ElevatedButton(
                        onPressed: () => advisory.fetchRecommendations(),
                        child: Text(AppStrings.syncNow),
                      ),
                    ],
                  ),
                )
              : SingleChildScrollView(
                  padding: const EdgeInsets.all(16),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      // Header Card with Location & Soil Summary
                      Container(
                        padding: const EdgeInsets.all(14),
                        decoration: BoxDecoration(
                          color: AppColors.surface,
                          borderRadius: BorderRadius.circular(16),
                          border: Border.all(color: Colors.black.withOpacity(0.06)),
                        ),
                        child: Row(
                          children: [
                            Container(
                              padding: const EdgeInsets.all(10),
                              decoration: BoxDecoration(
                                color: AppColors.primaryLight.withOpacity(0.15),
                                shape: BoxShape.circle,
                              ),
                              child: const Icon(Icons.check_circle_rounded, color: AppColors.primary, size: 24),
                            ),
                            const SizedBox(width: 12),
                            Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(
                                    AppStrings.isHindi ? "एआई मॉडल विश्लेषण पूर्ण" : "AI Multi-Pillar Analysis Complete",
                                    style: const TextStyle(fontSize: 14, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
                                  ),
                                  Text(
                                    "Location: ${advisory.selectedLocation['name_en']} • Previous: ${advisory.previousCrop}",
                                    style: const TextStyle(fontSize: 11, color: AppColors.textSecondary),
                                  ),
                                ],
                              ),
                            ),
                          ],
                        ),
                      ),
                      const SizedBox(height: 18),

                      Text(
                        AppStrings.isHindi ? "शीर्ष अनुशंसित फसलें (Ranked)" : "Top Ranked Crop Recommendations",
                        style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
                      ),
                      const SizedBox(height: 12),

                      ...rec.topRecommendations.map((crop) => _buildCropCard(context, crop)).toList(),
                    ],
                  ),
                ),
    );
  }

  Widget _buildCropCard(BuildContext context, CropItem crop) {
    final cropName = AppStrings.isHindi ? crop.cropNameHi : crop.cropName;
    final isRank1 = crop.rank == 1;

    return Container(
      margin: const EdgeInsets.only(bottom: 16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(
          color: isRank1 ? AppColors.primaryLight.withOpacity(0.6) : Colors.black.withOpacity(0.06),
          width: isRank1 ? 2 : 1,
        ),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.04),
            blurRadius: 10,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Row(
                  children: [
                    Container(
                      width: 28,
                      height: 28,
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        color: isRank1 ? AppColors.secondary : AppColors.primary,
                      ),
                      child: Center(
                        child: Text(
                          "#${crop.rank}",
                          style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 13),
                        ),
                      ),
                    ),
                    const SizedBox(width: 10),
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          cropName,
                          style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
                        ),
                        Text(
                          crop.scientificName,
                          style: const TextStyle(fontSize: 11, fontStyle: FontStyle.italic, color: AppColors.textSecondary),
                        ),
                      ],
                    ),
                  ],
                ),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                  decoration: BoxDecoration(
                    color: AppColors.primaryLight.withOpacity(0.12),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Text(
                    "${crop.matchScorePct.toStringAsFixed(1)}% Match",
                    style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: AppColors.primaryDark),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),
            Text(
              AppStrings.isHindi ? crop.whyThisCropHi : crop.whyThisCropEn,
              style: const TextStyle(fontSize: 13, color: AppColors.textSecondary, height: 1.3),
            ),
            const SizedBox(height: 14),

            // 4 Mini Score Pillars
            Row(
              children: [
                _buildMiniPillar("Soil", "${crop.soilFitPct.toInt()}%", AppColors.accent),
                const SizedBox(width: 8),
                _buildMiniPillar("Weather", "${crop.weatherFitPct.toInt()}%", AppColors.info),
                const SizedBox(width: 8),
                _buildMiniPillar("Market", "${crop.marketProfitabilityPct.toInt()}%", AppColors.success),
                const SizedBox(width: 8),
                _buildMiniPillar("Rotation", "${crop.rotationImpactPct.toInt()}%", AppColors.secondary),
              ],
            ),
            const SizedBox(height: 16),
            const Divider(height: 1),
            const SizedBox(height: 12),

            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      AppStrings.isHindi ? "अपेक्षित उपज / एकड़" : "Expected Yield",
                      style: const TextStyle(fontSize: 11, color: AppColors.textMuted),
                    ),
                    Text(
                      crop.expectedYield,
                      style: const TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
                    ),
                  ],
                ),
                ElevatedButton.icon(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: AppColors.primary,
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                    padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                  ),
                  icon: const Icon(Icons.analytics_rounded, size: 16, color: Colors.white),
                  label: Text(
                    AppStrings.whyThisCrop,
                    style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.white),
                  ),
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (_) => ExplainabilityDetailScreen(crop: crop),
                      ),
                    );
                  },
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildMiniPillar(String label, String value, Color color) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 6),
        decoration: BoxDecoration(
          color: color.withOpacity(0.08),
          borderRadius: BorderRadius.circular(8),
        ),
        child: Column(
          children: [
            Text(value, style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: color)),
            Text(label, style: const TextStyle(fontSize: 10, color: AppColors.textSecondary)),
          ],
        ),
      ),
    );
  }
}
