import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews.models import Review
from users.models import User
from books.models import Book
from movies.models import Movie


class Command(BaseCommand):

    help = "This command creates reviews"

    def add_arguments(self, parser):
        parser.add_argument("--total",
                            default=1,
                            type=int,
                            help="How many reviews do you want to create?")

    def handle(self, *args, **options):
        number = options.get("total")
        seeder = Seed.seeder()
        all_users = User.objects.all()
        all_movies = Movie.objects.all()
        all_books = Book.objects.all()
        seeder.add_entity(
            Review, number, {
                "created_by": lambda x: random.choice(all_users),
                "text": lambda x: seeder.faker.sentence(),
                "book": lambda x: random.choice(all_books),
                "movie": lambda x: random.choice(all_movies),
                "rating": lambda x: random.randrange(1, 5 + 1)
            })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews(s) created!"))
