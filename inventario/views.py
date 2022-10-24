from ast import Try
#from typing_extensions import Required
from django.shortcuts import render, redirect, get_object_or_404 #usamos render para llamar los archivos y redirect para redireccionar a las vistas 
#from django.http import HttpResponse #solo emplo para ver funcion por http
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #para crear el form de registro y para el formulario de inicio de sesion
from django.contrib.auth.models import User #para registrar usuario en la aplicacion no en la db 
from django.contrib.auth import login, logout, authenticate #ejecuta una cooky que guardar la informacion del usuario, logout cierra sesion, authenticate comprueba si el usuario existe
from django.db import IntegrityError #gestiona los errores
from .forms import PropietarioForm  #importamos el formulario que creamos
from .forms import VehiculoForm
from .models import propietario, vehiculos #desde modelo me traigo el modelo de los propietarios

# Create your views here.
def registro(request):
    
    if request.method == 'GET':#verificamos si entra por el get queremos que solo cargue el formulario
        return render(request, 'registro.html',{         
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])#preparamos los datos para ser guardados en la db
                #login(request, user) #de esta forma guarda la info en una cooky
                user.save()#guardamos los datos en la db
                login(request, user) #de esta forma guarda la info en una cooky
                return redirect('home')
                #return HttpResponse('ususraio creado')
            except IntegrityError: 
                #nos deja en la misma pagina pero nos muestra el error encima, hay que pasar el error a la pagina Login.html 
                return render(request, 'registro.html',{         
                'form': UserCreationForm,
                'error': 'usuario ya existe'
    })   

        print(request.POST)#si entra por el post enviaremos los datos 
        print('por medio de post') 
        return render(request, 'registro.html',{         
            'form': UserCreationForm,
            'error': 'las contraseñas no coinciden'}) 
    
#ver lista de propietarios
def verPropietarios(request):
   #datos= propietario.objects.all()#para llamar a todos los datos sin de la db en esa tabla
   datos = propietario.objects.filter(user = request.user)
   return render(request, 'verPropietarios.html', {
    'verPropietario': datos})

#ver vehiculo
def verVehiculo(request):
    datos = vehiculos.objects.filter(user = request.user)
    #datos = vehiculo.objects.all() #filter(propie = request.propie_id)
    return render(request, 'verVehiculos.html', {
        'verVehiculo': datos
    })

#home
def home(request): #mostrare la lista de propietarios
    return render(request, 'home.html')   

#tareas
""" def tareas(request):
    return render(request, 'tareas.html') """

#iniciar sesion
def entrar(request):
    if request.method == 'GET':
        return render(request, 'entrar.html',{
            'form': AuthenticationForm
        })
    else:
        #verifico ssi el usuario existe o no
        user = authenticate( request, username=request.POST['username'], password=request.POST['password'])
        #verifico si el ususario existe o no verificando la variable user si esta vacia
        if user is None:
            return render(request, 'entrar.html',{
            'form': AuthenticationForm,
            'error': 'ususario no existe'
            })
        else:
            login(request, user)
            return redirect('home')    
        #print(request.POST) #comprobar que los datos si se estan enviando
        return render(request, 'entrar.html',{
            'form': AuthenticationForm
        })
        
            
#cerrar sesion
def cerrar(request):
    logout(request)
    return redirect('home') 

#propietario
def new_propietario(request):
    if request.method == 'GET':
        return render(request, 'propietario.html',{
            'form': PropietarioForm
        })    
    else:
        try:
            form= PropietarioForm(request.POST)
            nuevo_propietario = form.save(commit=False)
            nuevo_propietario.user = request.user #obtengo el usuario que tengo en cookys
            nuevo_propietario.save()
            return redirect('home')
            """ return render(request, 'propietario.html',{
                'form': PropietarioForm
            })  """ 
        except ValueError:
            return render(request, 'propietario.html',{
                'form': PropietarioForm,
                'error': 'porfavor verifique sus datos'
            })   

#crear vehiculo
def new_vehiculo(request):
    if request.method == 'GET':
        return render(request, 'vehiculo.html',{
            'form': VehiculoForm    
        })    
    else:
        try: 
            form= VehiculoForm(request.POST)
            nuevo_vehiculo = form.save(commit=False)
            nuevo_vehiculo.user = request.user #obtengo el usuario que tengo en cookys
            nuevo_vehiculo.save()
            return redirect('home')             
        except ValueError:
            return render(request, 'vehiculo.html',{
            'form': VehiculoForm,
            'error': 'porfavor verifique sus datos'
        }) 

#adtualizar propietario
""" def actualizarP(request, actu_id):
    if request.method == 'GET':
        form = PropietarioForm(instance=propietario)
        return render(request, 'actualizaP.html', {'form': form})
    else:
        actualiza = get_object_or_404(propietario, pk = actu_id)
        form = PropietarioForm(request.POST, instance=actualiza) 
        form.save()
        return redirect('verPropietarios')    """
