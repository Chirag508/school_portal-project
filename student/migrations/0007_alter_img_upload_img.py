# Generated by Django 5.1.3 on 2024-12-09 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_img_upload_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img_upload',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
