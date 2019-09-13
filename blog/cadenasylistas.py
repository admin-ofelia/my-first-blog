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

def cuentapalabra(cadena):
	contador = 0
	cx = cadena
	lista = cx.split()
	print cx
	for i in lista:
		#print i
		if len(i) > 5:
			contador += 1
			#print len(i)
	print "Hay", contador, "palabras con mas de cinco letras"

def telegramas(cadena,costopc,costopl):

	print cadena
		
	num_cortas = 0
	num_largas = 0

	palabras = cadena.split(" ")

	telegrama = []

	for palabra in palabras:

		nueva_palabra = palabra

		if len(palabra ) > 5:
			num_largas += 1
			nueva_palabra = nueva_palabra[:5] + "@"

		else:
			num_cortas += 1

		telegrama.append( nueva_palabra )

		if palabra == palabras[-1]:
			telegrama.append('STOPSTOP')

		else:
			if palabra.endswith('.'):
				telegrama.append('STOP')

	print " ".join(telegrama)

	costototal = costopc * num_cortas + costopl * num_largas

	print "Longitud:", len(palabras)
	print "Cortas:", num_cortas
	print "Largas:", num_largas
	print "Total", costototal


	
	"""


	frase1 = cadena.split(" ")
	print frase1 
	frase2 = []
	for lista in frase1:
		if len(lista) > 5:
			palabra = lista[:5]
			frase2.append(palabra)	
	print frase2

	aux = []
	for y in frase2:
		a = "@"
		cadenaf = y + a
		aux.append(cadenaf)
	print aux

	#			Aquí se forma el resultado del texto del telegrama final 

	q = " ".join(frase2)

	for indice1, i in enumerate(frase1):
		#print indice1, "-", i
			for indice2, j in enumerate(frase2):
				if not frase2[indice1] in frase1: 
					print "Estoy Aquí"
			#print frase1[indice1], frase2[indice2]
			#else:
			#	print "No son iguales"

	"""

	

if __name__ == "__main__":

	#cuentapalabra("una cadena de palabras separadas por espacios")
	telegramas(u"Llego manana. Alrededor del mediodia. Voy a almorzar.".encode('utf-8'),5,10)