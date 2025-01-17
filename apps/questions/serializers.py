from rest_framework.serializers import ModelSerializer
from apps.questions.models import Question

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'user', 'text']
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        user = self.context['user']
        validated_data['user'] = user
        return super().create(validated_data)
