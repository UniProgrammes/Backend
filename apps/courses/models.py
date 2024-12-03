from django.db.models import CharField, DecimalField, TextField, ManyToManyField

from apps.lib.models import UUIDModel


class Course(UUIDModel):
    name = CharField(max_length=255)
    code = CharField(max_length=255)
    credits = DecimalField(max_digits=5, decimal_places=2)
    educational_level = CharField(max_length=255)
    description = TextField()
    main_area = CharField(max_length=255)

    learning_outcomes = ManyToManyField(
        "learning_outcomes.LearningOutcome",
        related_name="courses",
        blank=True,
    )

    prerequisites = ManyToManyField("self", symmetrical=False, blank=True)
