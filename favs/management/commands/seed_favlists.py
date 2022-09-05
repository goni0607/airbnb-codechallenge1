import random
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand
from django_seed import Seed
from favs.models import FavList
from books.models import Book
from movies.models import Movie
from users.models import User


class Command(BaseCommand):

    help = "This command creates favorite Lists"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=1,
            type=int,
            help="How many favorite lists do you want to create?")

    def handle(self, *args, **options):
        number = options.get("total")
        seeder = Seed.seeder()
        all_books = Book.objects.all()
        all_movies = Movie.objects.all()
        all_users = User.objects.all()

        seeder.add_entity(FavList, number, {
            "created_by": lambda x: random.choice(all_users),
        })
        created_lists = seeder.execute()
        created_clean = flatten(list(created_lists.values()))

        for pk in created_clean:
            fav = FavList.objects.get(pk=pk)

            for b in all_books:
                magic_number = random.randint(1, all_books.count())
                if magic_number % 2 == 0:
                    fav.books.add(b)
            for m in all_movies:
                magic_number = random.randint(1, all_movies.count())
                if magic_number % 2 == 0:
                    fav.movies.add(m)

        self.stdout.write(self.style.SUCCESS(f"{number} list(s) created!"))
