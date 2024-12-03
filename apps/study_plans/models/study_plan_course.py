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

    class Meta:
        unique_together = [("study_plan", "course", "semester")]

    def __str__(self):
        return f"{self.course.name} in {self.study_plan.name} - Semester {self.semester}"
