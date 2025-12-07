from django.db import models
from oauth.models import User

class Home(models.Model):
    STATUS_CHOICES = (
        ('booked', 'Booked'),
        ('available', 'Available')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='homes')
    img_url = models.CharField(max_length=500, blank=False, null=False)
    house_type = models.CharField(max_length=200, blank=False)
    description = models.TextField(help_text='House Description')
    location = models.CharField(max_length=256, blank=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    price_per_night = models.FloatField(blank=False)
    offer = models.FloatField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.house_type
    
