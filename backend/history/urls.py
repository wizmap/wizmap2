from django.urls import path
from .views import history_list

app_name="history"

urlpatterns = [
    path('', history_list, name='history-list'),
]