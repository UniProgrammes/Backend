from django.db.models import ForeignKey, CASCADE, IntegerField, BooleanField

from apps.lib.models import UUIDModel


class ProgrammeCourse(UUIDModel):
    programme = ForeignKey("programmes.Programme", on_delete=CASCADE)
    course = ForeignKey("courses.Course", on_delete=CASCADE)

    year = IntegerField()
    period_months = IntegerField()
    is_mandatory = BooleanField(default=False)
