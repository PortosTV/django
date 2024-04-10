from django.db import models

"""
    primary_key
    unique
    default
    null
    blank

    Charfield
    integerfield
    datefield
    datetimerfield
    floatfield
    emailfield
    booleanfield

    (aide pour sql)
"""

class train(models.Model):
    trajet = models.CharField(max_length = 64, unique=True)
    temps = models.CharField(max_length=32, unique=False)
    quantity = models.IntegerField(default=1)

class ville(models.Model):
    nom= models.CharField(max_length=32, unique=True)
    region= models.CharField(max_length=32, unique=True)

