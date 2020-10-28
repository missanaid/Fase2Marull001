from django.shortcuts import render
from . models import Anime, Genero, Usuario
from django.views import generic

# Create your views here.
# objects.all() es como un select
# objects.filter es como un where


def index(request):
    num_Animes = Anime.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_animes':  num_Animes}
    )


def galeria(request):

    return render(
        request,
        'galeria.html',
    )


def contacto(request):

    return render(
        request,
        'contacto.html',
    )


def login(request):

    return render(
        request,
        'login.html',
    )


def register(request):

    return render(
        request,
        'register.html',
    )
