from ..models import Gmina, Wojewodztwo, Kandydat, RodzajGminy
from ..serializers import GminaSerializer, WojewodztwoSerializer
from ..serializers import KandydatSerializer, RodzajSerializer
from ..serializers import UserSerializer
from rest_framework import mixins, generics, status, permissions
from rest_framework.response import Response
from django.db import transaction
from django.contrib.auth.models import User

class GminaList(generics.ListCreateAPIView):
    queryset = Gmina.objects.all()
    serializer_class = GminaSerializer

class GminaDetail(mixins.RetrieveModelMixin,
        generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Gmina.objects.all()
    serializer_class = GminaSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @transaction.atomic
    def patch(self, request, pk, format=None):
        try:
            revnum = int(request.data["rev"])
            k1 = int(request.data["liczbaGlosowKand1"])
            k2 = int(request.data["liczbaGlosowKand2"])
        except KeyError:
            return Response("Missing data", status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response("Bad data", status=status.HTTP_400_BAD_REQUEST)
        try:
            gmina = Gmina.objects.get(pk=pk)
        except Gmina.DoesNotExist:
            return Response("Gmina not found", status=status.HTTP_400_BAD_REQUEST)
        if revnum != gmina.rev or k1 + k2 > gmina.liczbaGlosowOddanych:
            return Response("Newer version available",
                    status=status.HTTP_409_CONFLICT)

        gmina.update_glosy(k1, k2, revnum, request.user);
        
        return Response("OK", status=status.HTTP_200_OK)


class WojewodztwoList(generics.ListAPIView):
    queryset = Wojewodztwo.objects.all()
    serializer_class = WojewodztwoSerializer

class KandydatList(generics.ListAPIView):
    queryset = Kandydat.objects.all()
    serializer_class = KandydatSerializer

class KandydatDetail(generics.RetrieveAPIView):
    queryset = Kandydat.objects.all()
    serializer_class = KandydatSerializer

class RodzajList(generics.ListAPIView):
    queryset = RodzajGminy.objects.all()
    serializer_class = RodzajSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
