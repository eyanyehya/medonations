# Generated by Django 3.2.5 on 2022-01-05 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_alter_medicinepost_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinepost',
            name='address',
            field=models.TextField(),
        ),
    ]
