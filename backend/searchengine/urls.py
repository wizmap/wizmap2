from django.urls import path
from .views import TestView

app_name="searchengine"

urlpatterns = [
    path('', TestView.as_view(), name='test'),
]