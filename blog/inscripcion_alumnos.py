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



if __name__ == "__main__":

	# Iniciamos la interacción con el usuario
	print "Inscripcion en el curso 04 de 75.40"

	# Leemos el primer padrón

	ins = []
	
	while True:

		print "Presiona 1 para mostrar"
		print "Presiona 2 para agregar"
		print "Presiona 0 para borrar"
		print "Presiona -1 para salir"
		a = input("Ingresa una opcion: ") 


		if (a == 1):


			print "Esta es la lista de inscritos: ", ins

		if (a == 2):

			padron = input("Ingresa un # de padron: ")
			name = raw_input("Ingresa el nombre: ")
			apellido = raw_input("Ingresa el apellido: ")

			if padron not in ins:
      				d = padron,name,apellido
      				ins.append(d) 
      				#print ins 

		if (a == 0):
			e = input("Ingresar un padron para borrar: ")
   			
   			aux = []

   			encontrado = 'no'
   			for indice, i in enumerate(ins):
   				#print indice, "-", i
   				aux.append(ins[indice])

   				tupla = aux[indice]
   				x,y,z = tupla

   				
   				if x == e:
 
   					ins.pop(indice)
   					encontrado = 'si'
   					#print ins[indice]

   			if encontrado == "no":
   				print "El padron no se encuentra en la lista"

		if (a == -1):
			break

