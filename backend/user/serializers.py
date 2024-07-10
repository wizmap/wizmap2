from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # 비밀번호는 쓰기 전용 필드로 설정

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'gender', 'birth', 'password']
