# Generated by Django 2.2.1 on 2019-11-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0002_question_closed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='team_a',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='team_b',
            field=models.CharField(max_length=100),
        ),
    ]
