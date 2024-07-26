from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import List, MyPin,QuickSlot,Place, ListLike
from rest_framework.permissions import IsAuthenticated
from .serializers import ListSerializer, MyPinSerializer,QuickSlotSerializer, PlaceSerializer, AddressSerializer, ListLikeSerializer
from search.models import BusinessHour
from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from user.models import User
from django.db.models import Count

def CheckBusinessHour(place):
    # 현재 요일 체크 (숫자 -> 문자)
    days = ['월', '화', '수', '목', '금', '토', '일']
    
    now = datetime.now()
    now_day = now.weekday()
    today = days[now_day]
    place_hours = BusinessHour.objects.filter(place = place, day = today)

    days = ['월', '화', '수', '목', '금', '토', '일']
    
    
    for place_hour in place_hours:
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
                    'place_id':mypin.place.id,
                    'place_name': mypin.place.name,
                    'address': mypin.place.address.address,
                    'category': mypin.place.category,
                    'isopen':CheckBusinessHour(mypin.place),
                    'mypin_id':mypin.id,
                    'mypin_name': mypin.name,
                    'list_name': mypin.list.name,
                    'latitude' : mypin.place.address.latitude,
                    'longitude' : mypin.place.address.longitude
                }
            )
        # print(data)
        
        return Response({'MyPin': data}, status=status.HTTP_200_OK)
    
class ListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ListSerializer(data=request.data, context={'request': request}, partial=True)
        # print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # print(serializer.errors)
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
        print(request.data)
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
         # 주소 데이터를 Address 모델에 저장
        address_data = {
            'address': request.data.get('address'),
            'latitude': request.data.get('latitude'),
            'longitude': request.data.get('longitude')
        }
        address_serializer = AddressSerializer(data=address_data)
        if address_serializer.is_valid():
            address = address_serializer.save()
        else:
            print("address")
            print(request.data.get('address'), type(request.data.get('latitude')), type(request.data.get('longitude')))
            print(address_serializer.errors)
            return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Place 데이터를 Place 모델에 저장
        place_data = {
            'address': address.id,
            'name': request.data.get('name'),
            'menu': request.data.get('menu'),
            'phone': request.data.get('phone'),
            'memo': request.data.get('memo'),
            'category': request.data.get('category')
        }
        place_serializer = PlaceSerializer(data=place_data)
        if place_serializer.is_valid():
            place = place_serializer.save()
        else:
            print("place")
            print(place_serializer.errors)
            return Response(place_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # MyPin 데이터를 MyPin 모델에 저장
        mypin_data = {
            'list': list_id,
            'place': place.id,
            'name': request.data.get('name')
        }
        serializer = MyPinSerializer(data=mypin_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        try:
            mypin_obj = MyPin.objects.get(id=pk)
        except MyPin.DoesNotExist:
            return Response({'error': 'MyPin not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MyPinSerializer(mypin_obj, data=request.data, partial=True)
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
            return Response({'error': 'MyPin not found'}, status=status.HTTP_404_NOT_FOUND)

        mypin_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FavoritesView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        quickslots = QuickSlot.objects.filter(user=user)
        mylist = List.objects.filter(user=user)  # 여기서 클래스 이름을 List로 변경
        public_list = List.objects.filter(private=False).exclude(user=request.user).annotate(like_count=Count('listlike')).order_by('-like_count')   # 내 리스트를 제외한 것 중 공개 리스트만 추출 
        

        quickslots_data = QuickSlotSerializer(quickslots, many=True).data
        user_list = ListSerializer(mylist, many=True).data  # 변수 이름을 user_list로 변경
        public_list_data = ListSerializer(public_list, many=True).data

        # user 정보 추가
        for public_list_item in public_list_data:
            user_id = public_list_item['user']
            user_obj = User.objects.get(id=user_id)
            public_list_item['username'] = user_obj.username
            likes = ListLike.objects.filter(list = public_list_item['id']).count()
            # print(public_list_item, likes)
            public_list_item['likes'] = likes

        response_data = {
            "list": user_list,  
            "quicktype": quickslots_data,
            'public_list': public_list_data
        }

        return Response(response_data)

class QuickView(APIView):
 

    def get(self, request, pk):
        quickslot = get_object_or_404(QuickSlot, pk=pk)
        place = quickslot.place
        is_open = CheckBusinessHour(place)  # 영업 상태 확인

        data = {
            'place_name': place.name,
            'address': place.address.address,
            'category': place.category,
            'isopen': is_open,
            'quick_name': quickslot.name
        }
        return Response(data, status=status.HTTP_200_OK)
class QuickUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            quick_obj = QuickSlot.objects.get(id=pk)
            serializer = QuickSlotSerializer(quick_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except QuickSlot.DoesNotExist:
            return Response({'error': 'QuickSlot not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        try:
            quick_obj = QuickSlot.objects.get(id=pk)
        except QuickSlot.DoesNotExist:
            return Response({'error': 'QuickSlot not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = QuickSlotSerializer(quick_obj, data=request.data, partial=True)
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
         # 주소 데이터를 Address 모델에 저장
        
        address_data = {
            'address': request.data.get('address'),
            'latitude': request.data.get('latitude'),
            'longitude': request.data.get('longitude')
        }
        address_serializer = AddressSerializer(data=address_data)
        if address_serializer.is_valid():
            address = address_serializer.save()
        else:
            print("address")
            print(request.data.get('address'), type(request.data.get('latitude')), type(request.data.get('longitude')))
            print(address_serializer.errors)
            return Response(address_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Place 데이터를 Place 모델에 저장
        place_data = {
            'address': address.id,
            'name': request.data.get('name'),
            'menu': request.data.get('menu'),
            'phone': request.data.get('phone'),
            'memo': request.data.get('memo'),
            'category': request.data.get('category')
        }
        place_serializer = PlaceSerializer(data=place_data)
        if place_serializer.is_valid():
            place = place_serializer.save()
        else:
            print("place")
            print(place_serializer.errors)
            return Response(place_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # QuickSlot 데이터 QuickSlot 모델에 저장 
        quick_data = {
            'user':request.user.id,
            'place': place.id,
            'name': request.data.get('name'),
            'type': request.data.get('type'),
        }
        serializer = QuickSlotSerializer(data=quick_data,context={'request': request})
        print(request.user.id)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LikeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            listlike = ListLike.objects.filter(user=request.user)
            serializer = ListLikeSerializer(listlike, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ListLike.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class ListLikeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        print(request.data, request.user)
        serializer = ListLikeSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListUnLikeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, list_id):
        try:
            # print(pk)/
            list_data = List.objects.get(id=list_id)
            listlike = ListLike.objects.get(list=list_data, user=request.user)
            listlike.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ListLike.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)