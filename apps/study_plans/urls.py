from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.study_plans.views import StudyPlanViewSet

router = DefaultRouter()
router.register("study-plans", StudyPlanViewSet, basename="study-plan")

urlpatterns = [
    path("", include(router.urls)),
]
