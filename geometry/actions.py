from geometry.domain import CreateGeometryObjectDomain, GeoJsonGeometry, UpdateGeometryObjectDomain
from geometry.models import GeometryObject


class CreateGeometryObjectAction:

    @staticmethod
    def get_location_by_type(feature: GeoJsonGeometry):
        latitude, longitude = 0, 0
        if feature.type == 'LineString':
            latitude = feature.coordinates[0][1]
            longitude = feature.coordinates[0][0]
        if feature.type == 'Point':
            latitude = feature.coordinates[1]
            longitude = feature.coordinates[0]
        return latitude, longitude
    
    @staticmethod
    def run(data: dict):
        geometry = CreateGeometryObjectDomain(**data)
        if len(geometry.geometry.features) > 0:
            latitude, longitude = CreateGeometryObjectAction.get_location_by_type(geometry.geometry.features[0].geometry)
            geometry.latitude = latitude
            geometry.longitude = longitude

        obj = GeometryObject(**geometry.model_dump())
        obj.save()
        return obj


class UpdateGeometryObjectAction:

    @staticmethod
    def run(data: dict, pk: int):
        geometry = UpdateGeometryObjectDomain(**data)
        obj = GeometryObject.objects.get(id=pk)
        obj.geometry = geometry.geometry.model_dump()
        obj.info = geometry.info
        if geometry.category_id is not None:
            obj.category_id = geometry.category_id
        obj.save()
        return obj
