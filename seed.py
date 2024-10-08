import django
import os
from loguru import logger
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'district_map_backend.settings')

django.setup()

from seader.core import GeoInfoSeeder

seeders = [GeoInfoSeeder()]

for seed in seeders:
    logger.info(f"Seeding {seed.model.__name__}")
    seed.import_model()


logger.info(f"Finished seeding models")