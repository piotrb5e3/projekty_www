from django.shortcuts import get_object_or_404
from django import forms
from ..models import Gmina, Kandydat

class GminaEditForm(forms.Form):
    gid = forms.IntegerField(widget=forms.HiddenInput())
    rev = forms.IntegerField(widget=forms.HiddenInput())
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
            self.fields['rev'].initial = gm.rev
            self.fields['k1'].label = kand1.nazwa
            self.fields['k2'].label = kand2.nazwa
        else:
            kand1 = get_object_or_404(Kandydat, numer = 1)
            kand2 = get_object_or_404(Kandydat, numer = 2)
            self.fields['k1'].label = kand1.nazwa
            self.fields['k2'].label = kand2.nazwa

    def clean(self):
        cleaned_data = super(GminaEditForm, self).clean()
        gm = Gmina.objects.get(id = cleaned_data.get("gid"))

        if (cleaned_data.get("k1") is not None and
                cleaned_data.get("k2") is not None) :
            if (cleaned_data.get("k1") + cleaned_data.get("k2") >
                gm.liczbaGlosowOddanych) :
                msg = "Liczba głosów przekracza liczbę głosów oddanych (" + str(gm.liczbaGlosowOddanych) +")"
                self.add_error('k1', msg)
                self.add_error('k2', msg)
        if(cleaned_data.get("rev") != gm.rev):
            self.add_error('rev', "Dane zostały zmodyfikowane. Odświerz!")

