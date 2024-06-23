from rest_framework.routers import DefaultRouter

from geometry import views


geo_router = DefaultRouter()
geo_router.register("geometries", views.GeometryViewSet)
geo_router.register("categories", views.GeometryCategoryViewSet)

urlpatterns = geo_router.urls
