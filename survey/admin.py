from django.contrib import admin
from .models import Survey


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title', 'started_at', 'finished_at', )

# Register your models here.
