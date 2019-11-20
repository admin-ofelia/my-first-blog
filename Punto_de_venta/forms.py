from django import forms

from .models import Ubicacion, Contacto, Provedores, Caja, UnidadMedida, Departamento, Marca, Productos, Clientes, Ventas, DetalleVenta, CajaOperacion

class ProductoNuevo(forms. ModelForm):
	class Meta:
		model = Productos
		#fields = ('nombre','existencia',)
		exclude = ()

class MarcaNueva(forms. ModelForm):
	class Meta:
		model = Marca
		fields = ('nombre',)
		#exclude = ()

class DepNuevo(forms. ModelForm):
	class Meta:
		model = Departamento
		fields = ('nombre',)

class MedNuevo(forms. ModelForm):
	class Meta:
		model = UnidadMedida
		fields = ('tipo_medida',)

class UbicacionNueva(forms. ModelForm):	
	class Meta:
		model = Ubicacion
		#fields = ()
		exclude = ()
		
class ContactoNuevo(forms. ModelForm):	
	class Meta:
		model = Contacto
		exclude = ()

class ProvedorNuevo(forms. ModelForm):	
	class Meta:
		model = Provedores
		#fields = ()
		exclude=('ubicacion','contacto',)

class ClienteNuevo(forms. ModelForm):
	class Meta:
		model = Clientes
		exclude = ('ubicacion','contacto',)

class VentaNueva(forms. ModelForm):
	class Meta:
		model = Ventas
		exclude = ('forma_de_pago', 'monto_pagado', 'caja', 'cliente', 'cambio',)

class CajaNueva(forms. ModelForm):
	class Meta:
		models = Caja
		fields = ('nombre',)