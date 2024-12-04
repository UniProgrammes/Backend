from factory.django import DjangoModelFactory
from factory import SubFactory
from factory.faker import Faker

from apps.study_plans.models import StudyPlan, StudyPlanCourse
from apps.users.factories import UserFactory
from apps.courses.factories import SimpleCourseFactory

class StudyPlanFactory(DjangoModelFactory):
    class Meta:
        model = StudyPlan

    name = Faker("name")
    user = SubFactory(UserFactory)


class StudyPlanCourseFactory(DjangoModelFactory):
    class Meta:
        model = StudyPlanCourse

    study_plan = SubFactory(StudyPlanFactory)
    course = SubFactory(SimpleCourseFactory)
    semester = Faker("random_int", min=1, max=8)
