from typing import List, Dict, Any, Union

from pydantic import BaseModel
from pydantic.fields import Field


class GeoJsonGeometry(BaseModel):
    coordinates: Union[List[float], List[List[float]], List[List[List[float]]]]= None
    type: str


class GeoJson(BaseModel):
    type: str = 'Feature'
    properties: Dict[str, Any] = {}
    geometry: GeoJsonGeometry


class GeoJsonCollection(BaseModel):
    type: str = 'FeatureCollection'
    features: List[GeoJson]


class CreateGeometryObjectDomain(BaseModel):
    geometry: GeoJsonCollection = Field(..., description="Гео Json Обьект")
    info: Dict[str, Any] = Field(..., description="Инфо")
    region_id: int = Field(...)
    category_id: int = Field(...)