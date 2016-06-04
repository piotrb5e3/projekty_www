from rest_framework import serializers
from ..models import Wojewodztwo

class WojewodztwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wojewodztwo
        fields = ('pk', 'numer', 'nazwa', 'hckey')
