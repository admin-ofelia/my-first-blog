# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.utils import timezone

from django.http import HttpResponse
import json
from Punto_de_venta.models import Ubicacion, Contacto, Provedores, Caja, UnidadMedida, Departamento, Marca, Productos, Clientes, Ventas, DetalleVenta, CajaOperacion
from django.shortcuts import render, get_object_or_404
from .forms import ProductoNuevo, MarcaNueva, DepNuevo, MedNuevo, ProvedorNuevo, UbicacionNueva, ContactoNuevo, ClienteNuevo

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
	#return render(request, 'ptoventa_marcaedit.html')

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
	print "estoy Aqui"
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
	print produc;	
	objeto = Productos.objects.filter(nombre__icontains=produc).values('nombre','codigo_barras','existencia','precio')
	print objeto
	data = json.dumps(list(objeto))
	mimetype = 'applications/json'
	return HttpResponse(data,mimetype)