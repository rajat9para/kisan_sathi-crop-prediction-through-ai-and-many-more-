class ShapFeature {
  final String feature;
  final String featureNameHi;
  final double impactScore;
  final String explanationEn;
  final String explanationHi;
  final String status; // positive, neutral, negative

  ShapFeature({
    required this.feature,
    required this.featureNameHi,
    required this.impactScore,
    required this.explanationEn,
    required this.explanationHi,
    required this.status,
  });

  factory ShapFeature.fromJson(Map<String, dynamic> json) {
    return ShapFeature(
      feature: json['feature'] ?? '',
      featureNameHi: json['feature_name_hi'] ?? '',
      impactScore: (json['impact_score'] as num?)?.toDouble() ?? 0.0,
      explanationEn: json['farmer_explanation_en'] ?? '',
      explanationHi: json['farmer_explanation_hi'] ?? '',
      status: json['status'] ?? 'neutral',
    );
  }

  Map<String, dynamic> toJson() => {
    'feature': feature,
    'feature_name_hi': featureNameHi,
    'impact_score': impactScore,
    'farmer_explanation_en': explanationEn,
    'farmer_explanation_hi': explanationHi,
    'status': status,
  };
}

class CropItem {
  final int rank;
  final String cropName;
  final String cropNameHi;
  final String scientificName;
  final double matchScorePct;
  final double baseMlConfidencePct;
  final double soilFitPct;
  final double weatherFitPct;
  final double marketProfitabilityPct;
  final double rotationImpactPct;
  final String expectedYield;
  final String estimatedRevenue;
  final double estimatedCostPerAcre;
  final double estimatedNetProfitPerAcre;
  final String mandiPrice;
  final String priceTrend;
  final String waterRequirement;
  final String sowingWindowEn;
  final String sowingWindowHi;
  final int harvestDurationDays;
  final double sustainabilityScorePct;
  final String sustainabilityRating;
  final String whyThisCropEn;
  final String whyThisCropHi;
  final List<ShapFeature> shapContributions;
  final List<Map<String, String>> fertilizerSchedule;
  final List<Map<String, String>> irrigationSchedule;

  CropItem({
    required this.rank,
    required this.cropName,
    required this.cropNameHi,
    required this.scientificName,
    required this.matchScorePct,
    required this.baseMlConfidencePct,
    required this.soilFitPct,
    required this.weatherFitPct,
    required this.marketProfitabilityPct,
    required this.rotationImpactPct,
    required this.expectedYield,
    required this.estimatedRevenue,
    this.estimatedCostPerAcre = 22000.0,
    this.estimatedNetProfitPerAcre = 55000.0,
    required this.mandiPrice,
    required this.priceTrend,
    required this.waterRequirement,
    required this.sowingWindowEn,
    required this.sowingWindowHi,
    required this.harvestDurationDays,
    this.sustainabilityScorePct = 85.0,
    this.sustainabilityRating = "High (Eco-Friendly)",
    required this.whyThisCropEn,
    required this.whyThisCropHi,
    required this.shapContributions,
    required this.fertilizerSchedule,
    required this.irrigationSchedule,
  });

  factory CropItem.fromJson(Map<String, dynamic> json) {
    List<ShapFeature> shaps = [];
    if (json['shap_contributions'] != null) {
      shaps = (json['shap_contributions'] as List)
          .map((e) => ShapFeature.fromJson(e as Map<String, dynamic>))
          .toList();
    }

    List<Map<String, String>> fert = [];
    if (json['recommended_fertilizer_schedule'] != null) {
      fert = (json['recommended_fertilizer_schedule'] as List)
          .map((e) => Map<String, String>.from(e as Map))
          .toList();
    }

    List<Map<String, String>> irrig = [];
    if (json['irrigation_schedule'] != null) {
      irrig = (json['irrigation_schedule'] as List)
          .map((e) => Map<String, String>.from(e as Map))
          .toList();
    }

    return CropItem(
      rank: json['rank'] ?? 1,
      cropName: json['crop_name'] ?? '',
      cropNameHi: json['crop_name_hi'] ?? '',
      scientificName: json['scientific_name'] ?? '',
      matchScorePct: (json['match_score_pct'] as num?)?.toDouble() ?? 85.0,
      baseMlConfidencePct: (json['base_ml_confidence_pct'] as num?)?.toDouble() ?? 80.0,
      soilFitPct: (json['soil_fit_pct'] as num?)?.toDouble() ?? 85.0,
      weatherFitPct: (json['weather_fit_pct'] as num?)?.toDouble() ?? 85.0,
      marketProfitabilityPct: (json['market_profitability_pct'] as num?)?.toDouble() ?? 85.0,
      rotationImpactPct: (json['rotation_impact_pct'] as num?)?.toDouble() ?? 85.0,
      expectedYield: json['expected_yield_per_acre'] ?? '',
      estimatedRevenue: json['estimated_revenue_per_acre'] ?? '',
      estimatedCostPerAcre: (json['estimated_cost_per_acre_rs'] as num?)?.toDouble() ?? 22000.0,
      estimatedNetProfitPerAcre: (json['estimated_net_profit_per_acre_rs'] as num?)?.toDouble() ?? 55000.0,
      mandiPrice: json['mandi_price_per_quintal'] ?? '',
      priceTrend: json['price_trend'] ?? 'stable',
      waterRequirement: json['water_requirement_level'] ?? 'Medium',
      sowingWindowEn: json['sowing_window'] ?? '',
      sowingWindowHi: json['sowing_window_hi'] ?? '',
      harvestDurationDays: json['harvest_duration_days'] ?? 120,
      sustainabilityScorePct: (json['sustainability_score_pct'] as num?)?.toDouble() ?? 85.0,
      sustainabilityRating: json['sustainability_rating'] ?? 'High (Eco-Friendly)',
      whyThisCropEn: json['why_this_crop_summary_en'] ?? '',
      whyThisCropHi: json['why_this_crop_summary_hi'] ?? '',
      shapContributions: shaps,
      fertilizerSchedule: fert,
      irrigationSchedule: irrig,
    );
  }

  Map<String, dynamic> toJson() => {
    'rank': rank,
    'crop_name': cropName,
    'crop_name_hi': cropNameHi,
    'scientific_name': scientificName,
    'match_score_pct': matchScorePct,
    'base_ml_confidence_pct': baseMlConfidencePct,
    'soil_fit_pct': soilFitPct,
    'weather_fit_pct': weatherFitPct,
    'market_profitability_pct': marketProfitabilityPct,
    'rotation_impact_pct': rotationImpactPct,
    'expected_yield_per_acre': expectedYield,
    'estimated_revenue_per_acre': estimatedRevenue,
    'estimated_cost_per_acre_rs': estimatedCostPerAcre,
    'estimated_net_profit_per_acre_rs': estimatedNetProfitPerAcre,
    'mandi_price_per_quintal': mandiPrice,
    'price_trend': priceTrend,
    'water_requirement_level': waterRequirement,
    'sowing_window': sowingWindowEn,
    'sowing_window_hi': sowingWindowHi,
    'harvest_duration_days': harvestDurationDays,
    'sustainability_score_pct': sustainabilityScorePct,
    'sustainability_rating': sustainabilityRating,
    'why_this_crop_summary_en': whyThisCropEn,
    'why_this_crop_summary_hi': whyThisCropHi,
    'shap_contributions': shapContributions.map((e) => e.toJson()).toList(),
    'recommended_fertilizer_schedule': fertilizerSchedule,
    'irrigation_schedule': irrigationSchedule,
  };
}

class RecommendationResult {
  final String timestamp;
  final bool isCachedDemoLocation;
  final Map<String, dynamic> location;
  final Map<String, dynamic> soilSnapshot;
  final Map<String, dynamic> weatherSnapshot;
  final List<CropItem> topRecommendations;
  final List<Map<String, String>> advisoryWarnings;

  RecommendationResult({
    required this.timestamp,
    required this.isCachedDemoLocation,
    required this.location,
    required this.soilSnapshot,
    required this.weatherSnapshot,
    required this.topRecommendations,
    required this.advisoryWarnings,
  });

  factory RecommendationResult.fromJson(Map<String, dynamic> json) {
    List<CropItem> crops = [];
    if (json['top_recommendations'] != null) {
      crops = (json['top_recommendations'] as List)
          .map((e) => CropItem.fromJson(e as Map<String, dynamic>))
          .toList();
    }

    List<Map<String, String>> warnings = [];
    if (json['advisory_warnings'] != null) {
      warnings = (json['advisory_warnings'] as List)
          .map((e) => Map<String, String>.from(e as Map))
          .toList();
    }

    return RecommendationResult(
      timestamp: json['timestamp'] ?? '',
      isCachedDemoLocation: json['is_cached_demo_location'] ?? false,
      location: Map<String, dynamic>.from(json['location'] ?? {}),
      soilSnapshot: Map<String, dynamic>.from(json['soil_snapshot'] ?? {}),
      weatherSnapshot: Map<String, dynamic>.from(json['weather_snapshot'] ?? {}),
      topRecommendations: crops,
      advisoryWarnings: warnings,
    );
  }

  Map<String, dynamic> toJson() => {
    'timestamp': timestamp,
    'is_cached_demo_location': isCachedDemoLocation,
    'location': location,
    'soil_snapshot': soilSnapshot,
    'weather_snapshot': weatherSnapshot,
    'top_recommendations': topRecommendations.map((e) => e.toJson()).toList(),
    'advisory_warnings': advisoryWarnings,
  };
}
