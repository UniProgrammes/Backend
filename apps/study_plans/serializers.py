from rest_framework.serializers import ModelSerializer

from apps.study_plans.models import StudyPlan


class StudyPlanSerializer(ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = "__all__"
        read_only_fields = ["user"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
