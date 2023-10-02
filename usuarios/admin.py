from django.contrib import admin

# Register your models here.
from .models import Usuario, Habitacion

admin.site.register(Usuario)
admin.site.register(Habitacion)

