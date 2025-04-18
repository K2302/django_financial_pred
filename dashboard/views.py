from django.shortcuts import render

def dashboard_view(request):
    context = {
        "roi": "300.0%",
        "best_channel": "Facebook Ads",
        "costliest_campaign": "LinkedIn Ads",
        "channels": ["Google Ads", "Facebook Ads", "LinkedIn Ads", "Twitter Ads"],
        "spend": [1200, 700, 900, 500],
        "roi_values": [300, 500, 250, 400],
        "channel_distribution": [25, 35, 20, 20],
    }
    return render(request, 'dashboard/dashboard.html', context)
import logging
logger = logging.getLogger(__name__)

def dashboard_view(request):
    logger.info("Dashboard accessed by user")
    try:
        # your existing context + view code
        return render(request, 'dashboard/dashboard.html', context)
    except Exception as e:
        logger.error(f"Dashboard view failed: {e}")
        return render(request, 'dashboard/error.html')
