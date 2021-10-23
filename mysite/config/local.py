from .base import *
import django.db.backends.postgresql

INSTALLED_APPS += [
    "debug_toolbar",
    "django_pydenticon",
    "accounts",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config["DB_NAME"],
        "USER": config["DB_USER"],
        "PASSWORD": config["DB_PASSWORD"],
        "HOST": "localhost",
        "PORT": "",
    }
}
