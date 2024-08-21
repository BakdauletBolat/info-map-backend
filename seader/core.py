import json
from typing import Any
from district import models
from geometry.models import GeometryObject, GeometryObjectCategory
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv
# loading variables from .env file
load_dotenv("prod.env")

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


class CoorsUpdateSeeder(JsonSeeder):
    model = models.GeographicRegion
    file_path = './seedjsons/new_coors.json'

    def import_model(self):
        with open(self.file_path, 'r') as f:
            import_list = json.load(f)

        for l in import_list:
            model = self.model.objects.filter(id=l.get("id")).first()
            if model:
                model.latitude = float(l.get("coors")[0])
                model.longitude = float(l.get("coors")[1])
                model.save()
                print("updated", l)


class GeoInfoSeeder(JsonSeeder):

    model = models.RegionInfo
    file_path = './seedjsons/infos.json'

    def import_model(self):
        with open(self.file_path, 'r') as f:
            import_list = json.load(f)

        for l in import_list:
            model = self.model.objects.filter(region=l.get("id")).first()
            if not model:
                new_model = self.model.objects.create(region_id=l.get("id"))
            else:
                new_model = model

            new_model.information_keys = l.get("infos")
            new_model.save()


