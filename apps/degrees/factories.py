import random
import factory
from factory.django import DjangoModelFactory

from apps.degrees.models import Degree, DegreeProgramme
from apps.programmes.factories import ProgrammeFactory


class DegreeFactory(DjangoModelFactory):
    class Meta:
        model = Degree

    name = factory.Faker("word")

    @factory.post_generation
    def programmes(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for programme in extracted:
                DegreeProgramme.objects.create(
                    degree=self,
                    programme=programme,
                    period_years=random.randint(1, 4),
                )
                programme.save()
        else:
            programmes = ProgrammeFactory.create_batch(4)
            for programme in programmes:
                DegreeProgramme.objects.create(
                    degree=self,
                    programme=programme,
                    period_years=random.randint(1, 4),
                )
                programme.save()


class SimpleDegreeFactory(DjangoModelFactory):
    class Meta:
        model = Degree

    name = factory.Faker("word")
