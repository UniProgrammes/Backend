from django.db.models import CharField, TextField

from apps.lib.models import UUIDModel


class LearningOutcome(UUIDModel):
    description = TextField()
    category = CharField(max_length=255)

    def __str__(self):
        return f"{self.category} - {self.description}"
