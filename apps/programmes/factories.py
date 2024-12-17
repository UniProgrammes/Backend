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
    credits = factory.Faker("random_element", elements=[60, 120, 180])

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
                    year=random.randint(1, 4),
                    is_mandatory=random.choice([True, False]),
                )
                courses.append(course)
        else:
            for _ in range(50):
                course = CourseFactory()
                ProgrammeCourse.objects.create(
                    programme=self,
                    course=course,
                    year=random.randint(1, 4),
                    is_mandatory=random.choice([True, False]),
                )
                courses.append(course)

        for index, course in enumerate(courses):
            potential_prereqs = courses[:index]

            valid_prereqs = []
            for prereq in potential_prereqs:
                if prereq == course:
                    continue
                if prereq.year < course.year:
                    valid_prereqs.append(prereq)
                elif prereq.year == course.year and prereq.semester < course.semester:
                    valid_prereqs.append(prereq)
                elif (
                    prereq.year == course.year
                    and prereq.semester == course.semester
                    and prereq.period == 1
                    and course.period == 2
                ):
                    valid_prereqs.append(prereq)

            num_prereqs = random.choice([0, 1, 2])
            selected_prereqs = random.sample(valid_prereqs, k=min(num_prereqs, len(valid_prereqs)))
            course.prerequisites.set(selected_prereqs)


class SimpleProgrammeFactory(DjangoModelFactory):
    class Meta:
        model = Programme

    name = factory.LazyFunction(fake.programme_name)
    credits = factory.Faker("random_element", elements=[60, 120, 180])
