from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from newspaper.models import Topic, Newspaper, Redactor


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "published_date",
        "topic",
    )
    search_fields = (
        "title",
        "publishers",
        "published_date",
    )
    list_filter = (
        "title",
        "publishers",
        "published_date",
    )


@admin.register(Redactor)
class Redactor(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "years_of_experience",
                )
            },
        ),
    )
