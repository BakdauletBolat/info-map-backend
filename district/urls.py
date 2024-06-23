from rest_framework.routers import DefaultRouter
from district import views

district_router = DefaultRouter()
district_router.register("village", views.VillageViewSet)

urlpatterns = district_router.urls
