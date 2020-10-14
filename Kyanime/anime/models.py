from django.db import models

from django.urls import reverse
import uuid


class Genero(models.Model):

    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Anime(models.Model):

    nombre_anime = models.CharField(max_length=200)
    episodios = models.IntegerField(
        help_text='Cantidad de Capítulos del Anime')
    sinopsis = models.CharField(
        max_length=255, help_text='Descripción del Anime')
    rating_general = models.ForeignKey(
        'Review', on_delete=models.SET_NULL, null=True)
    genero = models.ManyToManyField(Genero)

    def __str__(self):
        return self.nombre_anime

    def get_absolute_url(self):
        """Devuelve la url para acceder a un registro detallado de el Anime."""
        return reverse('anime-detail', args=[str(self.id)])


class Review(models.Model):

    nombre_anime = models.ForeignKey(
        'Anime', on_delete=models.SET_NULL, null=True)
    review_date = models.DateField(null=True, blank=True)
    rating_general = models.FloatField(
        help_text='Valoración General del Anime')
    rating_animacion = models.FloatField(
        help_text='Valoración de la Animación')
    rating_traduccion = models.FloatField(
        help_text='Valoración de la Traducción del Anime')
    rating_personajes = models.FloatField(
        help_text='Valoración de los Personajes del Anime')

    def get_absolute_url(self):
        return reverse('review-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.nombre_anime


class Usuario(models.Model):

    nombre_usuario = models.CharField(max_length=100)
    primer_nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(help_text='Email de Usuario')

    def get_absolute_url(self):
        return reverse('usuario-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.nombre_usuario
