from django.db import models
from django.urls import reverse
import uuid


class Galeria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre_anime = models.CharField(max_length=200)
    descripcion = models.TextField(
        help_text='Descripcion de la Imagen')
    imagen = models.ImageField(upload_to='img/Animes/', null=True, blank=True)

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
