from rest_framework import serializers

from .models import VirtualReality


class VirtualRealitySerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualReality
        fields = '__all__'