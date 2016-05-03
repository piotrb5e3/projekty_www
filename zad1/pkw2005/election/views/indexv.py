from django.shortcuts import render, get_object_or_404
from ..models import Kandydat

def index(request):
    kand1 = get_object_or_404(Kandydat, numer = 1)
    kand2 = get_object_or_404(Kandydat, numer = 2)

    return render(request, 'index.html',
            {
                'kand1'               : kand1,
                'kand2'               : kand2,
                })

