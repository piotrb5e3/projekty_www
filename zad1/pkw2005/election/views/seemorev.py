from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import Http404
from ..models import Gmina, Wojewodztwo, RodzajGminy, Kandydat

def seemore(request):
    vals = [5000, 10000, 20000, 50000, 100000, 200000, 500000]

    if request.method == 'POST':
        raise Http404("Wrong method")

    kand1 = get_object_or_404(Kandydat, numer = 1)
    kand2 = get_object_or_404(Kandydat, numer = 2)

    gminy = {
            'w' :
            lambda: get_object_or_404(
                Wojewodztwo,
                numer = request.GET['v']
                ).gmina_set.all(),
            'r' :
            lambda: get_object_or_404(
                RodzajGminy,
                nazwa = request.GET['v']
                ).gmina_set.all(),
            's' :
            lambda:
            {
                # statki i zagranica
                '0' : lambda: (Gmina.objects.all().filter(
                    Q(rodzaj__nazwa = "statki") |
                    Q(rodzaj__nazwa = "zagranica")
                    )),
                '1' : lambda: (Gmina.objects.all().filter(
                    liczbaMieszkancow__lte=5000)),
                '8' : lambda: (Gmina.objects.all().filter(
                    liczbaMieszkancow__gt=500000)),
                }.get(
                    request.GET['v'],
                    (lambda:(
                        Gmina.objects.all().filter(
                            liczbaMieszkancow__lte=vals[int(request.GET['v'])-1]
                            ).filter(
                                liczbaMieszkancow__gt=
                                vals[int(request.GET['v'])-2]))))()
            }[request.GET['type']]()
    return render(request, 'lista.html',{
        'gminy' : gminy,
        'kand1' : kand1,
        'kand2' : kand2,
    })
