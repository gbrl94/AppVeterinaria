from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def enviar_recordatorio(cita):
    asunto = 'Recordatorio de Cita Veterinaria'
    mensaje_html = render_to_string('emails/recordatorio_cita.html', {'cita': cita})
    mensaje_texto = strip_tags(mensaje_html)
    destinatario = cita.cliente.correo

    send_mail(
        asunto,
        mensaje_texto,
        settings.DEFAULT_FROM_EMAIL,
        [destinatario],
        html_message=mensaje_html,
    )
