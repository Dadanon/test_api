from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser

from survey.models import Survey, Question
from .serializers import (
    SurveySerializer,
    QuestionSerializer,
    SurveySerializerAfterCreate,
)


class SurveyListAPIView(generics.ListAPIView):
    queryset = Survey.objects.filter(is_active=True)
    serializer_class = SurveySerializer


@permission_classes([IsAdminUser])
class SurveyCreateAPIView(generics.CreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


@permission_classes([IsAdminUser])
class SurveyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializerAfterCreate


@permission_classes([IsAdminUser])
class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


@permission_classes([IsAdminUser])
class QuestionCreateAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# Create your views here.
