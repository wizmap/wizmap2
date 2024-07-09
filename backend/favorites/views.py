from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import List, MyPin
from rest_framework.permissions import IsAuthenticated
from .serializers import ListSerializer, MyPinSerializer
from search.models import BusinessHour
from datetime import datetime

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

