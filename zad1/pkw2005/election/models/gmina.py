from django.db import models, transaction
from django.core.exceptions import ValidationError
from django.contrib.auth.models import BaseUserManager, AbstractUser, User

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
        if(self.liczbaGlosowKand1 < 0 or self.liczbaGlosowKand2 <0):
            raise ValidationError(
                    "Liczba głosów oddanych na kandydata nie może być ujemna!")

    @transaction.atomic
    def update_glosy(self, lk1, lk2, revnum, user):
        if (revnum != self.rev or lk1 < 0 or lk2 < 0 or
                lk1 + lk2 > self.liczbaGlosowOddanych) :
                    return False
        else:
            self.rev += 1
            self.revuser = user
            self.liczbaGlosowKand1 = lk1
            self.liczbaGlosowKand2 = lk2
            self.liczbaGlosowWaznych = lk1 + lk2
            self.save()
            return True

    rev = models.IntegerField(default=0)
    revtime = models.DateTimeField(auto_now=True)
    revuser = models.ForeignKey(User, default=None, null=True)

    nazwa = models.CharField(max_length = 200, unique = False)
    rodzaj = models.ForeignKey("RodzajGminy", on_delete=models.CASCADE)
    wojewodztwo = models.ForeignKey("Wojewodztwo", blank = True, null = True)
    liczbaMieszkancow = models.IntegerField(default=0)
    liczbaUprawnionych = models.IntegerField(default=0)
    liczbaWydanychKart = models.IntegerField(default=0)
    liczbaGlosowOddanych = models.IntegerField(default=0)
    liczbaGlosowWaznych = models.IntegerField(default=0)
    liczbaGlosowKand1 = models.IntegerField(default=0)
    liczbaGlosowKand2 = models.IntegerField(default=0)

from .rodzaj import RodzajGminy
from .wojewodztwo import Wojewodztwo


