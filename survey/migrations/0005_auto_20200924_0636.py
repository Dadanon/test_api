# Generated by Django 3.1 on 2020-09-24 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_response_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='body',
            new_name='question_text',
        ),
    ]