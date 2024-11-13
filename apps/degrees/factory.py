import factory
from factory.django import DjangoModelFactory

from apps.degrees.models import Degree


class DegreeFactory(DjangoModelFactory):
    class Meta:
        model = Degree

    name = factory.Faker("word")
