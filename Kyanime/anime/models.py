from django.db import models
from django.urls import reverse
import uuid


class Genero(models.Model):

    nombre = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse("genre-detail", args=[str(self.id)])

    def __str__(self):
        return self.nombre


class Anime(models.Model):
    nombre_anime = models.CharField(max_length=200)
    episodios = models.IntegerField(
        help_text='Cantidad de Capítulos del Anime')
    sinopsis = models.TextField(
        max_length=1000)
    genero = models.ManyToManyField(Genero)
    imagen = models.ImageField(upload_to='img/Animes/', null=True, blank=True)
    opening = models.URLField(max_length=100, default='')

    def __str__(self):
        return self.nombre_anime

    def get_absolute_url(self):
        """Devuelve la url para acceder a un registro detallado de el Anime."""
        return reverse('anime-detail', args=[str(self.id)])


class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    primer_nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(help_text='Email de Usuario')

    def __str__(self):
        """String for representing the Model object."""
        return self.nombre_usuario

    def get_absolute_url(self):
        return reverse('usuario-detail', args=[str(self.id)])
