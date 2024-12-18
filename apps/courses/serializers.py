from rest_framework import serializers

from apps.courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if programme := self.context.get("programme"):
            programme_course = programme.programmecourse_set.filter(course=instance).first()
            representation["year"] = programme_course.year
            representation["is_mandatory"] = programme_course.is_mandatory
        return representation
