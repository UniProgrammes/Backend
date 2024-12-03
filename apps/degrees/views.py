from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.lib.pagination import StandardPagination
from apps.degrees.models import Degree
from apps.degrees.serializers import DegreeSerializer


class DegreeViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
    pagination_class = StandardPagination

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
