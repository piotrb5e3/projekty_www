from django.test import TestCase
from .models import Gmina, RodzajGminy, Wojewodztwo

class WojewodztwoTestCase(TestCase):
    def setUp(self):
        RodzajGminy.objects.create(nazwa="wieś")
        Wojewodztwo.objects.create(numer=1, nazwa="xxx")
        Wojewodztwo.objects.create(numer=2, nazwa="yyy")
        Gmina.objects.create(nazwa = "AAB",
                rodzaj = RodzajGminy.objects.get(nazwa="wieś"),
                wojewodztwo = Wojewodztwo.objects.get(numer = 1),
                liczbaMieszkancow = 100,
                liczbaUprawnionych = 90,
                liczbaWydanychKart = 80,
                liczbaGlosowOddanych = 70,
                liczbaGlosowWaznych = 11,
                liczbaGlosowKand1 = 10,
                liczbaGlosowKand2 = 1
        )
        Gmina.objects.create(nazwa = "CCC",
                rodzaj = RodzajGminy.objects.get(nazwa="wieś"),
                wojewodztwo = Wojewodztwo.objects.get(numer = 1),
                liczbaMieszkancow = 100,
                liczbaUprawnionych = 90,
                liczbaWydanychKart = 80,
                liczbaGlosowOddanych = 70,
                liczbaGlosowWaznych = 23,
                liczbaGlosowKand1 = 7,
                liczbaGlosowKand2 = 16
        )
        Gmina.objects.create(nazwa = "ZZZ",
                rodzaj = RodzajGminy.objects.get(nazwa="wieś"),
                wojewodztwo = Wojewodztwo.objects.get(numer = 2),
                liczbaMieszkancow = 100,
                liczbaUprawnionych = 90,
                liczbaWydanychKart = 80,
                liczbaGlosowOddanych = 70,
                liczbaGlosowWaznych = 17,
                liczbaGlosowKand1 = 9,
                liczbaGlosowKand2 = 8
        )

    def test_sums_count_properly(self):
        gmaab = Gmina.objects.get(nazwa= "AAB") # w1
        gmccc = Gmina.objects.get(nazwa= "CCC") # w1
        gmzzz = Gmina.objects.get(nazwa= "ZZZ") # w2
        w1 = Wojewodztwo.objects.get(numer = 1)
        w2 = Wojewodztwo.objects.get(numer = 2)

        self.assertEqual(w1.glosowKand1,
                gmaab.liczbaGlosowKand1 + gmccc.liczbaGlosowKand1)
        self.assertEqual(w1.glosowKand2,
                gmaab.liczbaGlosowKand2 + gmccc.liczbaGlosowKand2)
        self.assertEqual(w1.glosowWaznych,
                gmaab.liczbaGlosowWaznych + gmccc.liczbaGlosowWaznych)

        self.assertEqual(w2.glosowKand1, gmzzz.liczbaGlosowKand1)
        self.assertEqual(w2.glosowKand2, gmzzz.liczbaGlosowKand2)
        self.assertEqual(w2.glosowWaznych, gmzzz.liczbaGlosowWaznych)


