from django.contrib import admin

# Register your models here.

from .models import subscribe, vehicle

admin.site.register(subscribe)
admin.site.register(vehicle)