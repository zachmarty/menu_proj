from django.contrib import admin
from menu.models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "parent",
        "slug",
    )
    list_filter = ("id", "name", "parent")
    search_fields = ("name", "parent")
    prepopulated_fields = {"slug": ("name",)}


# Register your models here.
