from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, PasswordChangeSerializer, PhoneChangeSerializer, EmailChangeSerializer, PasswordConfirmSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])  # 비밀번호 해시화
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({'message': '삭제 완료'}, status=status.HTTP_200_OK)

#비밀번호 변경 뷰
class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PasswordChangeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            request.user.set_password(serializer.validated_data['new_password'])
            request.user.save()
            return Response({'message': '비밀번호 변경 완료'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#이메일 변경 뷰
class EmailChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EmailChangeSerializer(data=request.data)
        if serializer.is_valid():
            request.user.email = serializer.validated_data['email']
            request.user.save()
            return Response({'message': '이메일 변경 완료'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#폰번호 변경 뷰
class PhoneChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PhoneChangeSerializer(data=request.data)
        if serializer.is_valid():
            request.user.phone = serializer.validated_data['phone']
            request.user.save()
            return Response({'message': '폰번호 변경 완료'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#비밀번호 확인 뷰
class PasswordConfirmView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PasswordConfirmSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return Response({"message": "비밀번호 확인이 완료되었습니다."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#아이디 찾기 뷰
class FindIdView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        phone = request.data.get('phone')
        if email and phone:
            user = User.objects.filter(email=email, phone=phone).first()
            if user:
                return Response({'username': user.username}, status=status.HTTP_200_OK)
        return Response({'message': '일치하는 정보가 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)