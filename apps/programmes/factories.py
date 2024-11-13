import factory
from factory.django import DjangoModelFactory

from apps.programmes.models import Programme


class ProgrammeFactory(DjangoModelFactory):
    class Meta:
        model = Programme

    name = factory.Faker("word")
    degree_type = factory.Faker("word")
    credits = factory.Faker("pydecimal", left_digits=2, right_digits=1, positive=True)

    @factory.post_generation
    def courses(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for course in extracted:
                self.programmecourse_set.create(course=course)
