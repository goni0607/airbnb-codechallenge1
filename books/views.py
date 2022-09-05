from django.views.generic import ListView, DetailView, UpdateView, CreateView
from . import models as models


class List(ListView):

    """List Class Definition"""

    model = models.Book
    context_object_name = "books"
    paginate_by = 10
    paginate_orphans = 5
    ordering = "-created_at"


class Detail(DetailView):

    """Detail Class Definition"""

    model = models.Book


class Update(UpdateView):

    """Update Class Definition"""

    model = models.Book
    template_name = "books/book_edit.html"
    fields = (
        "title",
        "year",
        "category",
        "rating",
        "writer",
    )


class Create(CreateView):

    model = models.Book
    template_name = "books/book_create.html"
    fields = (
        "title",
        "year",
        "category",
        "rating",
        "writer",
    )


# class detail(request, pk):
#     try:
#         book = models.Book.objects.get(pk=pk)
#         return render(request, "books/detail.html", {"book": book})
#     except models.Book.DoesNotExist:
#         raise Http404()
