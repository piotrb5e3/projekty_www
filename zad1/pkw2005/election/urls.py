from django.conf.urls import url, include
from django.contrib.staticfiles import views
from . import views as v

urlpatterns = [
        url(r'^(?:index.html)?$', views.serve, kwargs={'path': 'index.html'}),
        url(r'^stats', v.stats, name = 'stats'),
        url(r'gminy/$', v.GminaList.as_view()),
        url(r'gminy/(?P<pk>[0-9]+)/$$', v.GminaDetail.as_view()),
        url(r'wojewodztwa/$', v.WojewodztwoList.as_view()),
        url(r'kandydaci/$', v.KandydatList.as_view()),
        url(r'kandydaci/(?P<pk>[0-9]+)/$$', v.KandydatDetail.as_view()),
        url(r'rodzaje/$', v.RodzajList.as_view()),
        url('^', include('django.contrib.auth.urls')),

]
