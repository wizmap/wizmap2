from rest_framework import serializers
from .models import Address, Place, BusinessHour

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

    class Meta:
        model = Place
        fields = ['address', 'name', 'menu', 'phone', 'memo', 'category', 'business_hours']

        