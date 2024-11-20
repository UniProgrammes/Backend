from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.lib.pagination import StandardPagination
from apps.study_plans.models import StudyPlan, StudyPlanCourse
from apps.study_plans.serializers import (
    StudyPlanSerializer,
    StudyPlanCourseSerializer,
    StudyPlanSummarySerializer,
)


class StudyPlanViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    pagination_class = StandardPagination

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=True, methods=["get", "post", "delete"])
    def courses(self, request, *args, **kwargs):
        study_plan = self.get_object()

        if request.method == "GET":
            study_plan_courses = study_plan.study_plan_courses.all()
            serializer_data = StudyPlanCourseSerializer(
                study_plan_courses, many=True
            ).data

            return Response(serializer_data)

        if request.method == "POST":
            courses = request.data["courses"]
            study_plan_courses = []
            for course in courses:
                study_plan_courses.append(
                    StudyPlanCourse(
                        study_plan=study_plan,
                        course_id=course["id"],
                        semester=course["semester"],
                    )
                )
            StudyPlanCourse.objects.bulk_create(study_plan_courses)

        elif request.method == "DELETE":
            courses_ids = request.data["courses_ids"]
            study_plan.study_plan_courses.filter(course_id__in=courses_ids).delete()

        return Response(status=HTTP_204_NO_CONTENT)

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

    @action(detail=True, methods=["get"], url_path="validate-prerequisites")
    def validate_prerequisites(self, request, *args, **kwargs):
        study_plan = self.get_object()

        return Response({
            "is_valid": study_plan.is_valid,
            "not_satisfied_prerequisites": study_plan.not_satisfied_prerequisites,
        })
