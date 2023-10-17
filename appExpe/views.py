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
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User



# Create your views here.
###################################################################################################################################


def musica (req):

    eventos_musica = Evento.objects.filter(categoria__nombre="Musica")
    
    return render (req, "musica.html", {"eventos_musica": eventos_musica})


def teatro(req):

    eventos_teatro = Evento.objects.filter(categoria__nombre="Teatro")
    
    return render (req, "teatro.html", {"eventos_teatro": eventos_teatro})


def danza(req):

    eventos_danza = Evento.objects.filter(categoria__nombre="Danza")
    
    return render (req, "danza.html", {"eventos_danza": eventos_danza})

def inicio(req):

    return render (req, "inicio.html")

def literatura(req):

    eventos_literatura = Evento.objects.filter(categoria__nombre="Literatura")
    
    return render (req, "literatura.html", {"eventos_literatura": eventos_literatura})

def cine(req):

    eventos_cine = Evento.objects.filter(categoria__nombre="Cine")
    
    return render (req, "cine.html", {"eventos_cine": eventos_cine})

def visuales(req):

    eventos_visuales = Evento.objects.filter(categoria__nombre="Visuales")
    
    return render (req, "visuales.html", {"eventos_visuales": eventos_visuales})

def contacto(req):

    if req.method == 'POST':
        formulario = FormularioContacto(req.POST)

        if formulario.is_valid():
            data = Contacto()
            data.nombre = formulario.cleaned_data['nombre']
            data.email = formulario.cleaned_data['email']
            data.mensaje = formulario.cleaned_data['mensaje']
            formulario.save()
            return render(req, "inicio.html", {"mensaje": "Gracias por comunicarse con nosotros, le responderemos a la brevedad."})
    else:
        formulario = FormularioContacto
        return render (req, "contacto.html", {"formulario": formulario })
    

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
                return render(req, "inicio.html", {"mensaje": f"Bienvenido {usuario} !"})           
        else:
            return render(req, "inicio.html", {"mensaje": f"Datos incorrectos."})
    else:
        formulario = AuthenticationForm()
        return render(req, "login.html", {"formulario":formulario})
    

    

def registroUsuario(req):

    if req.method == "POST":

        formulario = RegistroUsuario(req.POST)

        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            if User.objects.filter(username=usuario).exists():
                return render(req, "inicio.html")
            else:
                password1 = formulario.cleaned_data['password1']
                usuario = User.objects.create_user(username=usuario, password=password1)
                return render(req,"inicio.html", {"mensaje": f"Usuario creado con éxito!"})
        else:
            # Devuelve una respuesta en caso de formulario inválido 
            return render(req, "registroUsuario.html", {"formulario": formulario})
    else:
        formulario = RegistroUsuario()
        return render(req, "registroUsuario.html", {"formulario": formulario})

def inicio(req):
    return render (req, "inicio.html")
    
def editarPerfil(req):

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
            return render(req, "perfil.html", {"miFormulario": miFormulario})

    else:
        miFormulario = EditarUsuario(instance=usuario)
        return render(req, "perfil.html", {"miFormulario": miFormulario})
    

@login_required(login_url='login')   
def creaArtista(req): 

    if req.method == 'POST':

        formulario = ArtistaFormulario(req.POST, req.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            artista = Artista(nombre=data["nombre"], categoria=data["categoria"], disciplina=data["disciplina"], descripcion=data["descripcion"], link=data["link"], imagen=data["imagen"])
            artista.save()

            return render(req, "inicio.html", {"mensaje": "Artista creado con éxito!"})
        else: 
            return render(req, "inicio.html", {"mensaje": "Formulario inválido, por favor, volvé a intentarlo."})
    
    else:
        formulario = ArtistaFormulario
        return render (req, "creaArtista.html", {"formulario": formulario})
    

def listaArtistas(req):

    artistas = Artista.objects.all()

    return render(req, "listaArtistas.html", {"artistas": artistas})

def listaEventos(req):

    eventos = Evento.objects.all()

    return render(req, "listaEventos.html", {"eventos": eventos}) 

@staff_member_required(login_url='login')
def eliminaArtista(req, id):

    if req.method == 'POST':

        artista = Artista.objects.get(id=id)
        artista.delete()

        artistas = Artista.objects.all()

        return render(req, "listaArtistas.html", {"artistas": artistas})
    
@staff_member_required(login_url='login')
def editarArtista(req, id):

    artista = Artista.objects.get(id=id)

    if req.method == 'POST':

        formulario = ArtistaFormulario(req.POST, req.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            artista.nombre = data["nombre"]
            artista.categoria = data["categoria"]
            artista.disciplina = data["disciplina"]
            artista.descripcion = data["descripcion"]
            artista.link = data["link"]
            artista.imagen = data["imagen"]
            artista.save()

            return render(req, "inicio.html")
    else:

        formulario = ArtistaFormulario(initial={
            "nombre": artista.nombre,
            "categoria": artista.categoria,
            "disciplina": artista.disciplina,
            "descripcion": artista.descripcion,
            "link": artista.link, 
            "imagen": artista.imagen,

        })
        return render(req, "editarArtista.html", {"formulario": formulario, "id": artista.id})
    

@login_required(login_url='login')   
def creaEvento(req): 

    if req.method == 'POST':

        formulario = EventoFormulario(req.POST, req.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            evento = Evento(nombre=data["nombre"], 
            categoria=data["categoria"],
            artista=data["artista"], 
            fecha=data["fecha"], 
            lugar=data["lugar"], 
            texto=data["texto"], 
            imagen=data["imagen"], 
            imagen2=data["imagen2"], 
            imagen3=data["imagen3"], 
            url=data["url"])
            evento.save()

            return render(req, "inicio.html", {"mensaje": "Evento creado con éxito!"})
        else: 
            return render(req, "inicio.html", {"mensaje": "Formulario inválido, por favor, volvé a intentarlo."})
    
    else:
        formulario = EventoFormulario
        return render (req, "creaEvento.html", {"formulario": formulario})
    

@staff_member_required(login_url='login')
def eliminaEvento(req, id):

    if req.method == 'POST':

        evento = Evento.objects.get(id=id)
        evento.delete()

        eventos = Evento.objects.all()

        return render(req, "listaEventos.html", {"eventos": eventos})
    
@staff_member_required(login_url='login')
def editarEvento(req, id):

    evento = Evento.objects.get(id=id)

    if req.method == 'POST':

        formulario = EventoFormulario(req.POST, req.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            evento.nombre = data["nombre"]
            evento.artista = data["artista"]
            evento.fecha = data["fecha"]
            evento.lugar = data["lugar"]
            evento.texto = data["texto"]
            evento.imagen = data["imagen"]
            evento.imagen2 = data["imagen2"]
            evento.imagen3 = data["imagen3"]
            evento.url = data["url"]
            evento.save()

            return render(req, "inicio.html")
    else:

        formulario = EventoFormulario(initial={
            "nombre": evento.nombre,
            "artista": evento.artista,
            "fecha": evento.fecha,
            "lugar": evento.lugar, 
            "texto": evento.texto,
            "imagen": evento.imagen,
            "imagen2": evento.imagen2,
            "imagen3": evento.imagen3,
            "url": evento.url,

        })
        return render(req, "editarEvento.html", {"formulario": formulario, "id": evento.id})
    

@login_required(login_url='login')   
def creaEstablecimiento(req): 

    if req.method == 'POST':

        formulario = EstablecimientoFormulario(req.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data
            establecimiento = Establecimiento(nombre=data["nombre"], 
            direccion=data["direccion"])

            establecimiento.save()

            return render(req, "inicio.html", {"mensaje": "Establecimiento cargado con éxito!"})
        else: 
            return render(req, "inicio.html", {"mensaje": "Formulario inválido, por favor, volvé a intentarlo."})
    
    else:
        formulario = EstablecimientoFormulario
        return render (req, "creaEstablecimiento.html", {"formulario": formulario})
        
























