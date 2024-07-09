from rest_framework import serializers
from .models import Address, Place, BusinessHour
from favorites.views import CheckBusinessHour
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address', 'latitude', 'longitude']
    
class BusinessHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessHour
        fields = ['day', 'open', 'close', 'b_start', 'b_end', 'dayoff']

class PlaceSerializer(serializers.ModelSerializer):
    business_hours = BusinessHourSerializer(many=True, read_only=True)
    is_open = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ['address', 'name', 'menu', 'phone', 'memo', 'category', 'is_open', 'business_hours']

    def get_is_open(self, obj):
        return CheckBusinessHour(obj)