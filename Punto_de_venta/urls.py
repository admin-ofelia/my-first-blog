from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.ptoventa_list, name='pagina_inicio'),
	url(r'^producto/nuevo/$', views.ptoventa_new, name='ptoventa_producto_nuevo'),
	url(r'^producto/consultar/$', views.ptoventa_detail, name='prod_consultar'),
	url(r'^producto/editar/(?P<pk>\d+)/editar/$', views.ptoventa_edit, name='prod_editar'),
	url(r'^producto/eliminar/(?P<pk>\d+)/$', views.prod_eliminar, name='prod_eliminar'),
	url(r'^marca/nuevo/$', views.marca_nueva, name='ptoventa_marca_nuevo'),
	url(r'^marca/consultar/$', views.marca_consultar, name='marca_consultar'),
	url(r'^marca/eliminar/(?P<pk>\d+)/$', views.marca_eliminar, name='marca_eliminar'),
	url(r'^marca/editar/(?P<pk>\d+)/editar/$', views.marca_editar, name='marca_editar'),
	url(r'^departamento/nuevo/$', views.dep_nuevo, name='dep_nuevo'),
	url(r'^departamento/consultar/$', views.dep_consultar, name='dep_consultar'),
	url(r'^departamento/eliminar/(?P<pk>\d+)/$', views.dep_eliminar, name='dep_eliminar'),
	url(r'^departamento/editar/(?P<pk>\d+)/editar/$', views.dep_editar, name='dep_editar'),
	url(r'^medida/nuevo/$', views.med_nuevo, name='med_nuevo'),
	url(r'^medida/consultar/$', views.med_consultar, name='med_consultar'),
	url(r'^medida/eliminar/(?P<pk>\d+)/$', views.med_eliminar, name='med_eliminar'),
	url(r'^medida/editar/(?P<pk>\d+)/editar/$', views.med_editar, name='med_editar'),
	url(r'^provedor/nuevo/$', views.prov_nuevo, name='prov_nuevo'),
	url(r'^provedor/consultar/$', views.prov_consultar, name='prov_consultar'),
	url(r'^provedor/editar/(?P<pk>\d+)/editar/$', views.prov_editar, name='prov_editar'),
	url(r'^provedor/eliminar/(?P<pk>\d+)/$', views.prov_eliminar, name='prov_eliminar'),
	url(r'^cliente/nuevo/$', views.cliente_nuevo, name='cliente_nuevo'),
	url(r'^cliente/consultar/$', views.cliente_consultar, name='cliente_consultar'),
	url(r'^cliente/editar/(?P<pk>\d+)/editar/$', views.cliente_editar, name='cliente_editar'),
	url(r'^cliente/eliminar/(?P<pk>\d+)/$', views.cliente_eliminar, name='cliente_eliminar'),
	url(r'^ventas/$', views.ventas_lista, name='ventas_lista'),
	url(r'^ventas/contacto/$', views.ventas_contacto, name='ventas_contacto'),
	url(r'^ventas/producto/$', views.ventas_producto, name='ventas_producto'),
	url(r'^ventas/nueva/$', views.venta_nueva, name='ventas_nueva'),
	url(r'^caja/$', views.caja, name='lista_caja'),
	url(r'^reporte/venta/$', views.reporte_venta, name='reporte_venta'),	

]