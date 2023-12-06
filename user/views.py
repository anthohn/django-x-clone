from itertools import chain

from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

# from Post import Post


from . import models
from . import forms
from .forms import UpdateUserForm


from post.models import Post

# Create your views here.
def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            # set the uploader to the user before saving the model
            user.uploader = request.user
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'user/signup.html', context={'form': form})

@login_required
def view_user(request, user_username):
    view_user = get_object_or_404(models.User, username=user_username)
    registration_date = view_user.date_joined

    usersposts = Post.objects.filter(uploader=view_user)
    sorted_usersposts = sorted(
        chain(usersposts),
        key=lambda instance: instance.date_created,
        reverse=True
    )

    is_own_profile = False
    profile_form = None

    if request.user == view_user:
        is_own_profile = True
        # Si c'est le profil de l'utilisateur connecté, créez le formulaire de modification du profil
        profile_form = UpdateUserForm(instance=view_user)

        if request.method == 'POST':
            # Si le formulaire est soumis, traitez les données
            profile_form = UpdateUserForm(request.POST, instance=view_user)
            if profile_form.is_valid():
                profile_form.save()
                # Ajoutez une redirection ou un message de succès ici si nécessaire


    context = {
        'sorted_usersposts': sorted_usersposts,
        'view_user': view_user,
        'registration_date': registration_date,
        'is_own_profile': is_own_profile,
        'profile_form': profile_form,
    }

    return render(request, 'user/view_user.html', context=context)