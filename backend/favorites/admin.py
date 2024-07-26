from django.contrib import admin
from .models import List, MyPin,QuickSlot, ListLike
# Register your models here.

admin.site.register(List)
admin.site.register(MyPin)
admin.site.register(QuickSlot)
admin.site.register(ListLike)