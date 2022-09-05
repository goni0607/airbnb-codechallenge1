from django.db import models
from django.urls import reverse
from core import models as core_models


class Movie(core_models.Timestamped):
    """Movie Model Definition"""

    title = models.CharField(max_length=80)
    year = models.IntegerField()
    cover_image = models.ImageField()
    rating = models.IntegerField()
    category = models.ManyToManyField("categories.Category", blank=True)
    director = models.ForeignKey(
        "people.Person",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="fk_persion",
    )
    cast = models.ManyToManyField("people.Person", blank=True)

    def __str__(self):
        return f"{self.title}({self.year})"

    def get_absolute_url(self):
        return reverse("movies:detail", kwargs={"pk": self.pk})
