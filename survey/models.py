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
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
        related_name='responses',
    )
    body = models.TextField()

# Create your models here.
