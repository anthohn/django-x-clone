from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    profile_photo = models.ImageField(verbose_name='Photo de profil')
    bio = models.TextField(verbose_name='Biographie', blank=True, null=True)