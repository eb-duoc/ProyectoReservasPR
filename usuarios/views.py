from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse ("Bienvenido, esta es una prueba de conexión")

def login(request):
    template = loader.get_template('usuarios/login.html')
    return HttpResponse (template.render())