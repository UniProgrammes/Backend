from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.learning_outcomes.views import LearningOutcomeViewSet

router = DefaultRouter()
router.register(
    "learning-outcomes", LearningOutcomeViewSet, basename="learning-outcome"
)

urlpatterns = [
    path("", include(router.urls)),
]
