from django.db import models

class Campaign(models.Model):
    CHANNEL_CHOICES = [
        ('Google Ads', 'Google Ads'),
        ('Facebook Ads', 'Facebook Ads'),
        ('LinkedIn Ads', 'LinkedIn Ads'),
        ('Twitter Ads', 'Twitter Ads'),
    ]

    channel = models.CharField(max_length=50, choices=CHANNEL_CHOICES)
    budget_spent = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    conversions = models.PositiveIntegerField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    roi = models.DecimalField(max_digits=6, decimal_places=2, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Auto-calculate ROI before saving
        if self.budget_spent > 0:
            self.roi = (self.revenue - self.budget_spent) / self.budget_spent * 100
        else:
            self.roi = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.channel} - {self.date}"
