from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.study_plans.models import StudyPlan


class StudyPlanSerializer(ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = "__all__"
        read_only_fields = ["user"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class StudyPlanSummarySerializer(ModelSerializer):
    num_courses = SerializerMethodField()

    class Meta:
        model = StudyPlan
        fields = ["name", "status", "num_courses", "created_at", "updated_at"]

    def get_num_courses(self, obj):
        return obj.courses.count()
