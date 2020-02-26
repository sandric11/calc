# Generated by Django 3.0.3 on 2020-02-23 08:47

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0007_zone_postal_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone_price',
            name='country',
            field=django_countries.fields.CountryField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]