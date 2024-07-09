from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListView, ListCreateView, ListUpdateView, ListDeleteView, MyPinCreateView, MyPinUpdateView, MyPinDeleteView,FavoritesView,QuickView,QuickUpdateView,QuickDeleteView,QuickCreateView


app_name='favorite'
urlpatterns = [
    path('list/<int:pk>', ListView.as_view(), name = 'list-datail'),
    path('list/create', ListCreateView.as_view()),
    path('list/update/<int:pk>', ListUpdateView.as_view()),
    path('list/delete/<int:pk>', ListDeleteView.as_view()),
    path('mypin/create', MyPinCreateView.as_view()),
    path('mypin/update/<int:pk>', MyPinUpdateView.as_view()),
    path('mypin/delete/<int:pk>', MyPinDeleteView.as_view()),
    path('',FavoritesView.as_view()),
    path('quick/<int:pk>',QuickView.as_view()),
    path('quick/update/<int:pk>',QuickUpdateView.as_view()),
    path('quick/delete/<int:pk>', QuickDeleteView.as_view()),
    path('quick/create/',QuickCreateView.as_view()),
]
