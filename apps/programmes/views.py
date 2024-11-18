from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from apps.lib.pagination import StandardPagination
from apps.programmes.models import Programme
from apps.programmes.serializers import ProgrammeSerializer
from apps.programmes.filters import ProgrammeFilter
from apps.courses.serializers import CourseSerializer

class ProgrammeViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer
    pagination_class = StandardPagination

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProgrammeFilter

class ProgramCoursesView(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        programme_uuid = self.kwargs.get('uuid')
        programme = get_object_or_404(Programme, uuid=programme_uuid)
        return programme.courses.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        programme = get_object_or_404(Programme, uuid=self.kwargs.get('uuid'))
        
        response_data = {
            'programme': ProgrammeSerializer(programme).data,
            'courses': CourseSerializer(queryset, many=True).data
        }
        
        return Response(response_data, status=status.HTTP_200_OK)