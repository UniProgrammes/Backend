from django.db.models import ForeignKey, CASCADE

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

    class Meta:
        unique_together = [("study_plan", "course")]

    def __str__(self):
        return f"{self.course.name} in {self.study_plan.name}"
