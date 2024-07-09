from django.contrib import admin
from django.urls import *
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='register'),
    path('delete/', DeleteUserView.as_view(), name='delete_user'),
   
]
