from socket import create_connection
from statistics import correlation
from django.db import models

# Create your models here.

class EstudiantePublicaciones(models.Model):
    carnet = models.CharField(max_length=5)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombre,self.apellido)

class EstudianteAutorizaciones(models.Model):
    carnet = models.CharField(max_length=5)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombre,self.apellido)

class Articulos(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    autoriza = models.ForeignKey(EstudianteAutorizaciones,on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s' % (self.titulo)

class Publicaciones(models.Model):
    articulo = models.ForeignKey(Articulos,on_delete=models.CASCADE)
    publica = models.ForeignKey(EstudiantePublicaciones,on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s' % (self.articulo,self.publica)

class Comentarios(models.Model):
    articulo = models.ManyToManyField(Articulos)
    comentario = models.CharField(max_length=500)
    comenta = models.ForeignKey(EstudiantePublicaciones,on_delete=models.CASCADE) 
    creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s' % (self.comenta,self.comentario)