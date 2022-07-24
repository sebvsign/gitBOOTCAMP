from django.db import router
from django.urls import URLPattern, path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('sucursal', SucursalViewset)

urlpatterns = [
    path('', home, name="home"),
    path('autos/', galeria, name="galeria"),
    path('sucursales/', sucursal, name="sucursal"),
    path('login/', login, name="login"),
    path('listar/', listarClientes, name="listarClientes"),


    path('listar_ventas/', listarVentas, name="listarVentas"),

    path('ventas/', venta_view, name="ventas"),

    path('login/registrar/', registrar, name="registrar"),
    path('cerrarSesion/', cerrarSesion, name='cerrarSesion'),
    path('clientes/', listarClientes, name='clientes'),
    path('eliminar-cliente/<id>',eliminarCliente,name="eliminarCliente"),
    path('modificar-cliente/<id>',modificarCliente,name="modificarCliente"),
    path('api/',include(router.urls)),
]
