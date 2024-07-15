from django.contrib import admin
from district import models


class GeographicRegionTabularAdmin(admin.TabularInline):
    model = models.GeographicRegion
    fields = ("id", "name", "photo")


@admin.register(models.GeographicRegion)
class GeographicRegionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "dwelling_count", "population_count")
    list_display_links = ("id", "name")
    # exclude = ('slug',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [GeographicRegionTabularAdmin]
