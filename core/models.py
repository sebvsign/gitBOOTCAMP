from django.db import models

# Create your models here.
class Sucursal(models.Model):
    idSucursal = models.AutoField(primary_key=True, verbose_name='sucursal id:')
    region = models.CharField(max_length=100, verbose_name='region')
    comuna = models.CharField(max_length=100, verbose_name='comuna')
    direccion = models.CharField(max_length=100, verbose_name='direccion')
    imagen = models.ImageField(upload_to = "sucursales", null= True)

    ###

    def __str__(self):
        return self.comuna

# Create your models here.
class Clientes(models.Model):
    rutCliente = models.CharField(max_length=10,primary_key=True,null=False, unique= True ,verbose_name='rut_vededor')
    nombreCliente = models.CharField(max_length=50,verbose_name="Nombre del Cliente")

    def __str__(self):
        return self.nombreCliente

class Vehiculo(models.Model):
    idVehiculo= models.AutoField(primary_key=True,verbose_name='Id del vehiculo')
    patente= models.CharField(max_length=6,verbose_name='Patente')
    marca=models.CharField(max_length=20, verbose_name='Marca vehiculo')
    modelo= models.CharField(max_length=20,null=True,blank=True,verbose_name='Modelo')
    color=models.CharField(max_length=20,verbose_name='Color vehiculo')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = "vehiculos", null= True)
    def __str__(self) :
        return self.patente


class Vendedores(models.Model):
    rutVendedor = models.CharField(max_length=10,primary_key=True,null=False, unique= True ,verbose_name='rut_vededor')
    nombreVendedor = models.CharField(max_length=50,verbose_name="Nombre del vendedor")
    cantidadventa = models.IntegerField(null=True, verbose_name='cantidad venta', default=0)
    username = models.CharField(max_length=50,verbose_name="username",null=True, blank=True )
    password1 = models.CharField(max_length=50,verbose_name='password', null=True, blank=True )
    def __str__(self):
        return self.rutVendedor

class Ventas(models.Model):
    idVenta= models.AutoField(primary_key=True, verbose_name='Id venta')
    vendedor = models.ForeignKey(Vendedores,on_delete=models.PROTECT)
    vehiculo = models.ForeignKey(Vehiculo,on_delete=models.PROTECT)
    cliente = models.ForeignKey(Clientes,on_delete=models.PROTECT)
    
    def __str__(self) :
        return self.idVenta