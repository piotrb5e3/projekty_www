from django.shortcuts import get_object_or_404
from django import forms
from ..models import Gmina, Kandydat

class GminaEditForm(forms.Form):
    gid = forms.IntegerField(widget=forms.HiddenInput())
    k1 = forms.IntegerField(label='K1', min_value = 0)
    k2 = forms.IntegerField(label='k2', min_value = 0)

    def __init__(self, gminaid=None, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        if gminaid is not None:
            kand1 = get_object_or_404(Kandydat, numer = 1)
            kand2 = get_object_or_404(Kandydat, numer = 2)
            self.fields['gid'].initial = gminaid
            gm = Gmina.objects.get(id = gminaid)
            self.fields['k1'].initial = gm.liczbaGlosowKand1
            self.fields['k2'].initial = gm.liczbaGlosowKand2
            self.fields['k1'].label = kand1.nazwa
            self.fields['k2'].label = kand2.nazwa
