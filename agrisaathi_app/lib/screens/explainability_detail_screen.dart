import 'package:flutter/material.dart';
import '../models/crop_recommendation.dart';
import '../constants/app_colors.dart';
import '../constants/app_strings.dart';
import '../widgets/shap_bar_chart.dart';

class ExplainabilityDetailScreen extends StatelessWidget {
  final CropItem crop;

  const ExplainabilityDetailScreen({super.key, required this.crop});

  @override
  Widget build(BuildContext context) {
    final cropName = AppStrings.isHindi ? crop.cropNameHi : crop.cropName;

    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: AppBar(
        backgroundColor: AppColors.primary,
        title: Text(
          "${AppStrings.whyThisCrop} • $cropName",
          style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
        ),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Header Summary Banner
            Container(
              padding: const EdgeInsets.all(18),
              decoration: BoxDecoration(
                gradient: const LinearGradient(
                  colors: [AppColors.primaryDark, AppColors.primary],
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
                borderRadius: BorderRadius.circular(20),
                boxShadow: [
                  BoxShadow(
                    color: AppColors.primary.withOpacity(0.2),
                    blurRadius: 12,
                    offset: const Offset(0, 4),
                  ),
                ],
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        cropName,
                        style: const TextStyle(fontSize: 26, fontWeight: FontWeight.bold, color: Colors.white),
                      ),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                        decoration: BoxDecoration(
                          color: AppColors.secondary,
                          borderRadius: BorderRadius.circular(14),
                        ),
                        child: Text(
                          "${crop.matchScorePct}% Match",
                          style: const TextStyle(fontSize: 14, fontWeight: FontWeight.bold, color: Colors.white),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 8),
                  Text(
                    AppStrings.isHindi ? crop.whyThisCropHi : crop.whyThisCropEn,
                    style: const TextStyle(fontSize: 14, color: Colors.white, height: 1.4),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 20),

            // 1. 4-Pillar Visual Breakdown
            Text(
              AppStrings.isHindi ? "1. चार-स्तंभीय अनुकूलता स्कोर (4 Pillars)" : "1. 4-Pillar Fit Breakdown",
              style: const TextStyle(fontSize: 17, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
            ),
            const SizedBox(height: 12),
            Row(
              children: [
                Expanded(
                  child: _buildPillarCard(
                    title: AppStrings.soilFit,
                    pct: crop.soilFitPct,
                    color: AppColors.accent,
                    icon: Icons.grass_rounded,
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: _buildPillarCard(
                    title: AppStrings.weatherFit,
                    pct: crop.weatherFitPct,
                    color: AppColors.info,
                    icon: Icons.cloud_rounded,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),
            Row(
              children: [
                Expanded(
                  child: _buildPillarCard(
                    title: AppStrings.marketProfit,
                    pct: crop.marketProfitabilityPct,
                    color: AppColors.success,
                    icon: Icons.trending_up_rounded,
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: _buildPillarCard(
                    title: AppStrings.rotationImpact,
                    pct: crop.rotationImpactPct,
                    color: AppColors.secondary,
                    icon: Icons.autorenew_rounded,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 24),

            // 2. SHAP Feature Influence Bar Chart (Mathematical explainability)
            Container(
              padding: const EdgeInsets.all(18),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(20),
                border: Border.all(color: Colors.black.withOpacity(0.06)),
                boxShadow: [
                  BoxShadow(
                    color: Colors.black.withOpacity(0.03),
                    blurRadius: 10,
                    offset: const Offset(0, 4),
                  ),
                ],
              ),
              child: ShapBarChart(contributions: crop.shapContributions),
            ),
            const SizedBox(height: 24),

            // 3. Recommended Fertilizer Schedule
            _buildScheduleSection(
              title: AppStrings.fertilizerPlan,
              icon: Icons.science_rounded,
              color: AppColors.primary,
              items: crop.fertilizerSchedule.map((f) => {
                "header": f["stage"] ?? "",
                "body": "${f['dosage'] ?? ''}\n(${f['purpose'] ?? ''})"
              }).toList(),
            ),
            const SizedBox(height: 16),

            // 4. Irrigation Schedule
            _buildScheduleSection(
              title: AppStrings.irrigationPlan,
              icon: Icons.water_drop_rounded,
              color: AppColors.info,
              items: crop.irrigationSchedule.map((i) => {
                "header": "${i['stage']} • ${i['timing']}",
                "body": i['note'] ?? ""
              }).toList(),
            ),
            const SizedBox(height: 24),

            // Economics & Sowing Guide
            Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: AppColors.surfaceElevated,
                borderRadius: BorderRadius.circular(16),
                border: Border.all(color: AppColors.primaryLight.withOpacity(0.3)),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      const Icon(Icons.calendar_month_rounded, color: AppColors.primaryDark, size: 20),
                      const SizedBox(width: 8),
                      Text(
                        AppStrings.isHindi ? "बुवाई का समय व कटाई अवधि" : "Sowing Window & Harvest Timeline",
                        style: const TextStyle(fontSize: 14, fontWeight: FontWeight.bold, color: AppColors.primaryDark),
                      ),
                    ],
                  ),
                  const SizedBox(height: 10),
                  Text(
                    "• ${AppStrings.isHindi ? 'बुवाई समय:' : 'Sowing:'} ${AppStrings.isHindi ? crop.sowingWindowHi : crop.sowingWindowEn}",
                    style: const TextStyle(fontSize: 13, color: AppColors.textPrimary, fontWeight: FontWeight.w500),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    "• ${AppStrings.isHindi ? 'फसल अवधि:' : 'Crop Duration:'} ${crop.harvestDurationDays} ${AppStrings.isHindi ? 'दिन' : 'Days'}",
                    style: const TextStyle(fontSize: 13, color: AppColors.textPrimary, fontWeight: FontWeight.w500),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    "• ${AppStrings.isHindi ? 'जल मांग स्तर:' : 'Water Demand:'} ${crop.waterRequirement}",
                    style: const TextStyle(fontSize: 13, color: AppColors.textPrimary, fontWeight: FontWeight.w500),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 20),
          ],
        ),
      ),
    );
  }

  Widget _buildPillarCard({
    required String title,
    required double pct,
    required Color color,
    required IconData icon,
  }) {
    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: color.withOpacity(0.2)),
        boxShadow: [
          BoxShadow(
            color: color.withOpacity(0.05),
            blurRadius: 8,
            offset: const Offset(0, 3),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Icon(icon, color: color, size: 22),
              Text(
                "${pct.toInt()}%",
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: color),
              ),
            ],
          ),
          const SizedBox(height: 10),
          Text(
            title,
            style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w600, color: AppColors.textPrimary),
          ),
          const SizedBox(height: 6),
          ClipRRect(
            borderRadius: BorderRadius.circular(4),
            child: LinearProgressIndicator(
              value: (pct / 100).clamp(0.0, 1.0),
              backgroundColor: color.withOpacity(0.12),
              valueColor: AlwaysStoppedAnimation<Color>(color),
              minHeight: 6,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildScheduleSection({
    required String title,
    required IconData icon,
    required Color color,
    required List<Map<String, String>> items,
  }) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: Colors.black.withOpacity(0.06)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(icon, color: color, size: 20),
              const SizedBox(width: 8),
              Text(
                title,
                style: const TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
              ),
            ],
          ),
          const SizedBox(height: 12),
          ...items.map((item) {
            return Container(
              margin: const EdgeInsets.only(bottom: 10),
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(
                color: color.withOpacity(0.04),
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: color.withOpacity(0.15)),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    item["header"] ?? "",
                    style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: color),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    item["body"] ?? "",
                    style: const TextStyle(fontSize: 12, color: AppColors.textPrimary, height: 1.3),
                  ),
                ],
              ),
            );
          }),
        ],
      ),
    );
  }
}
