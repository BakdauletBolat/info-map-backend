from typing import List

from geometry.utils import get_nearby_locations
from rest_framework.generics import get_object_or_404

from geometry.actions import CreateGeometryObjectAction, \
    UpdateGeometryObjectAction
from rest_framework import viewsets
from rest_framework.response import Response
from geometry.models import GeometryObjectCategory, GeometryObject
from geometry.serializers import GeometryCategorySerializer, GeometryObjectSerializer, \
    GeometryObjectQueryParamsSerializer
from django.db.models import QuerySet
from district.models import GeographicRegion
from rest_framework.permissions import AllowAny, IsAuthenticated


class GeometryCategoryViewSet(viewsets.ViewSet):
    serializer_class = GeometryCategorySerializer
    queryset = GeometryObjectCategory.objects.all()
    permission_classes = [AllowAny]

    def list(self, request):
        queryset = self.queryset
        if request.user.is_authenticated and hasattr(request.user, 'profile'):
            categories = request.user.profile.role.categories.all().values_list('id')
            queryset = self.queryset.filter(id__in=categories)

        return Response(self.serializer_class(queryset, many=True, context={'request': request}).data)


class GeometryViewSet(viewsets.ViewSet):
    serializer_class = GeometryObjectSerializer
    queryset = GeometryObject.objects.all()
    query_params_serializer = GeometryObjectQueryParamsSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [AllowAny()]

    def _get_all_ids_from_regions(self, regions: List[GeographicRegion], ids: set):
        for region in regions:
            if len(region.children.all()) > 0:
                ids.add(region.id)
                self._get_all_ids_from_regions(region.children.all(), ids)
            else:
                ids.add(region.id)

    def _get_filtered_queryset(self, queryset: QuerySet, query_params: dict):
        return_query_set = queryset
        if (category_ids := query_params.get('category_ids')) is not None:
            return_query_set = return_query_set.filter(category_id__in=category_ids)
        if (geographic_region_id := query_params.get('geographic_region_id')) is not None:
            ids = set()
            region = GeographicRegion.objects.get(id=geographic_region_id)
            self._get_all_ids_from_regions([region], ids)
            return_query_set = return_query_set.filter(region_id__in=ids)
        return return_query_set

    def get_meter_for_zoom(self, zoom: int):
        zoom_to_tile_width = {
            0: 40075016.69,
            1: 20037508.34,
            2: 10018754.17,
            3: 5009377.09,
            4: 2504688.54,
            5: 1252344.27,
            6: 626172.14,
            7: 313086.07,
            8: 156543.03,
            9: 78271.52,
            10: 39135.76,
            11: 19567.88,
            12: 9783.94,
            13: 4891.97,
            14: 2445.98,
            15: 1222.99,
            16: 611.50,
            17: 305.75,
            18: 152.87,
            19: 76.44,
            20: 38.22
        }
        return zoom_to_tile_width[zoom]

    def list(self, request):
        query_params_serializer = self.query_params_serializer(data=request.GET)
        query_params_serializer.is_valid(raise_exception=True)
        query_params = query_params_serializer.validated_data
        latitude, longitude, zoom = None, None, 12
        if request.user.is_authenticated and hasattr(request.user, 'profile'):
            categories = request.user.profile.role.categories.all().values_list('id')
            query_params['category_ids'] = [*categories, *query_params.get('category_ids', [])]

        queryset = self._get_filtered_queryset(queryset=self.queryset, query_params=query_params)

        
        if query_params.get('latitude') and query_params.get('longitude'):
            latitude = query_params.get('latitude')
            longitude = query_params.get('longitude')
            zoom = query_params.get('zoom')
        elif query_params.get('geographic_region_id') and latitude is None and longitude is None:
            region = GeographicRegion.objects.get(id=query_params.get('geographic_region_id'))
            latitude = region.latitude
            longitude = region.longitude
            zoom = region.zoom
        else:
            latitude = 0
            longitude = 0


        radius_in_meters = self.get_meter_for_zoom(zoom)

        queryset = get_nearby_locations(latitude, 
                                        longitude,
                                        radius_in_meters, 
                                        queryset)
        

        data = self.serializer_class(instance=queryset, many=True, context={'request': request}).data

        for item in data:
            item['geometry']['id'] = item['id']

        return Response(data)

    def create(self, request):
        obj = CreateGeometryObjectAction.run(data=request.data)
        return Response({"id": obj.id})

    def update(self, request, pk: int):
        obj = UpdateGeometryObjectAction.run(data=request.data, pk=pk)
        return Response({"id": obj.id})

    def destroy(self, request, pk: int):
        obj = self.queryset.get(id=pk)
        obj.delete()
        return Response({}, status=204)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(GeometryObject, pk=pk)
        return Response(self.serializer_class(instance=obj, context={'request': request}).data)
