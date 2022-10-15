from django.contrib import admin
from .models import EstudiantePublicaciones,EstudianteAutorizaciones,ArticuloEstudiante,Publicaciones,ComentariosEstud, Usuario

# Register your models here.

admin.site.register(EstudiantePublicaciones)
admin.site.register(EstudianteAutorizaciones)
admin.site.register(ArticuloEstudiante)
admin.site.register(Publicaciones)
admin.site.register(ComentariosEstud)
admin.site.register(Usuario)