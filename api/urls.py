from django.urls import path, include

from .views import (
    SurveyListAPIView,
    SurveyDetailAPIView,
    SurveyCreateAPIView,
    QuestionDetailAPIView,
    QuestionCreateAPIView,
)

urlpatterns = [
    path('', include('pages.urls')),
    path('survey-list/', SurveyListAPIView.as_view(), name='survey_list'),
    path('survey-list/create/', SurveyCreateAPIView.as_view(), name='survey_create'),
    path('survey-list/<int:pk>/', SurveyDetailAPIView.as_view(), name='survey_detail'),
    path('question/<int:pk>/', QuestionDetailAPIView.as_view(), name='question_detail'),
    path('question/create/', QuestionCreateAPIView.as_view(), name='question_create'),
]
