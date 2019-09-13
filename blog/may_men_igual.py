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

def clasificar(lista,numero):
	menores = []
	mayores = []
	iguales = []

	for i in lista:
		if i < numero:
			menores.append(i)
		if i == numero:
			iguales.append(i)
		if i > numero:
			mayores.append(i)
	
	print "Menores que ", numero, menores	
	print "Mayores que ", numero, mayores
	print "Iguales que ", numero, iguales



if __name__ == "__main__":

	clasificar([78455,89211,66540,45750,89211],89211)