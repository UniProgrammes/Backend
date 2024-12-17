# Generated by Django 5.1.2 on 2024-12-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0003_programme_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programme',
            name='degree_type',
        ),
        migrations.RemoveField(
            model_name='programmecourse',
            name='period_months',
        ),
        migrations.AlterField(
            model_name='programmecourse',
            name='year',
            field=models.PositiveIntegerField(),
        ),
    ]
