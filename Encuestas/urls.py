from django.conf.urls import url, include

from . import views

app_name = 'encuestas'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<pregunta_id>[0-9]+)/$', views.detalle, name='detalle'),
	url(r'^(?P<pregunta_id>[0-9]+)/resultados/$', views.resultados, name='resultados'),
	url(r'^(?P<pregunta_id>[0-9]+)/voto/$', views.voto, name='voto'),


]