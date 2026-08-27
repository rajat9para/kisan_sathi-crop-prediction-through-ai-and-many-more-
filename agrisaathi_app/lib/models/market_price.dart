class MarketPrice {
  final String commodity;
  final String commodityHi;
  final String variety;
  final String marketName;
  final String state;
  final double modalPriceRsQuintal;
  final double minPriceRsQuintal;
  final double maxPriceRsQuintal;
  final double trendPct7d;
  final String trendDirection; // up, down, stable
  final String arrivalDate;

  MarketPrice({
    required this.commodity,
    required this.commodityHi,
    required this.variety,
    required this.marketName,
    required this.state,
    required this.modalPriceRsQuintal,
    required this.minPriceRsQuintal,
    required this.maxPriceRsQuintal,
    required this.trendPct7d,
    required this.trendDirection,
    required this.arrivalDate,
  });

  factory MarketPrice.fromJson(Map<String, dynamic> json) {
    return MarketPrice(
      commodity: json['commodity'] ?? '',
      commodityHi: json['commodity_hi'] ?? '',
      variety: json['variety'] ?? '',
      marketName: json['market_name'] ?? '',
      state: json['state'] ?? '',
      modalPriceRsQuintal: (json['modal_price_rs_quintal'] as num?)?.toDouble() ?? 0.0,
      minPriceRsQuintal: (json['min_price_rs_quintal'] as num?)?.toDouble() ?? 0.0,
      maxPriceRsQuintal: (json['max_price_rs_quintal'] as num?)?.toDouble() ?? 0.0,
      trendPct7d: (json['trend_pct_7d'] as num?)?.toDouble() ?? 0.0,
      trendDirection: json['trend_direction'] ?? 'stable',
      arrivalDate: json['arrival_date'] ?? '',
    );
  }

  Map<String, dynamic> toJson() => {
    'commodity': commodity,
    'commodity_hi': commodityHi,
    'variety': variety,
    'market_name': marketName,
    'state': state,
    'modal_price_rs_quintal': modalPriceRsQuintal,
    'min_price_rs_quintal': minPriceRsQuintal,
    'max_price_rs_quintal': maxPriceRsQuintal,
    'trend_pct_7d': trendPct7d,
    'trend_direction': trendDirection,
    'arrival_date': arrivalDate,
  };
}
