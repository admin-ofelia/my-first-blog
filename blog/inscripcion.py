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
	padron=input("Ingresa un padron (<0 para terminar =0 para borrar): ")

	# Procesamos los padrones
	# Inicialmente no hay inscritos
	ins = [] 

	while padron >= 0:
   		if padron not in ins and padron != 0:
      			ins.append(padron)
   		elif padron == 0:
   				a = input("Ingresar un padron para borrar: ")
   				if a in ins:
   					ins.remove(a)
   				else:
   					print "El valor no esta en lista"
   		else:
      			print "Ya figura en la lista"

   		# Leemos otro padrón mas
   		padron=input("Ingresa un padron (<0 para terminar =0 para borrar): ")

	# Mostramos el resultado
	print "Esta es la lista de inscritos: ", ins