from rest_framework import serializers

from .models import History

# --------------------------------------------------------------------------- #

class HistorySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.user_name', read_only=True)
    class Meta:
        model = History
        fields = '__all__'

# --------------------------------------------------------------------------- #