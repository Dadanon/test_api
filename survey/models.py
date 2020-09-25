from django.db import models
from datetime import datetime

TEXT = 'TX'
ONE_CHOICE = 'OC'
MANY_CHOICES = 'MC'
QUESTION_TYPES = [
    (TEXT, 'Text'),
    (ONE_CHOICE, 'One choice'),
    (MANY_CHOICES, 'Many choices'),
]


class Survey(models.Model):
    title = models.CharField(max_length=255, unique=True)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
        related_name='questions',
    )
    question_text = models.CharField(max_length=4096, blank=False, null=False)
    question_type = models.CharField(
        max_length=2,
        choices=QUESTION_TYPES,
    )

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )
    answer_text = models.CharField(max_length=4096)

    def __str__(self):
        return self.answer_text

# Create your models here.
