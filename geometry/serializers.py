from rest_framework import serializers


class GeometryCategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    icon = serializers.FileField()


class GeometryObjectSerializer(serializers.Serializer):

    geometry = serializers.JSONField()
    info = serializers.JSONField(allow_null=True)


class GeometryObjectQueryParamsSerializer(serializers.Serializer):
    category_ids = serializers.ListField(child=serializers.IntegerField(), required=False)
    village_ids = serializers.ListField(child=serializers.IntegerField(), required=False)
    villages_district_ids = serializers.ListField(child=serializers.IntegerField(), required=False)
    district_ids = serializers.ListField(child=serializers.IntegerField())