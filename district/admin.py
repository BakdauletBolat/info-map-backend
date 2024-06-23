from django.contrib import admin
from district import models


@admin.register(models.District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(models.VillageDistrict)
class VillageDistrictAdmin(admin.ModelAdmin):
    list_filter = ("district", )
    list_display = ("id", "name")


@admin.register(models.Village)
class VillageAdmin(admin.ModelAdmin):
    pass
