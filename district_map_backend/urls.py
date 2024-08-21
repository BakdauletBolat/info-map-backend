from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from auth_user import views as auth_views

urlpatterns = [
    path('api/', include('district.urls')),
    path('api/', include('geometry.urls')),
    path('auth/token/', views.obtain_auth_token),
    path('auth/me/', auth_views.get_user),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns += geo_router.urls
