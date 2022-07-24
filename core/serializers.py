from attr import field
from .models import *
from rest_framework import serializers

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'
