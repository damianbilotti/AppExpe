from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class ContactForm(ModelForm):
    class Meta:
        model = FormularioContacto
        fields = ['nombre', 'email', 'disciplina', 'mensaje']



class FormularioBusqueda(forms.Form):

    busqueda = forms.CharField(max_length=50)

class RegistroUsuario(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]

class EditarUsuario(UserCreationForm):
    nombreUsuario = forms.CharField(label="Nombre de Usuario")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
    nombre = forms.CharField(label="Nombre")
    apellido = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ["nombreUsuario","nombre", "apellido", "email", "password1", "password2"]
         