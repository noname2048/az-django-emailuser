from django.contrib.auth.backends import BaseBackend
from .models import MyUser

from django.contrib.auth.hashers import check_password


class MyBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        email = kwargs.get("email")
        password = kwargs.get("password")

        if not (email and password):
            return None

        try:
            user = MyUser.objects.get(email=email)
            # param1: plain-text
            # param2: db-password
            if not check_password(password, user.password):
                return None

        except MyUser.DoesNotExist:
            return None

        return user

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None
