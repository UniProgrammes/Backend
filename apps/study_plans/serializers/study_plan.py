from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError

from apps.study_plans.models import StudyPlan


class StudyPlanSerializer(ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = "__all__"
        read_only_fields = ["user"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, attrs):
        if self.instance and attrs.get("status") == "completed":
            if not self.instance.is_valid:
                raise ValidationError({
                    "status": (
                        "This study plan cannot be marked as completed because "
                        "not all prerequisites are satisfied."
                    )
                })
        return attrs


class StudyPlanSummarySerializer(ModelSerializer):
    num_courses = SerializerMethodField()

    class Meta:
        model = StudyPlan
        fields = ["name", "status", "num_courses", "created_at", "updated_at"]

    def get_num_courses(self, obj):
        return obj.courses.count()
