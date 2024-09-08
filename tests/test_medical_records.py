from django.test import TestCase
from main.models import Mascota, Expediente

class ExpedienteTestCase(TestCase):
    def setUp(self):
        self.mascota = Mascota.objects.create(nombre='Rex', especie='perro')

    def test_subir_expediente(self):
        with open('test_file.pdf', 'w') as f:
            f.write('Contenido del archivo')
        expediente = Expediente.objects.create(
            mascota=self.mascota,
            archivo='test_file.pdf',
            nombre_archivo='test_file.pdf',
            tipo_archivo='PDF'
        )
        self.assertEqual(Expediente.objects.count(), 1)
        self.assertEqual(expediente.nombre_archivo, 'test_file.pdf')
