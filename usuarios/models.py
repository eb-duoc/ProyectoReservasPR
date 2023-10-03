from django.db import models

# Create your models here.

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True, verbose_name='id de usuario')
    rutUsuario = models.CharField(max_length=20, verbose_name='rut de usuario')
    nombreUsuario = models.CharField(max_length=20, verbose_name='nombre de usuario')
    apeUsuario = models.CharField(max_length=20,default='', verbose_name='apellido de usuario')
    pais = models.CharField(max_length=20,default='', verbose_name='pais')
    correo = models.CharField(max_length=20,default='', verbose_name='correo de usuario')
    contraseña = models.CharField(max_length=20,default='NO VALUE', verbose_name='constraseña de usuario')


    def __str__(self):
        return str(self.idUsuario)
    


class Habitacion(models.Model):
     idHab = models.AutoField(primary_key=True, verbose_name='id de habitacion')
     tipoHab = models.CharField(max_length=50, verbose_name='tipo de habitacion')
     pisoHab = models.IntegerField(verbose_name='piso de habitacion')
     capacidad = models.CharField(max_length=10, verbose_name='capacidad habitacion')
     comentario = models.CharField(max_length=50, verbose_name='comentario de habitacion')
     precioHab = models.IntegerField(verbose_name='precio de habitacion')


     def __str__(self):
         return str(self.idHab)