from django.apps import AppConfig


class DistrictConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'district'
    verbose_name = 'Регион'
    verbose_name_plural = 'Регионы'
