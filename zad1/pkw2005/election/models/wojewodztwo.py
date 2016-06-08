from django.db import models

class Wojewodztwo(models.Model):

    def __str__(self):
        return self.nazwa

    numer = models.IntegerField(primary_key=True)
    nazwa = models.CharField(max_length = 100, unique = True)
    hckey = models.CharField(max_length = 15)

from .gmina import Gmina
