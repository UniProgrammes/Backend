from rest_framework.serializers import ModelSerializer

from apps.study_plans.models import StudyPlan


class StudyPlanSerializer(ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = "__all__"
