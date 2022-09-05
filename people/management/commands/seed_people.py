from django.core.management.base import BaseCommand
from django_seed import Seed
from people.models import Person


class Command(BaseCommand):

    help = "This command creates people"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=1,
            type=int,
            help="How many people do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("total")
        seeder = Seed.seeder()
        seeder.add_entity(
            Person, number, {"name": lambda x: seeder.faker["en-US"].name()}
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} people created!"))
