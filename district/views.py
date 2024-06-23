from rest_framework import viewsets
from district.models import Village
from rest_framework.request import Request
from rest_framework.response import Response
from district.serializers import VillageSerializer
from rest_framework.decorators import action


class VillageViewSet(viewsets.ViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer

    def retrieve(self, request: Request, pk:str):
        results = self.queryset.filter(village_district__district__slug=pk)
        return Response(self.serializer_class(instance=results, many=True).data)
