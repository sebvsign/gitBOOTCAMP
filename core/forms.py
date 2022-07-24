from django import forms
from django.forms import widgets

from .models import *
 

class VentaForm(forms.ModelForm):

    class Meta:
        model = Ventas

        fields = ('__all__')
        labels = {
            'cliente': 'cliente',
            'vehiculo': 'vehiculo',
            'vendedor': 'vendedor',
        }
        widgets = {
            'cliente': forms.Select(attrs={'Class':'formulario__input'}),
            'vehiculo': forms.Select(attrs={'Class':'formulario__input'}),
            'vendedor': forms.Select(attrs={'Class':'formulario__input'}),            
        }