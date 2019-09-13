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


def operacion():
	a = 10
	b = 100
	c = 1000

	#((b * b) - (4 * a * c)) / (2 * a), b) (b * b - 4 * a * c) / (2 * a)   
	resultado = (b * b) - (4 * a * c / 2 * a)
	print resultado

def pcn_loop():
    hayMasDatos = "Si"
    while hayMasDatos == "Si":
        x = input("Ingrese un numero: ")
        if x > 0:
            print "Numero positivo"
        elif x == 0:
            print "Igual a 0"
        else:
            print "Numero negativo"

        hayMasDatos = raw_input("Quiere seguir? <Si-No>: ")

""" Ciclo while usando centinela"""
def pcn_loop2():
    x=raw_input("Ingrese un numero ('*' para terminar): ")

    while x != "*":
        if x > 0:
            print "Numero positivo"
        elif x == 0:
            print "Igual a 0"
        else:
            print "Numero negativo"

        x=raw_input("Ingrese un numero ('*' para terminar): ")

""" Ahora usando while True"""
def pcn_loop3():
    while True:
        x = raw_input("Ingrese un numero ('*' para terminar): ")
        if x == '*':
            break
        elif x > 0:
            print "Numero positivo"
        elif x == 0:
            print "Igual a 0"
        else:
            print "Numero negativo"

def menor_factor_primo(x):
    """ Devuelve el menor factor primo del número x. """
    n = 2
    while n <= x:
        if x % n == 0:
            return n

def buscar_impar(x):
    """ Divide el número recibido por 2 hasta que sea impar. """
    while x % 2 == 0:
        
        x = x / 2 if x > 0 else 1

    return x


if __name__ == "__main__":

	#operacion()
	#pcn_loop()
	#pcn_loop2()
	#pcn_loop3()
	#resultado = menor_factor_primo(35)
	#print resultado
	resultado2 = buscar_impar(0)
	print resultado2