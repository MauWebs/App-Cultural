from rest_framework import serializers

from .models import Comment, DigitalObject, Rating

# --------------------------------------------------------------------------- #

class DigitalObjectSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.user_name', read_only=True)
    class Meta:
        model = DigitalObject
        fields = '__all__'

# --------------------------------------------------------------------------- #

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'user', 'digital_object', 'rating_value')
        
# --------------------------------------------------------------------------- #

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'description', 'digital_object', 'start_date')