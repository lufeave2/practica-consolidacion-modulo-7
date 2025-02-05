from django.test import TestCase
from django.urls import reverse
from laboratorio.models import Laboratorio

class LaboratorioTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear un laboratorio de prueba
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Lab Químico",
            direccion="Calle 123",
            telefono="123456789",
            ciudad="Ciudad Ejemplo",
            pais="País Ejemplo"
        )
    
    def test_laboratorio_nombre(self):
        # Verificar que el nombre es el esperado
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(laboratorio.nombre, "Lab Químico")

    def test_laboratorio_url_lista(self):
        # Verificar que la URL de la lista de laboratorios devuelve un 200
        url = reverse('lista_laboratorios')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)