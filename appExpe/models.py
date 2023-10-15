from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User



# Create your models here.

class Categoria(models.Model):

    nombre = models.CharField(null=False, max_length=30)

    def __str__(self):
        return self.nombre


class Contacto(models.Model):

    nombre = models.CharField(null=True, max_length=20)
    email = models.EmailField(null=True, max_length=50)
    mensaje = models.TextField(null=True, max_length=300)

    def __str__(self):
        return self.nombre

class Artista(models.Model):

    nombre = models.CharField(null=True, max_length=40)
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.CASCADE)
    disciplina = models.CharField(null=True, max_length=40)
    descripcion = models.CharField(null=True, max_length=500)
    link = models.URLField(null=True, max_length=250, blank=True)
    imagen = models.ImageField(upload_to='fotos', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre
    
class Establecimiento(models.Model):

    nombre = models.CharField(null=True, max_length=40)
    direccion = models.CharField(null=True, max_length=60)

    def __str__(self):
        return self.nombre

class Evento(models.Model):

    nombre= models.CharField(max_length=40)
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.CASCADE)
    artista= models.ForeignKey(Artista, on_delete=models.CASCADE, null=True, max_length=50)
    fecha = models.DateTimeField(null=True, blank=True)
    lugar = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, max_length=60, null=True)
    texto = models.TextField(max_length=5000, null=True)
    imagen = models.ImageField(upload_to='fotos', blank = True)
    imagen2 = models.ImageField(upload_to='fotos', blank=True)
    imagen3 = models.ImageField(upload_to='fotos', blank=True)
    url = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.nombre
    def image_table(self):
        if self.imagen:
            return mark_safe('<img src="{}" height="50" />'.format(self.imagen.url))
        else:
            return mark_safe('<p>Sem imagem</p>')

# El modelo de notas fue creado para agregar contenido de entrevistas

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
    

