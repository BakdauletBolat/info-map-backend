from rest_framework import viewsets
from rest_framework.response import Response
from geometry.models import GeometryObjectCategory, GeometryObject
from geometry.serializers import GeometryCategorySerializer, GeometryObjectSerializer, \
    GeometryObjectQueryParamsSerializer
from django.db.models import QuerySet


class GeometryCategoryViewSet(viewsets.ViewSet):

    serializer_class = GeometryCategorySerializer
    queryset = GeometryObjectCategory.objects.all()

    def list(self, request):
        return Response(self.serializer_class(self.queryset, many=True, context={'request': request}).data)


class GeometryViewSet(viewsets.ViewSet):

    serializer_class = GeometryObjectSerializer
    queryset = GeometryObject.objects.all()
    query_params_serializer = GeometryObjectQueryParamsSerializer

    @staticmethod
    def _get_filtered_queryset(queryset: QuerySet, query_params: dict):
        return_query_set = queryset
        if (category_ids := query_params.get('category_ids')) is not None:
            return_query_set = return_query_set.filter(category_id__in=category_ids)
        if (village_ids := query_params.get('village_ids')) is not None:
            return_query_set = return_query_set.filter(village_id__in=village_ids)
        if (villages_district_ids := query_params.get('villages_district_ids')) is not None:
            return_query_set = return_query_set.filter(village__village_district_id__in=villages_district_ids)
        if (district_ids := query_params.get('district_ids')) is not None:
            return_query_set = return_query_set.filter(village__village_district__district_id__in=district_ids)
        return return_query_set

    def list(self, request):
        query_params_serializer = self.query_params_serializer(data=request.GET)
        query_params_serializer.is_valid(raise_exception=True)
        query_params = query_params_serializer.validated_data
        queryset = self._get_filtered_queryset(queryset=self.queryset, query_params=query_params)
        return Response(self.serializer_class(instance=queryset, many=True, context={'request': request}).data)

