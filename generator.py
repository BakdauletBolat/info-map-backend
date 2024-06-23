from faker import Faker
from slugify import slugify
import json

fake = Faker('ru_Ru')  # Устанавливаем казахский язык для Faker



def generate_districts():
    districts = []
    for i in range(10):
        name = fake.city()  # Генерируем случайное название города на казахском языке
        district = {
            "id": i+1,
            "name": name,
            "slug": slugify(name),
            "latitude": float(fake.latitude()),
            "longitude": float(fake.longitude()),
            "zoom": 1
        }
        districts.append(district)

    # Сохраняем данные в JSON файл
    with open('seedjsons/districts.json', 'w') as f:
        json.dump(districts, f, ensure_ascii=False, indent=4)

    print("Данные успешно сгенерированы и сохранены в 'districts.json'")

def generate_districts_villages():
    district_villages = []
    all_count = 1
    for i in range(10):
        for j in range(10):
            name = fake.city()
            district_id = i+1
            district_village = {
                "id": all_count,
                "name": name,
                "district_id": district_id,
                "latitude": float(fake.latitude()),
                "longitude": float(fake.longitude()),
                "zoom": 1
            }
            district_villages.append(district_village)
            all_count += 1

    with open('seedjsons/districts_villages.json', 'w') as f:
        json.dump(district_villages, f, ensure_ascii=False, indent=4)

    print("Данные успешно сгенерированы и сохранены в 'districts_villages.json'")


def generate_villages():
    villages = []
    all_count = 1
    for i in range(100):
        for j in range(10):
            name = fake.city()
            description = fake.paragraph()
            dwelling_count = fake.random_int(1000,8000)
            population_count = fake.random_int(4000, 20000)
            village_district_id = i+1
            villages.append({
                "id": all_count,
                "name": name,
                "description": description,
                "dwelling_count": dwelling_count,
                "population_count": population_count,
                "village_district_id": village_district_id,
                "latitude": float(fake.latitude()),
                "longitude": float(fake.longitude()),
                "zoom": 1
            })
            all_count += 1

    with open('seedjsons/villages.json', 'w') as f:
        json.dump(villages, f, ensure_ascii=False, indent=4)

    print("Данные успешно сгенерированы и сохранены в 'villages.json'")



def generate_geometry_object():
    geometries = []

    all_count = 1
    for i in range(1000):
        for j in range(100):
            geometry = {
                "id": all_count,
                "geometry": {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [float(fake.longitude()), float(fake.latitude())]
                    },
                    "properties": {
                        "name": fake.name(),
                        "slug": slugify(fake.name())
                    }
                },
                "info": {
                        "name": fake.name(),
                        "slug": slugify(fake.name())
                },
                "village_id": i+1,
                "category_id": fake.random_int(1, 11)
            }
            geometries.append(geometry)
            all_count += 1

    with open('seedjsons/geometry_object.json', 'w') as f:
        json.dump(geometries, f, ensure_ascii=False, indent=4)

    print("Данные успешно сгенерированы и сохранены в 'geometry_object.json'")


generate_districts()
generate_districts_villages()
generate_villages()
generate_geometry_object()