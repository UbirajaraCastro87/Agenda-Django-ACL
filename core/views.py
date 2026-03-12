from http.client import responses

from django.contrib import messages
from django.shortcuts import render, redirect
from core.models import Eventos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def index(request):
   return  redirect('/agenda/')

def login_user(request):
    return render(request,'login.html')

def logout_user(request):
   logout(request)
   return redirect('/')
@login_required(login_url='/login/')
def evento(request):
    return render(request,'evento.html')
@login_required(login_url='/login/')
def submit_evento(request):
    if request.method == 'POST':
        titulo = request.POST['evento']
        data_evento =request.POST['data_evento']

        descricao =request.POST['description']
        usuario =request.user

        Eventos.objects.create(
            titulo = titulo,
            data_evento = data_evento,
            descricao = descricao,
            usuario = usuario

        )



    return redirect('/')



def submit_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('/agenda/')
        else:
            messages.error(request,'usuario ou senha incorretos')


    return redirect('/')

@login_required(login_url='/login/')

def lista_eventos(request):
    usuario = request.user
    #eventos = Eventos.objects.filter(usuario=usuario)
    eventos = Eventos.objects.all()

    dados = {'eventos': eventos}

    return  render(request,'agenda.html',dados)