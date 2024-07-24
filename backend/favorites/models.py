from django.db import models
from search.models import Place
from django.conf import settings


# Create your models here.

class QuickSlot(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=50)
    type = models.IntegerField()
    icon = models.IntegerField(default=1)
    
class List(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    private = models.BooleanField(default=True)
    memo = models.CharField(max_length=255, null=True)

class MyPin(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=50) 
    

    