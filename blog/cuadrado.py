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


def cuadrado():
    print "Se calcularan cuadrados de numeros"

    n1 = input("Ingrese un numero entero: ")
    n2 = input("Ingrese otro numero entero: ")

    for x in range(n1,n2):
        print x, x*x

    print "Es todo por ahora" 

if __name__ == "__main__":
    cuadrado()