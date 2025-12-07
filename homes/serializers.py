from rest_framework import serializers
from .models import Home

class HomeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Home
        fields = [
            'id', 'user', 'img_url', 'house_type', 'description',
            'location', 'status', 'price_per_night', 'offer',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at', 'user']
