from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.hashers import check_password
from django.db import models
from django.db.models.fields.files import FileField, FieldFile, ImageFieldFile
from django.shortcuts import resolve_url
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy


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

    date_joined = models.DateTimeField(
        gettext_lazy("date joined"), default=timezone.now
    )

    class Meta:
        verbose_name = gettext_lazy("myuser")
        verbose_name_plural = gettext_lazy("myusers")

    def __str__(self):
        return f"{self.email}({self.nickname})"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def avatar_url(self):
        # a: ImageFieldFile = self.avatar
        if self.avatar:
            return self.avatar.url
        else:
            return reverse("django_pydenticon:identicon", args=[self.user.email])
