from django.urls import path

from . import  views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("home/", views.home, name="home"),
    path("habitaciones/", views.habitaciones, name="habitaciones"),
    path('registro_usuario', views.Usuario_Form , name="registro_usuario"),
    path('registro_habitacion', views.habitaciones2 , name="registro_habitacion"),
    path('registro_habitacion2', views.Habitacion_Form , name="registro_habitacion2"),
]