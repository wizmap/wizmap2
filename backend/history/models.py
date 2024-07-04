from django.db import models
from django.conf import settings
from search.models import Address

# Create your models here.

class SearchHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    search = models.TextField()