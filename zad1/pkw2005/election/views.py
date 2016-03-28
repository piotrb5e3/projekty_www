from django.shortcuts import render
from .models import Gmina, Kandydat, RodzajGminy, Wojewodztwo


# Create your views here.
def index(request):
    class Rozmiar():
        def __init__(self):
            pass

    def createranges():
        gminy = Gmina.objects.all()
        result = []
        r = Rozmiar()
        r.nazwa ="Statki i zagranica"
        r.waz = (RodzajGminy.objects.get(nazwa="statki").glosowWaznych + 
            RodzajGminy.objects.get(nazwa="zagranica").glosowWaznych)
        r.k1 = (RodzajGminy.objects.get(nazwa="statki").glosowKand1 +
            RodzajGminy.objects.get(nazwa="zagranica").glosowKand1)
        r.k2 = (RodzajGminy.objects.get(nazwa="statki").glosowKand2 +
            RodzajGminy.objects.get(nazwa="zagranica").glosowKand2)
        if(r.waz > 0 ):
            r.p1 = "{0:.2f}".format(100 * r.k1 / r.waz)
            r.p2 = "{0:.2f}".format(100 * r.k2 / r.waz)
        else:
            r.p1 = "--.--"
            r.p2 = "--.--"

        result.append(r)

        r = Rozmiar()
        r.nazwa ="do 5000"
        r.waz = sum( g.liczbaGlosowWaznych
                for g in gminy.filter(liczbaMieszkancow__lte=5000))
        r.k1 =  sum( g.liczbaGlosowKand1
                for g in gminy.filter(liczbaMieszkancow__lte=5000))
        r.k2 =  sum( g.liczbaGlosowKand2
                for g in gminy.filter(liczbaMieszkancow__lte=5000))
        if(r.waz > 0 ):
            r.p1 = "{0:.2f}".format(100 * r.k1 / r.waz)
            r.p2 = "{0:.2f}".format(100 * r.k2 / r.waz)
        else:
            r.p1 = "--.--"
            r.p2 = "--.--"

        result.append(r)


        vals = [5000, 10000, 20000, 50000, 100000, 200000, 500000]
        for i in range(0, len(vals)):
            pass

        return result

    rozmiary = createranges()
    listaGmin = Gmina.objects.all()
    rodzaje = RodzajGminy.objects.all()
    wojewodztwa = Wojewodztwo.objects.all()
    razemUp = sum(g.liczbaUprawnionych for g in listaGmin)
    razemWyd = sum(g.liczbaWydanychKart for g in listaGmin)
    razemOdd = sum(g.liczbaGlosowOddanych for g in listaGmin)
    razemWaz = sum(g.liczbaGlosowWaznych for g in listaGmin)
    kand1 = Kandydat.objects.get(numer = 1)
    kand2 = Kandydat.objects.get(numer = 2)
    kand1g = sum(g.liczbaGlosowKand1 for g in listaGmin)
    kand2g = sum(g.liczbaGlosowKand2 for g in listaGmin)
    if (razemWaz > 0):
        kand1p = "{0:.2f}".format(kand1g / razemWaz * 100)
        kand2p = "{0:.2f}".format(kand2g / razemWaz * 100)
    else:
        kand1p = "0.00"
        kand2p = "0.00"

    kand1Nazwa = kand1.nazwisko.upper() + ' ' + kand1.imiona
    kand2Nazwa = kand2.nazwisko.upper() + ' ' + kand2.imiona
    return render(request, 'index.html',
            {
                'razemUprawnionych'   : razemUp,
                'razemWydanychKart'   : razemWyd,
                'razemGlosowOddanych' : razemOdd,
                'razemGlosowWaznych'  : razemWaz,
                'kand1Nazwa'          : kand1Nazwa,
                'kand2Nazwa'          : kand2Nazwa,
                'kand1g'              : kand1g,
                'kand1p'              : kand1p,
                'kand2g'              : kand2g,
                'kand2p'              : kand2p,
                'listaGmin'           : listaGmin,
                'wojewodztwa'         : wojewodztwa,
                'listaRodzajow'       : rodzaje,
                'rozmiary'            : rozmiary,
                })
