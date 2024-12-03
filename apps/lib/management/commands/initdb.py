from django.core.management.base import BaseCommand

from apps.degrees.models import Degree
from apps.degrees.factories import DegreeFactory


class Command(BaseCommand):
    help = "Initialize the database with mock data."

    def handle(self, *args, **kwargs):
        degree_names = ["Bachelor", "Master"]

        for degree_name in degree_names:
            degree = Degree.objects.filter(name=degree_name).first()
            if not degree:
                degree = DegreeFactory(name=degree_name)
                self.stdout.write(self.style.SUCCESS(f"Created degree: {degree.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Degree already exists: {degree.name}"))
