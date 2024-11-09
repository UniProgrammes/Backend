from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.programmes.views import ProgrammeViewSet, ProgrammeStructureView

router = DefaultRouter()
router.register("programmes", ProgrammeViewSet, basename="programme")

urlpatterns = [
    path("", include(router.urls)),
    path("programmes/<uuid:programme_id>/courses", ProgrammeStructureView.as_view(), name="programme-structure"),
]
