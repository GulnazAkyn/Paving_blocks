from django.contrib import admin
from .models import User

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):

    list_display = ['id', 'username', 'email', 'phone']
    list_filter = ['is_admin']
    filter_horizontal = ()

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal information", {"fields": ("phone", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_admin",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", )}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", 'email', 'phone'),
            },
        ),
    )


admin.site.register(User, UserAdmin)
