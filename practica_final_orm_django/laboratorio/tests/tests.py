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

    def test_laboratorio_url_crear(self):
        # Verificar que la URL de crear laboratorio devuelve un 200 (o 302 si requiere login)
        response = self.client.get(reverse('crear_laboratorio'))
        self.assertIn(response.status_code, [200, 302])
    
    def test_laboratorio_url_editar(self):
        # Verificar que la URL de editar laboratorio devuelve un 200 (o 302 si requiere login)
        response = self.client.get(reverse('editar_laboratorio', args=[self.laboratorio.id]))
        self.assertIn(response.status_code, [200, 302])
    
    def test_laboratorio_url_eliminar(self):
        # Verificar que la URL de eliminar laboratorio devuelve un 200 (o 302 si requiere login)
        response = self.client.get(reverse('eliminar_laboratorio', args=[self.laboratorio.id]))
        self.assertIn(response.status_code, [200, 302])
    
    def test_lista_laboratorios_template(self):
        # Verificar que se usa la plantilla correcta para la lista de laboratorios
        response = self.client.get(reverse('lista_laboratorios'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio/lista.html')