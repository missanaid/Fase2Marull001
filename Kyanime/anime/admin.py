from django.contrib import admin

# Register your models here.
from . models import Genero, Anime, Usuario

admin.site.register(Anime)
admin.site.register(Genero)
admin.site.register(Usuario)
