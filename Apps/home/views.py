from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import ArticuloForm, ComentarioForm, EstudiantePForm, EstudianteAForm, PublicacionForm, ComentarioForm
from django.urls import reverse_lazy
from .models import EstudianteAutorizaciones, EstudiantePublicaciones, Publicaciones
from django.views import generic
from django.http import HttpRequest

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class ListadoView(generic.ListView):
    template_name = 'listado.html'
    model = EstudiantePublicaciones
    def get_queryset(self):
     return EstudiantePublicaciones.objects.all()

def CrearPublicacion (request):
    assert isinstance(request, HttpRequest)
    if request.method =='POST':
        Publicar = ListadoView()
        Publicar.carnet = request.POST ['carnet']
        Publicar.nombre = request.POST['nombre']
        Publicar.apellido = request.POST['apellido']
        Publicar.save()
    return render(request, "listado.html")

class AdministradoresView(generic.ListView):
    template_name = 'administradores.html'
    model = EstudianteAutorizaciones
    def get_queryset(self):
     return EstudianteAutorizaciones.objects.all()

def RealizarAutorizacion (request):
    assert isinstance(request, HttpRequest)
    if request.method =='POST':
        Autorizar = ListadoView()
        Autorizar.carnet = request.POST ['carnet']
        Autorizar.nombre = request.POST['nombre']
        Autorizar.apellido = request.POST['apellido']
        Autorizar.save()
    return render(request, "administradores.html")

class PublicacionesView(generic.ListView):
    template_name = 'Publicaciones.html'
    model = Publicaciones
    def get_queryset(self):
     return Publicaciones.objects.all()

def RealizarPublicacion (request):
    assert isinstance(request, HttpRequest)
    if request.method =='POST':
        Publicacion = ListadoView()
        Publicacion.articulo = request.POST ['articulo']
        Publicacion.publica = request.POST['publica']
        Publicacion.save()
    return render(request, "Publicaciones.html")

def RealizarAutorizacion (request):
    assert isinstance(request, HttpRequest)
    if request.method =='POST':
        Autorizar = ListadoView()
        Autorizar.carnet = request.POST ['carnet']
        Autorizar.nombre = request.POST['nombre']
        Autorizar.apellido = request.POST['apellido']
        Autorizar.save()
    return render(request, "administradores.html")

class AcercaDeView(TemplateView):
    template_name = 'acercaDe.html'

class CrearEstudianteAView(CreateView):
    template_name = 'crearEstudianteA.html'
    form_class = EstudianteAForm
    success_url = reverse_lazy('home:homeapp')

class CrearEstudiantePView(CreateView):
    template_name = 'crearEstudianteP.html'
    form_class = EstudiantePForm
    success_url = reverse_lazy('home:homeapp')

class CrearArticuloView(CreateView):
    template_name = 'CrearArticulo.html'
    form_class = ArticuloForm
    success_url = reverse_lazy('home:homeapp')

class CrearPublicacionView(CreateView):
    template_name = 'crearPublicacion.html'
    form_class = PublicacionForm
    success_url = reverse_lazy('home:homeapp')

class CrearComentarioView(CreateView):
    template_name = 'crearComentario.html'
    form_class = ComentarioForm
    success_url = reverse_lazy('home:homeapp')

