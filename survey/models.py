from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=255, unique=True)
    started_at = models.DateTimeField(editable=False)
    finished_at = models.DateTimeField()
    body = models.TextField()
    choice = models.TextChoices

    def __str__(self):
        return self.title


class Response(models.Model):
    TEXT = 'TX'
    ONE_CHOICE = 'OC'
    MANY_CHOICES = 'MC'
    QUESTION_TYPES = [
        (TEXT, 'Text'),
        (ONE_CHOICE, 'One choice'),
        (MANY_CHOICES, 'Many choices'),
    ]
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
        related_name='responses',
    )
    question_text = models.TextField()
    type = models.CharField(
        max_length=2,
        choices=QUESTION_TYPES,
        default=TEXT,
    )

    def __str__(self):
        return self.question_text

# Create your models here.
