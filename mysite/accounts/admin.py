from django.contrib import admin
from .models import MyUser


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "is_staff", "nickname", "date_joined"]
    list_display_links = ["email"]
