# Generated by Django 5.1.2 on 2024-12-17 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_remove_question_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='user_email',
        ),
    ]
