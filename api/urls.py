from django.urls import path
from .views import SurveyListAPIView, SurveyDetailAPIView, SurveyCreateAPIView

urlpatterns = [
    path('survey-list/', SurveyListAPIView.as_view(), name='survey_list'),
    path('survey-create/', SurveyCreateAPIView.as_view(), name='survey_create'),
    path('<int:pk>/', SurveyDetailAPIView.as_view(), name='survey_detail'),
]