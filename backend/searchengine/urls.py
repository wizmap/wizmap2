from django.urls import path
from .views import TestView, naver_direction_proxy

app_name="searchengine"

urlpatterns = [
    path('', TestView.as_view(), name='test'),
    path('api/map-direction/', naver_direction_proxy, name='naver_direction_proxy'),
]