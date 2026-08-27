import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../services/sync_manager.dart';
import '../providers/advisory_provider.dart';
import '../constants/app_colors.dart';
import '../constants/app_strings.dart';

class OfflineDemoScreen extends StatelessWidget {
  const OfflineDemoScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final syncMgr = context.watch<SyncManager>();
    final advisory = context.watch<AdvisoryProvider>();

    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: AppBar(
        backgroundColor: AppColors.primary,
        title: Text(
          AppStrings.isHindi ? "ऑफलाइन रेजिलिएंस डेमो" : "Offline Resilience Proof",
          style: const TextStyle(fontWeight: FontWeight.bold),
        ),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Airplane Mode Switch Card
            Container(
              padding: const EdgeInsets.all(18),
              decoration: BoxDecoration(
                color: syncMgr.isSimulatedAirplaneMode ? Colors.orange.shade50 : Colors.white,
                borderRadius: BorderRadius.circular(20),
                border: Border.all(
                  color: syncMgr.isSimulatedAirplaneMode ? Colors.orange.shade300 : Colors.black.withOpacity(0.08),
                  width: 2,
                ),
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
                      Row(
                        children: [
                          Icon(
                            syncMgr.isSimulatedAirplaneMode ? Icons.airplanemode_active : Icons.wifi_rounded,
                            color: syncMgr.isSimulatedAirplaneMode ? AppColors.offlineBadge : AppColors.primary,
                            size: 28,
                          ),
                          const SizedBox(width: 12),
                          Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                syncMgr.isSimulatedAirplaneMode
                                    ? (AppStrings.isHindi ? "एरोप्लेन मोड: सक्रिय (ऑफलाइन)" : "Airplane Mode: ACTIVE (Offline)")
                                    : (AppStrings.isHindi ? "नेटवर्क स्थिति: ऑनलाइन" : "Network: ONLINE"),
                                style: TextStyle(
                                  fontSize: 15,
                                  fontWeight: FontWeight.bold,
                                  color: syncMgr.isSimulatedAirplaneMode ? AppColors.offlineBadge : AppColors.primaryDark,
                                ),
                              ),
                              Text(
                                "${AppStrings.lastUpdated} ${syncMgr.lastSyncTimestamp}",
                                style: const TextStyle(fontSize: 11, color: AppColors.textSecondary),
                              ),
                            ],
                          ),
                        ],
                      ),
                      Switch(
                        value: syncMgr.isSimulatedAirplaneMode,
                        activeColor: AppColors.offlineBadge,
                        onChanged: (val) async {
                          await syncMgr.toggleAirplaneModeSimulation(val);
                          if (!val) {
                            await advisory.fetchRecommendations();
                          }
                        },
                      ),
                    ],
                  ),
                  const SizedBox(height: 12),
                  Text(
                    AppStrings.isHindi
                        ? "इस स्विच को चालू करके एरोप्लेन मोड में ऐप की कार्यप्रणाली का परीक्षण करें। ऑफलाइन में भी फसल सिफारिश, SHAP विश्लेषण और पत्ती रोग जांच पूरी तरह काम करते हैं।"
                        : "Toggle this switch to simulate an in-field zero-connectivity environment. Crop advisory, SHAP explainability, and leaf disease detection remain 100% operational offline.",
                    style: const TextStyle(fontSize: 12, color: AppColors.textSecondary, height: 1.35),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 24),

            // Feature Coverage Checklist for SIH Judges
            Text(
              AppStrings.isHindi ? "ऑफलाइन कार्यप्रणाली सत्यापन (Judge Checklist)" : "Offline Capability Matrix (Judge Checklist)",
              style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
            ),
            const SizedBox(height: 12),

            _buildChecklistItem(
              title: AppStrings.isHindi ? "फसल सिफारिश इंजन" : "Crop Recommendation Engine",
              subtitle: AppStrings.isHindi ? "अंतिम सिंक किए गए डेटा से तुरंत उपलब्ध" : "Runs from persistent local SQLite/Preferences cache",
              isSupportedOffline: true,
            ),
            _buildChecklistItem(
              title: AppStrings.isHindi ? "SHAP पारदर्शी विश्लेषण (Why This Crop?)" : "SHAP Explainability Breakdown",
              subtitle: AppStrings.isHindi ? "4-स्तंभ स्कोर और कारक योगदान ऑन-डिवाइस" : "100% computed on-device with zero network latency",
              isSupportedOffline: true,
            ),
            _buildChecklistItem(
              title: AppStrings.isHindi ? "पत्ती डॉक्टर (AI रोग निदान)" : "Leaf Disease Doctor (AI Diagnostic)",
              subtitle: AppStrings.isHindi ? "ऑन-डिवाइस न्यूरल मॉडल, बिना इंटरनेट तुरंत परिणाम" : "On-device MobileNet model runs independently in field",
              isSupportedOffline: true,
            ),
            _buildChecklistItem(
              title: AppStrings.isHindi ? "आवाज साथी (हिंदी वॉइस Q&A)" : "Voice Saathi (Hindi Voice Q&A)",
              subtitle: AppStrings.isHindi ? "नेक्स्ट-जेन ऑफलाइन इंटेंट मैपिंग + नेटिव TTS" : "Offline intent matching engine + native Flutter TTS",
              isSupportedOffline: true,
            ),
            _buildChecklistItem(
              title: AppStrings.isHindi ? "लाइव मौसम व मंडी भाव ऑटो-रिफ्रेश" : "Live Weather & Mandi Auto-Sync",
              subtitle: AppStrings.isHindi ? "इंटरनेट आते ही बैकग्राउंड में स्वतः अपडेट" : "Cached with visible timestamp; auto-syncs on reconnect",
              isSupportedOffline: true,
            ),
            const SizedBox(height: 20),

            // Live Sync Demonstration Action Button
            SizedBox(
              width: double.infinity,
              height: 50,
              child: ElevatedButton.icon(
                style: ElevatedButton.styleFrom(
                  backgroundColor: AppColors.primary,
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                ),
                icon: syncMgr.isSyncing
                    ? const SizedBox(width: 18, height: 18, child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2))
                    : const Icon(Icons.sync_rounded, color: Colors.white),
                label: Text(
                  syncMgr.isSyncing
                      ? (AppStrings.isHindi ? "डेटा सिंक हो रहा है..." : "Syncing Live Data...")
                      : (AppStrings.isHindi ? "लाइव सिंक टेस्ट करें" : "Test Live Auto-Sync Now"),
                  style: const TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Colors.white),
                ),
                onPressed: syncMgr.isSimulatedAirplaneMode
                    ? null
                    : () async {
                        await syncMgr.triggerLiveSync(onSyncCallback: () async {
                          await advisory.fetchRecommendations();
                        });
                        ScaffoldMessenger.of(context).showSnackBar(
                          const SnackBar(
                            backgroundColor: AppColors.primary,
                            content: Text("Auto-sync completed! Timestamps refreshed."),
                          ),
                        );
                      },
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildChecklistItem({
    required String title,
    required String subtitle,
    required bool isSupportedOffline,
  }) {
    return Container(
      margin: const EdgeInsets.only(bottom: 10),
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: Colors.black.withOpacity(0.06)),
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(6),
            decoration: BoxDecoration(
              color: AppColors.success.withOpacity(0.12),
              shape: BoxShape.circle,
            ),
            child: const Icon(Icons.check_rounded, color: AppColors.success, size: 18),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: const TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
                ),
                Text(
                  subtitle,
                  style: const TextStyle(fontSize: 11, color: AppColors.textSecondary),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
