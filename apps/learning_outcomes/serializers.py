from rest_framework.serializers import ModelSerializer

from apps.learning_outcomes.models import LearningOutcome


class LearningOutcomeSerializer(ModelSerializer):
    class Meta:
        model = LearningOutcome
        fields = "__all__"
