# Generated by Django 4.1.7 on 2023-03-31 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0008_alter_exampart_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exampart',
            name='pass_score',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
