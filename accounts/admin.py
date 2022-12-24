from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts import models

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = models.CustomUser
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (                    
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "role",
                    "profile_image",
                    "password",             
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)


admin.site.register(models.CustomUser, CustomUserAdmin)
admin.site.register(models.Roles)