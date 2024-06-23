from rest_framework import serializers


class VillageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField(required=False, read_only=True, allow_null=True)
    dwelling_count = serializers.IntegerField()
    population_count = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    zoom = serializers.IntegerField()