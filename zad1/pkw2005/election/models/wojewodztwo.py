from django.db import models
from django.core.exceptions import ValidationError

class Wojewodztwo(models.Model):

    def __str__(self):
        return self.nazwa

    @property
    def glosowWaznych(self):
        gminy = self.gmina_set.all()
        return sum(g.liczbaGlosowWaznych for g in gminy)

    @property
    def glosowKand1(self):
        gminy = self.gmina_set.all()
        return sum(g.liczbaGlosowKand1 for g in gminy)

    @property
    def glosowKand2(self):
        gminy = self.gmina_set.all()
        return sum(g.liczbaGlosowKand2 for g in gminy)

    @property
    def procKand1(self):
        gminy = self.gmina_set.all()
        return "{0:.2f}".format(
                100 * sum(g.liczbaGlosowKand1 for g in gminy) /
                sum(g.liczbaGlosowWaznych for g in gminy))

    @property
    def procKand2(self):
        gminy = self.gmina_set.all()
        return "{0:.2f}".format(
                100 * sum(g.liczbaGlosowKand2 for g in gminy) /
                sum(g.liczbaGlosowWaznych for g in gminy))


    numer = models.IntegerField(primary_key=True)
    nazwa = models.CharField(max_length = 100, unique = True)
    hckey = models.CharField(max_length = 15)

from .gmina import Gmina
