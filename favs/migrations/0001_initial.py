# Generated by Django 4.1 on 2022-09-05 00:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("books", "0001_initial"),
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FavList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "books",
                    models.ManyToManyField(
                        blank=True, related_name="favs", to="books.book"
                    ),
                ),
                (
                    "created_by",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="favs",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "movies",
                    models.ManyToManyField(
                        blank=True, related_name="favs", to="movies.movie"
                    ),
                ),
            ],
            options={
                "verbose_name": "Favorite List",
            },
        ),
    ]
