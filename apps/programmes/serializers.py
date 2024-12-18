from rest_framework import serializers

from apps.programmes.models import Programme

class ProgrammeSerializer(serializers.ModelSerializer):
    degree_type = serializers.SerializerMethodField()

    class Meta:
        model = Programme
        fields = ["id", "name", "credits", "degree_type"]

    def get_degree_type(self, obj):
        return obj.degree_type
