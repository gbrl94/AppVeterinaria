# Generated by Django 5.0.3 on 2024-09-08 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_cita_duracion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cita',
            old_name='medico_veterinario',
            new_name='medico',
        ),
        migrations.AlterField(
            model_name='cita',
            name='duracion',
            field=models.DurationField(),
        ),
    ]
