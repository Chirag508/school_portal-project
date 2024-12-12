# Generated by Django 5.1.3 on 2024-12-07 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_teacher_data_class_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='imgupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.AlterField(
            model_name='student_data',
            name='enrollment_no',
            field=models.BigIntegerField(unique=True),
        ),
    ]
