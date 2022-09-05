from django.shortcuts import render
# from django.core.paginator import Paginator
from books import models as book_models
from movies import models as movie_models
from people import models as people_models


def home(request):
    # page_b = request.GET.get("page_b", 1)
    # page_m = request.GET.get("page_m", 1)
    # page_p = request.GET.get("page_p", 1)

    book_list = book_models.Book.objects.all().order_by('-created_at')[0:10]
    movie_list = movie_models.Movie.objects.all().order_by('-created_at')[0:10]
    people_list = people_models.Person.objects.all().order_by(
        '-created_at')[0:10]

    # book_paginator = Paginator(book_list, 10, orphans=2)
    # movie_paginator = Paginator(movie_list, 10, orphans=2)
    # people_paginator = Paginator(people_list, 10, orphans=2)

    # books = book_paginator.page(int(page_b))
    # movies = movie_paginator.page(int(page_m))
    # people = people_paginator.page(int(page_p))

    return render(request, "home.html", {
        "books": book_list,
        "movies": movie_list,
        "people": people_list,
    })


def search(request):
    return render(request, "search.html")


def genres(request, genre='all'):
    return render(request, "genre.html", context={
        "genre": genre,
    })
