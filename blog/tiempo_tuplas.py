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

t1 = (40,)
t2 = (50,)

def suma(t1,t2):
	resultado = t1[0] + t2[0]
	return resultado

def diaSiguienteE():
	f1 = (3,9,2019)
	f2 = f1[0]
	f3 = (f2+1,9,2019)
	print f1[:3], f3[:3]

if __name__ == "__main__":

	#result = suma(t1,t2)
	#print result
	diaSiguienteE()