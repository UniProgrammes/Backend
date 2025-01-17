from django.db.models import (
    CharField,
    DecimalField,
    TextField,
    ManyToManyField,
    PositiveIntegerField,
)

from apps.lib.models import UUIDModel


class Course(UUIDModel):
    PERIOD_CHOICES = [
        (1, "First Period"),
        (2, "Second Period"),
        (3, "Both Periods"),
    ]
    name = CharField(max_length=255)
    code = CharField(max_length=255)
    credits = DecimalField(max_digits=5, decimal_places=2)
    educational_level = CharField(max_length=255)
    description = TextField()
    main_area = CharField(max_length=255)
    semester = PositiveIntegerField(default=1)
    period = PositiveIntegerField(choices=PERIOD_CHOICES, default=3)

    learning_outcomes = ManyToManyField(
        "learning_outcomes.LearningOutcome",
        related_name="courses",
        blank=True,
    )

    prerequisites = ManyToManyField("self", symmetrical=False, blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"
