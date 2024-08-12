from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from main.models import Cita  # Ajusta 'main' según el nombre real de tu aplicación
from main.email_utils import enviar_recordatorio  # Ajusta la importación según tu estructura

class Command(BaseCommand):
    help = 'Envía recordatorios de citas próximas'

    def handle(self, *args, **kwargs):
        ahora = timezone.now()
        en_24_horas = ahora + timedelta(hours=24)
        citas = Cita.objects.filter(fecha=en_24_horas.date(), hora__gte=ahora.time(), hora__lt=(ahora + timedelta(hours=1)).time())

        for cita in citas:
            enviar_recordatorio(cita)
            self.stdout.write(self.style.SUCCESS(f'Se ha enviado un recordatorio para la cita de {cita.mascota.nombre}'))
