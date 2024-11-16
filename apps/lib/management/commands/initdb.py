from django.core.management.base import BaseCommand

from apps.degrees.models import Degree
from apps.programmes.models import Programme
from apps.degrees.factories import DegreeFactory
from apps.programmes.factories import ProgrammeFactory


class Command(BaseCommand):
    help = "Initialize the database with mock data for degrees and programmes."

    def handle(self, *args, **kwargs):
        degrees_with_programmes = {
            "Bachelor": [
                {"name": "Computer Science", "degree_type": "Bachelor"},
                {"name": "Mechanical Engineering", "degree_type": "Bachelor"},
            ],
            "Master": [
                {"name": "Data Science", "degree_type": "Master"},
                {"name": "Civil Engineering", "degree_type": "Master"},
            ],
        }

        for degree_name, programme_data in degrees_with_programmes.items():
            self.get_or_create_degree(degree_name)

            for data in programme_data:
                self.get_or_create_programme(data)

        self.stdout.write(self.style.SUCCESS("Database initialization complete!"))

    def get_or_create_degree(self, degree_name):
        degree = Degree.objects.filter(name=degree_name).first()
        if not degree:
            degree = DegreeFactory(name=degree_name)
            self.stdout.write(self.style.SUCCESS(f"Created degree: {degree.name}"))
        else:
            self.stdout.write(self.style.WARNING(f"Degree already exists: {degree.name}"))

    def get_or_create_programme(self, data):
        programme = Programme.objects.filter(
            name=data["name"], degree_type=data["degree_type"]
        ).first()

        if not programme:
            programme = ProgrammeFactory(**data)
            self.stdout.write(self.style.SUCCESS(f"Created programme: {programme.name}"))
        else:
            self.stdout.write(self.style.WARNING(f"Programme already exists: {programme.name}"))
