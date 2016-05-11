from django.test import TestCase
from .models import Gmina, RodzajGminy, Wojewodztwo

class GminaTestCase(TestCase):
    def setUp(self):
        RodzajGminy.objects.create(nazwa="wieś")
        Wojewodztwo.objects.create(numer=1, nazwa="xxx")
        Gmina.objects.create(nazwa = "AAB",
                rodzaj = RodzajGminy.objects.get(nazwa="wieś"),
                wojewodztwo = Wojewodztwo.objects.get(numer = 1),
                liczbaMieszkancow = 100,
                liczbaUprawnionych = 90,
                liczbaWydanychKart = 80,
                liczbaGlosowOddanych = 70
        );

    def test_cannot_edit_with_bad_rev(self):
        gm = Gmina.objects.get(nazwa = "AAB")
        self.assertFalse(gm.update_glosy(2, 3, gm.rev + 4, None));
        self.assertFalse(gm.update_glosy(2, 3, gm.rev - 4, None));
        self.assertEqual(gm.liczbaGlosowKand1, 0);
        self.assertEqual(gm.liczbaGlosowKand2, 0);

    def test_cannot_edit_with_too_many_votes(self):
        gm = Gmina.objects.get(nazwa = "AAB")
        self.assertFalse(gm.update_glosy(30, 45, gm.rev, None));
        self.assertFalse(gm.update_glosy(44, 44, gm.rev, None));
        self.assertFalse(gm.update_glosy(-4, 44, gm.rev, None));
        self.assertFalse(gm.update_glosy(44, -4, gm.rev, None));
        self.assertEqual(gm.liczbaGlosowKand1, 0);
        self.assertEqual(gm.liczbaGlosowKand2, 0);

    def test_can_edit_with_right_rev(self):
        gm = Gmina.objects.get(nazwa = "AAB")
        rn = gm.rev
        self.assertTrue(gm.update_glosy(10, 12, rn, None))
        self.assertEqual(gm.rev, rn + 1)
        self.assertEqual(gm.liczbaGlosowKand1, 10)
        self.assertEqual(gm.liczbaGlosowKand2, 12)
        self.assertEqual(gm.liczbaGlosowWaznych, 22)

