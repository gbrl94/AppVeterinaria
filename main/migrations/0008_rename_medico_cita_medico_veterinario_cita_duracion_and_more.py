# Generated by Django 5.0.3 on 2024-09-08 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_mascota_fecha_vacuna_antirrabica_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cita',
            old_name='medico',
            new_name='medico_veterinario',
        ),
        migrations.AddField(
            model_name='cita',
            name='duracion',
            field=models.DurationField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expediente',
            name='categoria',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('motivo', models.TextField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cliente')),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.mascota')),
            ],
        ),
        migrations.CreateModel(
            name='HorarioTrabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=10)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.medicoveterinario')),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('dosis', models.CharField(max_length=100)),
                ('frecuencia', models.CharField(max_length=100)),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicamentos', to='main.consulta')),
            ],
        ),
    ]
