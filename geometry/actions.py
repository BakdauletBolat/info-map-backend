from geometry.domain import CreateGeometryObjectDomain, UpdateGeometryObjectDomain
from geometry.models import GeometryObject


class CreateGeometryObjectAction:

    @staticmethod
    def run(data: dict):
        geometry = CreateGeometryObjectDomain(**data)
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
