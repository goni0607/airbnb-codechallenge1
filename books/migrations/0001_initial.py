# Generated by Django 4.1 on 2022-09-05 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("people", "0001_initial"),
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=200)),
                ("year", models.IntegerField()),
                ("cover_image", models.ImageField(upload_to="")),
                ("rating", models.IntegerField()),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="books",
                        to="categories.category",
                    ),
                ),
                (
                    "writer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="books",
                        to="people.person",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]