from django.views.generic import ListView, DetailView, UpdateView, CreateView
from . import models as models


class List(ListView):

    """List Class Definition"""

    model = models.Person
    context_object_name = "people"
    paginate_by = 10
    paginate_orphans = 5
    ordering = "-created_at"


class Detail(DetailView):

    """Detail Class Definition"""

    model = models.Person


class Update(UpdateView):

    """Update Class Definition"""

    model = models.Person
    template_name = "people/person_edit.html"
    fields = (
        "name",
        "kind",
    )


class Create(CreateView):

    """Create Class Definition"""

    model = models.Person
    template_name = "people/person_edit.html"
    fields = (
        "name",
        "kind",
    )
