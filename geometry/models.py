from django.db import models

from district.models import Village


class GeometryObjectCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.FileField(upload_to='categoryIcons/')


class GeometryObject(models.Model):
    geometry = models.JSONField()
    info = models.JSONField()
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    category = models.ForeignKey(GeometryObjectCategory, on_delete=models.DO_NOTHING, default=None)
