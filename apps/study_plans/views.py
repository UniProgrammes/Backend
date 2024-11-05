from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.lib.pagination import StandardPagination
from apps.study_plans.models import StudyPlan
from apps.study_plans.serializers import StudyPlanSerializer


class StudyPlanViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    pagination_class = StandardPagination

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]