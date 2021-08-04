# Generated by Django 3.2.5 on 2021-08-04 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_medicinepost_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinepost',
            name='post_type',
            field=models.CharField(choices=[('Donate', 'Donate'), ('Receive', 'Receive')], default='Post Type', max_length=9),
        ),
    ]
