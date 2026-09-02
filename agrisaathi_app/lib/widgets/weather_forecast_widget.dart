import 'package:flutter/material.dart';
import '../models/weather_data.dart';
import '../constants/app_colors.dart';

class WeatherForecastWidget extends StatelessWidget {
  final WeatherData weather;

  const WeatherForecastWidget({super.key, required this.weather});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: AppColors.surface,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.black.withOpacity(0.06)),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.03),
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
                  const Icon(Icons.wb_sunny_rounded, color: AppColors.secondary, size: 22),
                  const SizedBox(width: 8),
                  Text(
                    "${weather.currentTempC.toStringAsFixed(1)}°C",
                    style: const TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                      color: AppColors.textPrimary,
                    ),
                  ),
                  const SizedBox(width: 8),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                    decoration: BoxDecoration(
                      color: AppColors.surfaceElevated,
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Text(
                      weather.currentCondition,
                      style: const TextStyle(fontSize: 11, fontWeight: FontWeight.w600, color: AppColors.primaryDark),
                    ),
                  ),
                ],
              ),
              Row(
                children: [
                  const Icon(Icons.water_drop_rounded, color: AppColors.info, size: 14),
                  const SizedBox(width: 2),
                  Text(
                    "${weather.currentHumidityPct.toInt()}%",
                    style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w600, color: AppColors.textSecondary),
                  ),
                  const SizedBox(width: 10),
                  const Icon(Icons.air_rounded, color: Colors.blueGrey, size: 14),
                  const SizedBox(width: 2),
                  Text(
                    "${weather.windSpeedKmh.toInt()} km/h",
                    style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w600, color: AppColors.textSecondary),
                  ),
                ],
              ),
            ],
          ),
          if (weather.alerts.isNotEmpty) ...[
            const SizedBox(height: 12),
            Container(
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(
                color: AppColors.primaryLight.withOpacity(0.08),
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: AppColors.primaryLight.withOpacity(0.3)),
              ),
              child: Row(
                children: [
                  const Icon(Icons.check_circle_outline_rounded, color: AppColors.primary, size: 18),
                  const SizedBox(width: 8),
                  Expanded(
                    child: Text(
                      weather.alerts[0]['message_hi'] ?? weather.alerts[0]['message_en'] ?? '',
                      style: const TextStyle(fontSize: 11, color: AppColors.primaryDark, fontWeight: FontWeight.w500),
                    ),
                  ),
                ],
              ),
            ),
          ],
          const SizedBox(height: 14),
          const Divider(height: 1),
          const SizedBox(height: 12),
          // 7-day forecast horizontal cards
          SizedBox(
            height: 96,
            child: ListView.separated(
              scrollDirection: Axis.horizontal,
              itemCount: weather.forecast7d.length,
              separatorBuilder: (ctx, i) => const SizedBox(width: 10),
              itemBuilder: (context, idx) {
                final day = weather.forecast7d[idx];
                final isRain = day.precipitationProb > 30;

                return Container(
                  width: 76,
                  padding: const EdgeInsets.symmetric(vertical: 8, horizontal: 4),
                  decoration: BoxDecoration(
                    color: isRain ? Colors.blue.shade50 : AppColors.surfaceElevated,
                    borderRadius: BorderRadius.circular(12),
                    border: Border.all(color: isRain ? Colors.blue.shade200 : Colors.transparent),
                  ),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        day.dayName.substring(0, 3),
                        style: const TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
                      ),
                      Icon(
                        isRain ? Icons.grain_rounded : Icons.wb_sunny_rounded,
                        color: isRain ? AppColors.info : AppColors.secondary,
                        size: 20,
                      ),
                      Text(
                        "${day.tempMax.toInt()}° / ${day.tempMin.toInt()}°",
                        style: const TextStyle(fontSize: 10, color: AppColors.textSecondary),
                      ),
                    ],
                  ),
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}
