from django.db import models

# Create your models here.

class FormularioContacto(models.Model):

    nombre = models.CharField(max_length=40, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    disciplina = models.CharField(max_length=40, blank=False)
    mensaje = models.TextField(blank=False)

    def __str__(self):
        return self.nombre

class Evento(models.Model):

    nombre= models.CharField(max_length=40)
    fecha = models.DateField()
    lugar = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

class Artista(models.Model):

    nombre = models.CharField(null=True, max_length=40)
    apellido = models.CharField(null=True, max_length=40)
    email = models.EmailField(null=True)
    disciplina = models.CharField(null=True, max_length=40)

    def __str__(self):
        return self.nombre

class Notas(models.Model):

    nombre = models.CharField(null=True, max_length=100)
    artista = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):

    nombre = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
