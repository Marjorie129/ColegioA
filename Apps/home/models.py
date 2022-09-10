from socket import create_connection
from statistics import correlation
from django.db import models

# Create your models here.


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.correo)

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    seccion = models.CharField(max_length=200)
    creacion = models.DateTimeField(auto_now_add=True)
    Estudiante = models.ManyToManyField(Estudiante)

    def __str__(self):
        return '%s %s' % (self.nombre, self.seccion)

class Telefono(models.Model):
    tipo_telefono=(
        ('C', 'Casa'),
        ('M', 'Celular'),
        ('T', 'Trabajo'),
    )
    telefono = models.CharField(max_length=100)
    Estudiante=models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    tipo = models.CharField(
        max_length=1,
        choices=tipo_telefono,
        default='C',
    )
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.telefono, self.tipo)
