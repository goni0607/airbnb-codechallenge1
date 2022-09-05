import random
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand
from django_seed import Seed
from movies.models import Movie
from categories.models import Category
from people.models import Person


class Command(BaseCommand):

    help = "This command creates movies"

    def add_arguments(self, parser):
        parser.add_argument("--total",
                            default=1,
                            type=int,
                            help="How many movies do you want to create?")

    def handle(self, *args, **options):
        number = options.get("total")
        seeder = Seed.seeder()
        movie_categories = Category.objects.filter(kind="movie")
        all_people = Person.objects.all()
        seeder.add_entity(
            Movie, number, {
                "title": lambda x: seeder.faker.sentence(),
                "director": lambda x: random.choice(all_people),
                "year": lambda x: random.randrange(1900, 2022 + 1),
                "rating": lambda x: random.randrange(1, 5 + 1)
            })
        created_movies = seeder.execute()
        created_clean = flatten(list(created_movies.values()))

        for pk in created_clean:
            movie = Movie.objects.get(pk=pk)

            for c in movie_categories:
                masic_number = random.randint(0, movie_categories.count())
                if masic_number % 2 == 0:
                    movie.category.add(c)
            for p in all_people:
                masic_number = random.randint(0, all_people.count())
                if masic_number % 2 == 0:
                    movie.cast.add(p)

        self.stdout.write(self.style.SUCCESS(f"{number} movie(s) created!"))
