from .base import *
import django.db.backends.postgresql

INSTALLED_APPS += [
    "debug_toolbar",
    "accounts",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_test",
        "USER": "swook",
        "PASSWORD": "swook",
        "HOST": "localhost",
        "PORT": "",
    }
}
