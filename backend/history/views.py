from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .models import SearchHistory
from .serializers import SearchHistorySerializer
from search.models import Place

# 검색기록 확인
class HistoryListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        histories = SearchHistory.objects.filter(user=user).order_by('-created_at')  # 검색기록확인
        serializer = SearchHistorySerializer(histories, many=True)
        return Response({'histories': serializer.data}, status=status.HTTP_200_OK)

# 검색기록 삭제    
class DeleteHistoryView(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, pk):
        try:
            history = SearchHistory.objects.get(pk=pk, user=request.user)
        except SearchHistory.DoesNotExist:
            raise NotFound({'error': '검색기록을 찾을 수 없습니다.'})
        
        history.delete()
        return Response({'message': '검색기록 삭제'}, status=status.HTTP_200_OK)

# 검색기록 저장
def save_history(user, search):
    SearchHistory.objects.filter(user=user, search=search).delete()  # 기존검색기록 확인 후 존재하면 삭제
    SearchHistory.objects.create(user=user, search=search) # 새롭게 저장(검색한 시간때문에)
    
# 검색 핀 저장
def save_pin_history(user, pk):
    place = Place.objects.get(pk=pk)
    SearchHistory.objects.filter(user=user, search='📍' + place.name).delete()  # 기존검색기록 확인 후 존재하면 삭제
    SearchHistory.objects.create(user=user, search='📍' + place.name, place=place)