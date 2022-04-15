from django.contrib import admin

from cooking_world.main.models import Blog, Recipe


@admin.register(Blog)
class PetAdmin(admin.ModelAdmin):
    list_display = ("title", )

@admin.register(Recipe)
class PetAdmin(admin.ModelAdmin):
    list_display = ("title", )


