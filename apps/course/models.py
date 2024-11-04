from django.db.models import CharField, DecimalField, TextField

from apps.lib.models import UUIDModel

class Course(UUIDModel):
    courseName = CharField(max_length=255)
    courseCode = CharField(max_length=255)
    credits = DecimalField(max_digits=5, decimal_places=2)
    educationalLevel = CharField(max_length=255)
    courseDescription = TextField()
    mainArea = CharField(max_length=255)