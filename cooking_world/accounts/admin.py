from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from cooking_world.accounts.models import AppUser, Profile


# admin.site.register(AppUser)
@admin.register(AppUser)
class UserAdmin(UserAdmin):
    list_display = ("email", "is_staff","is_superuser")
    list_filter = ("is_staff", "is_superuser", "groups")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    readonly_fields = ("date_joined",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
