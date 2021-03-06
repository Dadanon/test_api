from django.contrib import admin
from .models import Survey, Question, Answer


class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 0


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title', 'started_at', 'finished_at', )
    inlines = [QuestionInLine, ]
    readonly_fields = ('started_at', )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['started_at', ]
        else:
            return []


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'survey', )
    list_filter = ('survey', )


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

# Register your models here.
