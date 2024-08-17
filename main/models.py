from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    create = models.DateField(auto_now_add=True)
    CHOICES = {
        'Cliente':'Cliente',
        'Operario':'Operario'
    }
    tipo = models.CharField(max_length=12, choices=CHOICES)


class Equipo(models.Model):
    CHOICES_CATEGORIA = {
       'Ski' :'Ski',
       'Botas' :'Botas',
       'Trineo' :'Trineo',
       'Snow Board' :'Snow Board',
       'Otros' :'Otros'
    }
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=15, choices=CHOICES_CATEGORIA)
    imagen = models.CharField(max_length=500)
    precio = models.IntegerField(blank=True, null=True)
    CHOICES = {
       'Disponible' :'Disponible',
       'Arrendado' :'Arrendado',
       'Mantencion' :'Mantencion'
    }
    estado = models.CharField(max_length=12, choices=CHOICES)


class Arriendo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    observacion = models.TextField(blank=True,null=True)
    daniado =models.BooleanField(default=False)

