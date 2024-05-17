import os
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource
from facilities.models import HealthFacilities


healthfacilities_mapping = {
    'name': 'name',
    'healthcare': 'healthcare',
    'amenity': 'amenity',
    'operator': 'operator',
    'geom': 'MULTIPOINT',
}

def run(verbose=True):
    file=os.getcwd() + '/data/health_facilities1.gpkg'
    data_source=DataSource(file)
    facilities_layer=data_source[0].name

    lm=LayerMapping(
        HealthFacilities, file, healthfacilities_mapping, layer=facilities_layer, transform=False)
    lm.save(strict=True, verbose=verbose)
