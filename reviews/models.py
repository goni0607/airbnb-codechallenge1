from django.db import models
from core import models as core_models


class Review(core_models.Timestamped):
    """Review Model Definition"""

    created_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )
    text = models.TextField()
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.created_by.username} - {self.text}"
