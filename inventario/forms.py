#creamos los formularios orientados a los datos que ya tenemos en los modelos
from ast import Mod
from dataclasses import field, fields
from pyexpat import model
from turtle import color
from django.forms import ModelForm
from .models import propietario, vehiculos #importamos el modelo de propietario


#creando formulario apartir del modelo
class PropietarioForm(ModelForm):
    class Meta:
        model = propietario #decimos que usaremos eel modelo de propietario
        fields = ['tipoDocumento','documento','nombre','direccion','telefono','email'] #los campos a usar

class VehiculoForm(ModelForm):
    class Meta:
        exclude = ("first_name", "last_name")
        model = vehiculos
        field = ['placa','marca','modelo','color','observaciones']
