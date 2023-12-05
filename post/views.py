from itertools import chain
from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from . import models
from . import forms

@login_required
def homepage(request):
    form = forms.PostForm()
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # set the uploader to the user before saving the model
            post.uploader = request.user
            # now we can save
            post.save()
            return redirect('homepage')


    posts = models.Post.objects.all()
    sorted_posts = sorted(
        chain(posts),
        key=lambda instance: instance.date_created,
        reverse=True
    )

    context = {
        'sorted_posts': sorted_posts,
    }

    return render(request, 'post/homepage.html', context=context)

@login_required
def post_upload(request):
    form = forms.PostForm()
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # set the uploader to the user before saving the model
            post.uploader = request.user
            # now we can save
            post.save()
            return redirect('homepage')
    return render(request, 'post/post_upload.html', context={'form': form})

@login_required
def view_post(request, post_id):
    post = get_object_or_404(models.Post, id=post_id)
    return render(request, 'post/view_post.html', {'post': post})

