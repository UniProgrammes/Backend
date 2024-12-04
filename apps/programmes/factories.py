import random
import factory
from factory.django import DjangoModelFactory

from apps.programmes.models import Programme, ProgrammeCourse
from apps.courses.factories import CourseFactory
from apps.lib.faker import fake


class ProgrammeFactory(DjangoModelFactory):
    class Meta:
        model = Programme

    name = factory.LazyFunction(fake.programme_name)
    degree_type = factory.Faker("random_element", elements=["Bachelor", "Master"])
    credits = factory.Faker("random_element", elements=[120, 180, 240])

    @factory.post_generation
    def courses(self, create, extracted, **kwargs):
        if not create:
            return

        courses = []
        if extracted:
            for course in extracted:
                ProgrammeCourse.objects.create(
                    programme=self,
                    course=course,
                    year=random.randint(1, 3),
                    period_months=random.randint(1, 12),
                    is_mandatory=random.choice([True, False]),
                )
                courses.append(course)
        else:
            for _ in range(50):
                course = CourseFactory()
                ProgrammeCourse.objects.create(
                    programme=self,
                    course=course,
                    year=random.randint(1, 3),
                    period_months=random.randint(1, 12),
                    is_mandatory=random.choice([True, False]),
                )
                courses.append(course)

        for index, course in enumerate(courses):
            potential_prereqs = courses[:index]
            num_prereqs = random.choice([0, 1, 2])
            selected_prereqs = random.sample(
                potential_prereqs, k=min(num_prereqs, len(potential_prereqs))
            )
            course.prerequisites.set(selected_prereqs)

class SimpleProgrammeFactory(DjangoModelFactory):
    class Meta:
        model = Programme

    name = factory.LazyFunction(fake.programme_name)
    degree_type = factory.Faker("random_element", elements=["Bachelor", "Master"])
    credits = factory.Faker("random_element", elements=[120, 180, 240])
