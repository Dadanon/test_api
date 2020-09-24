from rest_framework import serializers

from survey.models import Survey, Response


class SurveySerializer(serializers.ModelSerializer):
    responses = serializers.StringRelatedField(many=True)

    class Meta:
        model = Survey
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'
