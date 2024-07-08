from rest_framework import serializers
from .models import List, MyPin

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'name', 'user']

class MyPinSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPin
        fields = ['id', 'list', 'place', 'name']
