from rest_framework import serializers


class GeometryCategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    icon = serializers.FileField()
    id = serializers.IntegerField()


class GeometryObjectSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    region_slug = serializers.CharField(source="region.slug")
    geometry = serializers.JSONField()
    info = serializers.JSONField(allow_null=True)
    category = GeometryCategorySerializer()


class GeometryObjectQueryParamsSerializer(serializers.Serializer):
    category_ids = serializers.ListField(child=serializers.IntegerField(), required=False)
    geographic_region_id = serializers.IntegerField()
