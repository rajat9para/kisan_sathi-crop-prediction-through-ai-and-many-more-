import 'package:flutter/material.dart';
import '../models/crop_recommendation.dart';
import '../constants/app_colors.dart';
import '../constants/app_strings.dart';

class ShapBarChart extends StatelessWidget {
  final List<ShapFeature> contributions;

  const ShapBarChart({super.key, required this.contributions});

  @override
  Widget build(BuildContext context) {
    if (contributions.isEmpty) {
      return const Center(child: Text("No SHAP values available."));
    }

    // Find max absolute value for normalization
    double maxAbs = 0.01;
    for (var c in contributions) {
      if (c.impactScore.abs() > maxAbs) {
        maxAbs = c.impactScore.abs();
      }
    }

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          children: [
            const Icon(Icons.analytics_rounded, color: AppColors.primary, size: 20),
            const SizedBox(width: 8),
            Expanded(
              child: Text(
                AppStrings.shapDrivers,
                style: const TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                  color: AppColors.textPrimary,
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: 6),
        Text(
          AppStrings.isHindi
              ? "हरा रंग (+) फसल के लिए अनुकूल कारक दर्शाता है, लाल रंग (-) सुधार योग्य कारक है।"
              : "Green bars (+) boost crop suitability, while red bars (-) highlight limiting factors.",
          style: const TextStyle(fontSize: 12, color: AppColors.textSecondary),
        ),
        const SizedBox(height: 14),
        ...contributions.map((feat) {
          final isPositive = feat.impactScore >= 0;
          final normWidth = (feat.impactScore.abs() / maxAbs).clamp(0.08, 1.0);
          final barColor = isPositive ? AppColors.shapPositive : AppColors.shapNegative;
          final title = AppStrings.isHindi ? feat.featureNameHi : feat.feature;
          final desc = AppStrings.isHindi ? feat.explanationHi : feat.explanationEn;

          return Container(
            margin: const EdgeInsets.only(bottom: 12),
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: barColor.withOpacity(0.04),
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: barColor.withOpacity(0.2)),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      title,
                      style: const TextStyle(
                        fontSize: 13,
                        fontWeight: FontWeight.w600,
                        color: AppColors.textPrimary,
                      ),
                    ),
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                      decoration: BoxDecoration(
                        color: barColor.withOpacity(0.12),
                        borderRadius: BorderRadius.circular(6),
                      ),
                      child: Text(
                        "${isPositive ? '+' : ''}${(feat.impactScore * 100).toStringAsFixed(1)}%",
                        style: TextStyle(
                          fontSize: 12,
                          fontWeight: FontWeight.bold,
                          color: barColor,
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 6),
                // Visual Impact Bar
                ClipRRect(
                  borderRadius: BorderRadius.circular(4),
                  child: Container(
                    height: 8,
                    width: double.infinity,
                    color: Colors.grey.shade200,
                    alignment: isPositive ? Alignment.centerLeft : Alignment.centerRight,
                    child: FractionallySizedBox(
                      widthFactor: normWidth,
                      child: Container(
                        decoration: BoxDecoration(
                          color: barColor,
                          borderRadius: BorderRadius.circular(4),
                        ),
                      ),
                    ),
                  ),
                ),
                const SizedBox(height: 6),
                Text(
                  desc,
                  style: TextStyle(
                    fontSize: 12,
                    color: Colors.grey.shade700,
                    height: 1.3,
                  ),
                ),
              ],
            ),
          );
        }),
      ],
    );
  }
}
