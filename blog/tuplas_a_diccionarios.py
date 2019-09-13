# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

import os,sys
import random

os.environ['DJANGO_SETTINGS_MODULE'] = 'capacitacion.settings'
sys.path.append("/opt/capacitacion/")

from django.core. wsgi import get_wsgi_application
application = get_wsgi_application()



def cuentapalabras(cadena):
	lista = []
	diccionario = {}
	cadena = cadena[0].lower() + cadena[1: ]
	print cadena
	lista = cadena.split()
	cont = 1

	for i in lista:

		if diccionario.has_key(i):
			cont += 1
			diccionario[i] = cont
		else:
			cont = 1
			diccionario[i] = cont

	print diccionario

def cuentaletras(cadena):
	diccionario = {}

	cadena = cadena.replace(" ", "").lower()

	for i in cadena:
		diccionario[i] = 0 

	for letra in cadena:
		diccionario[letra] = diccionario[letra] + 1

	print diccionario

def tuplas_dict(lista):
	resultado = {}

	for elemento in lista:

		if resultado.has_key( elemento[0]  ):

			resultado[elemento[0]].append( elemento[1] ) 

		else:
			resultado[elemento[0]] = [ elemento[1]  ]		

	print resultado

def tuplas_a_diccionario(lista):
	
	diccionario = {}

	cont1 = 0
	cadena = ""
	cont2 = 1
	aux = ""
	for i, palabras in enumerate(lista):

		if cadena != palabras[cont1] :

			if i > 1:

				cadena = palabras[cont1]

				aux = palabras[cont2]

				llave = palabras[cont1]

				diccionario[llave] = [aux]	

				print diccionario

			else:	
				cadena = palabras[cont1]

				aux = palabras[cont2]
				#print cadena
		else:

			llave = palabras[cont1]

			diccionario[llave] = [aux,palabras[cont2]]
		

if __name__ == "__main__":

	# deberá mostrar{ 'Hola': ['don Pepito', 'don Jose'], 'Buenos': ['días'] }

	l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'dias'), ('como', 'esta'), ('como', 'que hay de nuvo') ]
	#tuplas_a_diccionario(l)
	#tuplas_dict( l )

	cadena = "Que lindo dia que hace hoy hoy"
	cadena1 = "palabras"

	cuentapalabras(cadena)

	cuentaletras(cadena1)
