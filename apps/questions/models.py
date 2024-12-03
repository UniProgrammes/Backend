from django.db.models import (
    CharField,
    CASCADE,
    ForeignKey,
    ManyToManyField,
    DateTimeField,
    EmailField,
)

from apps.lib.models import UUIDModel

# Create your models here.
class Question(UUIDModel):
    question_text = CharField(max_length=200)
    user = ForeignKey("users.User", on_delete=CASCADE, related_name="questions")
    user_email = EmailField()


    def __str__(self):
        return self.question_text
