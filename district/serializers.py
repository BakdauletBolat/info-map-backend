from rest_framework import serializers


class GeographicRegionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    slug = serializers.SlugField()
    dwelling_count = serializers.IntegerField()
    population_count = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField(required=False, read_only=True, allow_null=True)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    zoom = serializers.IntegerField()
    photo = serializers.ImageField()
    children = serializers.SerializerMethodField()
    parent_slug = serializers.SlugField(source="parent.slug", allow_null=True, required=False)
    level = serializers.IntegerField()
    info = serializers.SerializerMethodField()

    def get_info(self, obj):
        if hasattr(obj, "info"):
            return obj.info.information_keys
        return None

    def get_children(self, obj):
        if obj.children.all():
            return GeographicRegionSerializer(obj.children, many=True, context={
                'request': self.context['request']
            }).data
        return None


class GeographicRegionResponseSerializer(serializers.Serializer):
    region = GeographicRegionSerializer()