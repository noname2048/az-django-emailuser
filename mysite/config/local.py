from .base import *
import django.db.backends.postgresql

INSTALLED_APPS += [
    "debug_toolbar",
    "django_pydenticon",
    "accounts",
    "drf_yasg",
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

STATIC_URL = "/static/"  # static(주소창에서의 주소)
STATICFILES_DIRS = [  # 개발용 static files
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "static_root"  # 업로드용 모음 파일 이름(debug=False 일 때만 작동)
