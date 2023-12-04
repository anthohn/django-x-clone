from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.urls import include, path
from django.views.generic.base import RedirectView


import user.views
import post.views

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
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
    path('', RedirectView.as_view(url='home/')),
    path('home', post.views.home, name='home'),
    path('post/upload/', post.views.post_upload, name='post_upload'),
    path('post/<int:post_id>', post.views.view_post, name='view_post'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
