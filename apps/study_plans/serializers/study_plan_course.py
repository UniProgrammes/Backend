from rest_framework.serializers import ModelSerializer

from apps.study_plans.models import StudyPlanCourse
from apps.courses.serializers import CourseSerializer


class StudyPlanCourseSerializer(ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = StudyPlanCourse
        fields = ["course", "semester", "is_completed"]

    def to_representation(self, instance):
        return {
            **CourseSerializer(instance.course).data,
            "semester": instance.semester,
            "is_completed": instance.is_completed,
        }