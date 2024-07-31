from django.contrib import admin
from django.urls import *
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='register'),
    path('delete/', DeleteUserView.as_view(), name='delete_user'),
    path('change-password/', PasswordChangeView.as_view(), name='change_password'),
    path('change-phone/', PhoneChangeView.as_view(), name='change_phone'),
    path('change-email/', EmailChangeView.as_view(), name='change_email'),
    path('check-password/', PasswordConfirmView.as_view(), name='check_password'),
    path('find-id/', FindIdView.as_view(), name='find_id'),
]
