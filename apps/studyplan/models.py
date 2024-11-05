# models.py
from django.db.models import CharField, DateTimeField, ForeignKey, CASCADE

from apps.lib.models import UUIDModel

class StudyPlan(UUIDModel):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('completed', 'Completed'),
    ]

    name = CharField(max_length=255)
    status = CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    user = ForeignKey(User, on_delete=CASCADE, related_name='study_plans')

    def __str__(self):
        return f"{self.name} ({self.status})"

    class Meta:
        ordering = ['-created_at']
