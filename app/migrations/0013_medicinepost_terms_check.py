# Generated by Django 3.2.5 on 2021-11-13 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_medicinepost_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicinepost',
            name='terms_check',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
