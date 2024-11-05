# apps/course/views.py
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from apps.lib.pagination import StandardPagination
from apps.courses.models import Course
from apps.courses.serializers import CourseSerializer

class CourseViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = StandardPagination