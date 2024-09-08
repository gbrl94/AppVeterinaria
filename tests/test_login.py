from django.test import TestCase
from django.contrib.auth import authenticate
from main.models import Cliente

class LoginTestCase(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre='Juan',
            apellido='Pérez',
            correo='juan@example.com',
            password='password123'
        )

    def test_login_correcto(self):
        user = authenticate(correo='juan@example.com', password='password123')
        self.assertIsNotNone(user)
        self.assertTrue(user.is_authenticated)

    def test_login_incorrecto(self):
        user = authenticate(correo='juan@example.com', password='wrongpassword')
        self.assertIsNone(user)
