from django.db import models
from search.models import Address
from django.conf import settings


# Create your models here.

class QuickSlot(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    type = models.IntegerField()
    
class List(models.Model):
    name = models.CharField(max_length=50)
    
class MyPin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50) 
    

    