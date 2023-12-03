from django.db import models
from . import models
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['image', 'content']