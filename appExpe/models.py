from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.

class FormularioContacto(models.Model):

    nombre = models.CharField(max_length=40, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    disciplina = models.CharField(max_length=40, blank=False)
    mensaje = models.TextField(blank=False)

    def __str__(self):
        return self.nombre
    
class Artista(models.Model):

    nombre = models.CharField(null=True, max_length=40)
    disciplina = models.CharField(null=True, max_length=40)

    def __str__(self):
        return self.nombre
    
class Establecimiento(models.Model):

    nombre = models.CharField(null=True, max_length=40)
    direccion = models.CharField(null=True, max_length=60)

    def __str__(self):
        return self.nombre

class Evento(models.Model):

    nombre= models.CharField(max_length=40)
    artista= models.ForeignKey(Artista, on_delete=models.CASCADE, null=True, max_length=50)
    fecha = models.DateTimeField(null=True, blank=True)
    lugar = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, max_length=60, null=True)
    texto = models.TextField(max_length=5000, null=True)
    imagen = models.ImageField(upload_to='appExpe\static\images', blank = True)
    imagen2 = models.ImageField(upload_to='appExpe\static\images', blank=True)
    imagen3 = models.ImageField(upload_to='appExpe\static\images', blank=True)
    url = models.URLField(max_length=250, null=True)

    def __str__(self):
        return self.nombre
    def image_table(self):
        if self.image:
            return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
        else:
            return mark_safe('<p>Sem imagem</p>')



class Notas(models.Model):

    titulo = models.CharField(null=True, max_length=100)
    subtitulo = models.CharField(null=True, max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, null=True, max_length=50)
    fecha = models.DateTimeField(null=True)
    texto = models.TextField(max_length=5000, null=True)
    imagen = models.ImageField(upload_to='appExpe\static\images', blank=True)
    imagen2 = models.ImageField(upload_to='appExpe\static\images', blank=True)
    imagen3 = models.ImageField(upload_to='appExpe\static\images', blank=True)
    url = models.URLField(max_length=250,null=True)

    def __str__(self):
        return self.titulo
    def image_table(self):
        if self.image:
            return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
        else:
            return mark_safe('<p>Sem imagem</p>')   
    

class Usuario(models.Model):

    nombre = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
