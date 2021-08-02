# Generated by Django 3.2.5 on 2021-08-02 17:11

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210802_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='havemedicinepost',
            name='address_google_maps',
            field=django_google_maps.fields.AddressField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='havemedicinepost',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(blank=True, max_length=100),
        ),
    ]