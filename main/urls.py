from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('interfaz/', views.interfaz, name='interfaz'),
    path('crear_usuario/', views.crear_usuario,name='crear_usuario'),
    path('login/', views.login ),
    path('comprobacion/', views.ingresar_usuario),
    path('eliminar/<id_m>/',views.eliminar),
    path('actualizar/<int:id_m>/', views.actualizar, name='actualizar'),
    path('guardar_mascota/', views.guardar_mascota, name='guardar_mascota'),
    path('guardar_cita/<int:cliente_id>/', views.guardar_cita, name='guardar_cita'),
    path('guardar_cita/', views.guardar_cita, name='guardar_cita'),
    path('ver_mascotas/', views.ver_mascotas, name='ver_mascotas'),
    path('cerrar_sesion/',views.logout),

    # Refactoring 1
    path('actualizar_cuenta/<int:cliente_id>/', views.actualizar_cuenta, name='actualizar_cuenta'),
    path('eliminar_cuenta/<int:cliente_id>/', views.eliminar_cuenta, name='eliminar_cuenta'),

    # Refactoring 2
    path('crear-mascota/', views.crear_mascota, name='crear_mascota'),
    path('solicitar-cita/', views.solicitar_cita, name='solicitar_cita'),
    path('proximas-citas/', views.proximas_citas, name='proximas_citas'),
    path('ver-mascotas/', views.ver_mascotas, name='ver_mascotas'),

    path('actualizar/<int:id_m>/', views.actualizar, name='actualizar'),
    path('eliminar/<int:id_m>/', views.eliminar, name='eliminar'),
    path('mascotas/', views.ver_mascotas, name='ver_mascotas'),
    path('recomendaciones-vacunacion/', views.recomendaciones_vacunacion, name='recomendaciones_vacunacion'),
    path('mascota/<int:mascota_id>/expedientes/', views.ver_expedientes, name='ver_expedientes'),
    path('veterinario/cuenta/', views.veterinario_cuenta, name='veterinario_cuenta'),

    #vista veterinario
    path('veterinario/', views.veterinario_interfaz, name='veterinario_interfaz'),
    path('veterinario/citas/', views.veterinario_citas, name='veterinario_citas'),
    path('veterinario-expediente/', views.subir_expediente, name='veterinario_expediente'),
    path('veterinario-expediente/', views.subir_expediente, name='subir_expediente'),


    #prueba correo notificacion


    #descarga expediente
   
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

