from rest_framework import serializers

from suggestions.models import Suggestions


class SuggestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        fields = '__all__'