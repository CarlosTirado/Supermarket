from rest_framework import serializers
from supermarket_ms.models.color_model import Color

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['id', 'name', 'description', 'codehexa']
