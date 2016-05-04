from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name = 'index'),
        url(r'^mapdata', views.mapdata, name = 'mapdata'),
        url(r'^rodzaje', views.rodzaje, name = 'rodzaje'),
        url(r'^wojewodztwa', views.wojewodztwa, name = 'wojewodztwa'),
        url(r'^stats', views.stats, name = 'stats'),
        url(r'^seemore', views.seemore, name = 'seemore'),
]
