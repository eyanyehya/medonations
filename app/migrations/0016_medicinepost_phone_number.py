# Generated by Django 3.2.5 on 2021-08-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_medicinepost_medicine_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicinepost',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
