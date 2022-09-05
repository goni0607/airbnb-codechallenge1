import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from books.models import Book
from categories.models import Category
from people.models import Person


class Command(BaseCommand):

    help = "This command creates books"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total", default=1, type=int, help="How many books do you want to create?")

    def handle(self, *args, **options):
      number = options.get("total")
      seeder = Seed.seeder()
      book_categories = Category.objects.filter(kind="book")
      all_people = Person.objects.all()
      seeder.add_entity(Book, number, {"category": lambda x: random.choice(book_categories), 
                                       "writer": lambda x: random.choice(all_people),
                                      "year": lambda x: random.randrange(1900, 2022+1),
                                      "rating": lambda x: random.randrange(1,5+1)})
      seeder.execute()
      self.stdout.write(self.style.SUCCESS(f"{number} book(s) created!"))
      
