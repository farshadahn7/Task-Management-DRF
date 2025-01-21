from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "is_staff", "is_active", 'is_verified', 'created_date','updated_date')
    list_filter = ("username", "email", "is_staff", "is_active", 'is_verified')
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", 'is_verified', "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "email", "password1", "password2", "is_staff",
                "is_active", 'is_verified', "groups", "user_permissions"
            )}
         ),
    )
    search_fields = ("username", "email")
    ordering = ("username", "email")