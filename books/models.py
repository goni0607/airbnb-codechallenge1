from django.db import models
from django.urls import reverse
from core import models as core_models


class Book(core_models.Timestamped):
    """Book Model Definition"""

    title = models.CharField(max_length=200)
    year = models.IntegerField()
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books",
    )
    cover_image = models.ImageField()
    rating = models.IntegerField()
    writer = models.ForeignKey(
        "people.Person",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books",
    )

    def __str__(self):
        return f"{self.title}({self.year})"

    def get_absolute_url(self):
        return reverse("books:detail", kwargs={"pk": self.pk})
