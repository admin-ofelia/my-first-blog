# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import simplejson
from django.shortcuts import render

from django.utils import timezone

from django.http import HttpResponse
import json
from django.template.loader import render_to_string
from django.template import RequestContext		
from Punto_de_venta.models import Ubicacion, Contacto, Provedores, Caja, UnidadMedida, Departamento, Marca, Productos, Clientes, Ventas, DetalleVenta, CajaOperacion
from django.shortcuts import render, get_object_or_404
from .forms import ProductoNuevo, MarcaNueva, DepNuevo, MedNuevo, ProvedorNuevo, UbicacionNueva, ContactoNuevo, ClienteNuevo, VentaNueva, CajaNueva

from django.shortcuts import redirect
# Create your views here.

def ptoventa_list(request):
	return render(request, 'ptoventa_list.html', {})

def ptoventa_detail(request):
	producto = Productos.objects.all()
	return render(request, 'prodconsultar.html', {'form': producto})

def ptoventa_new(request):
	
	form = ProductoNuevo()

	if request.method == "POST":
		form = ProductoNuevo(request.POST)
		if form.is_valid():
			producto = form.save()
			producto.save()

			#Aqui ya se puede imprimir el registro de la base de datos
			#print producto.nombre

			return redirect('prod_consultar')
	else:
		form = ProductoNuevo()
	return render(request, 'ptoventa_edit.html', {'form': form})

def ptoventa_edit(request, pk):
	producto = get_object_or_404(Productos, pk=pk)
	print request.method

	if request.method == "POST":
		form = ProductoNuevo(request.POST, instance=producto)
		if form.is_valid():
			producto = form.save(commit=False)

			producto.save()
			return redirect('prod_consultar')
	else:
		form = ProductoNuevo(instance=producto)
	return render(request, 'ptoventa_edit.html', {'form':form})

def prod_eliminar(request, pk):
	producto = Productos.objects.get(pk=pk)
	producto.delete()

	return redirect('prod_consultar')

def ptoventa_marca(request, pk):
	marca = get_object_or_404(Marca, pk=pk)
	return render(request, 'ptoventa_marca.html')

def marca_consultar(request):
	marcas = Marca.objects.all()
	return render(request, 'marcaconsultar.html', {'marcas':marcas}) 

def marca_eliminar(request, pk):
	objeto = Marca.objects.get(pk=pk)
	#objeto = get_object_or_404(marca, pk=pk)
	objeto.delete()

	return redirect('marca_consultar')

def marca_nueva(request):
	forma = MarcaNueva()
	
	if request.method == "POST":
		forma = MarcaNueva(request.POST)
		if forma.is_valid():
			marca = forma.save()

			return redirect('marca_consultar')
	else:
		forma = MarcaNueva()			
	return render(request, 'ptoventa_marca.html', {'hola': forma, 'jaja': 20, 'lista': [7, 'texto']})

def marca_editar(request, pk):
	objeto = get_object_or_404(Marca, pk=pk)

	if request.method == "POST":
		form = MarcaNueva(request.POST, instance=objeto)
		if form.is_valid():
			objeto = form.save(commit=False)
			objeto.save()
			return redirect('marca_consultar')
	else:
		form = MarcaNueva(instance=objeto)
	return render(request, 'ptoventa_marcaedit.html', {'form':form})

def dep_consultar(request):
	dptos = Departamento.objects.all()
	return render(request, 'depconsultar.html', {'dep':dptos}) 

def dep_nuevo(request):
	objeto = DepNuevo()

	if request.method == "POST":
		objeto = DepNuevo(request.POST)
		if objeto.is_valid():
			dpto = objeto.save()

			return redirect('dep_consultar')
	else:
		objeto = DepNuevo()			
	return render(request, 'dep_nuevo.html', {'dep': objeto})

def dep_editar(request, pk):
	objeto = get_object_or_404(Departamento, pk=pk)

	if request.method == "POST":
		form = DepNuevo(request.POST, instance=objeto)
		if form. is_valid():
			objeto = form.save(commit=False)
			objeto.save()
			return redirect('dep_consultar')
	else:
		form = DepNuevo(instance=objeto)
	return render(request, 'dep_editar.html', {'dep': form})

def dep_eliminar(request, pk):
	objeto = Departamento.objects.get(pk=pk)
	objeto.delete()

	return redirect('dep_consultar')

def med_consultar(request):
	medida = UnidadMedida.objects.all()
	return render(request, 'medconsultar.html', {'med': medida})

def med_nuevo(request):
	objeto = MedNuevo()

	if request.method == "POST":
		objeto = MedNuevo(request.POST)
		if objeto.is_valid():
			dpto = objeto.save()

			return redirect('med_consultar')
	else:
		objeto = MedNuevo()			
	return render(request, 'med_nuevo.html', {'med': objeto})

def med_editar(request, pk):	
	objeto = get_object_or_404(UnidadMedida, pk=pk)

	if request.method == "POST":
		form = MedNuevo(request.POST, instance=objeto)
		if form. is_valid():
			objeto = form.save(commit=False)
			objeto.save()
			return redirect('med_consultar')
	else:
		form = MedNuevo(instance=objeto)
	return render(request, 'med_editar.html', {'med': form})

def med_eliminar(request, pk):
	objeto = UnidadMedida.objects.get(pk=pk)
	objeto.delete()

	return redirect('med_consultar')

def prov_consultar(request):
	proveedor = Provedores.objects.all()
	return render(request, 'provconsultar.html', {'prov': proveedor}) 

def prov_nuevo(request):
	objeto = ProvedorNuevo()
	ubica = UbicacionNueva()
	contacto = ContactoNuevo()

	
	if request.method == "POST":
		
		ubica = UbicacionNueva(request.POST)
		contacto = ContactoNuevo(request.POST)
		objeto = ProvedorNuevo(request.POST)

		if objeto.is_valid() and ubica.is_valid() and contacto.is_valid():
			
			ubicacion = ubica.save()
			contacto = contacto.save()
			
			provedores = objeto.save(commit=False)
			provedores.ubicacion = ubicacion
			provedores.contacto = contacto
			provedores.save()

			return redirect('prov_consultar')

	else:
		objeto = ProvedorNuevo()
		ubica = UbicacionNueva()
		contacto = ContactoNuevo()
		return render(request, 'prov_nuevo.html', {'prov': objeto, 'ubi':ubica, 'cont':contacto })

def prov_editar(request, pk):	
	
	objeto = get_object_or_404(Provedores, pk=pk)

	if request.method == "POST":
		ubica = UbicacionNueva(request.POST, instance=objeto.ubicacion)
		contacto = ContactoNuevo(request.POST, instance=objeto.contacto)
		objeto = ProvedorNuevo(request.POST, instance=objeto)
		
		if ubica.is_valid() and contacto.is_valid() and objeto.is_valid():
			ubicacion = ubica.save()
			contacto = contacto.save()

			provedores = objeto.save(commit=False)
			provedores.ubicacion = ubicacion
			provedores.contacto = contacto
			provedores.save()
			return redirect('prov_consultar')
	else:
		ubicacion = UbicacionNueva(instance=objeto.ubicacion)
		contacto = ContactoNuevo(instance=objeto.contacto)
		objeto = ProvedorNuevo(instance=objeto)
	return render(request, 'prov_editar.html', {'prov': objeto, 'ubi': ubicacion, 'conta': contacto})


def prov_eliminar(request, pk):
	objeto = Provedores.objects.get(pk=pk)
	objeto.delete()

	return redirect('prov_consultar')

def cliente_consultar(request):
	objeto = Clientes.objects.all()
	return render(request, 'clienteconsultar.html', {'cliente': objeto})

def cliente_nuevo(request):
	formu = ClienteNuevo()
	ubi = UbicacionNueva()
	contact = ContactoNuevo()

	if request.method == "POST":
		ubi = UbicacionNueva(request.POST)
		contact = ContactoNuevo(request.POST)
		formu = ClienteNuevo(request.POST)
		if formu.is_valid() and ubi.is_valid() and contact.is_valid():
			ubicacion = ubi.save()
			contacto = contact.save()
			cliente = formu.save(commit=False)
			cliente.ubicacion = ubicacion
			cliente.contacto = contacto
			cliente.save()
			return redirect('cliente_consultar')
	else:
		formu = ClienteNuevo()
		ubi = UbicacionNueva()
		contact = ContactoNuevo()
			
		return render(request, 'cliente_nuevo.html', {'cliente': formu, 'ubic': ubi, 'contac': contact})

def cliente_editar(request, pk):
	objeto = get_object_or_404(Clientes, pk=pk)

	if request.method == "POST":
		ubi = UbicacionNueva(request.POST, instance = objeto.ubicacion)
		cont = ContactoNuevo(request.POST, instance = objeto.contacto)
		objeto = ClienteNuevo(request.POST, instance = objeto) 

		if ubi.is_valid() and cont.is_valid() and objeto.is_valid():
			ubicacion = ubi.save()
			contacto = cont.save()
			clientes = objeto.save(commit=False)
			clientes.ubicacion = ubicacion
			clientes.contacto = contacto
			clientes.save()
			#return redirect('cliente_consultar')
	else:
		ubicacion = UbicacionNueva( instance = objeto.ubicacion)
		contacto = ContactoNuevo( instance = objeto.contacto)
		objeto = ClienteNuevo( instance = objeto) 

	return render(request, 'cliente_editar.html', {'clien': objeto, 'ubicac': ubicacion, 'conta': contacto})

def cliente_eliminar(request, pk):
	objeto = Clientes.objects.get(pk=pk)
	objeto.delete()

	return redirect('cliente_consultar')

def ventas_lista(request):
	return render(request, 'ventas.html', {})
	
def ventas_contacto(request):
	
	termino = request.GET.get('term')
	objeto = Clientes.objects.filter(nombre__icontains=termino).values('pk','nombre','RFC', 'contacto__telefono','ubicacion__estado')
	data = json.dumps(list(objeto))
	mimetype = 'applications/json'
	return HttpResponse(data,mimetype)

def ventas_producto(request):
	produc = request.GET.get('term')	
	objeto = Productos.objects.filter(nombre__icontains=produc).values('pk','nombre','codigo_barras','existencia','precio','iva')
	data = json.dumps(list(objeto))
	mimetype = 'applications/json'
	return HttpResponse(data,mimetype)

def venta_nueva(request):

	respuesta = {'exito':False}
	#print request.POST['articulos']
	#print type( request.POST['articulos'] )
	#print type(articulos)
	#articulos = simplejson.loads(request.POST['articulos'])

	fecha = timezone.now()

	if request.method == "POST":

		monto_pagado = request.POST['monto_pagado']
		subtotal = request.POST['subtotal']
		iva = request.POST['iva']
		total = request.POST['total'] 
		metodo_pago = request.POST['metodo_pago']
		cambio = request.POST['total_cambio']
		cliente_id = request.POST['cliente_id']
		forma_pago = request.POST['metodo_pago']

		articulos = simplejson.loads(request.POST['articulos'])

		venta = Ventas(
			caja_id = 1,
			forma_de_pago=metodo_pago,
			monto_pagado=monto_pagado, 
			total   = total, 
			fecha   = fecha, 
			subtotal=subtotal, 
			iva     =iva, 
			cambio  =cambio,
			cliente_id = cliente_id,
			empleado_id =1
			)

		venta.save()
		for elemento in articulos:

			detalle_venta = DetalleVenta(
				productos_id = elemento['id'],
				cantidad = elemento['cantidad'],
				precio = elemento['precio'],
				iva = elemento['iva'],
				descuento = elemento['descuento'],
				ventas = venta

			)
			detalle_venta.save()
		respuesta['exito']=True

	return HttpResponse(simplejson.dumps(respuesta), content_type='application/json')

def caja(request):
	objeto = Caja.objects.all()
	return render(request, 'caja.html', {'objeto': objeto})	

def reporte_venta(request):
	
	if request.method == 'POST':

		fecha_inicio = request.POST['fecha_inicio']
		fecha_fin = request.POST['fecha_fin']
		cliente_id = request.POST['cliente']

		filtros = {
			

		}
		if fecha_inicio:
			filtros['fecha__gte']=fecha_inicio
		if fecha_fin:
			filtros.setdefault('fecha__lte',fecha_fin)
		if cliente_id:
			filtros['cliente_id']=cliente_id

		print filtros

		consulta = Ventas.objects.filter(**filtros)

		salida = render_to_string('contenido_reporte.html', {'objeto': consulta})
		return HttpResponse(salida)

	consulta = Ventas.objects.all()
	return render(request, 'reporte.html', {'objeto': consulta},)