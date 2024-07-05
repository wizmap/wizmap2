import csv
from django.core.management.base import BaseCommand
from search.models import Address, Place, BusinessHour  # 실제 모델과 앱 이름으로 변경
from datetime import datetime

class Command(BaseCommand):
    help = 'Load places from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                address, created = Address.objects.get_or_create(
                    address=row['도로명주소'],
                    latitude=row['위도'],
                    longitude=row['경도']
                )
                place, created = Place.objects.get_or_create(
                    address=address,
                    name=row['\ufeff사업장명'],
                    menu=row['대표메뉴'],
                    phone=row['소재지전화'],
                    memo=row['휴무'],  # 메모 필드에 업종분류 저장 예시
                    category=row['업종분류'],  # 카테고리 필드에 업종분류 저장 예시
                )

                business_hours = row.get('영업시간', '').split(',')
                for hour in business_hours:
                    if hour.strip():  # 빈 문자열이 아닐 경우에만 처리
                        try:
                            hour = hour.strip()
                            day, time_range = hour.split(maxsplit=1) # 첫번째 공백만 분리
                            open_time_str, close_time_str = time_range.split('-')
                            open_time_str = open_time_str.strip()
                            close_time_str = close_time_str.strip()

                            # 시간 문자열을 datetime 객체로 변환
                            open_time = datetime.strptime(open_time_str, '%H:%M').time()
                            close_time = datetime.strptime(close_time_str, '%H:%M').time()
                            print(open_time,close_time)
                            
                            BusinessHour.objects.create(
                                place=place,
                                day=day,
                                open=open_time,
                                close=close_time,
                            )
                        except ValueError as e:
                            print(f"ValueError occurred: {e}")
                        except Exception as e:
                            print(f"Exception occurred: {e}")
                            

        self.stdout.write(self.style.SUCCESS('Successfully loaded places'))
        
        # python manage.py load_csv "파일경로.csv"