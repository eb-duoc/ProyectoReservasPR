from django import forms
from django.forms import ModelForm
from .models import Usuario, Habitacion

# clase para formulario desde bbdd

class UsuarioForm(ModelForm):
    contraseña= forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['rutUsuario', 'nombreUsuario', 'apeUsuario', 'pais', 'correo','contraseña']
        #fields = '__all__'


class HabForm(ModelForm):

    class Meta:
        model = Habitacion
        fields = ['tipoHab', 'pisoHab', 'capacidad', 'comentario', 'precioHab']
    
