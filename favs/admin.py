from django.contrib import admin
from . import models


@admin.register(models.FavList)
class FavListAdmin(admin.ModelAdmin):

    list_display = ("created_by",)
