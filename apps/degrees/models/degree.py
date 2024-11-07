from django.db.models import CharField, ManyToManyField

from apps.lib.models import UUIDModel


class Degree(UUIDModel):
    name = CharField(max_length=255)

    programmes = ManyToManyField(
        "programmes.Programme",
        related_name="degrees",
        through="degrees.DegreeProgramme",
        blank=True,
    )
