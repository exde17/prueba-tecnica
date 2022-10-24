"""djangoPrueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logyn',views.entrar, name='entrar'),
    path('',views.home, name='home' ),#enrutando y dando direcciones
    #path('tareas/', views.tareas, name='tareas'),
    path('cerrar/', views.cerrar, name='cerrar'), #cerrar sesion
    path('registro/', views.registro, name='registro'), #inicio de sesion
    path('propietario/', views.new_propietario, name='newPropietario'),
    path('listaPropietarios', views.verPropietarios, name='verPropietarios'),
    #path('actualizarP/<int:actu_id>', views.actualizarP, name='actualizarP'),
    path('vehiculo/', views.new_vehiculo, name='newVehiculo'),
    path('listaVehiculos', views.verVehiculo, name='listaVehiculos')
]
