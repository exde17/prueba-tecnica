
#from unittest.util import _MAX_LENGTH
from email.policy import default
from random import choices
#from turtle import color
from django.db import models
from django.contrib.auth.models import User
from .choice import tipoDocumento, marca, color

# Create your models here.

class propietario(models.Model):
    tipoDocumento = models.CharField(max_length =2, choices=tipoDocumento, default='cc')
    documento = models.CharField(max_length =100)
    nombre = models.CharField(max_length =100)
    direccion = models.CharField(max_length =100)
    telefono = models.CharField(max_length =100)
    email = models.CharField(max_length =100)
    user = models.ForeignKey(User, on_delete= models.CASCADE) #creamos la llave foranea con tabla ususario y decimos que si se borra un usuario que borre tambien todos los datos relacionados con el

    """ def __str__(self):
        return self.nombre """

class vehiculos(models.Model):
    placa = models.CharField(max_length =30)
    marca = models.CharField(max_length =3, choices=marca, default='toy')        
    modelo = models.CharField(max_length =4)
    color = models.CharField(max_length =3, choices= color, default='roj')
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    observaciones = models.TextField(blank= True)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    