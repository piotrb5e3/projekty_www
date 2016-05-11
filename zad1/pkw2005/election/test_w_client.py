from django.test import Client, TestCase
from .models import Kandydat
from django.contrib.auth.models import User

class ClientTestCase(TestCase):
    def setUp(self):
        Kandydat.objects.create(
                numer = 1,
                nazwisko = 'abC',
                imiona = 'as wq')
        Kandydat.objects.create(
                numer = 2,
                nazwisko = 'Zxd',
                imiona = 'aq wn')
        User.objects.create_user(
                "eve",
                "eve@eve.com",
                "evilevilevil"
                )

    def test_login_logout_works(self):
        c = Client()
        resp = c.get("/")
        self.assertContains(resp, "Zaloguj")
        l_resp = c.post("/login/", {
            'username' : 'eve',
            'password' : 'evilevilevil',
            'next'     : '/'
            }, follow=True)
        self.assertContains(l_resp, "eve");
        o_resp = c.get("/logout/", follow=True)
        self.assertEquals(o_resp.status_code, 200)
        resp = c.get("/")
        self.assertEquals(resp.status_code, 200)
        self.assertContains(resp, "Zaloguj")



