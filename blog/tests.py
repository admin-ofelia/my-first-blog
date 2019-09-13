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

#def lista():

#	lista = [10, "cadena", ['cadena_lista', { 'nombres': ['juan', 'pedro', 'maria'] }], {5: 'cadena en diccionario'} ]

#	lista.insert(1 ,'cadena_final')

#	print lista[3][1]['nombres'][2]

#	lista[3][1]['nombres'].append('Jorge')
#	print lista

#	if a=="algo"
#	if a!="algo"
#	if a>="algo"
#	if a<"algo"

#	valor = 0
#	valor = None
#	valor = ""
#	valor = Decimal()
#	valor = datetime.now()
#	valor = []
#	valor = {'nombre': 'juan', 'edad': '20'}
#	valor = ()


def holaMar():
	print "Hola Martha!"
	print "Estoy programando en Python. "

def hola(alguien):
	print "Hola", alguien, "!"
	print "Estoy programando en Python."

def cuad1(num):
	print num*num

def cuad2():
	n = input(u"Ingrese un número: ".encode('utf-8'))
	cuad1(n)

def cuadrado(x):
	cua = x * x
	return cua

def cuadrado3():
	print cuadrado(2) 
	print cuadrado(3) 
	print cuadrado(4) 
	print cuadrado(5) 
	print cuadrado(6) 
	print cuadrado(7) 
	print cuadrado(8) 
	 
#def cuadradofor():
#	for x in range(2,9)
#		print cuadrado(x)

#def sumar2():
#	print "prueba"


if __name__ == "__main__":

	#lista()
	#holaMar()
	#hola("Ana")
	#hola("Juan")
	#cuad1(3)
	#cuad2()
	#s = cuadrado(5)
	#print s
	#cuadrado3()
	#cuadradofor()

	for i in [3, 1, 4, 1, 5]:
		print i