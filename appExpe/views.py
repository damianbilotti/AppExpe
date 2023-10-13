from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import *
from django.http import HttpResponse, HttpRequest
from django.template import Template, Context
from datetime import datetime
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView 



# Create your views here.

def evento(req, nombre, fecha, lugar):

    evento = Evento(nombre=nombre, fecha=fecha, lugar=lugar)
    evento.save()

    return HttpResponse(f"""
<p>Evento: {evento.nombre} el día {evento.fecha} en {evento.lugar}- creado con exito! </p>
""")

# def creaNota (req):

 #   if req.method == 'POST':








###################################################################################################################################

def listaEventos (req):

    evento = Evento.objects.all()

    return render(req, "lista-eventos.html", {"lista_eventos": evento})

def musica (req):

    return render (req, "musica.html")

def teatro(req):

    return render (req, "teatro.html")

def danza(req):

    return render (req, "danza.html")

def inicio(req):

    return render (req, "inicio.html")

def literatura(req):

    return render (req, "literatura.html")

def contacto(req):

    if req.method == 'POST':

        formularioContacto = FormularioContacto(req.POST)

        if formularioContacto.is_valid():
            data = FormularioContacto
            data.nombre = formularioContacto.cleaned_data['nombre']
            data.email = formularioContacto.cleaned_data['email']
            data.disciplina = formularioContacto.cleaned_data['disciplina']
            data.mensaje = formularioContacto.cleaned_data['mensaje']
            data.save()

            return render (req, "inicio", {"mensaje": f"Su mensaje ha sido enviado con éxito, muchas gracias!"})
    
    formularioContacto = FormularioContacto
    return render(req, 'contacto.html')
    

def buscar(req: HttpRequest):
    if req.GET["busqueda"]:
        busqueda = req.GET["busqueda"]
        eventos = Evento.objects.filter(nombre__icontains=busqueda)
        return render (req, "resultadosBusqueda.html", {"eventos": eventos})
    else: 
        return render(req, 'inicio')


def login_request(req):
    if req.method == "POST":
        formulario = AuthenticationForm(req, data=req.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = data["username"]
            contraseña = data["password"]
            
            usuario = authenticate(username=usuario, password=contraseña)
            
            if usuario :
                login(req, usuario)
                return redirect( "inicio" )           
        else:
            return render(req, "inicio", {"mensaje": f"Datos incorrectos."})
    else:
        formulario = AuthenticationForm()
        return render(req, "login.html", {"formulario":formulario})
    
def registroUsuario(req):

    if req.method == "POST":

        formulario = RegistroUsuario (req.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data
            usuario = data["username"]
            formulario.save()
            return render (req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con éxito!"})
        
        return render (req, "inicio.html", {"mensaje": f"Formulario inválido, por favor, intente nuevamente"})
    
    else: 
        formulario = RegistroUsuario
        return render (req, "registroUsuario.html", {"formulario": formulario})
    
def editar_perfil(req):

    usuario = req.user
    if req.method == 'POST':

        miFormulario = EditarUsuario(req.POST, instance=req.user)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()

            return render(req, "inicio.html", {"mensaje": "Datos actualizados con éxito!"})
        else:
            return render(req, "editar-perfil.html", {"miFormulario": miFormulario})

    else:
        miFormulario = EditarUsuario(instance=usuario)
        return render(req, "editar-perfil.html", {"miFormulario": miFormulario})
        
























