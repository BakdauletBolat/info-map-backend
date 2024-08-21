from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from district.models import GeographicRegion, RegionInfo
from rest_framework.request import Request
from rest_framework.response import Response
from district.serializers import GeographicRegionResponseSerializer, GeographicRegionInfoCreateSerializer
from rest_framework import decorators


class GeographicRegionViewSet(viewsets.ViewSet):
    queryset = GeographicRegion.objects.all()
    serializer_class = GeographicRegionResponseSerializer
    permission_classes = [IsAuthenticated]

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

        info = RegionInfo.objects.filter(region_id=pk).first()
        if not info:
            info = RegionInfo.objects.create(region_id=pk)

        data = serializer.data
        info.information_keys = data.get('information_keys')
        info.category_id = data.get('category_id')
        info.save()
        return Response({"status": True}, status=200)
