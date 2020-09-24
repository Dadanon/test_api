from django.urls import path, include
from .views import SurveyListAPIView, SurveyDetailAPIView, SurveyCreateAPIView, ResponseDetailAPIView

urlpatterns = [
    path('', include('pages.urls')),
    path('survey-list/', SurveyListAPIView.as_view(), name='survey_list'),
    path('survey-create/', SurveyCreateAPIView.as_view(), name='survey_create'),
    path('survey/<int:pk>/', SurveyDetailAPIView.as_view(), name='survey_detail'),
    path('response/<int:pk>/', ResponseDetailAPIView.as_view(), name='response_detail'),
]
