# Generated by Django 3.0.3 on 2020-02-22 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0005_auto_20200219_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pretvornik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_ldm', models.IntegerField()),
                ('one_cbm', models.IntegerField()),
                ('one_pal', models.IntegerField()),
            ],
        ),
    ]
