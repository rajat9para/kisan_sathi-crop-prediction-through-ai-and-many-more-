import 'package:flutter_test/flutter_test.dart';
import 'package:agrisaathi_app/main.dart';

void main() {
  testWidgets('AgriSaathi App loads and navigates successfully', (WidgetTester tester) async {
    await tester.pumpWidget(const AgriSaathiApp());
    expect(find.byType(AgriSaathiApp), findsOneWidget);
    
    // Advance time past the splash timer
    await tester.pump(const Duration(milliseconds: 2500));
    await tester.pump(const Duration(milliseconds: 600));
  });
}
