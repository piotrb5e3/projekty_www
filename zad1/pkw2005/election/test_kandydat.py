from django.test import TestCase
from .models import Kandydat

class GminaTestCase(TestCase):
    def setUp(self):
        Kandydat.objects.create(
                numer = 1,
                nazwisko = 'abC',
                imiona = 'as wq')
        Kandydat.objects.create(
                numer = 2,
                nazwisko = 'Zxd',
                imiona = 'aq wn')

    def test_name_prints_properly(self):
        k1 = Kandydat.objects.get(numer = 1)
        k2 = Kandydat.objects.get(numer = 2)
        self.assertEqual(k1.nazwa, 'ABC as wq');
        self.assertEqual(k2.nazwa, 'ZXD aq wn');


