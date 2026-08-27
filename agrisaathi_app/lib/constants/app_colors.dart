import 'package:flutter/material.dart';

class AppColors {
  // Primary Palette: Modern Agri-Tech Emerald & Earth
  static const Color primary = Color(0xFF137547);        // Rich Crop Emerald
  static const Color primaryLight = Color(0xFF2E933C);   // Vibrant Sprout Green
  static const Color primaryDark = Color(0xFF0B4628);    // Deep Forest Green
  
  // Secondary Palette: Sun & Soil
  static const Color secondary = Color(0xFFD8973C);      // Golden Wheat Harvest
  static const Color secondaryLight = Color(0xFFF4C542); // Sunlit Amber
  static const Color accent = Color(0xFF8B5E3C);         // Rich Organic Soil Brown

  // Background & Surfaces
  static const Color background = Color(0xFFF5F8F4);     // Ultra-clean Field Tint
  static const Color surface = Color(0xFFFFFFFF);        // Pure Card White
  static const Color surfaceElevated = Color(0xFFEBF3EA);// Soft Mint Elevation
  
  // Status & Feedback
  static const Color success = Color(0xFF2E7D32);
  static const Color warning = Color(0xFFED6C02);
  static const Color error = Color(0xFFD32F2F);
  static const Color info = Color(0xFF0288D1);

  // Text colors
  static const Color textPrimary = Color(0xFF1E2922);
  static const Color textSecondary = Color(0xFF5F7166);
  static const Color textMuted = Color(0xFF8C9E93);

  // SHAP and Explainability specific colors
  static const Color shapPositive = Color(0xFF2E7D32);   // Boosts recommendation
  static const Color shapNegative = Color(0xFFC62828);   // Penalizes recommendation
  static const Color shapNeutral = Color(0xFF78909C);
  
  // Offline and Sync states
  static const Color onlineBadge = Color(0xFF2E7D32);
  static const Color offlineBadge = Color(0xFFE65100);
}
