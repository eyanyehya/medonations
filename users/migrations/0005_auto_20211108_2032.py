# Generated by Django 3.2.5 on 2021-11-08 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='test',
        ),
    ]
