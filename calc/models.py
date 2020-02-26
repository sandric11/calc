from _pydecimal import Decimal

from django.db import models
from django_countries.fields import CountryField
from rest_framework import serializers,viewsets

# CHOICES
LOADING_FROM = [
    ('L1', 'Zalog'),
    ('L2', 'BTC'),
]

LOADING_TO = [
    ('T1', 'Warehouse1'),
    ('T2', 'Warehouse2'),
]
# Create your models here.

#CALCULATOR

class Destination_from(models.Model):
     country = CountryField(blank_label='(izberi državo)')
     loading_from = models.CharField(max_length=2, choices=LOADING_FROM)
     zip_code = models.IntegerField()

def __str__(self):
    return self.country

class Destination_to(models.Model):
    country = CountryField(blank_label='(izberi državo)')
    loading_from = models.CharField(max_length=2, choices=LOADING_TO)
    zip_code = models.IntegerField()

def __str__(self):
    return self.country

class Shipment(models.Model):
    weight = models.IntegerField()
    ldm = models.DecimalField(max_digits=4, decimal_places=2)

#PRETVORNIKi MERSKIH ENOT

class Pretvornik(models.Model):
    one_ldm = models.IntegerField()
    one_cbm = models.IntegerField()
    one_pal = models.IntegerField()

    def __init__(self):
        return self.one_ldm


## IMPORT MODELI

class Zone_postal(models.Model):
    country = CountryField(blank_label='(Izberi državo)')
    zone = models.CharField(max_length=10)
    postal_code = models.IntegerField()

    def __str__(self):
        return self.zone

class Zone_price(models.Model):
    weight = models.CharField(max_length=10)
    zone = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    country = CountryField()







