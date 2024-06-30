from django.contrib import admin
from district import models


class GeographicRegionTabularAdmin(admin.TabularInline):
    model = models.GeographicRegion
    fields = ("id", "name", "photo")


@admin.register(models.GeographicRegion)
class GeographicRegionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    inlines = [GeographicRegionTabularAdmin]
