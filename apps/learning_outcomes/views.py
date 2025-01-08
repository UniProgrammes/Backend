from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from apps.learning_outcomes.models import LearningOutcome
from apps.learning_outcomes.serializers import LearningOutcomeSerializer
from apps.lib.pagination import StandardPagination


class LearningOutcomeViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = LearningOutcome.objects.all()
    serializer_class = LearningOutcomeSerializer
    pagination_class = StandardPagination
