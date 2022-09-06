from django.views.generic import ListView, DetailView, UpdateView, CreateView
from . import models as models


class List(ListView):
    """List Class Definition"""

    model = models.Movie
    context_object_name = "movies"
    paginate_by = 10
    paginate_orphans = 5
    ordering = "-created_at"


class Detail(DetailView):

    """Detail Class Definition"""

    model = models.Movie


class Update(UpdateView):

    """Update Class Definition"""

    model = models.Movie
    template_name = "movies/movie_edit.html"
    fields = (
        "title",
        "year",
        "rating",
        "category",
        "director",
        "cast",
        "cover_image",
    )


class Create(CreateView):

    """Create Class Definition"""

    model = models.Movie
    template_name = "movies/movie_create.html"
    fields = (
        "title",
        "year",
        "rating",
        "category",
        "director",
        "cast",
        "cover_image",
    )
