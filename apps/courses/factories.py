import random
import factory
from factory.django import DjangoModelFactory

from apps.courses.models import Course
from apps.programmes.models import ProgrammeCourse
from apps.learning_outcomes.factories import LearningOutcomeFactory
from apps.lib.faker import fake


class CourseFactory(DjangoModelFactory):
    class Meta:
        model = Course

    name = factory.LazyFunction(fake.course_name)
    code = factory.Faker("bothify", text="???###")
    credits = factory.Faker("random_element", elements=[3, 5, 6, 10])
    educational_level = factory.Faker("word")
    description = factory.Faker("sentence")
    main_area = factory.Faker("random_element", elements=["ELA", "DVA"])

    @factory.post_generation
    def prerequisites(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            self.prerequisites.set(extracted)
        else:
            programme_courses = ProgrammeCourse.objects.filter(
                programme=self.programmes.first()
            )
            potential_prereqs = programme_courses.exclude(course=self).values_list(
                "course", flat=True
            )

            num_prereqs = random.choice([0, 1, 2])
            selected_prereqs = random.sample(
                list(potential_prereqs), k=min(num_prereqs, len(potential_prereqs))
            )
            self.prerequisites.set(selected_prereqs)

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
