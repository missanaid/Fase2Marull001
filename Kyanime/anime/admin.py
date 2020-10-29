from django.contrib import admin

# Register your models here.
from . models import Galeria, Usuario

admin.site.register(Galeria)
admin.site.register(Usuario)
