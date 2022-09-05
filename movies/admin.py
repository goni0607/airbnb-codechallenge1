from django.contrib import admin
from . import models


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "year",
        "rating",
        "director",
    )

    list_filter = (
        "title",
        "year",
        "rating",
        "category",
        "director",
        "cast",
    )
