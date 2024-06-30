from django.contrib import admin
from geometry.models import GeometryObject, GeometryObjectCategory


# Register your models here.
@admin.register(GeometryObject)
class GeometryObjectAdmin(admin.ModelAdmin):
    list_display = ("id", "region", "info")
    list_filter = ("region",)


@admin.register(GeometryObjectCategory)
class GeometryObjectAdmin(admin.ModelAdmin):
    pass
