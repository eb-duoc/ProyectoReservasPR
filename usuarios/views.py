from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Habitacion
from .forms import UsuarioForm, HabForm

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


def Usuario_Form (request):
    data={
        'form':UsuarioForm()

    }
    if request.method=='POST':
        formulario =UsuarioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            data['mensaje'] = "Registro exitoso"
    return render(request, 'usuarios/registro_usuario.html',data)

def habitaciones2(request):
    habs=Habitacion.objects.all()
    print(habs)

    datos={
        'habs': habs
        }

    return render(request, 'usuarios/registro_habitacion.html', datos)


def Habitacion_Form (request):
    data={
        'form':HabForm()

    }
    if request.method=='POST':
        formulario =HabForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            data['mensaje'] = "Registro exitoso"
    return render(request, 'usuarios/registro_habitacion2.html',data)