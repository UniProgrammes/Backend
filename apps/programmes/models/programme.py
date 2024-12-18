from django.db.models import CharField, DecimalField, ManyToManyField

from apps.lib.models import UUIDModel


class Programme(UUIDModel):
    name = CharField(max_length=255)
    credits = DecimalField(max_digits=5, decimal_places=2)

    courses = ManyToManyField(
        "courses.Course",
        related_name="programmes",
        through="programmes.ProgrammeCourse",
        blank=True,
    )

    @property
    def degree_type(self):
        degrees = getattr(self, "degrees", None)
        if degrees:
            degree = degrees.first()
            return degree.name if degree else None
        return None

    def __str__(self):
        return f"{self.name} - Degree: {self.degree_type or 'No Degree'}"
