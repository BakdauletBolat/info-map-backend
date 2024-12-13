from django.contrib import admin
from auth_user import models

admin.site.register(models.UserRole)
admin.site.register(models.UserProfile)
