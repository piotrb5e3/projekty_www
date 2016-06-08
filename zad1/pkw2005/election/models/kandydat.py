from django.db import models
from django.core.exceptions import ValidationError
from .gmina import Gmina

class Kandydat(models.Model):

    def __str__(self):
        return self.nazwisko + ' ' + self.imiona

    numer = models.IntegerField(unique = True, choices=[(1, "1"), (2, "2")])
    nazwisko = models.CharField(max_length = 50)
    imiona = models.CharField(max_length = 100)


