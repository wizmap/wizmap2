from rest_framework import serializers
from .models import List, MyPin,QuickSlot

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'name', 'user']
        
    def create(self, validated_data):
        # 사용자 정보를 자동으로 추가
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class MyPinSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPin
        fields = ['id', 'list', 'place', 'name']

class QuickSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuickSlot
        fields = ['id', 'name', 'user','place','type']