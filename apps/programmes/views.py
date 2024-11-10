from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.lib.pagination import StandardPagination
from apps.programmes.models import Programme
from apps.programmes.serializers import ProgrammeSerializer
from apps.programmes.filters import ProgrammeFilter


class ProgrammeViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer
    pagination_class = StandardPagination

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProgrammeFilter
