from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Address, Place, BusinessHour
from .serializers import AddressSerializer, PlaceSerializer, BusinessHourSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from history.views import save_history, save_pin_history
from favorites.views import CheckBusinessHour
from rest_framework.permissions import AllowAny
# Create your views here.
class SearchAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        search_term = request.data.get('search_term')
        
        print('search_term',search_term)
        # 검색어 저장
        if request.user.is_authenticated:
            save_history(user=request.user, search=search_term)

        
        places = Place.objects.filter(name__icontains=search_term)

        
        place_data = []
        for place in places:
            business_hours = BusinessHour.objects.filter(place=place)
            business_hour_serializer = BusinessHourSerializer(business_hours, many=True)
            place_serializer = PlaceSerializer(place)
            place_data.append({
                'place': place_serializer.data,
                'business_hours': business_hour_serializer.data
            })

        return Response(place_data)

class PinPlaceAPIView(APIView):
    def get(self, request, id, *args, **kwargs):
        place = get_object_or_404(Place, id=id)
        business_hours = BusinessHour.objects.filter(place=place)
        
        # 검색 핀 저장
        if request.user.is_authenticated:
            save_pin_history(user=request.user, pk=id)
        
        place_serializer = PlaceSerializer(place)
        business_hour_serializer = BusinessHourSerializer(business_hours, many=True)
        
        return Response({
            'place': place_serializer.data,
            'business_hours': business_hour_serializer.data,
        })