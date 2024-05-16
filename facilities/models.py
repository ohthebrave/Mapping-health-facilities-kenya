from django.contrib.gis.db import models

class HealthFacilities(models.Model):
    name = models.CharField(max_length=80)
    healthcare = models.CharField(max_length=100)
    amenity = models.CharField(max_length=80)
    operator:type = models.CharField(max_length=80)
    geom = models.MultiPointField(srid=4326)