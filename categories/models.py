from django.db import models
from core import models as core_models


class Category(core_models.Timestamped):
    """Category Model Definition"""

    KIND_BOOK = "book"
    KIND_MOVIE = "movie"
    KIND_BOTH = "both"

    KIND_CHOICES = (
        (KIND_BOOK, "Book"),
        (KIND_MOVIE, "Movie"),
        (KIND_BOTH, "Both"),
    )

    name = models.CharField(max_length=80)
    kind = models.CharField(max_length=10, choices=KIND_CHOICES, default=KIND_BOTH)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}({self.kind})"
