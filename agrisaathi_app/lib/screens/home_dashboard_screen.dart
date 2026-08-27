import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/advisory_provider.dart';
import '../providers/weather_provider.dart';
import '../providers/market_provider.dart';
import '../services/sync_manager.dart';
import '../constants/app_colors.dart';
import '../constants/app_strings.dart';
import '../widgets/sync_banner.dart';
import '../widgets/weather_forecast_widget.dart';
import '../widgets/metric_card.dart';
import 'location_soil_input_screen.dart';
import 'recommendation_screen.dart';
import 'explainability_detail_screen.dart';
import 'voice_saathi_screen.dart';
import 'disease_doctor_screen.dart';
import 'offline_demo_screen.dart';
import 'roadmap_schemes_screen.dart';
import 'language_selection_screen.dart';

class HomeDashboardScreen extends StatefulWidget {
  const HomeDashboardScreen({super.key});

  @override
  State<HomeDashboardScreen> createState() => _HomeDashboardScreenState();
}

class _HomeDashboardScreenState extends State<HomeDashboardScreen> {
  int _currentNavIndex = 0;

  @override
  Widget build(BuildContext context) {
    final advisory = context.watch<AdvisoryProvider>();
    final weather = context.watch<WeatherProvider>();
    final market = context.watch<MarketProvider>();
    final syncMgr = context.watch<SyncManager>();

    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: AppBar(
        backgroundColor: AppColors.primary,
        elevation: 0,
        title: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(6),
              decoration: BoxDecoration(
                color: Colors.white.withOpacity(0.2),
                borderRadius: BorderRadius.circular(10),
              ),
              child: const Icon(Icons.eco_rounded, color: Colors.white, size: 20),
            ),
            const SizedBox(width: 10),
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  AppStrings.appName,
                  style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white),
                ),
                Text(
                  AppStrings.appTagline,
                  style: const TextStyle(fontSize: 10, color: AppColors.secondaryLight),
                ),
              ],
            ),
          ],
        ),
        actions: [
          // Language Switcher (Opens 11-Language Selector Modal)
          IconButton(
            tooltip: "Switch Language / भाषा बदलें",
            icon: Container(
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
              decoration: BoxDecoration(
                color: Colors.white.withOpacity(0.2),
                borderRadius: BorderRadius.circular(12),
              ),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Icon(Icons.translate, color: Colors.white, size: 14),
                  const SizedBox(width: 4),
                  Text(
                    AppStrings.isHindi ? "हिन्दी" : "EN",
                    style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 12),
                  ),
                ],
              ),
            ),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => const LanguageSelectionScreen(isModalMode: true),
                ),
              ).then((_) => setState(() {}));
            },
          ),
          // Airplane Mode Demo Toggle
          IconButton(
            tooltip: "Offline / Airplane Mode Demo",
            icon: Icon(
              syncMgr.isSimulatedAirplaneMode ? Icons.airplanemode_active : Icons.airplanemode_inactive,
              color: syncMgr.isSimulatedAirplaneMode ? AppColors.secondaryLight : Colors.white,
            ),
            onPressed: () {
              Navigator.push(context, MaterialPageRoute(builder: (_) => const OfflineDemoScreen()));
            },
          ),
        ],
      ),
      body: Column(
        children: [
          const SyncBanner(),
          Expanded(
            child: RefreshIndicator(
              onRefresh: () async {
                await syncMgr.triggerLiveSync(onSyncCallback: () async {
                  await advisory.fetchRecommendations();
                });
              },
              child: SingleChildScrollView(
                physics: const AlwaysScrollableScrollPhysics(),
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Location Selector Chip
                    _buildLocationSelector(context, advisory),
                    const SizedBox(height: 14),

                    // Weather Forecast Strip
                    if (weather.weather != null)
                      WeatherForecastWidget(weather: weather.weather!)
                    else
                      const Center(child: CircularProgressIndicator()),
                    const SizedBox(height: 18),

                    // Quick Actions Grid (Advisory, Soil Card, Leaf Doctor, Voice)
                    _buildQuickActionsGrid(context),
                    const SizedBox(height: 20),

                    // Top Crop Recommendation Card Preview
                    _buildTopRecommendationPreview(context, advisory),
                    const SizedBox(height: 20),

                    // Market Prices Ticker
                    _buildMarketPriceSection(market),
                    const SizedBox(height: 24),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentNavIndex,
        selectedItemColor: AppColors.primary,
        unselectedItemColor: AppColors.textSecondary,
        backgroundColor: Colors.white,
        type: BottomNavigationBarType.fixed,
        onTap: (idx) {
          setState(() => _currentNavIndex = idx);
          if (idx == 1) {
            Navigator.push(context, MaterialPageRoute(builder: (_) => const RecommendationScreen()));
          } else if (idx == 2) {
            Navigator.push(context, MaterialPageRoute(builder: (_) => const VoiceSaathiScreen()));
          } else if (idx == 3) {
            Navigator.push(context, MaterialPageRoute(builder: (_) => const DiseaseDoctorScreen()));
          } else if (idx == 4) {
            Navigator.push(context, MaterialPageRoute(builder: (_) => const RoadmapSchemesScreen()));
          }
        },
        items: [
          BottomNavigationBarItem(icon: const Icon(Icons.home_rounded), label: AppStrings.home),
          BottomNavigationBarItem(icon: const Icon(Icons.psychology_rounded), label: AppStrings.advisory),
          BottomNavigationBarItem(icon: const Icon(Icons.mic_rounded), label: AppStrings.voiceSaathi),
          BottomNavigationBarItem(icon: const Icon(Icons.healing_rounded), label: AppStrings.leafDoctor),
          BottomNavigationBarItem(icon: const Icon(Icons.account_balance_rounded), label: AppStrings.schemesRoadmap),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        backgroundColor: AppColors.primary,
        child: const Icon(Icons.mic_rounded, color: Colors.white, size: 28),
        onPressed: () {
          Navigator.push(context, MaterialPageRoute(builder: (_) => const VoiceSaathiScreen()));
        },
      ),
    );
  }

  Widget _buildLocationSelector(BuildContext context, AdvisoryProvider advisory) {
    final locationName = AppStrings.isHindi
        ? (advisory.selectedLocation['name_hi'] ?? 'नासिक, महाराष्ट्र')
        : (advisory.selectedLocation['name_en'] ?? 'Nashik, Maharashtra');

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
      decoration: BoxDecoration(
        color: AppColors.surface,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.black.withOpacity(0.06)),
      ),
      child: Row(
        children: [
          const Icon(Icons.location_on_rounded, color: AppColors.primary, size: 22),
          const SizedBox(width: 8),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  locationName,
                  style: const TextStyle(fontSize: 14, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
                ),
                Text(
                  "${advisory.selectedLocation['soil_type']} • ${advisory.farmSizeAcres} Acres",
                  style: const TextStyle(fontSize: 11, color: AppColors.textSecondary),
                ),
              ],
            ),
          ),
          ElevatedButton(
            style: ElevatedButton.styleFrom(
              backgroundColor: AppColors.surfaceElevated,
              foregroundColor: AppColors.primaryDark,
              elevation: 0,
              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
            ),
            onPressed: () {
              Navigator.push(context, MaterialPageRoute(builder: (_) => const LocationSoilInputScreen()));
            },
            child: Text(
              AppStrings.isHindi ? "बदलें" : "Edit",
              style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildQuickActionsGrid(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          AppStrings.isHindi ? "त्वरित सुविधाएं" : "Quick Actions",
          style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
        ),
        const SizedBox(height: 12),
        Row(
          children: [
            Expanded(
              child: MetricCard(
                title: AppStrings.advisory,
                value: AppStrings.isHindi ? "फसल सिफारिश" : "AI Advisory",
                subtitle: "XGBoost + SHAP",
                icon: Icons.psychology_rounded,
                color: Colors.white,
                iconColor: AppColors.primary,
                onTap: () => Navigator.push(context, MaterialPageRoute(builder: (_) => const RecommendationScreen())),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: MetricCard(
                title: AppStrings.leafDoctor,
                value: AppStrings.isHindi ? "पत्ती डॉक्टर" : "Leaf Doctor",
                subtitle: "100% Offline",
                icon: Icons.camera_alt_rounded,
                color: Colors.white,
                iconColor: AppColors.secondary,
                onTap: () => Navigator.push(context, MaterialPageRoute(builder: (_) => const DiseaseDoctorScreen())),
              ),
            ),
          ],
        ),
        const SizedBox(height: 12),
        Row(
          children: [
            Expanded(
              child: MetricCard(
                title: AppStrings.scanSoilCard,
                value: AppStrings.isHindi ? "मृदा कार्ड OCR" : "Soil Card OCR",
                subtitle: "Govt SHC",
                icon: Icons.document_scanner_rounded,
                color: Colors.white,
                iconColor: AppColors.accent,
                onTap: () => Navigator.push(context, MaterialPageRoute(builder: (_) => const LocationSoilInputScreen())),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: MetricCard(
                title: AppStrings.voiceSaathi,
                value: AppStrings.isHindi ? "आवाज साथी" : "Voice Saathi",
                subtitle: "Hindi TTS/STT",
                icon: Icons.mic_rounded,
                color: Colors.white,
                iconColor: Colors.teal,
                onTap: () => Navigator.push(context, MaterialPageRoute(builder: (_) => const VoiceSaathiScreen())),
              ),
            ),
          ],
        ),
      ],
    );
  }

  Widget _buildTopRecommendationPreview(BuildContext context, AdvisoryProvider advisory) {
    if (advisory.isLoading) {
      return Container(
        height: 140,
        decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(20)),
        child: const Center(child: CircularProgressIndicator()),
      );
    }

    final rec = advisory.recommendation;
    if (rec == null || rec.topRecommendations.isEmpty) {
      return const SizedBox.shrink();
    }

    final topCrop = rec.topRecommendations[0];
    final cropTitle = AppStrings.isHindi ? topCrop.cropNameHi : topCrop.cropName;

    return Container(
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [AppColors.primaryDark, AppColors.primary],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(22),
        boxShadow: [
          BoxShadow(
            color: AppColors.primary.withOpacity(0.25),
            blurRadius: 16,
            offset: const Offset(0, 6),
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
                  color: AppColors.secondary,
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Row(
                  children: [
                    const Icon(Icons.star_rounded, color: Colors.white, size: 14),
                    const SizedBox(width: 4),
                    Text(
                      "#1 Ranked Match • ${topCrop.matchScorePct}%",
                      style: const TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Colors.white),
                    ),
                  ],
                ),
              ),
              Text(
                topCrop.scientificName,
                style: const TextStyle(fontSize: 11, fontStyle: FontStyle.italic, color: Colors.white70),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Text(
            cropTitle,
            style: const TextStyle(fontSize: 26, fontWeight: FontWeight.bold, color: Colors.white),
          ),
          const SizedBox(height: 6),
          Text(
            AppStrings.isHindi ? topCrop.whyThisCropHi : topCrop.whyThisCropEn,
            style: const TextStyle(fontSize: 13, color: Colors.white70, height: 1.3),
            maxLines: 2,
            overflow: TextOverflow.ellipsis,
          ),
          const SizedBox(height: 14),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    AppStrings.isHindi ? "अपेक्षित आय / एकड़" : "Est. Revenue / Acre",
                    style: const TextStyle(fontSize: 10, color: Colors.white60),
                  ),
                  Text(
                    topCrop.estimatedRevenue,
                    style: const TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: AppColors.secondaryLight),
                  ),
                ],
              ),
              ElevatedButton.icon(
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.white,
                  foregroundColor: AppColors.primaryDark,
                  elevation: 0,
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                  padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
                ),
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (_) => ExplainabilityDetailScreen(crop: topCrop),
                    ),
                  );
                },
                icon: const Icon(Icons.analytics_rounded, size: 16),
                label: Text(
                  AppStrings.whyThisCrop,
                  style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildMarketPriceSection(MarketProvider market) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Row(
              children: [
                const Icon(Icons.storefront_rounded, color: AppColors.primary, size: 20),
                const SizedBox(width: 8),
                Text(
                  AppStrings.marketMandi,
                  style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
                ),
              ],
            ),
            Text(
              "Agmarknet • ${market.selectedState}",
              style: const TextStyle(fontSize: 11, color: AppColors.textSecondary),
            ),
          ],
        ),
        const SizedBox(height: 12),
        if (market.prices.isEmpty)
          const Center(child: Text("No mandi data available."))
        else
          SizedBox(
            height: 115,
            child: ListView.separated(
              scrollDirection: Axis.horizontal,
              itemCount: market.prices.length,
              separatorBuilder: (_, __) => const SizedBox(width: 10),
              itemBuilder: (context, idx) {
                final item = market.prices[idx];
                final isUp = item.trendDirection == "up";
                final name = AppStrings.isHindi ? item.commodityHi : item.commodity;

                return Container(
                  width: 155,
                  padding: const EdgeInsets.all(12),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(color: Colors.black.withOpacity(0.06)),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Expanded(
                            child: Text(
                              name,
                              style: const TextStyle(fontSize: 14, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
                              overflow: TextOverflow.ellipsis,
                            ),
                          ),
                          Icon(
                            isUp ? Icons.trending_up_rounded : Icons.trending_flat_rounded,
                            color: isUp ? AppColors.success : Colors.grey,
                            size: 18,
                          ),
                        ],
                      ),
                      Text(
                        "₹${item.modalPriceRsQuintal.toInt()} / Qtl",
                        style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: AppColors.primaryDark),
                      ),
                      Text(
                        "${item.marketName} (${item.trendPct7d > 0 ? '+' : ''}${item.trendPct7d}%)",
                        style: TextStyle(fontSize: 10, color: isUp ? AppColors.success : AppColors.textSecondary),
                        overflow: TextOverflow.ellipsis,
                      ),
                    ],
                  ),
                );
              },
            ),
          ),
      ],
    );
  }
}
