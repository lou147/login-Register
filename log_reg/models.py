from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    belong = models.OneToOneField(to=User, related_name='profile')
    name = models.CharField(max_length=24, null=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField()
    avatar = models.ImageField()

    def __str__(self):
        return str(self.name)
