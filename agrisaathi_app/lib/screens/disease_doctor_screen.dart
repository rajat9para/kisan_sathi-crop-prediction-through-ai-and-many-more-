import 'package:flutter/material.dart';
import '../services/disease_detector.dart';
import '../models/disease_result.dart';
import '../constants/app_colors.dart';
import '../constants/app_strings.dart';
import '../constants/demo_constants.dart';

class DiseaseDoctorScreen extends StatefulWidget {
  const DiseaseDoctorScreen({super.key});

  @override
  State<DiseaseDoctorScreen> createState() => _DiseaseDoctorScreenState();
}

class _DiseaseDoctorScreenState extends State<DiseaseDoctorScreen> {
  DiseaseDiagnosis? _currentDiagnosis;
  bool _isAnalyzing = false;
  int _selectedSampleIdx = 0;

  @override
  void initState() {
    super.initState();
    _runDiagnosis(0);
  }

  Future<void> _runDiagnosis(int index) async {
    setState(() {
      _selectedSampleIdx = index;
      _isAnalyzing = true;
    });

    final res = await DiseaseDetector.diagnoseLeaf(sampleIndex: index);

    if (mounted) {
      setState(() {
        _currentDiagnosis = res;
        _isAnalyzing = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    final diag = _currentDiagnosis;
    final diseaseTitle = AppStrings.isHindi
        ? (diag?.diseaseNameHi ?? "रोग की पहचान")
        : (diag?.diseaseNameEn ?? "Leaf Diagnosis");

    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: AppBar(
        backgroundColor: AppColors.primary,
        title: Text(
          AppStrings.leafDoctor,
          style: const TextStyle(fontWeight: FontWeight.bold),
        ),
        actions: [
          Container(
            margin: const EdgeInsets.only(right: 14),
            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.2),
              borderRadius: BorderRadius.circular(12),
            ),
            child: Row(
              mainAxisSize: MainAxisSize.min,
              children: const [
                Icon(Icons.wifi_off_rounded, size: 14, color: Colors.white),
                SizedBox(width: 4),
                Text(
                  "100% On-Device",
                  style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: Colors.white),
                ),
              ],
            ),
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Sample Leaf Selector Cards (for instant testing during Demo)
            Text(
              AppStrings.isHindi ? "पत्ती का नमूना चुनें या फोटो लें" : "Select Sample Leaf or Take Photo",
              style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
            ),
            const SizedBox(height: 12),
            SizedBox(
              height: 80,
              child: ListView.separated(
                scrollDirection: Axis.horizontal,
                itemCount: DemoConstants.leafDiseaseSamples.length,
                separatorBuilder: (_, __) => const SizedBox(width: 10),
                itemBuilder: (context, idx) {
                  final sample = DemoConstants.leafDiseaseSamples[idx];
                  final isSelected = _selectedSampleIdx == idx;

                  return InkWell(
                    onTap: () => _runDiagnosis(idx),
                    borderRadius: BorderRadius.circular(14),
                    child: Container(
                      width: 130,
                      padding: const EdgeInsets.all(10),
                      decoration: BoxDecoration(
                        color: isSelected ? AppColors.primary : Colors.white,
                        borderRadius: BorderRadius.circular(14),
                        border: Border.all(
                          color: isSelected ? AppColors.primary : Colors.black.withOpacity(0.08),
                          width: isSelected ? 2 : 1,
                        ),
                      ),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(
                            Icons.eco_rounded,
                            color: isSelected ? Colors.white : AppColors.primary,
                            size: 20,
                          ),
                          const SizedBox(height: 4),
                          Text(
                            sample['crop'] ?? '',
                            style: TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.bold,
                              color: isSelected ? Colors.white : AppColors.textPrimary,
                            ),
                            maxLines: 1,
                            overflow: TextOverflow.ellipsis,
                          ),
                        ],
                      ),
                    ),
                  );
                },
              ),
            ),
            const SizedBox(height: 20),

            // Camera / Scan Trigger Button
            SizedBox(
              width: double.infinity,
              height: 48,
              child: ElevatedButton.icon(
                style: ElevatedButton.styleFrom(
                  backgroundColor: AppColors.secondary,
                  foregroundColor: Colors.white,
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                  elevation: 1,
                ),
                icon: const Icon(Icons.camera_alt_rounded, size: 20),
                label: Text(
                  AppStrings.isHindi ? "कैमरा से नई पत्ती स्कैन करें" : "Scan Leaf via Camera",
                  style: const TextStyle(fontSize: 14, fontWeight: FontWeight.bold),
                ),
                onPressed: () => _runDiagnosis((_selectedSampleIdx + 1) % DemoConstants.leafDiseaseSamples.length),
              ),
            ),
            const SizedBox(height: 20),

            // Diagnosis Result Card
            if (_isAnalyzing)
              Container(
                height: 200,
                decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(20)),
                child: const Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      CircularProgressIndicator(color: AppColors.primary),
                      SizedBox(height: 12),
                      Text("On-device MobileNet Neural Inference...", style: TextStyle(color: AppColors.textSecondary)),
                    ],
                  ),
                ),
              )
            else if (diag != null) ...[
              Container(
                padding: const EdgeInsets.all(18),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(color: Colors.black.withOpacity(0.06)),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black.withOpacity(0.04),
                      blurRadius: 10,
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
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                          decoration: BoxDecoration(
                            color: AppColors.surfaceElevated,
                            borderRadius: BorderRadius.circular(10),
                          ),
                          child: Text(
                            diag.crop,
                            style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: AppColors.primaryDark),
                          ),
                        ),
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                          decoration: BoxDecoration(
                            color: AppColors.success.withOpacity(0.12),
                            borderRadius: BorderRadius.circular(10),
                          ),
                          child: Text(
                            "${diag.confidencePct}% Confidence",
                            style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: AppColors.success),
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 14),
                    Text(
                      diseaseTitle,
                      style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      "Severity: ${diag.severity}",
                      style: const TextStyle(fontSize: 12, color: AppColors.warning, fontWeight: FontWeight.w600),
                    ),
                    const SizedBox(height: 16),
                    const Divider(height: 1),
                    const SizedBox(height: 16),

                    // Organic Treatment Plan
                    _buildRemedyCard(
                      title: AppStrings.isHindi ? "जैविक उपचार (Organic Remedy)" : "Organic Treatment",
                      desc: AppStrings.isHindi ? diag.organicRemedyHi : diag.organicRemedyEn,
                      icon: Icons.eco_rounded,
                      color: AppColors.primary,
                    ),
                    const SizedBox(height: 12),

                    // Chemical Treatment Plan
                    _buildRemedyCard(
                      title: AppStrings.isHindi ? "रासायनिक उपचार (Chemical Remedy)" : "Chemical Treatment",
                      desc: AppStrings.isHindi ? diag.chemicalRemedyHi : diag.chemicalRemedyEn,
                      icon: Icons.science_rounded,
                      color: AppColors.accent,
                    ),
                  ],
                ),
              ),
            ],
          ],
        ),
      ),
    );
  }

  Widget _buildRemedyCard({
    required String title,
    required String desc,
    required IconData icon,
    required Color color,
  }) {
    return Container(
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: color.withOpacity(0.05),
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: color.withOpacity(0.2)),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Icon(icon, color: color, size: 22),
          const SizedBox(width: 10),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: color),
                ),
                const SizedBox(height: 4),
                Text(
                  desc,
                  style: const TextStyle(fontSize: 12, color: AppColors.textPrimary, height: 1.35),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
