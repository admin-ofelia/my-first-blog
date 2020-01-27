# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import Template
from django.template import loader
from django.http import Http404
from django.views import generic

from .models import Pregunta, Opcion


# Create your views here.

def index(request):
	ultima_pregunta = Pregunta.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('index.html')
	contexto = {
		'ultima_pregunta': ultima_pregunta,
	}
	#return HttpResponse(template.render(contexto, request))

	#*******Utlizando render*****
	return render(request, 'index.html', contexto)
	#salida = ', '.join([q.texto_pregunta for q in ultima_pregunta])
	#return HttpResponse(salida)

def detalle(request, pregunta_id):
	"""try:
		pregunta = Pregunta.objects.get(pk=pregunta_id)
	except Pregunta.DoesNotExist:
		raise Http404("Pregunta no encontrada")
	return render(request, 'detalle.html', {'pregunta': pregunta})
	#return HttpResponse("Estas viendo la pregunta %s." % pregunta_id)"""
	pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
	return render(request, 'detalle.html', {'pregunta': pregunta})

def resultados(request, pregunta_id):
	pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
	return render(request, 'resultados.html', {'pregunta': pregunta})

def voto(request, pregunta_id):
	pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
	try:
		seleccion_opcion = pregunta.opcion_set.get(pk=request.POST['opcion'])
	except (KeyError, Opcion.DoesNotExist):
		return render(request, 'detalle.html', {
			'pregunta': pregunta,
			'mensaje_error': "No seleccionaste una opcion.",
		})
	else:
		seleccion_opcion.votos += 1
		seleccion_opcion.save()
		return HttpResponseRedirect(reverse('encuestas:resultados', args=(pregunta.id,)))
	#return HttpResponse("Votaste por la pregunta %s." % pregunta_id)