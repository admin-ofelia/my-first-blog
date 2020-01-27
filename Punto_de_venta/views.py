# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import simplejson

from pyexcel_xls import save_data
from collections import OrderedDict
#------reporte pdf---------
import os
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer, Paragraph, Table, TableStyle)
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
"""---------------------------------------------------"""
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from StringIO import StringIO
from django.conf import settings
from django.shortcuts import render

from django.utils import timezone

from django.http import HttpResponse
import json
from django.template.loader import render_to_string
from django.template import RequestContext		
from Punto_de_venta.models import Ubicacion, Contacto, Provedores, Caja, UnidadMedida, Departamento, Marca, Productos, Clientes, Ventas, DetalleVenta, CajaOperacion
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductoNuevo, MarcaNueva, DepNuevo, MedNuevo, ProvedorNuevo, UbicacionNueva, ContactoNuevo, ClienteNuevo, VentaNueva, CajaNueva, CajaAbrir, CajaCerrar

from django.shortcuts import redirect
# Create your views here.

@login_required
def ptoventa_list(request):
	return render(request, 'ptoventa_list.html', {})

@login_required
def ptoventa_detail(request):
	producto = Productos.objects.all()
	return render(request, 'prodconsultar.html', {'form': producto})

@login_required
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

@login_required
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

@login_required
def prod_eliminar(request, pk):
	producto = Productos.objects.get(pk=pk)
	producto.delete()

	return redirect('prod_consultar')

@login_required
def ptoventa_marca(request, pk):
	marca = get_object_or_404(Marca, pk=pk)
	return render(request, 'ptoventa_marca.html')

@login_required
def marca_consultar(request):
	marcas = Marca.objects.all()
	return render(request, 'marcaconsultar.html', {'marcas':marcas}) 

@login_required
def marca_eliminar(request, pk):
	objeto = Marca.objects.get(pk=pk)
	#objeto = get_object_or_404(marca, pk=pk)
	objeto.delete()

	return redirect('marca_consultar')

@login_required
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

@login_required
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

@login_required
def dep_consultar(request):
	dptos = Departamento.objects.all()
	return render(request, 'depconsultar.html', {'dep':dptos}) 

@login_required
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

@login_required
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

@login_required
def dep_eliminar(request, pk):
	objeto = Departamento.objects.get(pk=pk)
	objeto.delete()

	return redirect('dep_consultar')

@login_required
def med_consultar(request):
	medida = UnidadMedida.objects.all()
	return render(request, 'medconsultar.html', {'med': medida})

@login_required
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

@login_required
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

@login_required
def med_eliminar(request, pk):
	objeto = UnidadMedida.objects.get(pk=pk)
	objeto.delete()

	return redirect('med_consultar')

@login_required
def prov_consultar(request):
	proveedor = Provedores.objects.all()
	return render(request, 'provconsultar.html', {'prov': proveedor}) 

@login_required
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

@login_required
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

@login_required
def prov_eliminar(request, pk):
	objeto = Provedores.objects.get(pk=pk)
	objeto.delete()

	return redirect('prov_consultar')

@login_required
def cliente_consultar(request):
	objeto = Clientes.objects.all()
	return render(request, 'clienteconsultar.html', {'cliente': objeto})

@login_required
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

@login_required
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

@login_required
def cliente_eliminar(request, pk):
	objeto = Clientes.objects.get(pk=pk)
	objeto.delete()

	return redirect('cliente_consultar')

@login_required
def ventas_lista(request):
	return render(request, 'ventas.html', {})

@login_required
def ventas_contacto(request):
	
	termino = request.GET.get('term')
	objeto = Clientes.objects.filter(nombre__icontains=termino).values('pk','nombre','RFC', 'contacto__telefono','ubicacion__estado')
	data = json.dumps(list(objeto))
	mimetype = 'applications/json'
	return HttpResponse(data,mimetype)

@login_required
def ventas_producto(request):
	produc = request.GET.get('term')	
	objeto = Productos.objects.filter(nombre__icontains=produc).values('pk','nombre','codigo_barras','existencia','precio','iva')
	data = json.dumps(list(objeto))
	mimetype = 'applications/json'
	return HttpResponse(data,mimetype)

@login_required
def venta_nueva(request):
	if not request.session.has_key('caja'):
		return redirect('lista_caja')
	
	caja = request.session["caja"]
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
			caja_id = caja,
			forma_de_pago=metodo_pago,
			monto_pagado=monto_pagado, 
			total   = total, 
			fecha   = fecha, 
			subtotal=subtotal, 
			iva     =iva, 
			cambio  =cambio,
			cliente_id = cliente_id,
			empleado_id = request.user.id
			)

		venta.save()
		for elemento in articulos:

			detalle_venta = DetalleVenta(
				productos_id = elemento['id'],
				cantidad = elemento['cantidad'],
				precio = elemento['precio'],
				iva = elemento['iva'],
				descuento = elemento['descuento'],
				ventas = venta,
				importe = elemento['importe_factura'],

			)
			detalle_venta.save()
		respuesta['exito']=True

	return HttpResponse(simplejson.dumps(respuesta), content_type='application/json')

@login_required
def caja(request):
	objeto = Caja.objects.all()
	#operacion = CajaOperacion.objects.values('cajas__pk', 'pk', 'fecha_apertura')
	return render(request, 'caja.html', {'objeto': objeto})	

@login_required
def caja_sesion(request, pk):
	objeto = get_object_or_404(Caja, pk=pk)
	abrir_caja = CajaAbrir(request.POST)
	if request.method == 'POST':
		if abrir_caja.is_valid():
			operacion = abrir_caja.save(commit=False)
			operacion.empleado = request.user
			operacion.fecha_apertura = timezone.now()
			operacion.status = 1
			operacion.cajas = objeto
			operacion.save()

			request.session["caja"] = objeto.id
			request.session["operacion"] = operacion.id
			return redirect('lista_caja')

	return render(request, 'admin_cajas.html', {'caja': abrir_caja})

@login_required
def cerrar_caja(request):
	caja = request.session["operacion"]
	objeto = get_object_or_404(CajaOperacion, pk=caja)
	if request.method == 'POST':
		caja_cerrar = CajaCerrar(request.POST, instance=objeto)
		if caja_cerrar.is_valid():
			objeto = caja_cerrar.save(commit=False)
			objeto.fecha_cierre = timezone.now()
			objeto.save() 

			del request.session["caja"]
			del request.session["operacion"]
			return redirect('lista_caja')
	else:
		caja_cerrar = CajaCerrar(request.POST)

	return render(request, 'cerrar_cajas.html', {'caja': caja_cerrar})

@login_required
def operacion_caja(request):

	ubica = UbicacionNueva(request.POST, instance=objeto.ubicacion)

	if request.method == "POST":
		caja = CajaNueva(request.POST)
		objeto = CajaAbrir(request.POST)
		if objeto.is_valid() and caja.is_valid():
			caja_usuario = caja.save()
			caja_admin = objeto.save(commit=False) 
			caja_admin.cajas = caja_usuario
			caja_admin.empleado = request.user.id
			caja_admin.save()
			return redirect('lista_caja')
	else:
		caja = CajaNueva()
		objeto = CajaAbrir()
		return render(request, 'admin_cajas.html', {'objeto': objeto, 'caja': caja})

@login_required
def reporte_venta(request):
	
	if request.method == 'POST':

		fecha_inicio = request.POST['fecha_inicio']
		fecha_fin = request.POST['fecha_fin']
		cliente_id = request.POST['cliente']
		#caja = simplejson.loads(request.POST['caja'])
		caja = request.POST['caja']

		filtros = {
			

		}
		if fecha_inicio:
			filtros['fecha__gte']=fecha_inicio
		if fecha_fin:
			filtros.setdefault('fecha__lte',fecha_fin)
		if cliente_id:
			filtros['cliente_id']=cliente_id
		if caja:
			filtros['caja_id']=caja
		print filtros

		consulta = Ventas.objects.filter(**filtros)

		salida = render_to_string('contenido_reporte.html', {'objeto': consulta})
		return HttpResponse(salida)

	consulta = Ventas.objects.all()
	cajas = Caja.objects.all()
	return render(request, 'reporte.html', {'objeto': consulta, 'cajas':cajas},)
@login_required
def reporte(request):
	cliente = request.GET.get('term')	
	objeto = Clientes.objects.filter(nombre__icontains=cliente).values('pk','nombre')
	data = json.dumps(list(objeto))
	mimetype = 'applications/json'
	return HttpResponse(data,mimetype)
@login_required
def filtros_reporte(request):
	fecha_inicial = request.GET['fechaini']
	print fecha_inicial
	fecha_final = request.GET['fechafin']
	cliente_id = request.GET['cliente']
	caja = request.GET['caja']
	dicc_filtros = {}
	if fecha_inicial:
		dicc_filtros['fecha__gte']=fecha_inicial
	if fecha_final:
		dicc_filtros.setdefault('fecha__lte',fecha_final)
	if cliente_id:
		dicc_filtros['cliente_id']=cliente_id
	if caja:
		dicc_filtros['caja_id']=caja

	resultado = Ventas.objects.filter(**dicc_filtros)

	
	return resultado
@login_required
def reporte_excel(request):
	resultado = filtros_reporte(request)

	data = [
		['Id','Forma de pago','Monto pagado','total','Fecha','Subtotal','Iva','Cambio','Cliente','Caja','Empleado']
	] 

	for elemento in resultado:
		lista =[ elemento.id, elemento.get_forma_de_pago_display(), elemento.monto_pagado, elemento.total, elemento.fecha, elemento.subtotal, elemento.iva, elemento.cambio, elemento.cliente.nombre, elemento.caja.nombre, elemento.empleado.username]

		data.append( lista )
	datos = OrderedDict()
	datos.update({"Sheet 1": data})

	memoria =StringIO()

	save_data(memoria,datos)
	
	response = HttpResponse( memoria.getvalue(), content_type="application/vnd.ms-excel")
	response['Content-Disposition'] = 'inline; filename=reporte.xls'
	return response

@login_required
def reporte_pdf(request):
	print request.GET
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=Reporte.pdf'

	objeto = filtros_reporte(request)

	buffer = BytesIO()
	pdf = canvas.Canvas(buffer)
	pdf.drawImage('index.jpg', 200, 750, 120, 90,preserveAspectRatio=True)
	pdf.setFont("Helvetica", 14)
	pdf.drawString(400,770, "Reporte de ventas")
	pdf.setFont("Helvetica", 9)
	fecha_actual = datetime.now()
	print type(fecha_actual)
	r = "Fecha: %s"  % fecha_actual.strftime('%d/%m/%Y')
	pdf.drawString(60,708, r)
		
	encabezados = ('Id', 'Forma de pago', 'Monto pagado', 'Total', 'Fecha', 'Subtotal', 'Iva', 'Cambio', 'Cliente', 'Caja', 'Empleado')
	detalles = []
	y = 580
	for i in objeto:
		fecha_formateada = i.fecha.strftime('%d/%m/%Y')
		detalles.append([i.pk, i.get_forma_de_pago_display(), i.monto_pagado, i.total, fecha_formateada, i.subtotal, i.iva, i.cambio, i.cliente.nombre, i.caja.nombre, i.empleado_id])
		y = y -16
	detalle_orden = Table([encabezados] + detalles, colWidths=[25,50])
	detalle_orden.setStyle(TableStyle(
		[
			('ALIGN', (0,0),(3,0),'CENTER'),
			('GRID', (0,0),(-1,-1),1,colors.black),
			('BACKGROUND',(0,0),(-1,0),colors.green),
			('FONTSIZE',(0, 0), (-1, -1), 7)
		])
	)
	detalle_orden.wrapOn(pdf, 800, 600)
	detalle_orden.drawOn(pdf, 40, y)

	pdf.showPage()
	pdf.save()
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response

@login_required
def reporte_pdf_venta(request, pk):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=Reporte.pdf'

	objeto = DetalleVenta.objects.filter(ventas_id=pk)

	buffer = BytesIO()
	#pdf = canvas.Canvas("Reporte.pdf", pagesize = A4)
	pdf = canvas.Canvas(buffer)
	pdf.setFont("Helvetica", 16)
	pdf.drawString(40,790, "Factura")
	pdf.drawImage('index.jpg', 200, 750, 120, 90,preserveAspectRatio=True)
	#pdf.setFont("Helvetica", 14)
	#pdf.drawString(400,770, "Reporte de ventas")
	pdf.setFont("Helvetica", 9)
	for elemento in objeto:
		venta = elemento.ventas_id
		cliente = elemento.ventas.cliente.nombre
		direccion = elemento.ventas.cliente.ubicacion.calle
		numero = elemento.ventas.cliente.ubicacion.No
		ciudad = elemento.ventas.cliente.ubicacion.ciudad
		forma_pago = elemento.ventas.get_forma_de_pago_display()

	#print type(numero)
	a = str(numero)
	#print type(a)	
	pdf.drawString(60,740, "Número: %s" % venta)
	pdf.drawString(60,724, "Serie: 1")
	fecha_actual = datetime.now()
	r = "Fecha: %s"  % fecha_actual.strftime('%d/%m/%Y')
	pdf.drawString(60,708, r)

	#Tabla de informacion del cliente
	inf_cliente = []
	datos = ['Cliente: %s' % cliente, 'Comentarios']
	datos2= ['Direccion: ' + direccion + ' ' + a, '']
	datos3= ['Ciudad: %s' % ciudad, '']
	
	inf_cliente = Table([datos] + [datos2] + [datos3], colWidths=[200,150])
	inf_cliente.setStyle(TableStyle(
		[
			#('ALIGN', (0,0),(3,0),'CENTER') 
			('BOX', (0,0),(-1,-1),1,colors.black),
			('FONTSIZE',(0, 0), (-1, -1), 8)
		])
	)
	altura = 620
	inf_cliente.wrapOn(pdf, 800, 600)
	inf_cliente.drawOn(pdf,100,altura)
		
	encabezados = ('Código', 'Producto', 'Unidades', 'Precio Uni', 'Importe', 'IVA', 'Total con IVA')
	detalles = []
	y = 580
	importe_con_iva = 0
	descuento = 0
	iva = 0
	total_total = 0
	for i in objeto:
		total = i.importe + i.iva - i.descuento
		detalles.append([i.productos.codigo_barras,i.productos.nombre,i.cantidad,i.precio,i.importe,i.iva,total])
		y = y -16
		importe_con_iva = importe_con_iva + total
		descuento = descuento + i.descuento
		iva = iva + i.iva
		total_total = importe_con_iva - descuento
	print y
	detalle_orden = Table([encabezados] + detalles, colWidths=[80,70])
	detalle_orden.setStyle(TableStyle(
		[
			('ALIGN', (0,0),(3,0),'CENTER'),
			('GRID', (0,0),(-1,-1),1,colors.black),
			('BACKGROUND',(0,0),(-1,0),colors.green),
			('FONTSIZE',(0, 0), (-1, -1), 8)
		])
	)
	vertical = 440
	#subtotal_factura = 
	data = [
		['Forma de pago\n\n%s'%forma_pago,'','Subtotal','%s $'%importe_con_iva],
		['','','Descuento','%s $' %descuento],
		['','','I.V.A','%s $' %iva],
		['','','Total','%s $' %total_total]
	]

	detalle_factura = Table(data, colWidths=[29,157])
	detalle_factura.setStyle(TableStyle(
		[
			('ALIGN', (0,0),(3,0),'CENTER'),
			('GRID', (0,0),(-1,-1),1,colors.black),
			('SPAN',(0,0),(1,3)),
			('FONTSIZE',(0,0),(-1,-1),8),
			('ALIGN', (2,0),(3,2),'RIGHT'),
			('BACKGROUND', (2,3),(3,3),colors.lavender),
		])
	)
	#Establecemos el tamaño de la hoja que ocupará la tabla
	detalle_orden.wrapOn(pdf, 800, 600)
	#Definimos la coordenada donde se dibujará la tabla
	detalle_orden.drawOn(pdf, 60, y)

	detalle_factura.wrapOn(pdf,800,600)
	detalle_factura.drawOn(pdf,60,vertical)

	pdf.showPage()
	pdf.save()
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response

def bienvenida(request):
	if request.user.is_authenticated:
		return render(request, 'bienvenida.html', {})

	return redirect('login')

@login_required
def registro(request):
	# Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "registro.html", {'form': form})
	#return render(request, 'registro.html', {})	

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('pagina_inicio')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})
	#return render(request, 'login.html', {})

@login_required
def logout(request):
	do_logout(request)
	return redirect('bienvenida')
