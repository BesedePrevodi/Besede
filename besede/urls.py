from django.conf.urls import url

from besede import views

urlpatterns = [
    url(r'vpisN/$', views.vpisN, name='vpisN'),
    url(r'vpisS/$', views.vpisS, name='vpisS'),
    url(r'vpisB/$', views.vpisB, name='vpisB'),    
    url(r'kviz/$',   views.kviz,  name='kviz' ),
    url(r'kvizB/$',  views.kvizB,  name='kvizB' ),
    url(r'kvizC/$',  views.kvizC,  name='kvizC' ),
]
