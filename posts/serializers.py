from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'status', 'img_url', 'created_at', 'user']
        read_only_fields = ['id', 'created_at', 'user']
