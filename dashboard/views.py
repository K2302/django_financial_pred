from django.shortcuts import render
from datetime import datetime

# Simulated in-memory data
campaign_data = {
    "channels": ["Google Ads", "Facebook Ads", "LinkedIn Ads", "Twitter Ads"],
    "spend": [1200, 700, 900, 500],
    "roi_values": [300, 500, 250, 400],
    "channel_distribution": [25, 35, 20, 20]
}

def dashboard_view(request):
    if request.method == "POST":
        # Extract values from form
        channel = request.POST.get("channel")
        spend = float(request.POST.get("budget_spent"))
        revenue = float(request.POST.get("revenue"))

        # Calculate ROI
        roi = round((revenue - spend) / spend * 100, 2)

        # Update in-memory data (for now)
        if channel in campaign_data["channels"]:
            idx = campaign_data["channels"].index(channel)
            campaign_data["spend"][idx] += spend
            campaign_data["roi_values"][idx] = roi
            campaign_data["channel_distribution"][idx] += 1
        else:
            campaign_data["channels"].append(channel)
            campaign_data["spend"].append(spend)
            campaign_data["roi_values"].append(roi)
            campaign_data["channel_distribution"].append(1)

    # Prepare display stats
    max_roi = max(campaign_data["roi_values"])
    best_index = campaign_data["roi_values"].index(max_roi)
    best_channel = campaign_data["channels"][best_index]

    max_spend = max(campaign_data["spend"])
    costly_index = campaign_data["spend"].index(max_spend)
    costliest_campaign = campaign_data["channels"][costly_index]

    context = {
        "roi": f"{max_roi}%",
        "best_channel": best_channel,
        "costliest_campaign": costliest_campaign,
        "channels": campaign_data["channels"],
        "spend": campaign_data["spend"],
        "roi_values": campaign_data["roi_values"],
        "channel_distribution": campaign_data["channel_distribution"]
    }

    return render(request, 'dashboard/dashboard.html', context)
