from django.db import models

# Create your models here.

class Item(models.Model):
    WHAT_CHOICES = (
    ('IX', 'Iphone X'),
    ('IXR','Iphone XR'),
    ('IXS', 'Iphone XS'),
    ('IXSM', 'Iphone XS MAX'),
    ('I11', 'Iphone 11'),
    ('I11P', 'Iphone 11 Pro'),
    ('I11PM', 'Iphone 11 Pro MAX'),
    ('M', 'Macbook'),
    ('MA', 'Macbook Air'),
    ('MP', 'Macbook Pro'),
    ('A1','Airpod 1st Gen '),
    ('A2','Airpod 2nd Gen'),
    ('AP', 'Airpod Pro'),
    )
    REGION_CHOICES = (
    ('SE', 'Seoul'),
    ('GY','Gyeonggi'),
    ('BU','Busan'),
    ('IN','Incheon'),
    ('GW','Gwangju'),
    )
    titleline = models.CharField(max_length=30, default=None)
    what = models.CharField(max_length=30, choices = WHAT_CHOICES)
    price = models.IntegerField()
    userfile = models.ImageField(default=None, upload_to ='images/')
    body =models.TextField(default=None)
    Issold = models.IntegerField(default=0)
    region = models.CharField(max_length=10, choices = REGION_CHOICES)