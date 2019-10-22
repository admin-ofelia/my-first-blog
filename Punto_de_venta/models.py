# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.

class Ubicacion(models.Model):
	#id = models.AutoField(primary_key=True)
	estado = models.CharField(max_length=40)
	municipio = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=40)
	calle = models.CharField(max_length=50)
	No = models.IntegerField()

class Contacto(models.Model):
	#id = models.AutoField(primary_key=True)
	telefono = models.CharField(max_length=50)
	correo = models.EmailField(max_length=75)
	celular = models.CharField(max_length=50)

	def __str__(self):
        	return self.telefono

class Provedores(models.Model):
	nombre = models.CharField(max_length=30)
	clave = models.CharField(max_length=30)
	ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
	contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE)

	def __str__(self):
	        return self.nombre

class Caja(models.Model):
	nombre = models.CharField(max_length=30)
	empleado = models.ForeignKey('auth.User', on_delete=models.CASCADE)

	def __str__(self):
    	    return self.nombre

class UnidadMedida(models.Model):
	tipo_medida = models.CharField(max_length=50)
	
	def __str__(self):
        	return self.tipo_medida

class Departamento(models.Model):
	nombre = models.CharField(max_length=50)
	
	def __str__(self):
	        return self.nombre

class Marca(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
    	    return self.nombre

class Productos(models.Model):
	provedores = models.ManyToManyField(Provedores)
	nombre = models.CharField(max_length=50)
	codigo_barras = models.CharField(max_length=30)
	precio = models.IntegerField() 
	iva = models.CharField(max_length=5)
	existencia = models.IntegerField()
	marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
	dep = models.ForeignKey(Departamento, on_delete=models.CASCADE)
	unidad_de_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)

	def __str__(self):
        	return self.nombre

class Clientes(models.Model):
	nombre = models.CharField(max_length=30)
	RFC =  models.CharField(max_length=60)
	clave = models.CharField(max_length=30)
	contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE)
	ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

	def __str__(self):
 	       return self.nombre

class Ventas(models.Model):
	FORMA_PAGO = (
		('01', 'EFECTIVO'),
		('02', 'TRANSFERENCIA'),
		('03', 'TARJETA'),
	)
	forma_de_pago = models.CharField(max_length=2, choices=FORMA_PAGO, default='01')
	monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
	caja = models.ManyToManyField(Caja)
	total = models.DecimalField(max_digits=10, decimal_places=2)
	fecha = models.DateTimeField(default=timezone.now)
	subtotal = models.DecimalField(max_digits=10, decimal_places=2)
	iva = models.DecimalField(max_digits=10, decimal_places=2)
	cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
	cambio = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
    	    return self.cliente

class DetalleVenta(models.Model):
	productos = models.ForeignKey(Productos, on_delete=models.CASCADE)
	cantidad = models.DecimalField(max_digits=10, decimal_places=2)
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	iva = models.DecimalField(max_digits=10, decimal_places=2)
	descuento = models.DecimalField(max_digits=10, decimal_places=2)
	ventas = models.ForeignKey(Ventas, on_delete=models.CASCADE)

	def __str__(self):
        	return self.cantidad

class CajaOperacion(models.Model):
	fecha_apertura = models.DateTimeField(default=timezone.now)
	fecha_cierre = models.DateTimeField(default=timezone.now)
	saldo_inicial = models.DecimalField(max_digits=10, decimal_places=2)
	saldo_final = models.DecimalField(max_digits=10, decimal_places=2)
	empleado = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	cajas = models.ForeignKey(Caja, on_delete=models.CASCADE)

	def __str__(self):
        	return self.empleado
