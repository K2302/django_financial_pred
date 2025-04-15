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

    def __str__(self):
        return f"{self.channel} on {self.date}"