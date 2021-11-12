from django.urls import path, re_path, include
import django_pydenticon.urls
from django.conf.urls import url
from django_pydenticon.views import image as pydenticon_image
from .views import signup_view, welcome_view


app_name = "accounts"

urlpatterns = [
    path("identicon/<path:data>", pydenticon_image, name="identicon"),
    path("signup", signup_view, name="signup"),
    path("welcome", welcome_view, name="welcome"),
]
