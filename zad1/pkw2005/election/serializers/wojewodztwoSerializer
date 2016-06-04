from rest_framework import serializers
from ..models import Gmina

class GminaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gmina
        fields = ('pk', 'nazwa', 'rodzaj', 'wojewodztwo', 'liczbaMieszkancow',
                'liczbaUprawnionych', 'liczbaWydanychKart',
                'liczbaGlosowOddanych', 'liczbaGlosowWaznych',
                'liczbaGlosowKand1', 'liczbaGlosowKand2', 'rev', 'revtime',
                'revuser')
