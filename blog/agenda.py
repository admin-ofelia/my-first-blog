# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

import os,sys
import random

os.environ['DJANGO_SETTINGS_MODULE'] = 'capacitacion.settings'
sys.path.append("/opt/capacitacion/")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


def dados(iteraciones):
	lista = []
	resultado = {}

	import random 

	for i in range(1,iteraciones + 1):
		a = random.randint(1,6)
		b = random.randint(1,6)
		print a, b

		suma = a + b

		lista.append(suma)

		resultado[suma] = 0

	for y in lista:
		if resultado.has_key(y):
			resultado[y] = resultado[y] + 1
	print resultado


def agenda():

	print "A G E N D A"

	contactos = {}

	while True:

		print "Presiona 1 para BUSCAR"
		print "Presiona 2 para AGREGAR"
		print "Presiona 0 para BORRAR"
		print "Presiona * para SALIR"
		a = raw_input("Ingresa una opcion: ") 

		if a == "1":
			nombre = raw_input("Nombre a buscar: ")

			for clave,valor in contactos.iteritems(): 
				if clave == nombre:
					print clave, valor
					x = raw_input("Desea modificar el telefono (s/n): ")
					break
				else: 
					print "El contacto %s no esta agregado" %(nombre)

			if x == "s":
				nvotel = input("Ingresa el nuevo telefono: ")
				contactos[clave] = nvotel

		if a == "2":
			print "**Llenar los campos del contacto**"
			
			nom = raw_input("Ingresa el nombre: ")
			tel = input("Ingresa el telefono: ")

			contactos[nom] = tel 

		if a == "0":
			borrar = raw_input("Nombre a borrar: ")

			for llave,valor in contactos.iteritems():
				if llave == borrar:
					del contactos[llave]
					break

		if a == "*":
			break


if __name__ == "__main__":

	#dados(5);
	agenda()