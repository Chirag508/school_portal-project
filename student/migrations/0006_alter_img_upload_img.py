# Generated by Django 5.1.3 on 2024-12-09 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_rename_imgupload_img_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img_upload',
            name='img',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
