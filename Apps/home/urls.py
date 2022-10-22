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
from .views import HomeView, ListadoView, AdministradoresView, CrearEstudianteAView, CrearEstudiantePView, CrearArticuloView, CrearPublicacionView, CrearComentarioView, PublicacionesView,  ArticulosView, RegistroView, ComentariosView, Login, EditarEstudianteAView, EditarEstudiantePView, EditArticuloView, EditarComentarioView, EditarPublicacionView, detallesEP, detallesEA, detallesArt, detallesComent, detallesPub

app_name = 'home'

urlpatterns = [
    path('home/', HomeView.as_view(), name='homeapp'),
    path('listado/', ListadoView.as_view(), name='listadoapp'),
    path('editarEP/<int:pk>', EditarEstudiantePView.as_view(), name='editarEPapp'),
    path('administradores/', AdministradoresView.as_view(), name='adminapp'),
    path('editarEA/<int:pk>', EditarEstudianteAView.as_view(), name='editarEAapp'),
    path('crearEstA/', CrearEstudianteAView.as_view(), name='crearEstAapp'),
    path('crearEstP/', CrearEstudiantePView.as_view(), name='crearEstPapp'),
    path('Art/', ArticulosView.as_view(), name='acercaDeapp'),
    path('editArt/<int:pk>', EditArticuloView.as_view(), name='editarArtapp'),
    path('crearArt/', CrearArticuloView.as_view(), name='crearArtapp'),
    path('crearPub/', CrearPublicacionView.as_view(), name='crearPubapp'),
    path('editPub/<int:pk>', EditarPublicacionView.as_view(), name='editarPubapp'),
    path('crearCome/', CrearComentarioView.as_view(), name='crearComeapp'),
    path('verPub/', PublicacionesView.as_view(), name='Pubapp'),
    path('registro/', RegistroView.as_view(), name='RegistroApp'),
    path('comentarios/', ComentariosView.as_view(), name='verComentapp'),
    path('editComent/<int:pk>', EditarComentarioView.as_view(), name='editarComentapp'),
    path('detallesEP/<int:pk>', detallesEP.as_view(), name='detallesEPapp'),
    path('detallesEA/<int:pk>', detallesEA.as_view(), name='detallesEAapp'),
    path('detallesArt/<int:pk>', detallesArt.as_view(), name='detallesArtapp'),
    path('detallesComent/<int:pk>', detallesComent.as_view(), name='detallesComentapp'),
    path('detallesPub/<int:pk>', detallesPub.as_view(), name='detallesPubapp'),
    path('', Login, name='login'),
]
