from django.db import models
from django.conf import settings
from search.models import Place

# Create your models here.   
class SearchHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, null=True, blank=True, on_delete=models.SET_NULL)
    search = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.search}"