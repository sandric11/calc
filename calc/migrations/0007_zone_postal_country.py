# Generated by Django 3.0.3 on 2020-02-23 08:37

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0006_pretvornik'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone_postal',
            name='country',
            field=django_countries.fields.CountryField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]
