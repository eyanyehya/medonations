# Generated by Django 3.2.5 on 2022-01-22 02:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_alter_medicinepost_medicine_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinepost',
            name='medicine_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
