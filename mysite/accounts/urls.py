from django.urls import path, re_path
import django_pydenticon.urls

app_name = "accounts"

urlpatterns = [
    re_path("^identicon/", django_pydenticon.urls.get_patterns(), name="identicon"),
]
