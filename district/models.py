from django.db import models
from district_map_backend.models import TimeStampedModel


# Create your models here.

class District(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.IntegerField()

    def __str__(self):
        return self.name


class VillageDistrict(TimeStampedModel):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='village_district')
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.IntegerField()

    def __str__(self):
        return self.name


class Village(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    dwelling_count = models.IntegerField(default=0)
    population_count = models.IntegerField(default=0)
    village_district = models.ForeignKey(VillageDistrict, on_delete=models.CASCADE, related_name='village')
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.IntegerField()

    def __str__(self):
        return self.name
