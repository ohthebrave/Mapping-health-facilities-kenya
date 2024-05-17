from django.contrib.gis import admin
from .models import HealthFacilities

admin.site.register(HealthFacilities, admin.ModelAdmin)
