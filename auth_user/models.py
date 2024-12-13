from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from rest_framework.authtoken.models import Token
from geometry.models import GeometryObjectCategory

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserRole(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(GeometryObjectCategory, blank=True, related_name='categories')

    def __str__(self):
        return str(self.name)

class UserProfile(models.Model):
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='profile')

    def __str__(self):
        return f"{self.role.name} {self.user.username}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
