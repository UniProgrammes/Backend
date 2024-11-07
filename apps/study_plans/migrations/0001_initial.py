# Generated by Django 5.1.2 on 2024-11-07 00:10

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyPlan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_plans', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudyPlanCourse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('semester', models.PositiveIntegerField()),
                ('is_completed', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_plan_courses', to='courses.course')),
                ('study_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_plan_courses', to='study_plans.studyplan')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='studyplan',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='study_plans', through='study_plans.StudyPlanCourse', to='courses.course'),
        ),
    ]
