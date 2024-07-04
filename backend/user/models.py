from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 기본적으로 제공하는 필드 외에 원하는 필드를 적어준다.
    phone = models.CharField(max_length=11, null=True)
    gender = models.BooleanField(null=True)
    birth = models.DateField(null=True)