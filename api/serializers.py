from rest_framework import serializers

from survey.models import Survey, Question


class SurveySerializer(serializers.ModelSerializer):
    questions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Survey
        fields = ('title', 'started_at', 'finished_at', 'body', 'questions', )


class SurveySerializerAfterCreate(serializers.ModelSerializer):
    questions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Survey
        fields = ('title', 'finished_at', 'body', 'is_active', 'questions', )


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
