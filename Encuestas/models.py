# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType

import datetime

from django.utils import timezone
# Create your models here.

class Pregunta(models.Model):
	texto_pregunta = models.CharField(max_length=200)
	pub_date 		 = models.DateTimeField('date_published')

	def __str__(self):
		return self.texto_pregunta

class Opcion(models.Model):
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	opcion_texto = models.CharField(max_length=200)
	votos = models.IntegerField(default=0)

	def __str__(self):
		return self.opcion_texto