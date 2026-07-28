from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Admin configuration for the custom User model.
    """

    list_display = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_active", "first_name")
    search_fields = ("username", "email")

    ordering = ("username",)
