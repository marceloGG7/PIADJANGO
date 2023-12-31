# Generated by Django 4.2.7 on 2023-11-17 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroSerie', models.IntegerField()),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.IntegerField()),
                ('capacidadPasajeros', models.IntegerField()),
                ('ultimaFechaMantenimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=50)),
                ('capacidad', models.IntegerField()),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=50)),
                ('estatura', models.FloatField()),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50)),
                ('calle', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
    ]
