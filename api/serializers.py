from rest_framework import serializers

from survey.models import Survey, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = ('id', 'title', 'started_at', 'finished_at', 'body', 'is_active', )


class SurveyDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ('id', 'title', 'finished_at', 'body', 'is_active', 'questions', )
