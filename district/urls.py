from rest_framework.routers import DefaultRouter
from district import views

district_router = DefaultRouter()
district_router.register("region", views.GeographicRegionViewSet)

urlpatterns = district_router.urls
