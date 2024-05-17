from django.contrib.gis.db import models

class HealthFacilities(models.Model):
    name = models.CharField(max_length=80, null=True)
    healthcare = models.CharField(max_length=100, null=True)
    amenity = models.CharField(max_length=80, null=True)
    operator:type = models.CharField(max_length=80, null=True)
    geom = models.MultiPointField(srid=4326)

    # Returns the string representation of the model.
    def __str__(self):
        return self.name