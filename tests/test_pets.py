from django.test import TestCase
from main.models import Cliente, Mascota

class MascotaTestCase(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nombre='Juan', correo='juan@example.com', password='password123')

    def test_registrar_mascota(self):
        mascota = Mascota.objects.create(
            nombre='Rex',
            especie='perro',
            raza='labrador',
            sexo='M',
            peso=25.0,
            edad=5,
            cliente=self.cliente
        )
        self.assertEqual(Mascota.objects.count(), 1)
        self.assertEqual(mascota.nombre, 'Rex')
