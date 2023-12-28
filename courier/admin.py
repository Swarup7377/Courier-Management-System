from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Branch)
admin.site.register(Courier)
admin.site.register(CourierTracking)
admin.site.register(Staff)