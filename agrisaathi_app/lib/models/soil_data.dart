class SoilData {
  final double latitude;
  final double longitude;
  final String source;
  final double ph;
  final double nitrogen;
  final double phosphorus;
  final double potassium;
  final double organicCarbonPct;
  final double clayContentPct;
  final double sandContentPct;
  final String soilType;

  SoilData({
    required this.latitude,
    required this.longitude,
    required this.source,
    required this.ph,
    required this.nitrogen,
    required this.phosphorus,
    required this.potassium,
    required this.organicCarbonPct,
    required this.clayContentPct,
    required this.sandContentPct,
    required this.soilType,
  });

  factory SoilData.fromJson(Map<String, dynamic> json) {
    return SoilData(
      latitude: (json['latitude'] as num?)?.toDouble() ?? 0.0,
      longitude: (json['longitude'] as num?)?.toDouble() ?? 0.0,
      source: json['source'] ?? 'SoilGrids v2.0',
      ph: (json['ph'] as num?)?.toDouble() ?? 6.8,
      nitrogen: (json['nitrogen'] as num?)?.toDouble() ?? 75.0,
      phosphorus: (json['phosphorus'] as num?)?.toDouble() ?? 45.0,
      potassium: (json['potassium'] as num?)?.toDouble() ?? 50.0,
      organicCarbonPct: (json['organic_carbon_pct'] as num?)?.toDouble() ?? 0.65,
      clayContentPct: (json['clay_content_pct'] as num?)?.toDouble() ?? 35.0,
      sandContentPct: (json['sand_content_pct'] as num?)?.toDouble() ?? 30.0,
      soilType: json['soil_type'] ?? 'Clay Loam',
    );
  }

  Map<String, dynamic> toJson() => {
    'latitude': latitude,
    'longitude': longitude,
    'source': source,
    'ph': ph,
    'nitrogen': nitrogen,
    'phosphorus': phosphorus,
    'potassium': potassium,
    'organic_carbon_pct': organicCarbonPct,
    'clay_content_pct': clayContentPct,
    'sand_content_pct': sandContentPct,
    'soil_type': soilType,
  };
}
