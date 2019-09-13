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


def saludo():
  
    a = raw_input("¿Cual es su nombre?".encode('utf-8'))
    print "Hola", a

    #for elemento in range(100): print a,
    	
    cadena = list("esta es una frase")

    print cadena
    for x in cadena:
    	print x


def repite_saludo(n,bienvenida):
   for i in range(n):
   		a = bienvenida
   		print a

def repite_saludo2(n,msg):
	for i in range(n):
		salida = msg * n
		print salida

def contarA(x):
    """ La funcion contarA(x) cuenta cuántas
        letras "A" aparecen en la cadena x ."""
    contador = 0
    for letra in x:
        if letra == "A":
            contador = contador + 1
    return(contador)


if __name__ == "__main__":
    #saludo()
    #repite_saludo(10,"Hola usuario")
	repite_saludo2(2,"Hola usuario")
	contador = contarA("AAna")
	print contador