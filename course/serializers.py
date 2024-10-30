from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['courseid', 'coursename', 'coursecode', 'credits', 'educationallevel', 'coursedescription', 'mainarea']
        read_only_fields = fields