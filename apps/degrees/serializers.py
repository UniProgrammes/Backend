from rest_framework.serializers import ModelSerializer

from apps.degrees.models import Degree


class DegreeSerializer(ModelSerializer):
    class Meta:
        model = Degree
        fields = "__all__"
