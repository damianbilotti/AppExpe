from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('agrega-evento/<nombre>/<fecha>/<lugar>/', evento),
    path('musica/', musica, name="musica"),
    path('teatro/', teatro, name="teatro"),
    path('danza/', danza, name="danza"),
    path('inicio/', inicio, name="inicio"),
    path('literatura/', literatura, name="literatura"),
    path('lista-eventos/', listaEventos),
    path('contacto/', contacto, name="contacto"),
    path('buscar/', buscar, name="buscar"),
    path('registro-usuario/', registroUsuario, name="registroUsuario"),
    path('login/', login_request, name="login"),
    path('resultadosBusqueda/', buscar, name="resultadosBusqueda"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="logout"),


]