from rest_framework import serializers
from movies.models import Moviedata

class MoviedataSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, required=False)
    class Meta:
        model = Moviedata
        fields = ['id', 'title', 'duration', 'rating', 'typ', 'image']