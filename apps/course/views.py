# apps/course/views.py
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from apps.lib.pagination import StandardPagination
from apps.course.models import Course
from apps.course.serializers import CourseSerializer

class CourseViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = StandardPagination