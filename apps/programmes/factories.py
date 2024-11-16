import random
import factory
from factory.django import DjangoModelFactory

from apps.programmes.models import Programme, ProgrammeCourse
from apps.courses.factories import CourseFactory


class ProgrammeFactory(DjangoModelFactory):
    class Meta:
        model = Programme

    name = factory.Faker("word")
    degree_type = factory.Faker("random_element", elements=["Bachelor", "Master"])
    credits = factory.Faker("random_element", elements=[120, 180, 240])

    @factory.post_generation
    def courses(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for course in extracted:
                ProgrammeCourse.objects.create(
                    programme=self,
                    course=course,
                    year=random.randint(1, 3),
                    period_months=random.randint(1, 12),
                    is_mandatory=random.choice([True, False]),
                )
        else:
            courses = CourseFactory.create_batch(50)
            for course in courses:
                ProgrammeCourse.objects.create(
                    programme=self,
                    course=course,
                    year=random.randint(1, 3),
                    period_months=random.randint(1, 12),
                    is_mandatory=random.choice([True, False]),
                )
