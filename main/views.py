from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota, Cita, Cliente, MedicoVeterinario, Expediente
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib import messages
from .forms import ExpedienteForm

# Importar la función para enviar correos
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def crear_usuario(request):
    return render(request, 'crear_usuario.html')

def ingresar_usuario(request):
    cliente = Cliente(
        nombre=request.POST['nombre'],
        apellido=request.POST['apellido'],
        rut=request.POST['rut'],
        telefono=request.POST['telefono'],
        correo=request.POST['correo'],
        direccion=request.POST['direccion'],
        password=request.POST['password']
    )
    cliente.save()
    return render(request, 'index.html')

def interfaz(request):
    if 'cliente' not in request.session:
        return redirect('login')  # Redirige al login si no hay cliente en la sesión
    
    cliente_id = request.session['cliente'].get('id')
    cliente = get_object_or_404(Cliente, id=cliente_id)
    citas = Cita.objects.all()
    mascotas = Mascota.objects.filter(cliente=cliente)  # Filtrar mascotas por cliente
    veterinarios = MedicoVeterinario.objects.all()
    
    return render(request, 'interfaz.html', {
        'mascotas': mascotas,
        'veterinarios': veterinarios,
        'citas': citas,
        'cliente': cliente
    })

# Login 
def login(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        
        # Verificar si es un cliente
        try:
            cliente = Cliente.objects.get(correo=correo, password=password)
            if cliente.password != password:
                return render(request, 'index.html', {'error': 'La contraseña es incorrecta'})
            
            # Guardar información del cliente en la sesión
            request.session['cliente'] = {
                'id': cliente.id,
                'nombre': cliente.nombre,
                'correo': cliente.correo,
            }
            
            return redirect('interfaz')  # Redirige a la vista principal para clientes

        except Cliente.DoesNotExist:
            pass  # Si no es un cliente, sigue verificando si es un veterinario

        # Verificar si es un veterinario
        try:
            veterinario = MedicoVeterinario.objects.get(correo=correo, password=password)
            if veterinario.password != password:
                return render(request, 'index.html', {'error': 'La contraseña es incorrecta'})

            # Guardar información del veterinario en la sesión
            request.session['veterinario'] = {
                'id': veterinario.id,
                'nombre': veterinario.nombre,
                'correo': veterinario.correo,
            }

            return redirect('veterinario_interfaz')  # Redirige a la vista principal para veterinarios

        except MedicoVeterinario.DoesNotExist:
            # Si no es un veterinario, devolver un error genérico
            return render(request, 'index.html', {'error': 'Este usuario no existe'})
    
    return render(request, 'index.html')


# Crear Mascota
def crear_mascota(request):
    cliente_id = request.session.get('cliente', {}).get('id')
    return render(request, 'crear_mascota.html', {'cliente_id': cliente_id})

def eliminar(request, id_m):
    mascota = get_object_or_404(Mascota, id=id_m)
    mascota.delete()
    return redirect('interfaz')

 # Agregar un mensaje de éxito
    messages.success(request, 'La mascota se ha eliminado con éxito.')
    
    return redirect('ver_mascotas')

def guardar_mascota(request):
    if request.method == 'POST':
        cliente_id = request.session.get('cliente', {}).get('id')
        nombre = request.POST.get('nombre_mascota')
        especie = request.POST.get('especie_mascota')
        raza = request.POST.get('raza_mascota')
        sexo = request.POST.get('sexo_mascota')
        edad = request.POST.get('edad_mascota')
        peso = request.POST.get('peso_mascota')

        try:
            cliente = Cliente.objects.get(id=cliente_id)
            
            # Verificar si la mascota ya existe
            if not Mascota.objects.filter(nombre=nombre, especie=especie, raza=raza, sexo=sexo, edad=edad, peso=peso, cliente=cliente).exists():
                nueva_mascota = Mascota(
                    nombre=nombre,
                    especie=especie,
                    raza=raza,
                    sexo=sexo,
                    edad=edad,
                    peso=peso,
                    cliente=cliente
                )
                nueva_mascota.save()
            else:
                return render(request, 'crear_mascota.html', {'error': 'La mascota ya existe.'})

            return redirect('interfaz')  # Redirige a la página principal después de guardar
        except Cliente.DoesNotExist:
            return render(request, 'crear_mascota.html', {'error': 'No se encontró el cliente asociado.'})

    return render(request, 'crear_mascota.html')


def solicitar_cita(request):
    cliente_id = request.session.get('cliente', {}).get('id')
    
    if not cliente_id:
        return redirect('login')  # Redirige a la página de login si no hay cliente en la sesión
    
    cliente = get_object_or_404(Cliente, id=cliente_id)
    mascotas = Mascota.objects.filter(cliente=cliente)
    veterinarios = MedicoVeterinario.objects.all()

    return render(request, 'solicitar_cita.html', {
        'cliente': cliente,
        'mascotas': mascotas,
        'veterinarios': veterinarios,
    })

def guardar_cita(request):
    if request.method == 'POST':
        try:
            cliente_id = request.POST.get('cliente_id')
            mascota_id = request.POST.get('mascota')
            medico_id = request.POST.get('medico')
            fecha_formulario = request.POST.get('fecha')
            hora = request.POST.get('hora')
            motivo = request.POST.get('motivo')

            print(f'cliente_id: {cliente_id}, mascota_id: {mascota_id}, medico_id: {medico_id}, fecha: {fecha_formulario}, hora: {hora}, motivo: {motivo}')

            if fecha_formulario:
                fecha_entrada = datetime.strptime(fecha_formulario, '%d/%m/%Y').strftime('%Y-%m-%d')
            else:
                return render(request, 'solicitar_cita.html', {'error': 'La fecha es obligatoria.'})

            nueva_cita = Cita(
                cliente_id=cliente_id,
                mascota_id=mascota_id,
                medico_id=medico_id,
                fecha=fecha_entrada,
                hora=hora,
                motivo=motivo
            )
            nueva_cita.save()

            return redirect('proximas_citas')  # Redirecciona a la página principal después de guardar
        except Exception as e:
            return render(request, 'solicitar_cita.html', {'error': f'Ocurrió un error al guardar la cita: {str(e)}'})

    return redirect('solicitar_cita')


def ver_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'ver_mascotas.html', {'mascotas': mascotas})

def actualizar(request, id_m):
    try:
        editar_mascota = Mascota.objects.get(id=id_m)
    except Mascota.DoesNotExist:
        return render(request, 'error.html', {'mensaje': 'La mascota no existe.'})
    
    if request.method == 'GET':
        return render(request, 'editar_mascota.html', {'mascota': editar_mascota})
    if request.method == 'POST':
        editar_mascota.nombre = request.POST.get('nombre', editar_mascota.nombre)
        editar_mascota.especie = request.POST.get('especie', editar_mascota.especie)
        editar_mascota.raza = request.POST.get('raza', editar_mascota.raza)
        editar_mascota.sexo = request.POST.get('sexo', editar_mascota.sexo)
        editar_mascota.peso = request.POST.get('peso', editar_mascota.peso)
        editar_mascota.edad = request.POST.get('edad', editar_mascota.edad)
        editar_mascota.save()
        return redirect('interfaz')

def logout(request):
    request.session.flush()  # Limpiar toda la sesión
    return redirect('index')

def actualizar_cuenta(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.rut = request.POST['rut']
        cliente.telefono = request.POST['telefono']
        cliente.correo = request.POST['correo']
        cliente.direccion = request.POST['direccion']
        cliente.fecha_actualizacion = datetime.now()
        cliente.save()

        mensaje = "Los datos del cliente se han actualizado correctamente."
        return render(request, 'mi_cuenta.html', {'cliente': cliente, 'mensaje': mensaje})

    return render(request, 'mi_cuenta.html', {'cliente': cliente})

def eliminar_cuenta(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    cliente.delete()  # Borrar el cliente en lugar de solo actualizar la fecha de eliminación
    request.session.flush()  # Limpiar la sesión del cliente
    return redirect('index')  # Redirigir al inicio de sesión

def proximas_citas(request):
    cliente = get_object_or_404(Cliente, id=request.session['cliente']['id'])
    citas = Cita.objects.filter(cliente=cliente, fecha__gte=datetime.today().date()).order_by('fecha', 'hora')
    return render(request, 'proximas_citas.html', {'citas': citas})


# Expedientes
def ver_expedientes(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    expedientes = mascota.expedientes.all()

    if request.method == 'POST':
        form = ExpedienteForm(request.POST, request.FILES)
        if form.is_valid():
            expediente = form.save(commit=False)
            expediente.mascota = mascota
            expediente.save()
            return redirect('ver_expedientes', mascota_id=mascota_id)
    else:
        form = ExpedienteForm()

    return render(request, 'ver_expedientes.html', {'mascota': mascota, 'expedientes': expedientes, 'form': form})

def subir_expediente(request):
    if request.method == 'POST':
        mascota_id = request.POST.get('mascota')
        documento = request.FILES.get('documento')

        if mascota_id and documento:
            mascota = Mascota.objects.get(id=mascota_id)
            expediente = Expediente(
                mascota=mascota,
                archivo=documento,
                nombre_archivo=documento.name,
                tipo_archivo=documento.content_type
            )
            expediente.save()
            return redirect('veterinario_expediente')  # Redirige a la vista donde se muestran los expedientes

    mascotas = Mascota.objects.select_related('cliente').all()
    return render(request, 'subir_expediente.html', {'mascotas': mascotas})

#Interfaz veterinario
def veterinario_interfaz(request):
    veterinario_id = request.session.get('veterinario', {}).get('id')
    if not veterinario_id:
        return redirect('login')  
    return render(request, 'veterinario_interfaz.html')

# Citas del veterinario
def veterinario_citas(request):
    veterinario_id = request.session.get('veterinario', {}).get('id')
    
    if not veterinario_id:
        return redirect('login') 

    citas = Cita.objects.filter(medico_id=veterinario_id)

    return render(request, 'veterinario_citas.html', {
        'citas': citas,
    })

#modificar cuenta veterinario
def veterinario_cuenta(request):
    # Tu lógica aquí
    return render(request, 'veterinario_cuenta.html')


#vacunacion
def recomendaciones_vacunacion(request):
    mascotas = Mascota.objects.all()
    for mascota in mascotas:
        mascota.calcular_fechas_vacunacion()
    return render(request, 'recomendaciones_vacunacion.html', {'mascotas': mascotas})