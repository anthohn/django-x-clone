from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from . import models


from . import forms

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

# @login_required
# def view_user(request, user_username):
#     user = get_object_or_404(models.User, username=user_username)
#     return render(request, 'user/view_user.html', {'user': user})