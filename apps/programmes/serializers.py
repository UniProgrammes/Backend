from rest_framework import serializers

from apps.programmes.models import Programme, ProgrammeCourse


class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = "__all__"

class ProgrammeCourseSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='course.id')
    name = serializers.CharField(source='course.name')
    prerequisites = serializers.SerializerMethodField()

    class Meta:
        model = ProgrammeCourse
        fields = ['id', 'name', 'prerequisites']

    def get_prerequisites(self, obj):
        prerequisites = ProgrammeCourse.objects.filter(programme=obj.programme, course__in=obj.course.prerequisites.all())
        return ProgrammeCourseSerializer(prerequisites, many=True).data
    