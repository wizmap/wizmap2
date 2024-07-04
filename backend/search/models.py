from django.db import models

# Create your models here.

class Address(models.Model):
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)  # 위도
    longitude = models.DecimalField(max_digits=9, decimal_places=6)  # 경도
    
class Place(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    menu = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=20, null=True)
    memo = models.TextField(null=True)
    category = models.CharField(max_length=255) # 카페, 음식점 ... 
    
class BusinessHour(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    day = models.CharField(max_length=50, null=True)
    open = models.TimeField(null=True)
    close = models.TimeField(null=True)
    b_start = models.TimeField(null=True)
    b_end = models.TimeField(null=True)
    dayoff = models.BooleanField(default=False) # 휴무여부