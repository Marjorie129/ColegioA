from socket import create_connection
from statistics import correlation
from django.db import models
#login
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

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

class ArticuloEstudiante(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    autoriza = models.ForeignKey(EstudianteAutorizaciones,on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s' % (self.titulo)

class Publicaciones(models.Model):
    articulo = models.ForeignKey(ArticuloEstudiante,on_delete=models.CASCADE)
    publica = models.ForeignKey(EstudiantePublicaciones,on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s' % (self.articulo,self.publica)

class ComentariosEstud(models.Model):
    articulo = models.ForeignKey(ArticuloEstudiante,on_delete=models.CASCADE)
    comentario = models.CharField(max_length=500)
    comenta = models.ForeignKey(EstudiantePublicaciones,on_delete=models.CASCADE) 
    creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s' % (self.articulo,self.comentario)

class Usuario(models.Model):
    perfil = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.perfil.username

@receiver(post_save, sender=User)
def crear_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(perfil=instance)

@receiver(post_save, sender=User)
def guardar_usuario(sender, instance, created, **kwargs):
    instance.usuario.save()
