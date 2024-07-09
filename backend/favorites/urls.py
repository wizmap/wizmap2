from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListView, ListCreateView, ListUpdateView, ListDeleteView, MyPinCreateView, MyPinUpdateView, MyPinDeleteView


app_name='favorite'
urlpatterns = [
    path('list/<int:pk>', ListView.as_view(), name = 'list_datail'),
    path('list/create', ListCreateView.as_view(), name = 'list_create'),
    path('list/update/<int:pk>', ListUpdateView.as_view(), name='list_update'),
    path('list/delete/<int:pk>', ListDeleteView.as_view(), name='list_detail'),
    path('mypin/create/<int:list_id>', MyPinCreateView.as_view(), name='mypin_create'),
    path('mypin/update/<int:pk>', MyPinUpdateView.as_view(), name='mypin_update'),
    path('mypin/delete/<int:pk>', MyPinDeleteView.as_view(), name='mypin_delete'),
    
]
