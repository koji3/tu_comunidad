from django.test import TestCase

class QuestionMethodTests(TestCase):
	def test_de_prueba(self):
		numero = 4
		self.assertEqual(numero, 4)
		print ("OK")
