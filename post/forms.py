from django.db import models
from . import models
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['image', 'content']

    # Dans la méthode __init__, on appelle d'abord le constructeur de la classe mère (super(PostForm, self).__init__(*args, **kwargs)) pour s'assurer que toutes les initialisations nécessaires sont effectuées.
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['image', 'content']


    # Dans la méthode __init__, on appelle d'abord le constructeur de la classe mère (super(PostForm, self).__init__(*args, **kwargs)) pour s'assurer que toutes les initialisations nécessaires sont effectuées.
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False  
    