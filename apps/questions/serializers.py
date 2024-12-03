from rest_framework.serializers import ModelSerializer
from apps.questions.models import Question

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'user', 'user_email', 'question_text']
        read_only_fields = ['id', 'user', 'user_email']

    def create(self, validated_data):
        user = self.context['user']
        validated_data['user'] = user
        validated_data['user_email'] = user.email
        return super().create(validated_data)
