# Generated by Django 4.1.7 on 2023-03-31 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0007_remove_exam_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exampart',
            name='time',
            field=models.PositiveIntegerField(),
        ),
    ]
