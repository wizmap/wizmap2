from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import List, MyPin,QuickSlot,Place
from rest_framework.permissions import IsAuthenticated
from .serializers import ListSerializer, MyPinSerializer,QuickSlotSerializer
from search.models import BusinessHour
from datetime import datetime
from django.shortcuts import get_object_or_404

def CheckBusinessHour(place):
    # 현재 요일 체크 (숫자 -> 문자)
    days = ['월', '화', '수', '목', '금', '토', '일']
    
    now = datetime.now()
    now_day = now.weekday()
    today = days[now_day]
    place_hours = BusinessHour.objects.filter(place = place, day = today)

    days = ['월', '화', '수', '목', '금', '토', '일']
    
    
    for place_hour in place_hours:
        # print(place_hour.day, place_hour.open, place_hour.close)
        # 휴무 여부 체크 
        if place_hour.day == today and place_hour.dayoff == True: 
            return False
        # 영업 시간 체크 
        if now.time() >= place_hour.open and now.time() <= place_hour.close:
            if place_hour.b_start or place_hour.b_end:
                if place_hour.b_start <= now.time() <= place_hour.b_end:
                    return False
            else: 
                return True
    return False


class ListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        mylist = List.objects.get(id = pk)
        mypins = MyPin.objects.filter(list = mylist)
        data = []
        for mypin in mypins:
            data.append(
                {
                    'place_name': mypin.place.name,
                    'address': mypin.place.address.address,
                    'category': mypin.place.category,
                    'isopen':CheckBusinessHour(mypin.place),
                    'mypin_name': mypin.name,
                    'list_name': mypin.list.name
                }
            )
        # print(data)
        
        return Response({'MyPin': data}, status=status.HTTP_200_OK)
    
class ListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ListSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ListUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            list_obj = List.objects.get(id=pk)
            serializer = ListSerializer(list_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except List.DoesNotExist:
            return Response({'error': 'List not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        list_obj = List.objects.get(id = pk)
        
        if not list_obj:
            return Response({'error': 'List not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListSerializer(list_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        try:
            list_obj = List.objects.get(id=pk)
            serializer = ListSerializer(list_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except List.DoesNotExist:
            return Response({'error': 'List not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            list_obj = List.objects.get(id=pk)
        except List.DoesNotExist:
            return Response({'error': 'List not found'}, status=status.HTTP_404_NOT_FOUND)

        list_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
class MyPinCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, list_id):
        serializer = MyPinSerializer(data={**request.data, 'list': list_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class MyPinUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        try:
            mypin_obj = MyPin.objects.get(id=pk)
            serializer = MyPinSerializer(mypin_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except MyPin.DoesNotExist:
            return Response({'error': 'MyPin not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        mypin_obj = MyPin.objects.get(id = pk)
        
        if not mypin_obj:
            return Response({'error': 'MyPin not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MyPinSerializer(mypin_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MyPinDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        try:
            mypin_obj = MyPin.objects.get(id=pk)
            serializer = MyPinSerializer(mypin_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except MyPin.DoesNotExist:
            return Response({'error': 'MyPin not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            mypin_obj = MyPin.objects.get(id=pk)
        except MyPin.DoesNotExist:
            return Response({'error': 'mypin not found'}, status=status.HTTP_404_NOT_FOUND)

        mypin_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FavoritesView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        quickslots = QuickSlot.objects.filter(user=user)
        mylist = List.objects.filter(user=user)  # 여기서 클래스 이름을 List로 변경

        quickslots_data = QuickSlotSerializer(quickslots, many=True).data
        user_list = ListSerializer(mylist, many=True).data  # 변수 이름을 user_list로 변경

        response_data = {
            "list": user_list,  
            "quicktype": quickslots_data
        }

        return Response(response_data)

class QuickView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        quicks= QuickSlot.objects.filter(type = pk)
        data = []
        for quick in quicks:
            data.append(
                {
                    'place_name': quick.place.name,
                    'address': quick.place.address.address,
                    'category': quick.place.category,
                    'isopen':CheckBusinessHour(quick.place),
                    'quick_name': quick.name
                }
            )
        print(data)
        
        return Response({'quick': data}, status=status.HTTP_200_OK)
class QuickUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            quick_obj = QuickSlot.objects.get(id=pk)
            serializer = QuickSlotSerializer(quick_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except List.DoesNotExist:
            return Response({'error': 'quickslot not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        quick_obj = QuickSlot.objects.get(id = pk)
        
        if not quick_obj:
            return Response({'error': 'quickslot not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ListSerializer(quick_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class QuickDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        try:
            quick_obj = QuickSlot.objects.get(id=pk)
            serializer = QuickSlotSerializer(quick_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except QuickSlot.DoesNotExist:
            return Response({'error': 'quick not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            quick_obj = QuickSlot.objects.get(id=pk)
        except QuickSlot.DoesNotExist:
            return Response({'error': 'quick not found'}, status=status.HTTP_404_NOT_FOUND)

        quick_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class QuickCreateView(APIView):
    def post(self, request):
        serializer = QuickSlotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
