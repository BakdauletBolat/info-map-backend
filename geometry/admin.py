from django.contrib import admin
from geometry.models import GeometryObject, GeometryObjectCategory


# Register your models here.
@admin.register(GeometryObject)
class GeometryObjectAdmin(admin.ModelAdmin):
    list_display = ("id", "village","info")
    list_filter = ("village__village_district__district",)


@admin.register(GeometryObjectCategory)
class GeometryObjectAdmin(admin.ModelAdmin):
    pass
