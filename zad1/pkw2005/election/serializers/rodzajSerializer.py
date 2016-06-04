from rest_framework import serializers
from ..models import RodzajGminy

class RodzajSerializer(serializers.ModelSerializer):
    class Meta:
        model = RodzajGminy
        fields = ('pk', 'nazwa')
