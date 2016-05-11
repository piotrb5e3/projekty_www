from django.test import TestCase
from .models import Gmina, RodzajGminy, Wojewodztwo

class WojewodztwoTestCase(TestCase):
    def setUp(self):
        RodzajGminy.objects.create(nazwa="wieś")
        RodzajGminy.objects.create(nazwa="miasto")
        Wojewodztwo.objects.create(numer=1, nazwa="xxx")
        Gmina.objects.create(nazwa = "AAB",
                rodzaj = RodzajGminy.objects.get(nazwa="miasto"),
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
                rodzaj = RodzajGminy.objects.get(nazwa="miasto"),
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
                wojewodztwo = Wojewodztwo.objects.get(numer = 1),
                liczbaMieszkancow = 100,
                liczbaUprawnionych = 90,
                liczbaWydanychKart = 80,
                liczbaGlosowOddanych = 70,
                liczbaGlosowWaznych = 17,
                liczbaGlosowKand1 = 9,
                liczbaGlosowKand2 = 8
        )

    def test_sums_count_properly(self):
        gmaab = Gmina.objects.get(nazwa= "AAB") # r2
        gmccc = Gmina.objects.get(nazwa= "CCC") # r2
        gmzzz = Gmina.objects.get(nazwa= "ZZZ") # r1
        r1 = RodzajGminy.objects.get(nazwa = "wieś")
        r2 = RodzajGminy.objects.get(nazwa = "miasto")

        self.assertEqual(r2.glosowKand1,
                gmaab.liczbaGlosowKand1 + gmccc.liczbaGlosowKand1)
        self.assertEqual(r2.glosowKand2,
                gmaab.liczbaGlosowKand2 + gmccc.liczbaGlosowKand2)
        self.assertEqual(r2.glosowWaznych,
                gmaab.liczbaGlosowWaznych + gmccc.liczbaGlosowWaznych)

        self.assertEqual(r1.glosowKand1, gmzzz.liczbaGlosowKand1)
        self.assertEqual(r1.glosowKand2, gmzzz.liczbaGlosowKand2)
        self.assertEqual(r1.glosowWaznych, gmzzz.liczbaGlosowWaznych)


