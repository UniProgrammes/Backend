from django.contrib import admin
from apps.learning_outcomes.models import LearningOutcome


@admin.register(LearningOutcome)
class LearningOutcomeAdmin(admin.ModelAdmin):
    list_display = ("category", "description")
    search_fields = ("category", "description")
    list_filter = ("category",)
