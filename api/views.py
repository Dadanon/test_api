from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser

from survey.models import Survey, Question
from .serializers import SurveySerializer, QuestionSerializer


class SurveyListAPIView(generics.ListAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


@permission_classes([IsAdminUser])
class SurveyCreateAPIView(generics.CreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


@permission_classes([IsAdminUser])
class SurveyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


@permission_classes([IsAdminUser])
class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# Create your views here.
