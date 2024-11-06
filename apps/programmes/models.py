from django.db.models import CharField, DecimalField

from apps.lib.models import UUIDModel


class Programme(UUIDModel):
    name = CharField(max_length=255)
    degree_type = CharField(max_length=255)
    credits = DecimalField(max_digits=5, decimal_places=2)
