# Generated by Django 5.0.3 on 2024-08-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_medicoveterinario_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='fecha_vacuna_antirrabica',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='fecha_vacuna_sextuple_1',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='fecha_vacuna_sextuple_2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mascota',
            name='fecha_vacuna_sextuple_3',
            field=models.DateField(blank=True, null=True),
        ),
    ]
