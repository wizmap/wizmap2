from django.contrib import admin
from django.urls import *
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('delete/', DeleteUserView.as_view(), name='delete_user'),
]
