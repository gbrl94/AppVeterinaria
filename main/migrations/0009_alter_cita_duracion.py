# Generated by Django 5.0.3 on 2024-09-08 21:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_medico_cita_medico_veterinario_cita_duracion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='duracion',
            field=models.DurationField(default=datetime.timedelta(seconds=1800)),
        ),
    ]
