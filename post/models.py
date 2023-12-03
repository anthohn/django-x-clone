from django.db import models
from django.conf import settings

class Post(models.Model):
    image = models.ImageField(null=True)
    content = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
