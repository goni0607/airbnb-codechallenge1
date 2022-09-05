from django.db import models
from core import models as core_models


class FavList(core_models.Timestamped):
    """FavList Model Definition"""

    created_by = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="favs"
    )
    books = models.ManyToManyField("books.Book", blank=True, related_name="favs")
    movies = models.ManyToManyField("movies.Movie", blank=True, related_name="favs")

    class Meta:
        verbose_name = "Favorite List"

    def __str__(self):
        return f"list for {self.created_by.username}"
