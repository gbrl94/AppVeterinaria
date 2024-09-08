import pytest
from main.models import Cliente, Mascota, MedicoVeterinario, Cita

@pytest.fixture
def setup_data():
    cliente = Cliente.objects.create(
        nombre='Juan', apellido='Pérez', rut='12345678-9', telefono='123456789',
        correo='juan.perez@example.com', direccion='Calle Falsa 123', password='password'
    )
    medico = MedicoVeterinario.objects.create(
        nombre='Dr. Smith', especialidad='Cirugía', correo='dr.smith@example.com', telefono='987654321'
    )
    mascota = Mascota.objects.create(
        nombre='Fido', especie='Perro', raza='Labrador', sexo='M', peso=30.00, edad=5,
        cliente=cliente
    )
    return cliente, medico, mascota

def test_create_cita(setup_data):
    cliente, medico, mascota = setup_data
    cita = Cita.objects.create(
        cliente=cliente, mascota=mascota, medico=medico,
        fecha='2024-09-01', hora='10:00:00', duracion='01:00:00', motivo='Chequeo general'
    )
    assert cita.cliente == cliente
    assert cita.mascota == mascota
    assert cita.medico == medico
    assert cita.motivo == 'Chequeo general'
