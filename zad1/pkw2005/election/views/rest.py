from ..models import Gmina, Wojewodztwo, Kandydat, RodzajGminy
from ..serializers import GminaSerializer, WojewodztwoSerializer
from ..serializers import KandydatSerializer, RodzajSerializer
from rest_framework import mixins, generics

class GminaList(generics.ListCreateAPIView):
    queryset = Gmina.objects.all()
    serializer_class = GminaSerializer


class GminaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gmina.objects.all()
    serializer_class = GminaSerializer

class WojewodztwoList(generics.ListAPIView):
    queryset = Wojewodztwo.objects.all()
    serializer_class = WojewodztwoSerializer

class KandydatList(generics.ListAPIView):
    queryset = Kandydat.objects.all()
    serializer_class = KandydatSerializer

class RodzajList(generics.ListAPIView):
    queryset = RodzajGminy.objects.all()
    serializer_class = RodzajSerializer
