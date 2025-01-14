from math import radians, cos, sin, sqrt, atan2
from django.db.models import Q
from geometry.models import GeometryObject


def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    radius = 6371000  # Earth's radius in meters
    return radius * c



def get_nearby_locations(lat, lon, radius, queryset = GeometryObject.objects.all()):
    # Define a bounding box
    lat_diff = radius / 111000  # Roughly 111 km per degree latitude
    lon_diff = radius / (111000 * cos(radians(lat)))

    # Filter locations within the bounding box
    locations = queryset.filter(
        Q(latitude__gte=lat - lat_diff) &
        Q(latitude__lte=lat + lat_diff) &
        Q(longitude__gte=lon - lon_diff) &
        Q(longitude__lte=lon + lon_diff)
    )

    # Filter again using the Haversine formula
    nearby_locations = [
        loc for loc in locations
        if haversine(lat, lon, loc.latitude, loc.longitude) <= radius
    ]

    return nearby_locations
