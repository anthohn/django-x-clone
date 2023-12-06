from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    profile_photo = models.ImageField(verbose_name='Photo de profil')
    bio = models.TextField(verbose_name='Biographie', blank=True, null=True)

    follows = models.ManyToManyField(
        # indique que la relation se fait avec le même modèle User.
        'self',
        related_name='followers',
        #  indique que la relation n'est pas symétrique. En d'autres termes, si l'utilisateur A suit l'utilisateur B, cela ne signifie pas nécessairement que l'utilisateur B suit l'utilisateur A.
        symmetrical=False,
    )