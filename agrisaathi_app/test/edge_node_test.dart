import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:agrisaathi_app/screens/edge_node_controller_screen.dart';

void main() {
  testWidgets('EdgeNodeControllerScreen renders telemetry, relay, and Qualcomm RB3 specs', (WidgetTester tester) async {
    // Set a viewport height large enough to lay out the full dashboard page
    tester.view.physicalSize = const Size(1080, 4000);
    tester.view.devicePixelRatio = 1.0;
    addTearDown(() => tester.view.resetPhysicalSize());

    await tester.pumpWidget(
      const MaterialApp(
        home: EdgeNodeControllerScreen(),
      ),
    );
    await tester.pumpAndSettle();

    // Verify Title and Subtitle
    expect(find.textContaining('स्मार्ट फील्ड नोड व ऑटो सिंचाई'), findsOneWidget);

    // Verify Telemetry
    expect(find.textContaining('21.4%'), findsWidgets);
    expect(find.textContaining('FAO-56 ET₀'), findsOneWidget);

    // Verify 5V Relay Actuator Section
    expect(find.textContaining('5V रिले'), findsWidgets);
    expect(find.textContaining('वॉचडॉग'), findsWidgets);

    // Verify Qualcomm RB3 Gen 2 Card
    expect(find.textContaining('क्वालकॉम RB3 Gen 2'), findsOneWidget);
    expect(find.textContaining('12 TOPS'), findsOneWidget);

    // Test Toggling Relay Button (Motor ON)
    final motorOnBtn = find.text('मोटर चालू (ON)');
    expect(motorOnBtn, findsOneWidget);
    await tester.tap(motorOnBtn);
    await tester.pump();

    // Verify Pump ON status message
    expect(find.textContaining('मोटर चालू'), findsWidgets);

    // Turn Pump OFF
    final motorOffBtn = find.text('मोटर बंद (OFF)');
    expect(motorOffBtn, findsOneWidget);
    await tester.tap(motorOffBtn);
    await tester.pump();

    // Verify Standby state
    expect(find.textContaining('स्टैंडबाय'), findsWidgets);
  });
}
