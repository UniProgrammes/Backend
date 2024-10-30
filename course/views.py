from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(GenericViewSet, ListModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def list(self, request):
        course_id = request.query_params.get('id', None)
        if course_id:
            try:
                course = self.queryset.get(courseid=course_id)
                serializer = self.serializer_class(course)
                return Response(serializer.data)
            except Course.DoesNotExist:
                return Response({'error': 'Course not found'}, status=404)
        
        courses = self.queryset.all()
        serializer = self.serializer_class(courses, many=True)
        return Response(serializer.data)