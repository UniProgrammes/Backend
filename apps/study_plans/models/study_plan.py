from django.db.models import (
    CharField,
    CASCADE,
    ForeignKey,
    ManyToManyField,
)

from apps.lib.models import UUIDModel


class StudyPlan(UUIDModel):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("completed", "Completed"),
    ]
    name = CharField(max_length=255)
    status = CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    user = ForeignKey("users.User", on_delete=CASCADE, related_name="study_plans")
    courses = ManyToManyField(
        "courses.Course",
        related_name="study_plans",
        through="study_plans.StudyPlanCourse",
        blank=True,
    )

    @property
    def is_valid(self):
        return len(self.not_satisfied_prerequisites) == 0


    @property
    def not_satisfied_prerequisites(self) -> list[dict]:
        study_plan_courses = self.study_plan_courses.all().select_related("course")

        course_semesters = {str(spc.course_id): spc.semester for spc in study_plan_courses}
        not_satisfied_prerequisites = []

        for spc in study_plan_courses:
            prerequisites = spc.course.prerequisites.all()
            for prerequisite in prerequisites:
                if str(prerequisite.id) in course_semesters:
                    prereq_semester = course_semesters[str(prerequisite.id)]
                    current_semester = course_semesters[str(spc.course_id)]

                    if prereq_semester >= current_semester:
                        not_satisfied_prerequisites.append({
                            "course": str(spc.course_id),
                            "prerequisite": str(prerequisite.id),
                        })

        return not_satisfied_prerequisites
