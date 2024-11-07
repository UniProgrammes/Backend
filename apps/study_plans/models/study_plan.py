from django.db.models import CharField, DateTimeField, CASCADE, ForeignKey, ManyToManyField

from apps.lib.models import UUIDModel


class StudyPlan(UUIDModel):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("completed", "Completed"),
    ]
    name = CharField(max_length=255)
    status = CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    user = ForeignKey(
        "users.User", on_delete=CASCADE, related_name="study_plans"
    )
    courses = ManyToManyField(
        "courses.Course",
        related_name="study_plans",
        through="study_plans.StudyPlanCourse",
        blank=True,
    )
