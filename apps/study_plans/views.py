from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.lib.pagination import StandardPagination
from apps.study_plans.models import StudyPlan
from apps.study_plans.serializers import StudyPlanSerializer, StudyPlanSummarySerializer


class StudyPlanViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    pagination_class = StandardPagination

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"], url_path="my-study-plans")
    def my_study_plans(self, request):
        user = request.user
        status = request.query_params.get("status")

        if status:
            study_plans = StudyPlan.objects.filter(user=user, status=status)
        else:
            study_plans = StudyPlan.objects.filter(user=user)

        study_plans_data = StudyPlanSummarySerializer(study_plans, many=True).data
        return Response(study_plans_data, status=HTTP_200_OK)
