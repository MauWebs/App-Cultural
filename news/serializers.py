from rest_framework import serializers

from news.models import News


class NewSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'