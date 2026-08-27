class DiseaseDiagnosis {
  final String crop;
  final String diseaseNameEn;
  final String diseaseNameHi;
  final String severity;
  final double confidencePct;
  final String organicRemedyEn;
  final String organicRemedyHi;
  final String chemicalRemedyEn;
  final String chemicalRemedyHi;
  final String diagnosedTimestamp;

  DiseaseDiagnosis({
    required this.crop,
    required this.diseaseNameEn,
    required this.diseaseNameHi,
    required this.severity,
    required this.confidencePct,
    required this.organicRemedyEn,
    required this.organicRemedyHi,
    required this.chemicalRemedyEn,
    required this.chemicalRemedyHi,
    required this.diagnosedTimestamp,
  });

  factory DiseaseDiagnosis.fromJson(Map<String, dynamic> json) {
    return DiseaseDiagnosis(
      crop: json['crop'] ?? '',
      diseaseNameEn: json['disease_name_en'] ?? '',
      diseaseNameHi: json['disease_name_hi'] ?? '',
      severity: json['severity'] ?? 'Moderate',
      confidencePct: (json['confidence'] as num?)?.toDouble() ?? 95.0,
      organicRemedyEn: json['organic_remedy_en'] ?? '',
      organicRemedyHi: json['organic_remedy_hi'] ?? '',
      chemicalRemedyEn: json['chemical_remedy_en'] ?? '',
      chemicalRemedyHi: json['chemical_remedy_hi'] ?? '',
      diagnosedTimestamp: json['timestamp'] ?? DateTime.now().toString(),
    );
  }

  Map<String, dynamic> toJson() => {
    'crop': crop,
    'disease_name_en': diseaseNameEn,
    'disease_name_hi': diseaseNameHi,
    'severity': severity,
    'confidence': confidencePct,
    'organic_remedy_en': organicRemedyEn,
    'organic_remedy_hi': organicRemedyHi,
    'chemical_remedy_en': chemicalRemedyEn,
    'chemical_remedy_hi': chemicalRemedyHi,
    'timestamp': diagnosedTimestamp,
  };
}
