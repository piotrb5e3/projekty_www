from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
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

class Kandydat(models.Model):

    def __str__(self):
        return self.nazwisko + ' ' + self.imiona

    numer = models.IntegerField(unique = True, choices=[(1, "1"), (2, "2")])
    nazwisko = models.CharField(max_length = 50)
    imiona = models.CharField(max_length = 100)

class RodzajGminy(models.Model):

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

    nazwa = models.CharField(max_length = 100)

class Gmina(models.Model):

    def __str__(self):
        return self.nazwa

    def clean(self):
        if(self.liczbaMieszkancow < self.liczbaUprawnionych):
            raise ValidationError(
                    "Liczba mieszkańców < liczba uprawnionych") 
        if(self.liczbaUprawnionych < self.liczbaWydanychKart):
            raise ValidationError(
                    "Liczba uprawnionych < liczba wydanych kart") 
        if(self.liczbaWydanychKart < self.liczbaGlosowOddanych):
            raise ValidationError(
                    "Liczba wydanych kart < liczba głosów oddanych") 
        if(self.liczbaGlosowOddanych < self.liczbaGlosowWaznych):
            raise ValidationError(
                    "Liczba głosów oddanych < liczba głosów ważnych") 
        if(self.liczbaGlosowKand1 + self.liczbaGlosowKand2 !=
                self.liczbaGlosowWaznych):
            raise ValidationError(
                    "Zgubione głosy ważne!") 


    nazwa = models.CharField(max_length = 200, unique = True)
    rodzaj = models.ForeignKey(RodzajGminy, on_delete=models.CASCADE)
    wojewodztwo = models.ForeignKey(Wojewodztwo, blank = True, null = True)
    liczbaMieszkancow = models.IntegerField()
    liczbaUprawnionych = models.IntegerField()
    liczbaWydanychKart = models.IntegerField()
    liczbaGlosowOddanych = models.IntegerField()
    liczbaGlosowWaznych = models.IntegerField()
    liczbaGlosowKand1 = models.IntegerField()
    liczbaGlosowKand2 = models.IntegerField()

