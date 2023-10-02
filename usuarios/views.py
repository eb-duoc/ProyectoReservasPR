from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Habitacion

# Create your views here.

def index(request):
    return HttpResponse ("Bienvenido, esta es una prueba de conexión")

def login(request):
    template = loader.get_template('usuarios/login.html')
    return HttpResponse (template.render())

def home(request):
    template = loader.get_template('usuarios/home.html')
    return HttpResponse (template.render())

def habitaciones(request):
    habs=Habitacion.objects.all()
    print(habs)

    datos={
        'habs': habs
        }

    return render(request, 'usuarios/habitaciones.html', datos)