from uuid import uuid4
from django.db.models import Model, UUIDField, DateTimeField


class UUIDModel(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
