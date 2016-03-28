from django.contrib import admin
from .models import Wojewodztwo, Gmina, RodzajGminy, Kandydat

# Register your models here.
admin.site.register(Wojewodztwo)
admin.site.register(Gmina)
admin.site.register(RodzajGminy)
admin.site.register(Kandydat)

