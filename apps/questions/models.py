from django.db.models import (
    CharField,
    CASCADE,
    ForeignKey,
    DateTimeField,
)

from apps.lib.models import UUIDModel

# Create your models here.
class Question(UUIDModel):
    text = CharField(max_length=200)
    user = ForeignKey("users.User", on_delete=CASCADE, related_name="questions")

    def __str__(self):
        return self.text
