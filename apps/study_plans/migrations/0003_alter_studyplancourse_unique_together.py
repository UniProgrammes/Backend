# Generated by Django 5.1.2 on 2024-11-10 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_learning_outcomes_course_prerequisites'),
        ('study_plans', '0002_alter_studyplan_status'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='studyplancourse',
            unique_together={('study_plan', 'course', 'semester')},
        ),
    ]
