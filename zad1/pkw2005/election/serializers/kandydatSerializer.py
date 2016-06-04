from rest_framework import serializers
from ..models import Kandydat

class KandydatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kandydat
        fields = ('pk', 'numer', 'nazwisko', 'imiona')
