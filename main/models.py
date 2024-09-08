from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    rut = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=255)
    direccion = models.CharField(max_length=255)
    creado = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=255)

class Mascota(models.Model):
    nombre = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    raza = models.CharField(max_length=255)
    sexo = models.CharField(max_length=10)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    edad = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  

      # Fechas de vacunación
    fecha_vacuna_sextuple_1 = models.DateField(null=True, blank=True)
    fecha_vacuna_sextuple_2 = models.DateField(null=True, blank=True)
    fecha_vacuna_sextuple_3 = models.DateField(null=True, blank=True)
    fecha_vacuna_antirrabica = models.DateField(null=True, blank=True)

    def calcular_fechas_vacunacion(self):
        today = timezone.now().date()
        if self.especie.lower() == 'perro':
            if not self.fecha_vacuna_sextuple_1:
                self.fecha_vacuna_sextuple_1 = today + timezone.timedelta(days=60)  # 1 ½ - 2 meses
            if not self.fecha_vacuna_sextuple_2:
                self.fecha_vacuna_sextuple_2 = today + timezone.timedelta(days=90)  # 3 meses
            if not self.fecha_vacuna_sextuple_3:
                self.fecha_vacuna_sextuple_3 = today + timezone.timedelta(days=120)  # 4 meses
            if not self.fecha_vacuna_antirrabica:
                self.fecha_vacuna_antirrabica = today + timezone.timedelta(days=180)  # 6 meses
        elif self.especie.lower() == 'gato':
            if not self.fecha_vacuna_sextuple_1:
                self.fecha_vacuna_sextuple_1 = today + timezone.timedelta(days=60)  # 2 meses
            if not self.fecha_vacuna_sextuple_2:
                self.fecha_vacuna_sextuple_2 = today + timezone.timedelta(days=90)  # 3 meses
            if not self.fecha_vacuna_antirrabica:
                self.fecha_vacuna_antirrabica = today + timezone.timedelta(days=180)  # 6 meses
        self.save()

class Expediente(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='expedientes')
    archivo = models.FileField(upload_to='expedientes/')
    nombre_archivo = models.CharField(max_length=255)
    tipo_archivo = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50, null=True, blank=True) 
    fecha_subida = models.DateTimeField(auto_now_add=True)


class MedicoVeterinario(models.Model):
    nombre = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)
    correo = models.EmailField(max_length=255)
    telefono = models.CharField(max_length=20)
    password = models.CharField(max_length=255, default='default_password')


class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    medico = models.ForeignKey(MedicoVeterinario, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    duracion = models.DurationField() 
    motivo = models.TextField()
    confirmada = models.BooleanField(default=False)

# ADMIN
class Administrador(models.Model):
    correo = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Consulta(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    motivo = models.TextField()

    def __str__(self):
        return f"Consulta de {self.mascota.nombre} - {self.motivo[:20]}"

class Medicamento(models.Model):
    consulta = models.ForeignKey('Consulta', related_name='medicamentos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.dosis}"


class HorarioTrabajo(models.Model):
    medico = models.ForeignKey(MedicoVeterinario, on_delete=models.CASCADE)
    dia = models.CharField(max_length=10)  # Por ejemplo, "Lunes", "Martes", etc.
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()