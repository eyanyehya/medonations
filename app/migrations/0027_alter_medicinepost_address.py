# Generated by Django 3.2.5 on 2022-01-05 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_medicinepost_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinepost',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]