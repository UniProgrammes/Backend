import random
import factory
from factory.django import DjangoModelFactory

from apps.courses.models import Course
from apps.learning_outcomes.factories import LearningOutcomeFactory
from apps.lib.faker import fake


class CourseFactory(DjangoModelFactory):
    class Meta:
        model = Course

    name = factory.LazyFunction(fake.course_name)
    code = factory.Faker("bothify", text="???###")
    credits = factory.Faker("random_element", elements=[3, 5, 6, 10])
    educational_level = factory.Faker(
        "random_element",
        elements=["Beginner", "Intermediate", "Advanced", "Expert"],
    )
    description = factory.Faker("sentence")
    main_area = factory.Faker("random_element", elements=["ELA", "DVA"])
    semester = factory.Faker("random_element", elements=[1, 2])
    period = factory.Faker("random_element", elements=[1, 2, 3])

    @factory.post_generation
    def learning_outcomes(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.learning_outcomes.set(extracted)
        else:
            num_outcomes = random.choice([0, 1, 2])
            outcomes = LearningOutcomeFactory.create_batch(num_outcomes)
            self.learning_outcomes.set(outcomes)


class SimpleCourseFactory(DjangoModelFactory):
    class Meta:
        model = Course

    name = factory.Faker("word")
    credits = 5
