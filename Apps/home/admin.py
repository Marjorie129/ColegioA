from django.contrib import admin
from .models import EstudiantePublicaciones,EstudianteAutorizaciones,Articulos,Publicaciones,Comentarios, Usuario

# Register your models here.

admin.site.register(EstudiantePublicaciones)
admin.site.register(EstudianteAutorizaciones)
admin.site.register(Articulos)
admin.site.register(Publicaciones)
admin.site.register(Comentarios)
admin.site.register(Usuario)