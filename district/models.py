import enum

from django.db import models
from district_map_backend.models import TimeStampedModel

class RegionLevel(enum.Enum):
    COUNTRY = 0


class GeographicRegion(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    dwelling_count = models.IntegerField(default=0, verbose_name='Тургын уй')
    population_count = models.IntegerField(default=0, verbose_name='Адам саны')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.IntegerField()
    photo = models.ImageField(upload_to='GeographicRegion/', null=True, blank=True)

    @property
    def level(self):
        if self.parent is None:
            return 0
        return self.parent.level + 1

    @property
    def string_level(self):
        return RegionLevel(self.level).name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class RegionInfo(TimeStampedModel):
    information_keys = models.JSONField(default=[])
    category = models.ForeignKey("geometry.GeometryObjectCategory", on_delete=models.CASCADE,
                                 related_name='infos', null=True, blank=True)
    region = models.ForeignKey(GeographicRegion, on_delete=models.CASCADE, related_name='infos')
