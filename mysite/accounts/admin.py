from django.contrib import admin
from .models import MyUser


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "nickname", "created_at"]
    list_display_links = ["email"]