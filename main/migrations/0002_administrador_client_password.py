# Generated by Django 5.0.3 on 2024-04-17 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='password',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
