# Generated by Django 5.1.3 on 2024-11-23 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_teacher_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher_data',
            name='class_level',
        ),
    ]
