from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView


urlpatterns = [
    path('musica/', musica, name="musica"),
    path('teatro/', teatro, name="teatro"),
    path('danza/', danza, name="danza"),
    path('inicio/', inicio, name="inicio"),
    path('literatura/', literatura, name="literatura"),
    path('contacto/', contacto, name="contacto"),
    path('buscar/', buscar, name="buscar"),
    path('registro-usuario/', registroUsuario, name="registroUsuario"),
    path('login/', login_request, name="login"),
    path('resultadosBusqueda/', buscar, name="resultadosBusqueda"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('perfil', editarPerfil, name="Perfil"),
    path('wonderfullfarfalla', TemplateView.as_view(template_name="wonderfullfarfalla.html"), name="wonderfullfarfalla"),
    path('seacaboelmisterio', TemplateView.as_view(template_name="seacaboelmisterio.html"), name="seacaboelmisterio"),
    path('soulmates', TemplateView.as_view(template_name="soulmates.html"), name="soulmates"),
    path('suavecita', TemplateView.as_view(template_name="suavecita.html"), name="suavecita"),
    path('djfica', TemplateView.as_view(template_name="djfica.html"), name="djfica"),
    path('creaArtista', creaArtista, name="creaArtista"),
    path('eliminaArtista/<int:id>', eliminaArtista, name="eliminaArtista"),
    path('listaArtistas/', listaArtistas, name="listaArtistas"),
    path('editarArtista/<int:id>', editarArtista, name="editarArtista"),
    path('creaEvento', creaEvento, name="creaEvento"),
    path('eliminaEvento/<int:id>', eliminaEvento, name="eliminaEvento"),
    path('editarEvento/<int:id>', editarEvento, name="editarEvento"),
    path('listaEventos/', listaEventos, name="listaEventos"),

]