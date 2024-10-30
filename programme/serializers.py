from rest_framework import serializers
from .models import Programme

class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = ['programmeid', 'programmename', 'degreetype', 'credits']
        read_only_fields = fields