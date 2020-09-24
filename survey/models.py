from django.db import models
from django.contrib.auth import get_user_model


class Survey(models.Model):
    title = models.CharField(max_length=255, unique=True)
    started_at = models.DateTimeField(editable=False)
    finished_at = models.DateTimeField()
    body = models.TextField()

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


class Opros(models.Model):
    RECOMMEND_CHOICES = (
        ('1', '1 - Very Unlikely'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10 - Very Likely'),
    )
    BOOL_CHOICES = (
        ('1', 'Yes'),
        ('0', 'No')
    )

    created = models.DateTimeField(auto_now_add=True)

    recommend_company = models.CharField('How likely would you be to recommend this company to a friend?',
                                         max_length=2, choices=RECOMMEND_CHOICES, default='5')

    what_changes = models.CharField('What would you change about the product?',
                                    max_length=500, default='')

    was_researched = models.CharField('Did you research the product before purchasing it?',
                                      max_length=2, choices=BOOL_CHOICES, default='Yes')
    # optional field
    feedback = models.CharField('Would you like to provide any other feedback?',
                                max_length=500, blank=True, default='')

# Create your models here.
