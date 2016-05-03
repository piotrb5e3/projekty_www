from django.db import models
from django.core.exceptions import ValidationError
from .gmina import Gmina

class Kandydat(models.Model):

    def __str__(self):
        return self.nazwisko + ' ' + self.imiona

    @property
    def nazwa(self):
        return self.nazwisko.upper() + ' ' + self.imiona

    @property
    def glosow(self):
        lg = listaGmin = Gmina.objects.all()
        if(self.numer == 1):
            return sum(g.liczbaGlosowKand1 for g in listaGmin)
        else:
            return sum(g.liczbaGlosowKand2 for g in listaGmin)

    @property
    def proc(self):
        rw = sum(g.liczbaGlosowWaznych for g in Gmina.objects.all())
        if(rw > 0):
            return "{0:.2f}".format(self.glosow / rw * 100)
        else:
            return "--.--"

    numer = models.IntegerField(unique = True, choices=[(1, "1"), (2, "2")])
    nazwisko = models.CharField(max_length = 50)
    imiona = models.CharField(max_length = 100)


