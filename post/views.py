from django.shortcuts import render

from . import models

def home(request):
    # posts = models.Post.objects.all()
    return render(request, 'post/home.html'
                #   , context={'posts': posts}
                  )

