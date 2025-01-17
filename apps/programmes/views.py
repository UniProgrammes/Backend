from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.lib.pagination import StandardPagination
from apps.programmes.models import Programme
from apps.programmes.serializers import ProgrammeSerializer
from apps.programmes.filters import ProgrammeFilter
from apps.courses.serializers import CourseSerializer


class ProgrammeViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer
    pagination_class = StandardPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProgrammeFilter

    @action(detail=True, methods=["get"], url_path="courses")
    def courses(self, request, **kwargs):
        programme = self.get_object()
        courses = programme.courses.all()

        response_data = {
            "programme": ProgrammeSerializer(programme).data,
            "courses": CourseSerializer(
                courses, many=True, context={"programme": programme}
            ).data,
        }

        return Response(response_data, status=status.HTTP_200_OK)
