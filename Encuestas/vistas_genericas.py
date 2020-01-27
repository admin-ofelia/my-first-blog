class IndexView(generic.ListView):
	plantilla_nombre = 'index.html'
	contexto_obj_nombre = 'ultima_preg_lista'

	def get_queryset(self):
		return Pregunta.objects.order_by('-pub_date')[:5]

class DetalleView(generic.DetalleView):
	model = Pregunta
	plantilla_nombre = 'detalle.html'

class ResultadosView(generic.DetalleView):
	model = Pregunta
	plantilla_nombre = 'resultados.html'

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