from django.conf.urls import url, include
from django.contrib.staticfiles import views
from . import views as v

urlpatterns = [
        #url(r'^$', views.index, name = 'index'),
        #'django.contrib.staticfiles.views',
        url(r'^(?:index.html)?$', views.serve, kwargs={'path': 'index.html'}),
        url(r'^stats', v.stats, name = 'stats'),
        url(r'gminy/$', v.GminaList.as_view()),
        url(r'gminy/(?P<pk>[0-9]+)/$$', v.GminaDetail.as_view()),
        url(r'wojewodztwa/$', v.WojewodztwoList.as_view()),
        url(r'kandydaci/$', v.KandydatList.as_view()),
        url(r'rodzaje/$', v.RodzajList.as_view()),
        #url(r'^mapdata', views.mapdata, name = 'mapdata'),
        #url(r'^rodzaje', views.rodzaje, name = 'rodzaje'),
        #url(r'^wojewodztwa', views.wojewodztwa, name = 'wojewodztwa'),
        #url(r'^stats', views.stats, name = 'stats'),
        #url(r'^seemore', views.seemore, name = 'seemore'),
        #url(r'^gedit', views.edit_gmina, name = 'edit_gmina'),
        #url(r'^gverify', views.submit_gmina, name = 'submit_gmina'),
        url('^', include('django.contrib.auth.urls')),

]
