from django.test import TestCase
from django.core import mail
from main.models import Cliente

class NotificacionesTestCase(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nombre='Juan', correo='juan@example.com', password='password123')

    def test_envio_notificacion(self):
        # Simulación del envío de notificación
        mail.send_mail(
            'Asunto de prueba',
            'Contenido del mensaje',
            'from@example.com',
            [self.cliente.correo]
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Asunto de prueba')
