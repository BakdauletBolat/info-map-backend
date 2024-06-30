from rest_framework import viewsets
from district.models import GeographicRegion
from rest_framework.request import Request
from rest_framework.response import Response
from district.serializers import GeographicRegionResponseSerializer
from rest_framework.decorators import action


class GeographicRegionViewSet(viewsets.ViewSet):
    queryset = GeographicRegion.objects.all()
    serializer_class = GeographicRegionResponseSerializer

    def retrieve(self, request: Request, pk:str):
        geographic_region = self.queryset.get(slug=pk)
        instance = {
            'region': geographic_region
        }
        return Response(self.serializer_class(instance=instance, context={
            'request': request
        }).data)
