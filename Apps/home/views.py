from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class ListadoView(TemplateView):
    template_name = 'listado.html'

class AdministradoresView(TemplateView):
    template_name = 'administradores.html'

class AcercaDeView(TemplateView):
    template_name = 'acercaDe.html'
