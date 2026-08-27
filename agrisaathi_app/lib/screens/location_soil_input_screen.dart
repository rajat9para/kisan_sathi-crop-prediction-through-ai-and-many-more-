import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/advisory_provider.dart';
import '../services/api_service.dart';
import '../constants/app_colors.dart';
import '../constants/app_strings.dart';
import '../constants/demo_constants.dart';

class LocationSoilInputScreen extends StatefulWidget {
  const LocationSoilInputScreen({super.key});

  @override
  State<LocationSoilInputScreen> createState() => _LocationSoilInputScreenState();
}

class _LocationSoilInputScreenState extends State<LocationSoilInputScreen> {
  // Soil Sliders
  double _n = 85.0;
  double _p = 48.0;
  double _k = 190.0;
  double _ph = 6.8;
  double _oc = 0.72;
  String _texture = "Clay Loam";

  // Farm Parameters
  double _acres = 2.5;
  String _irrigation = "Borewell";
  String _previousCrop = "Cotton";
  bool _isOcrLoading = false;

  final List<String> _irrigationOptions = ["Borewell", "Rainfed", "Canal", "Drip"];
  final List<String> _cropOptions = ["None / Fallow", "Cotton", "Rice", "Maize", "Soybean", "Chickpea", "Wheat", "Sugarcane"];

  @override
  void initState() {
    super.initState();
    final adv = context.read<AdvisoryProvider>();
    _acres = adv.farmSizeAcres;
    _irrigation = adv.irrigationSource;
    _previousCrop = adv.previousCrop ?? "Cotton";

    if (adv.customSoilOverride != null) {
      final s = adv.customSoilOverride!;
      _n = (s['nitrogen'] as num?)?.toDouble() ?? _n;
      _p = (s['phosphorus'] as num?)?.toDouble() ?? _p;
      _k = (s['potassium'] as num?)?.toDouble() ?? _k;
      _ph = (s['ph'] as num?)?.toDouble() ?? _ph;
      _oc = (s['organic_carbon_pct'] as num?)?.toDouble() ?? _oc;
    }
  }

  Future<void> _scanPresetSoilCard(String presetId, String cardTitle) async {
    setState(() => _isOcrLoading = true);
    try {
      final res = await ApiService.parseSoilCardPreset(presetId);
      final p = res['parameters'];
      setState(() {
        _n = (p['nitrogen'] as num).toDouble();
        _p = (p['phosphorus'] as num).toDouble();
        _k = (p['potassium'] as num).toDouble();
        _ph = (p['ph'] as num).toDouble();
        _oc = (p['organic_carbon_pct'] as num).toDouble();
        _texture = p['texture'] ?? "Clay Loam";
        _useCustomSoil = true;
      });

      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            backgroundColor: AppColors.primary,
            content: Text("Soil Health Card parsed: ${res['farmer_name']}"),
          ),
        );
      }
    } finally {
      if (mounted) setState(() => _isOcrLoading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    final advisory = context.watch<AdvisoryProvider>();

    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: AppBar(
        backgroundColor: AppColors.primary,
        title: Text(
          AppStrings.isHindi ? "खेत का स्थान व मृदा विवरण" : "Farm Location & Soil Data",
          style: const TextStyle(fontWeight: FontWeight.bold),
        ),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // 1. Location Hub Selector
            Text(
              AppStrings.isHindi ? "1. खेत का स्थान चुनें (डेमो हब)" : "1. Select Farm Location (Demo Hub)",
              style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
            ),
            const SizedBox(height: 10),
            Wrap(
              spacing: 8,
              runSpacing: 8,
              children: DemoConstants.demoLocations.map((loc) {
                final isSelected = advisory.selectedLocation['id'] == loc['id'];
                final label = AppStrings.isHindi ? loc['name_hi'] : loc['name_en'];

                return ChoiceChip(
                  label: Text(label),
                  selected: isSelected,
                  selectedColor: AppColors.primary,
                  labelStyle: TextStyle(
                    color: isSelected ? Colors.white : AppColors.textPrimary,
                    fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                  ),
                  onSelected: (selected) {
                    if (selected) {
                      advisory.setLocation(loc);
                    }
                  },
                );
              }).toList(),
            ),
            const SizedBox(height: 20),

            // 2. Soil Health Card OCR Quick Presets
            Container(
              padding: const EdgeInsets.all(14),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(16),
                border: Border.all(color: Colors.black.withOpacity(0.06)),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Row(
                        children: [
                          const Icon(Icons.document_scanner_rounded, color: AppColors.accent, size: 20),
                          const SizedBox(width: 8),
                          Text(
                            AppStrings.isHindi ? "मृदा स्वास्थ्य कार्ड (SHC OCR)" : "Soil Health Card (SHC OCR)",
                            style: const TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
                          ),
                        ],
                      ),
                      if (_isOcrLoading)
                        const SizedBox(width: 16, height: 16, child: CircularProgressIndicator(strokeWidth: 2)),
                    ],
                  ),
                  const SizedBox(height: 6),
                  Text(
                    AppStrings.isHindi
                        ? "सरकारी मृदा कार्ड के आधार पर एन-पी-के और पीएच मान स्वतः भरें:"
                        : "Auto-fill NPK and pH values from a government Soil Health Card:",
                    style: const TextStyle(fontSize: 12, color: AppColors.textSecondary),
                  ),
                  const SizedBox(height: 12),
                  ...DemoConstants.sampleSoilCards.map((card) {
                    return Container(
                      margin: const EdgeInsets.only(bottom: 8),
                      child: OutlinedButton.icon(
                        style: OutlinedButton.styleFrom(
                          foregroundColor: AppColors.primaryDark,
                          alignment: Alignment.centerLeft,
                          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                        ),
                        icon: const Icon(Icons.description_outlined, size: 16, color: AppColors.primary),
                        label: Text(
                          "${card['title']} (${card['farmer']})",
                          style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w600),
                        ),
                        onPressed: () => _scanPresetSoilCard(card['id'], card['title']),
                      ),
                    );
                  }),
                ],
              ),
            ),
            const SizedBox(height: 20),

            // 3. Soil Parameter Sliders (N, P, K, pH)
            Text(
              AppStrings.isHindi ? "2. पोषक तत्व मान (संशोधन करें)" : "2. Soil Nutrients (Adjust Values)",
              style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
            ),
            const SizedBox(height: 10),
            _buildSlider(
              label: AppStrings.isHindi ? "नाइट्रोजन (N)" : "Nitrogen (N)",
              value: _n,
              min: 10,
              max: 160,
              unit: "kg/ha",
              onChanged: (v) => setState(() => _n = v),
            ),
            _buildSlider(
              label: AppStrings.isHindi ? "फास्फोरस (P)" : "Phosphorus (P)",
              value: _p,
              min: 5,
              max: 160,
              unit: "kg/ha",
              onChanged: (v) => setState(() => _p = v),
            ),
            _buildSlider(
              label: AppStrings.isHindi ? "पोटाश (K)" : "Potassium (K)",
              value: _k,
              min: 5,
              max: 220,
              unit: "kg/ha",
              onChanged: (v) => setState(() => _k = v),
            ),
            _buildSlider(
              label: AppStrings.isHindi ? "पीएच मान (pH)" : "pH Level",
              value: _ph,
              min: 4.0,
              max: 9.0,
              unit: "pH",
              divisions: 50,
              onChanged: (v) => setState(() => _ph = v),
            ),
            const SizedBox(height: 18),

            // 4. Farm Operations (Land Size, Irrigation, Previous Crop)
            Text(
              AppStrings.isHindi ? "3. कृषि परिचालन विवरण" : "3. Farm Operations & Rotation",
              style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
            ),
            const SizedBox(height: 10),
            Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(16),
                border: Border.all(color: Colors.black.withOpacity(0.06)),
              ),
              child: Column(
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        AppStrings.isHindi ? "खेत का आकार (एकड़):" : "Farm Land Size (Acres):",
                        style: const TextStyle(fontWeight: FontWeight.w600, color: AppColors.textPrimary),
                      ),
                      Text(
                        "${_acres.toStringAsFixed(1)} Acres",
                        style: const TextStyle(fontWeight: FontWeight.bold, color: AppColors.primary),
                      ),
                    ],
                  ),
                  Slider(
                    value: _acres,
                    min: 0.5,
                    max: 20.0,
                    divisions: 39,
                    activeColor: AppColors.primary,
                    onChanged: (v) => setState(() => _acres = v),
                  ),
                  const SizedBox(height: 12),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        AppStrings.isHindi ? "सिंचाई साधन:" : "Irrigation Source:",
                        style: const TextStyle(fontWeight: FontWeight.w600, color: AppColors.textPrimary),
                      ),
                      DropdownButton<String>(
                        value: _irrigation,
                        underline: const SizedBox(),
                        items: _irrigationOptions.map((opt) {
                          return DropdownMenuItem(value: opt, child: Text(opt));
                        }).toList(),
                        onChanged: (v) {
                          if (v != null) setState(() => _irrigation = v);
                        },
                      ),
                    ],
                  ),
                  const Divider(height: 20),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        AppStrings.isHindi ? "पिछली फसल (रोटेशन):" : "Previous Crop (Rotation):",
                        style: const TextStyle(fontWeight: FontWeight.w600, color: AppColors.textPrimary),
                      ),
                      DropdownButton<String>(
                        value: _previousCrop,
                        underline: const SizedBox(),
                        items: _cropOptions.map((opt) {
                          return DropdownMenuItem(value: opt, child: Text(opt));
                        }).toList(),
                        onChanged: (v) {
                          if (v != null) setState(() => _previousCrop = v);
                        },
                      ),
                    ],
                  ),
                ],
              ),
            ),
            const SizedBox(height: 28),

            // Submit & Save Button
            SizedBox(
              width: double.infinity,
              height: 52,
              child: ElevatedButton.icon(
                style: ElevatedButton.styleFrom(
                  backgroundColor: AppColors.primary,
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                  elevation: 2,
                ),
                icon: const Icon(Icons.check_circle_rounded, color: Colors.white),
                label: Text(
                  AppStrings.isHindi ? "सहेजें और नई सिफारिशें देखें" : "Save & Generate Recommendations",
                  style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.white),
                ),
                onPressed: () {
                  advisory.setFarmParameters(
                    acres: _acres,
                    irrigation: _irrigation,
                    prevCrop: _previousCrop,
                  );

                  advisory.setCustomSoil({
                    "nitrogen": _n,
                    "phosphorus": _p,
                    "potassium": _k,
                    "ph": _ph,
                    "organic_carbon_pct": _oc,
                    "texture": _texture,
                  });

                  Navigator.pop(context);
                },
              ),
            ),
            const SizedBox(height: 20),
          ],
        ),
      ),
    );
  }

  Widget _buildSlider({
    required String label,
    required double value,
    required double min,
    required double max,
    required String unit,
    int? divisions,
    required ValueChanged<double> onChanged,
  }) {
    return Container(
      margin: const EdgeInsets.only(bottom: 10),
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: Colors.black.withOpacity(0.06)),
      ),
      child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(label, style: const TextStyle(fontWeight: FontWeight.w600, fontSize: 13, color: AppColors.textPrimary)),
              Text(
                "${value.toStringAsFixed(1)} $unit",
                style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 13, color: AppColors.primary),
              ),
            ],
          ),
          Slider(
            value: value,
            min: min,
            max: max,
            divisions: divisions ?? ((max - min).toInt()),
            activeColor: AppColors.primary,
            onChanged: onChanged,
          ),
        ],
      ),
    );
  }
}
