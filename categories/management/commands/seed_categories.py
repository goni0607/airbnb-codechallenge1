from django.core.management.base import BaseCommand
from categories.models import Category


class Command(BaseCommand):

    help = "Generate categories"

    def handle(self, *args, **options):
        kind = ("book", "movie", "both")
        name = ("history", "thriller", "comedy", "action")

        if (Category.objects.count() > 0):
            Category.objects.all().delete()

        for k in kind:
            for n in name:
                Category.objects.create(name=n, kind=k)
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Category created - name={n}, kind={k}"))
        self.stdout.write(self.style.SUCCESS("Categories created sucessfully"))
