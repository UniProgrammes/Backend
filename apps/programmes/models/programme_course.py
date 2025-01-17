from django.db.models import ForeignKey, CASCADE, PositiveIntegerField, BooleanField

from apps.lib.models import UUIDModel


class ProgrammeCourse(UUIDModel):
    programme = ForeignKey("programmes.Programme", on_delete=CASCADE)
    course = ForeignKey("courses.Course", on_delete=CASCADE)

    year = PositiveIntegerField()
    is_mandatory = BooleanField(default=False)

    def __str__(self):
        return f"{self.course.name} in {self.programme.name} - Year {self.year}"
