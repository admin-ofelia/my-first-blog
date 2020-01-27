# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Pregunta

# Create your tests here.

class PreguntaModelTest(TestCase):
	def test_was_published_recently_with_future_pregunta(self):
		time = timezone.now() + datatime.timedelta(days=30)
		future_pregunta = Pregunta(pub_date=time)
		self.assertIs(future_pregunta.was_published_recently(), False)