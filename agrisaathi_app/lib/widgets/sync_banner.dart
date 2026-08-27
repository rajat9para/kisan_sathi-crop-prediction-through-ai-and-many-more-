import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../services/sync_manager.dart';
import '../constants/app_colors.dart';
import '../constants/app_strings.dart';

class SyncBanner extends StatelessWidget {
  const SyncBanner({super.key});

  @override
  Widget build(BuildContext context) {
    return Consumer<SyncManager>(
      builder: (context, syncMgr, child) {
        final isOnline = syncMgr.isOnline;
        final isSyncing = syncMgr.isSyncing;

        return AnimatedContainer(
          duration: const Duration(milliseconds: 300),
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
          decoration: BoxDecoration(
            color: isOnline
                ? AppColors.primaryLight.withOpacity(0.12)
                : AppColors.offlineBadge.withOpacity(0.15),
            border: Border(
              bottom: BorderSide(
                color: isOnline ? AppColors.primaryLight.withOpacity(0.3) : AppColors.offlineBadge.withOpacity(0.4),
                width: 1,
              ),
            ),
          ),
          child: Row(
            children: [
              Container(
                width: 10,
                height: 10,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: isOnline ? AppColors.onlineBadge : AppColors.offlineBadge,
                ),
              ),
              const SizedBox(width: 8),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Text(
                      isOnline ? AppStrings.liveOnline : AppStrings.offlineMode,
                      style: TextStyle(
                        fontSize: 12,
                        fontWeight: FontWeight.bold,
                        color: isOnline ? AppColors.primaryDark : AppColors.offlineBadge,
                      ),
                    ),
                    Text(
                      "${AppStrings.lastUpdated} ${syncMgr.lastSyncTimestamp}",
                      style: const TextStyle(
                        fontSize: 11,
                        color: AppColors.textSecondary,
                      ),
                    ),
                  ],
                ),
              ),
              if (isSyncing)
                const SizedBox(
                  width: 18,
                  height: 18,
                  child: CircularProgressIndicator(
                    strokeWidth: 2,
                    valueColor: AlwaysStoppedAnimation<Color>(AppColors.primary),
                  ),
                )
              else
                InkWell(
                  onTap: () => syncMgr.triggerLiveSync(),
                  borderRadius: BorderRadius.circular(20),
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                    decoration: BoxDecoration(
                      color: isOnline ? AppColors.primary : AppColors.textSecondary,
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        const Icon(Icons.sync, size: 13, color: Colors.white),
                        const SizedBox(width: 4),
                        Text(
                          AppStrings.syncNow,
                          style: const TextStyle(
                            fontSize: 11,
                            color: Colors.white,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
            ],
          ),
        );
      },
    );
  }
}
