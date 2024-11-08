from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.lib.pagination import StandardPagination
from apps.programmes.models import Programme, ProgrammeCourse
from apps.programmes.serializers import ProgrammeSerializer, ProgrammeCourseSerializer


class ProgrammeViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer
    pagination_class = StandardPagination

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class ProgrammeStructureView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, programme_id):
        try:
            programme = Programme.objects.get(id=programme_id)
            serializer = ProgrammeSerializer(programme)
            programme_data = serializer.data

            programme_courses = ProgrammeCourse.objects.filter(programme=programme)
            course_data = ProgrammeCourseSerializer(programme_courses, many=True).data

            programme_data["courses"] = course_data
            return Response(programme_data, status=status.HTTP_200_OK)
        except Programme.DoesNotExist:
            return Response({"error": "Programme not found"}, status=status.HTTP_404_NOT_FOUND)