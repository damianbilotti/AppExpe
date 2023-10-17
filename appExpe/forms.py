from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *



class FormularioContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'mensaje']

class FormularioBusqueda(forms.Form):

    busqueda = forms.CharField(max_length=50)


class RegistroUsuario(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]

    def __init__(self, *args, **kwargs):
        super(RegistroUsuario, self).__init__(*args, **kwargs)
        self.fields['username'].error_messages['unique'] = 'El nombre de usuario ya está en uso. Por favor, elige otro.'
    
    


class EditarUsuario(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ("email", "first_name", "last_name", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegistroUsuario, self).__init__(*args, **kwargs)
        self.fields['username'].error_messages['unique'] = 'El nombre de usuario ya está en uso. Por favor, elige otro.'

    def clean_password2(self):

        print(self.cleaned_data)

        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden!!!!")
        return password2


class ArtistaFormulario(forms.ModelForm):

    class Meta:
        model= Artista
        fields= ("nombre", "categoria", "disciplina", "descripcion", "link", "imagen")


class EventoFormulario(forms.ModelForm):
        fecha = forms.DateField(
        widget= forms.TextInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'])
    
        class Meta: 
            model= Evento
            fields= ("nombre", "categoria", "artista", "fecha", "lugar", "texto", "imagen", "imagen2", "imagen3", "url")

class EstablecimientoFormulario(forms.ModelForm):

    class Meta:
        model= Establecimiento
        fields= ("nombre", "direccion")
         