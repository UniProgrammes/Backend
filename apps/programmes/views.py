from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from apps.lib.pagination import StandardPagination
from apps.programmes.models import Programme
from apps.programmes.serializers import ProgrammeSerializer


class ProgrammeViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer
    pagination_class = StandardPagination
