"""ColegioA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from.views import HomeView, ListadoView, AdministradoresView, CrearEstudianteAView, CrearEstudiantePView, CrearArticuloView, CrearPublicacionView, CrearComentarioView, PublicacionesView,  ArticulosView, RegistroView, ComentariosView,Login

app_name='home'

urlpatterns = [
    path('home/', HomeView.as_view(), name='homeapp'),
    path('listado/', ListadoView.as_view(), name='listadoapp'),
    path('administradores/', AdministradoresView.as_view(), name='adminapp'),    
    path('crearEstA/', CrearEstudianteAView.as_view(), name='crearEstAapp'),
    path('crearEstP/', CrearEstudiantePView.as_view(), name='crearEstPapp'),
    path('Art/', ArticulosView.as_view(), name='acercaDeapp'),
    path('crearArt/', CrearArticuloView.as_view(), name='crearArtapp'),
    path('crearPub/', CrearPublicacionView.as_view(), name='crearPubapp'),
    path('crearCome/', CrearComentarioView.as_view(), name='crearComeapp'),
    path('verPub/', PublicacionesView.as_view(), name='Pubapp'),
    path('registro/', RegistroView.as_view(), name='RegistroApp'),
    path('comentarios/', ComentariosView.as_view(), name='verComentapp'),
    path('', Login, name='login'),
]
