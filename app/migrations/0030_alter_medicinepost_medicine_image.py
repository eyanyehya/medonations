# Generated by Django 3.2.5 on 2022-01-22 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_medicinepost_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinepost',
            name='medicine_image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]