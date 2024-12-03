import factory
from factory.django import DjangoModelFactory

from apps.learning_outcomes.models import LearningOutcome


class LearningOutcomeFactory(DjangoModelFactory):
    class Meta:
        model = LearningOutcome

    description = factory.Faker("sentence")
    category = factory.Faker("random_element", elements=["group work", "report writing"])
