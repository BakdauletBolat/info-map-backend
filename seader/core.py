import json
from typing import Any
from district import models
from geometry.models import GeometryObject, GeometryObjectCategory


class JsonSeeder(object):
    model: Any
    file_path: str

    def import_model(self):
        with open(self.file_path, 'r') as f:
            import_list = json.load(f)
        bulk_operations = [
            self.model(**row)
            for row in import_list
        ]
        self.model.objects.bulk_create(bulk_operations, ignore_conflicts=True)


class GeometryRegionSeeder(JsonSeeder):
    model = models.GeographicRegion
    file_path = './seedjsons/GeometryRegions.json'


class GeometryRegionChildSeeder(JsonSeeder):
    model = models.GeographicRegion
    file_path = './seedjsons/GeometryRegionsChilds.json'


class GeometryCategorySeeder(JsonSeeder):
    model = GeometryObjectCategory
    file_path = './seedjsons/geometry_object_category.json'


class GeometrySeeder(JsonSeeder):
    model = GeometryObject
    file_path = './seedjsons/geometry_object.json'
