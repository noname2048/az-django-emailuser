from django.urls import path, re_path, include
import django_pydenticon.urls

app_name = "accounts"

urlpatterns = [
    re_path(r"^identicon/", include(django_pydenticon.urls.get_patterns())),
]
