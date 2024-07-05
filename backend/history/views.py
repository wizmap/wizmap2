from django.http import JsonResponse
from .models import SearchHistory
from .serializers import SearchHistorySerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

@csrf_exempt
@login_required
def history_list(request):
    if request.method == 'GET':
        user=request.user
        histories = SearchHistory.objects.filter(user=user)
        serialized_histories = [SearchHistorySerializer(h).data for h in histories]
        return JsonResponse({'histories': serialized_histories}, safe=False)

# class SearchHistoryViewSet(viewsets.ModelViewSet):
#     queryset = SearchHistory.objects.all()
#     serializer_class = SearchHistorySerializer

#     @action(detail=True, methods=['get'])
#     def histories(self, request, pk=None):
#         histories = SearchHistory.objects.filter(pk=pk)
#         serializer = SearchHistorySerializer(histories, many=True)
#         return Response({'histories': serializer.data})
