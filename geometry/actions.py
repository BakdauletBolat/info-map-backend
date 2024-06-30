from geometry.domain import CreateGeometryObjectDomain
from geometry.models import GeometryObject


class CreateGeometryObjectAction:

    @staticmethod
    def run(data: dict):
        geometry = CreateGeometryObjectDomain(**data)
        obj = GeometryObject(**geometry.dict())
        obj.save()
        return obj
