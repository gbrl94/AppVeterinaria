# Generated by Django 5.0.3 on 2024-04-18 16:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_administrador_client_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('rut', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('especie', models.CharField(max_length=255)),
                ('raza', models.CharField(max_length=255)),
                ('sexo', models.CharField(max_length=10)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicoVeterinario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('especialidad', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='pet',
            name='dueno',
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('motivo', models.TextField()),
                ('confirmada', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cliente')),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.mascota')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.medicoveterinario')),
            ],
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Pet',
        ),
    ]
