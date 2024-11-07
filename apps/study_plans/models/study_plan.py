from django.db import models
from django.db.models import CharField, ForeignKey, ManyToManyField

from apps.lib.models import UUIDModel


class StudyPlan(UUIDModel):
    name = CharField(max_length=255)
    status = CharField(max_length=255)
    user = ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="study_plans"
    )
    courses = ManyToManyField(
        "courses.Course",
        related_name="study_plans",
        through="study_plans.StudyPlanCourse",
        blank=True,
    )
