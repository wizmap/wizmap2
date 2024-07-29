from search.models import Place, BusinessHour
from search.serializers import PlaceSerializer, BusinessHourSerializer
from history.views import save_history
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from rest_framework.views import APIView
from rest_framework.response import Response
from dotenv import load_dotenv
import os
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

load_dotenv()

openai_key = os.getenv('OPENAI_API_KEY')
persist_directory = 'db'
embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    openai_api_key=openai_key,
)

# client = chromadb.HttpClient(
#     host="13.125.226.6", port=8000, settings=Settings(allow_reset=True)
# )
# client.reset()
# collection = client.get_or_create_collection("my_collection")

class Document:
    def __init__(self, page_content, metadata=None):
        self.page_content = page_content
        self.metadata = metadata if metadata is not None else {}

def build_vectordb():
    places = Place.objects.select_related('address').prefetch_related('businesshour_set').all()

    documents = []

    for place in places:
        # Place 모델의 필드들
        place_data = f"Name: {place.name}, Menu: {place.menu}, Phone: {place.phone}, Memo: {place.memo}, Category: {place.category}"
        # Address 모델의 필드들
        address_data = f"Address: {place.address.address}, Latitude: {place.address.latitude}, Longitude: {place.address.longitude}"
        place_data += f", {address_data}"

        # BusinessHour 모델의 필드들
        business_hours_data = []
        for business_hour in place.businesshour_set.all():
            business_hours_data.append(f"Day: {business_hour.day}, Open: {business_hour.open}, Close: {business_hour.close}, Dayoff: {business_hour.dayoff}")

        place_data += f", Business Hours: {', '.join(business_hours_data)}"

        metadata = {'id': place.id}
        documents.append(Document(page_content=place_data, metadata=metadata))

    vectordb = Chroma.from_documents(
        documents=documents,
        embedding=embedding,
        persist_directory=persist_directory
    )

    return vectordb

# vectordb 빌드
# vectordb_instance = build_vectordb()

# 기존에 생성된 db 파일 로드
vectordb_instance = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding
)

# vectordb_instance = Chroma(
#         client=client,
#         collection_name="my_collection",
#         embedding_function=embedding,
#     )

@permission_classes([AllowAny])
class TestView(APIView):
    def post(self, request):
        search = request.data.get('search')
        category = request.data.get('category', '')  # 카테고리 값 추가
        
        if request.user.is_authenticated:
            save_history(user=request.user, search=search)
            
        places = Place.objects.filter(
            Q(name__icontains=search) | Q(menu__icontains=search)
        )
        
        if not places.exists():
            retriever = vectordb_instance.as_retriever(
                # 검색 유형을 "유사도 점수 임계값"으로 설정합니다.
                search_type="similarity_score_threshold",
                search_kwargs={"score_threshold": 0.2,"k":10},
            )
            docs = retriever.invoke(search)
            a = []
            for doc in docs:
                a.append(doc.metadata["id"])
                print(doc)
            
            places = Place.objects.filter(id__in=a)
            
        if category:
            places = places.filter(category=category)  # 카테고리로 필터링
        # places = places | Place.objects.filter(id__in=a)
            
        # 페이지네이션 적용
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(places, request)
        
        place_data = []
        for place in result_page:
            business_hours = BusinessHour.objects.filter(place=place)
            business_hour_serializer = BusinessHourSerializer(business_hours, many=True)
            place_serializer = PlaceSerializer(place)
            place_data.append({
                'place': place_serializer.data,
                'business_hours': business_hour_serializer.data
            })

        # 페이지네이션된 응답 반환
        return paginator.get_paginated_response(place_data)
    
    def get(self, request):
        query = request.query_params.get('query', '')
        if not query:
            return Response([])

        # name과 menu 필드의 값을 추출하여 검색어 자동완성 기능 제공
        name_results = Place.objects.filter(name__icontains=query).values_list('name', flat=True)
        menu_results = Place.objects.filter(menu__icontains=query).values_list('menu', flat=True)

        # 중복 제거 및 리스트 합치기
        results = list(set(name_results) | set(menu_results))[:5]  # 최대 10개 결과
        
        return Response(results)