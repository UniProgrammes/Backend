from django.db.models import ForeignKey, CASCADE, IntegerField

from apps.lib.models import UUIDModel


class DegreeProgramme(UUIDModel):
    degree = ForeignKey("degrees.Degree", on_delete=CASCADE)
    programme = ForeignKey("programmes.Programme", on_delete=CASCADE)
    period_years = IntegerField()
