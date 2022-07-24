from django.shortcuts import get_object_or_404, redirect, render
from matplotlib.style import context
from requests import request
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from .models import *


from core.forms import VentaForm

from rest_framework import viewsets
from .serializers import SucursalSerializer
# Create your views here.


def home(request):

    return render(request, 'core/home.html')

def sucursal(request):
    sucursales = Sucursal.objects.all()
    data = {
        'sucursales': sucursales
    }
    return render(request, 'core/sucursales.html', data)

def galeria(request):
    vehiculos = Vehiculo.objects.all()
    data = {
        'vehiculos': vehiculos
    }
    return render(request, 'core/galeria.html', data)


def venta_view(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('core:venta')
    else:
        form = VentaForm()
    return render(request, 'core/ventas/ventas.html', {'form':form})



def listarVentas(request):
    ventas = Ventas.objects.all()
    data = {
        'ventas':ventas
    }
    return render(request, 'core/ventas/listar_ventas.html', data)

def listarClientes(request):
    clientes = Clientes.objects.all()
    data = {
        'clientes':clientes
    }
    return render(request, 'core/clientes/listar.html', data)







def listarClientes(request):
    clientes = Clientes.objects.all()
    data = {
        'clientes': clientes
    }
    if request.method =='POST':
        rutCliente=request.POST['rutCliente']
        nombreCliente=request.POST['nombreCliente']
        rut = rutCliente
        exists = Clientes.objects.filter(rutCliente=rut).exists()
        if exists:
            messages.error(request, "Este rut ya existe")
        else:    
            Clientes(rutCliente=rutCliente,nombreCliente=nombreCliente).save() 
            messages.success(request,'El cliente '+request.POST['nombreCliente'] +' se registro exitosamente')
        
        return render(request,'core/clientes/clientes.html',data)
    else:
        return render(request,'core/clientes/clientes.html',data)

def modificarCliente(request,id):
    clientes = get_object_or_404(Clientes, rutCliente=id )
    data = {
        'clientes': clientes
    }
    if request.method =='POST':
        nombreCliente=request.POST['nombreCliente']
        Clientes(rutCliente=id,nombreCliente=nombreCliente).save() 
        messages.success(request,'El cliente '+request.POST['nombreCliente'] +' se registro exitosamente')
        return redirect(to="clientes")
    else:
        return render(request,'core/clientes/modificar.html', data)   


def eliminarCliente(request,id):
    cliente = get_object_or_404(Clientes, rutCliente=id )
    cliente.delete()

    return redirect(to="clientes")



## JOIN AL LOGIN :D

def registrar(request):
    if request.method =='POST':
        rutVendedor=request.POST['rutVendedor']
        nombreVendedor=request.POST['nombreVendedor']
        username=request.POST['username']
        password1=request.POST['password1']
        rut = rutVendedor
        exists = Vendedores.objects.filter(rutVendedor=rut).exists()
        if exists:
            messages.error(request, "Este rut ya existe")
        else:    
            Vendedores(rutVendedor=rutVendedor,nombreVendedor=nombreVendedor,password1=password1,username=username).save() 
            messages.success(request,'El usuario '+request.POST['nombreVendedor'] +' se registro exitosamente')
        
        return render(request,'core/registrar.html')
    else:
        return render(request,'core/registrar.html')
        
def login(request):
    if request.method=='POST':
        try:
            detalleUsuario=Vendedores.objects.get(username=request.POST['username'],password1=request.POST['password1'])
            print("Usuario=", detalleUsuario)
            request.session['username']=detalleUsuario.username
            return render(request, 'core/home.html')
        except Vendedores.DoesNotExist as e:
            messages.success(request,'Username o password no es correcto')
    
    return render(request,'core/login.html')

def cerrarSesion(request):
    try:
        del request.session['username']
    except:
        return render(request, 'core/home.html')
    return render(request, 'core/home.html')



class SucursalViewset(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
