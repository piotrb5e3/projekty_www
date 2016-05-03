from django.shortcuts import render, get_object_or_404
from ..models import Gmina, Kandydat, RodzajGminy, Wojewodztwo
from jsonview.decorators import json_view
from .rozmiary import createranges

@json_view
def mapdata(request):
    return [{'hc-key': x.hckey , 'value': x.procKand1 } for x in Wojewodztwo.objects.all()]

def wojewodztwa(request):
    kand1 = get_object_or_404(Kandydat, numer = 1)
    kand2 = get_object_or_404(Kandydat, numer = 2)
    wojewodztwa = Wojewodztwo.objects.all()
    razemWaz = sum(g.liczbaGlosowWaznych for g in Gmina.objects.all())


    return render(request, "wojewodztwa.html",
            {
                'kand1'          : kand1,
                'kand2'          : kand2,
                'wojewodztwa'    : wojewodztwa,
                'razemWaznych'   : razemWaz,
                })

def rodzaje(request):
    rozmiary = createranges()
    listaGmin = Gmina.objects.all()
    rodzaje = RodzajGminy.objects.all()
    kand1 = get_object_or_404(Kandydat, numer = 1)
    kand2 = get_object_or_404(Kandydat, numer = 2)

    return render(request, 'rodzaje.html',
            {
                'kand1'               : kand1,
                'kand2'               : kand2,
                'listaRodzajow'       : rodzaje,
                'rozmiary'            : rozmiary,
                })
@json_view
def stats(request):
    listaGmin = Gmina.objects.all()
    razemUp = sum(g.liczbaUprawnionych for g in listaGmin)
    razemWyd = sum(g.liczbaWydanychKart for g in listaGmin)
    razemOdd = sum(g.liczbaGlosowOddanych for g in listaGmin)
    razemWaz = sum(g.liczbaGlosowWaznych for g in listaGmin)
    kand1 = get_object_or_404(Kandydat, numer = 1)
    kand2 = get_object_or_404(Kandydat, numer = 2)
    return {
            'upr'      : razemUp,
            'wyd'      : razemWyd,
            'odd'      : razemOdd,
            'waz'      : razemWaz,
            'c1p'      : kand1.proc,
            'c1c'      : kand1.glosow,
            'c2p'      : kand2.proc,
            'c2c'      : kand2.glosow,
            }
