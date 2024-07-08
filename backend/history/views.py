from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .models import SearchHistory
from .serializers import SearchHistorySerializer

class HistoryListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        histories = SearchHistory.objects.filter(user=user)
        serializer = SearchHistorySerializer(histories, many=True)
        return Response({'histories': serializer.data}, status=status.HTTP_200_OK)
    
class DeleteHistoryView(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, pk):
        try:
            history = SearchHistory.objects.get(pk=pk, user=request.user)
        except SearchHistory.DoesNotExist:
            raise NotFound({'error': '검색기록을 찾을 수 없습니다.'})
        
        history.delete()
        return Response({'message': '검색기록 삭제'}, status=status.HTTP_200_OK)
