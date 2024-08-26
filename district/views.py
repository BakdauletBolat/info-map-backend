from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from district.models import GeographicRegion, RegionInfo
from geometry.models import GeometryObjectCategory
from rest_framework.request import Request
from rest_framework.response import Response
from district.serializers import (GeographicRegionResponseSerializer, GeographicRegionInfoCreateSerializer, 
                                  GeographicRegionInfoGetSerializer, GeographicRegionInfoCreateGetSerializer)
from rest_framework import decorators


class GeographicRegionViewSet(viewsets.ViewSet):
    queryset = GeographicRegion.objects.all()
    serializer_class = GeographicRegionResponseSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'retrieve':
            return [AllowAny]
        return [IsAuthenticated]

    def retrieve(self, request: Request, pk: str):
        geographic_region = self.queryset.get(slug=pk)
        instance = {
            'region': geographic_region
        }
        return Response(self.serializer_class(instance=instance, context={
            'request': request
        }).data)

    @decorators.action(methods=["POST"], detail=True)
    def update_info(self, request: Request, pk: str):
        serializer = GeographicRegionInfoCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        
        region = GeographicRegion.objects.get(id=pk)
        region.description = data.get("description")
        region.save()
        info = RegionInfo.objects.filter(region_id=pk, category_id=data.get('category_id')).first()
        if not info:
            info = RegionInfo.objects.create(region_id=pk)

        info.information_keys = data.get('information_keys')
        info.category_id = data.get('category_id')
        info.save()
        return Response({"status": True}, status=200)
    

    @decorators.action(methods=["GET"], detail=False)
    def get_update_info(self, request: Request):
        serializer = GeographicRegionInfoCreateGetSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        category = GeometryObjectCategory.objects.get(id=serializer.validated_data['category_id'])
        region = GeographicRegion.objects.get(slug=serializer.validated_data['region_slug'])
        infos = region.infos.filter(category=category).first()
        
        data = {
            'region_name': region.name,
            'region_id': region.id,
            'description': region.description,
            'category_name': category.name,
            'infos': infos.information_keys if infos is not None else []
        }
        
        return Response(GeographicRegionInfoGetSerializer(data).data, status=200)
