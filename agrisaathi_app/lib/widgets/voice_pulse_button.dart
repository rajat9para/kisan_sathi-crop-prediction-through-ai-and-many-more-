import 'package:flutter/material.dart';
import '../constants/app_colors.dart';

class VoicePulseButton extends StatefulWidget {
  final VoidCallback onTap;
  final bool isListening;

  const VoicePulseButton({
    super.key,
    required this.onTap,
    this.isListening = false,
  });

  @override
  State<VoicePulseButton> createState() => _VoicePulseButtonState();
}

class _VoicePulseButtonState extends State<VoicePulseButton> with SingleTickerProviderStateMixin {
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1200),
    )..repeat(reverse: true);
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: widget.onTap,
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, child) {
          final scale = widget.isListening ? 1.0 + (_controller.value * 0.15) : 1.0;
          return Transform.scale(
            scale: scale,
            child: Container(
              width: 72,
              height: 72,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                gradient: const LinearGradient(
                  colors: [AppColors.primaryLight, AppColors.primary],
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
                boxShadow: [
                  BoxShadow(
                    color: AppColors.primary.withOpacity(widget.isListening ? 0.5 : 0.3),
                    blurRadius: widget.isListening ? 20 : 10,
                    spreadRadius: widget.isListening ? 6 : 2,
                  ),
                ],
              ),
              child: const Icon(
                Icons.mic_rounded,
                color: Colors.white,
                size: 36,
              ),
            ),
          );
        },
      ),
    );
  }
}
