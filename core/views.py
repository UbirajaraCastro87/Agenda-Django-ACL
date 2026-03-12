from http.client import responses

from django.shortcuts import render, redirect
from core.models import Eventos

# Create your views here.

#def index(request):
#   return  redirect('/agenda/')
def lista_eventos(request):
    usuario = request.user
    eventos = Eventos.objects.filter(usuario=usuario)

    dados = {'eventos': eventos}

    return  render(request,'agenda.html',dados)