from django.contrib import admin
from .models import Campaign

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("channel", "budget_spent", "revenue", "roi", "created_at")
    search_fields = ("channel",)
    list_filter = ("created_at",)
