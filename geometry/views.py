from typing import List

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
        return Response(self.serializer_class(self.queryset, many=True, context={'request': request}).data)


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

    def list(self, request):
        query_params_serializer = self.query_params_serializer(data=request.GET)
        query_params_serializer.is_valid(raise_exception=True)
        query_params = query_params_serializer.validated_data
        queryset = self._get_filtered_queryset(queryset=self.queryset, query_params=query_params)

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

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(GeometryObject, pk=pk)
        return Response(self.serializer_class(instance=obj, context={'request': request}).data)
