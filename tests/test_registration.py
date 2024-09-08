from django.test import TestCase
from django.core import mail
from main.models import Cliente

class ClienteTestCase(TestCase):
    def test_registro_cliente(self):
        response = self.client.post('/register/', {
            'nombre': 'Juan',
            'apellido': 'Pérez',
            'rut': '12345678-9',
            'telefono': '123456789',
            'correo': 'juan@example.com',
            'direccion': 'Calle Falsa 123',
            'password': 'password123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Confirmación de registro', mail.outbox[0].subject)
