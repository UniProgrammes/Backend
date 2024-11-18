from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.programmes.views import ProgrammeViewSet

router = DefaultRouter()
router.register("programmes", ProgrammeViewSet, basename="programme")

urlpatterns = [
    path("", include(router.urls)),
    path('programmes/<uuid:uuid>/courses/', ProgrammeViewSet, name='programme-courses')
]
