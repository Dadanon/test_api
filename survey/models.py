from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=255, unique=True)
    started_at = models.DateTimeField(auto_now=True)
    finished_at = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

# Create your models here.
