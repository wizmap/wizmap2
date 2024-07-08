from django.urls import path
from .views import HistoryListView, DeleteHistoryView

app_name="history"

urlpatterns = [
    path('', HistoryListView.as_view(), name='history-list'),
    path('delete/<int:pk>', DeleteHistoryView.as_view(), name='history-delete'),
]