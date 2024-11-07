from django.db.models import ForeignKey, CASCADE, PositiveIntegerField, BooleanField

from apps.lib.models import UUIDModel


class StudyPlanCourse(UUIDModel):
    study_plan = ForeignKey(
        "study_plans.StudyPlan",
        on_delete=CASCADE,
        related_name="study_plan_courses",
    )
    course = ForeignKey(
        "courses.Course", on_delete=CASCADE, related_name="study_plan_courses"
    )
    semester = PositiveIntegerField()
    is_completed = BooleanField(default=False)
