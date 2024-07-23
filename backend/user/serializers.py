from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # 비밀번호는 쓰기 전용 필드로 설정

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'gender', 'birth', 'password']

#비밀번호 변경 시리얼라이저
class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

    def validate_old_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('기존 비밀번호가 일치하지 않습니다.')
        return value

    def validate(self, data):
        if data['new_password'] == data['old_password']:
            raise serializers.ValidationError({"new_password": "새 비밀번호는 기존 비밀번호와 다르게 설정해야 합니다."})
        return data
    
