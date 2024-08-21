from django.db import models

from district.models import GeographicRegion


class GeometryObjectCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.FileField(upload_to='categoryIcons/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '    Категория'
        verbose_name_plural = 'Категории'


class GeometryObject(models.Model):
    geometry = models.JSONField()
    info = models.JSONField()
    region = models.ForeignKey(GeographicRegion, on_delete=models.CASCADE, related_name='geometry_object')
    category = models.ForeignKey(GeometryObjectCategory, on_delete=models.DO_NOTHING, default=None)

    class Meta:
        verbose_name = 'Гео обьекты'
        verbose_name_plural = 'Гео обьекты'
