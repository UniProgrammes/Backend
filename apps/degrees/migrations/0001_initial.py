# Generated by Django 5.1.2 on 2024-11-07 00:17

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programmes', '0002_programmecourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DegreeProgramme',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('period_years', models.IntegerField()),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='degrees.degree')),
                ('programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programmes.programme')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='degree',
            name='programmes',
            field=models.ManyToManyField(blank=True, related_name='degrees', through='degrees.DegreeProgramme', to='programmes.programme'),
        ),
    ]