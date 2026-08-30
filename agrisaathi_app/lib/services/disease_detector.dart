import 'dart:convert';
import 'dart:typed_data';
import 'package:http/http.dart' as http;
import '../models/disease_result.dart';
import '../constants/demo_constants.dart';
import 'offline_storage.dart';
import 'sync_manager.dart';

class DiseaseDetector {
  static Future<DiseaseDiagnosis> diagnoseLeaf({
    String? imagePath,
    Uint8List? imageBytes,
    String? cropHint,
    int sampleIndex = 0,
  }) async {
    final syncMgr = SyncManager();

    // 1. If online and image is provided, run real PyTorch MobileNetV2 inference via API
    if (syncMgr.isOnline && (imageBytes != null || imagePath != null)) {
      try {
        String base64Image = "";
        if (imageBytes != null) {
          base64Image = base64Encode(imageBytes);
        }

        final response = await http
            .post(
              Uri.parse('${DemoConstants.backendBaseUrl}/api/doctor/diagnose'),
              headers: {'Content-Type': 'application/json'},
              body: jsonEncode({
                "image_base64": base64Image,
                "crop_hint": cropHint,
                "language": "hi",
              }),
            )
            .timeout(const Duration(seconds: 5));

        if (response.statusCode == 200) {
          final data = jsonDecode(response.body);
          if (data['error'] != true) {
            final diag = DiseaseDiagnosis(
              crop: data['crop_name_en'] ?? 'Crop',
              diseaseNameEn: data['disease_name_en'] ?? 'Diagnosed Pathology',
              diseaseNameHi: data['disease_name_hi'] ?? 'पहचाना गया रोग',
              severity: data['severity'] ?? 'Moderate',
              confidencePct: (data['confidence_pct'] as num?)?.toDouble() ?? 94.0,
              organicRemedyEn: data['organic_remedy_en'] ?? data['organic_remedy'] ?? '',
              organicRemedyHi: data['organic_remedy_hi'] ?? '',
              chemicalRemedyEn: data['chemical_remedy_en'] ?? data['chemical_remedy'] ?? '',
              chemicalRemedyHi: data['chemical_remedy_hi'] ?? '',
              diagnosedTimestamp: DateTime.now().toString(),
            );
            await OfflineStorage.saveDiseaseDiagnosis(diag);
            return diag;
          }
        }
      } catch (e) {
        print('Live Plant Doctor API error: $e. Falling back to offline engine.');
      }
    }

    // 2. Offline / Preset Demo Sample Fallback
    await Future.delayed(const Duration(milliseconds: 250));
    final sample = DemoConstants.leafDiseaseSamples[sampleIndex % DemoConstants.leafDiseaseSamples.length];

    final diag = DiseaseDiagnosis(
      crop: sample['crop'] ?? 'Tomato',
      diseaseNameEn: sample['disease_name_en'] ?? 'Early Blight',
      diseaseNameHi: sample['disease_name_hi'] ?? 'अगेती झुलसा रोग',
      severity: sample['severity'] ?? 'Moderate',
      confidencePct: (sample['confidence'] as num?)?.toDouble() ?? 95.0,
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
