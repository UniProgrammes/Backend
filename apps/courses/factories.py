import factory
from factory.django import DjangoModelFactory

from apps.courses.models import Course


class CourseFactory(DjangoModelFactory):
    class Meta:
        model = Course

    name = factory.Faker("word")
    code = factory.Faker("word")
    credits = factory.Faker("pydecimal", left_digits=2, right_digits=1, positive=True)
    educational_level = factory.Faker("word")
    description = factory.Faker("sentence")
    main_area = factory.Faker("random_element", elements=["ELA", "DVA"])

    @factory.post_generation
    def prerequisites(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for prereq in extracted:
                self.prerequisites.add(prereq)
