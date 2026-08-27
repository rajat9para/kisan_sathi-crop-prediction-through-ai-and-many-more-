import '../models/disease_result.dart';
import '../constants/demo_constants.dart';
import 'offline_storage.dart';

class DiseaseDetector {
  static Future<DiseaseDiagnosis> diagnoseLeaf({
    String? imagePath,
    int sampleIndex = 0,
  }) async {
    // On-device simulated TFLite inference latency (350ms)
    await Future.delayed(const Duration(milliseconds: 350));

    final sample = DemoConstants.leafDiseaseSamples[sampleIndex % DemoConstants.leafDiseaseSamples.length];

    final diag = DiseaseDiagnosis(
      crop: sample['crop'] ?? 'Tomato',
      diseaseNameEn: sample['disease_name_en'] ?? 'Early Blight',
      diseaseNameHi: sample['disease_name_hi'] ?? 'अगेती झुलसा रोग',
      severity: sample['severity'] ?? 'Moderate',
      confidencePct: (sample['confidence'] as num?)?.toDouble() ?? 96.0,
      organicRemedyEn: sample['organic_remedy_en'] ?? '',
      organicRemedyHi: sample['organic_remedy_hi'] ?? '',
      chemicalRemedyEn: sample['chemical_remedy_en'] ?? '',
      chemicalRemedyHi: sample['chemical_remedy_hi'] ?? '',
      diagnosedTimestamp: DateTime.now().toString(),
    );

    // Save to local offline history
    await OfflineStorage.saveDiseaseDiagnosis(diag);
    return diag;
  }
}
