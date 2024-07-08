from django.urls import path
from . import views

urlpatterns = [
    path('', views.SearchAPIView.as_view(), name='search'),
    path('pin/<int:id>/', views.PinPlaceAPIView.as_view(), name='pin-place-detail'),
]