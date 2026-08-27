class WeatherDay {
  final String date;
  final String dayName;
  final double tempMax;
  final double tempMin;
  final double humidityAvg;
  final double precipitationProb;
  final String weatherDesc;
  final String sprayConditionRating;

  WeatherDay({
    required this.date,
    required this.dayName,
    required this.tempMax,
    required this.tempMin,
    required this.humidityAvg,
    required this.precipitationProb,
    required this.weatherDesc,
    required this.sprayConditionRating,
  });

  factory WeatherDay.fromJson(Map<String, dynamic> json) {
    return WeatherDay(
      date: json['date'] ?? '',
      dayName: json['day_name'] ?? '',
      tempMax: (json['temp_max'] as num?)?.toDouble() ?? 28.0,
      tempMin: (json['temp_min'] as num?)?.toDouble() ?? 20.0,
      humidityAvg: (json['humidity_avg'] as num?)?.toDouble() ?? 70.0,
      precipitationProb: (json['precipitation_prob'] as num?)?.toDouble() ?? 10.0,
      weatherDesc: json['weather_desc'] ?? 'Clear',
      sprayConditionRating: json['spray_condition_rating'] ?? 'Good for Spraying',
    );
  }

  Map<String, dynamic> toJson() => {
    'date': date,
    'day_name': dayName,
    'temp_max': tempMax,
    'temp_min': tempMin,
    'humidity_avg': humidityAvg,
    'precipitation_prob': precipitationProb,
    'weather_desc': weatherDesc,
    'spray_condition_rating': sprayConditionRating,
  };
}

class WeatherData {
  final double latitude;
  final double longitude;
  final double currentTempC;
  final double currentHumidityPct;
  final String currentCondition;
  final double windSpeedKmh;
  final double rainfall7dTotalMm;
  final List<WeatherDay> forecast7d;
  final List<Map<String, String>> alerts;

  WeatherData({
    required this.latitude,
    required this.longitude,
    required this.currentTempC,
    required this.currentHumidityPct,
    required this.currentCondition,
    required this.windSpeedKmh,
    required this.rainfall7dTotalMm,
    required this.forecast7d,
    required this.alerts,
  });

  factory WeatherData.fromJson(Map<String, dynamic> json) {
    List<WeatherDay> days = [];
    if (json['forecast_7d'] != null) {
      days = (json['forecast_7d'] as List)
          .map((e) => WeatherDay.fromJson(e as Map<String, dynamic>))
          .toList();
    }

    List<Map<String, String>> al = [];
    if (json['alerts'] != null) {
      al = (json['alerts'] as List)
          .map((e) => Map<String, String>.from(e as Map))
          .toList();
    }

    return WeatherData(
      latitude: (json['latitude'] as num?)?.toDouble() ?? 0.0,
      longitude: (json['longitude'] as num?)?.toDouble() ?? 0.0,
      currentTempC: (json['current_temp_c'] as num?)?.toDouble() ?? 26.0,
      currentHumidityPct: (json['current_humidity_pct'] as num?)?.toDouble() ?? 70.0,
      currentCondition: json['current_condition'] ?? 'Partly Cloudy',
      windSpeedKmh: (json['wind_speed_kmh'] as num?)?.toDouble() ?? 10.0,
      rainfall7dTotalMm: (json['rainfall_7d_total_mm'] as num?)?.toDouble() ?? 0.0,
      forecast7d: days,
      alerts: al,
    );
  }

  Map<String, dynamic> toJson() => {
    'latitude': latitude,
    'longitude': longitude,
    'current_temp_c': currentTempC,
    'current_humidity_pct': currentHumidityPct,
    'current_condition': currentCondition,
    'wind_speed_kmh': windSpeedKmh,
    'rainfall_7d_total_mm': rainfall7dTotalMm,
    'forecast_7d': forecast7d.map((e) => e.toJson()).toList(),
    'alerts': alerts,
  };
}
