from typing import Any
from django.db import models

# Create your models here.

class Medico(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=50)
    estatura = models.FloatField()
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=400)
    ubicacion = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Ambulancia(models.Model):
    numeroSerie = models.IntegerField()
    marca = models.CharField(max_length=50)
    modelo = models.IntegerField()
    capacidadPasajeros = models.IntegerField()
    ultimaFechaMantenimiento = models.DateField()

    def __str__(self):
        return str(self.numeroSerie)