from rest_framework import serializers
from .models import SearchHistory
from search.serializers import PlaceSerializer

class SearchHistorySerializer(serializers.ModelSerializer):
    place = PlaceSerializer(read_only=True)
    class Meta:
        model = SearchHistory
        fields = '__all__'
