# Generated by Django 4.0.5 on 2022-07-24 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('rutCliente', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='rut_vededor')),
                ('nombreCliente', models.CharField(max_length=50, verbose_name='Nombre del Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('idSucursal', models.AutoField(primary_key=True, serialize=False, verbose_name='sucursal id:')),
                ('region', models.CharField(max_length=100, verbose_name='region')),
                ('comuna', models.CharField(max_length=100, verbose_name='comuna')),
                ('direccion', models.CharField(max_length=100, verbose_name='direccion')),
                ('imagen', models.ImageField(null=True, upload_to='sucursales')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('idVehiculo', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del vehiculo')),
                ('patente', models.CharField(max_length=6, verbose_name='Patente')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca vehiculo')),
                ('modelo', models.CharField(blank=True, max_length=20, null=True, verbose_name='Modelo')),
                ('color', models.CharField(max_length=20, verbose_name='Color vehiculo')),
                ('imagen', models.ImageField(null=True, upload_to='vehiculos')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='Vendedores',
            fields=[
                ('rutVendedor', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='rut_vededor')),
                ('nombreVendedor', models.CharField(max_length=50, verbose_name='Nombre del vendedor')),
                ('cantidadventa', models.IntegerField(null=True, verbose_name='cantidad venta')),
                ('username', models.CharField(blank=True, max_length=50, null=True, verbose_name='username')),
                ('password1', models.CharField(blank=True, max_length=50, null=True, verbose_name='password')),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('idVenta', models.AutoField(primary_key=True, serialize=False, verbose_name='Id venta')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.clientes')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.vehiculo')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.vendedores')),
            ],
        ),
    ]
