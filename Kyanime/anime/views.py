from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from . models import Galeria, Usuario
from django.views import generic

# Create your views here.
# objects.all() es como un select * from
# objects.filter es como un where


def index(request):
    num_Fotos = Galeria.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_animes':  num_Fotos}
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
