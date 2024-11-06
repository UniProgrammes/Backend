from rest_framework import serializers

from apps.programmes.models import Programme


class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = "__all__"
