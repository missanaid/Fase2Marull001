from django.contrib import admin

# Register your models here.
from . models import Genero, Anime, Review, Usuario

admin.site.register(Anime)
admin.site.register(Review)
admin.site.register(Genero)
admin.site.register(Usuario)
