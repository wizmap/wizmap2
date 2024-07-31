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

# phone 변경 시리얼라이저
class PhoneChangeSerializer(serializers.Serializer):
    phone = serializers.CharField()

    def validate_phone(self, value):
        if User.objects.filter(phone=value).exists(): # user 테이블에서 중복되는 번호가 있는지 확인
            raise serializers.ValidationError('이미 존재하는 번호입니다.')
        return value

# email 변경 시리얼라이저
class EmailChangeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():  # user 테이블에서 중복되는 이메일이 있는지 확인
            raise serializers.ValidationError('이미 존재하는 이메일입니다.')
        return value
    
# 패스워드 확인하는 시리얼라이저 (마이페이지 들어갈때 사용)
class PasswordConfirmSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = self.context['request'].user
        password = data['password']

        if not user.check_password(password):
            raise serializers.ValidationError("비밀번호가 올바르지 않습니다.")
        
        return data
    
#아이디찾기 시리얼라이저
class FindIdSerializer(serializers.Serializer):
    email = serializers.EmailField()
    phone = serializers.CharField()
    
    def validate(self, data):
        email = data['email']
        phone = data['phone']
        if not User.objects.filter(email=email, phone=phone).exists():
            raise serializers.ValidationError('일치하는 정보가 없습니다.')
        return data