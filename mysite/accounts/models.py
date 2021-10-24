from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.db.models.fields.files import FileField, FieldFile, ImageFieldFile
from django.shortcuts import resolve_url
from django.urls import reverse


class MyUserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, nickname, password):
        superuser = self.create_user(
            email=email,
            nickname=nickname,
            password=password,
        )
        superuser.is_admin = True
        superuser.save(using=self._db)
        return superuser


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(
        "닉네임", max_length=30, blank=False, unique=True, default=""
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to="image/avatar/",
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickname"]

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return f"{self.email}({self.nickname})"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def avatar_url(self):
        # a: ImageFieldFile = self.avatar
        if self.avatar:
            return self.avatar.url
        else:
            return reverse("django_pydenticon:identicon", args=[self.user.email])

    @property
    def is_staff(self):
        return self.is_admin
