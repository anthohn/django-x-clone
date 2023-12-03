from django.contrib import admin
from django.urls import path

from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)

import user.views
import post.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', user.views.signup_page, name='signup'),
    path('login/', LoginView.as_view(
            template_name='user/login.html',
            redirect_authenticated_user=True),
            name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='user/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
    template_name='user/password_change_done.html'),
        name='password_change_done'
        ),
    path('', post.views.home, name='home'),
]
