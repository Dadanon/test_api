from django.contrib import admin
from .models import Survey, Response, Opros


class ResponseInLine(admin.TabularInline):
    model = Response
    extra = 0


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title', 'started_at', 'finished_at', )
    inlines = [ResponseInLine, ]


admin.site.register(Response)
admin.site.register(Opros)

# Register your models here.
