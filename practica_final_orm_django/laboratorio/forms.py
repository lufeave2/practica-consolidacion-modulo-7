from django import forms
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre', 'ciudad', 'pais']
        labels = {
            'nombre': 'Nombre del Laboratorio',
            'ciudad': 'Ciudad',
            'pais': 'País',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: BioTech'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Ciudad de México'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: México'}),
        }

class DirectorGeneralForm(forms.ModelForm):
    class Meta:
        model = DirectorGeneral
        fields = ['nombre', 'especialidad', 'laboratorio']
        labels = {
            'nombre': 'Nombre del Director',
            'especialidad': 'Especialidad',
            'laboratorio': 'Laboratorio Asignado',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Juan Pérez'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Bioquímica'}),
            'laboratorio': forms.Select(attrs={'class': 'form-control'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta']
        labels = {
            'nombre': 'Nombre del Producto',
            'laboratorio': 'Laboratorio',
            'f_fabricacion': 'Fecha de Fabricación',
            'p_costo': 'Precio de Costo ($)',
            'p_venta': 'Precio de Venta ($)',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Vacuna X'}),
            'laboratorio': forms.Select(attrs={'class': 'form-control'}),
            'f_fabricacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'p_costo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 50.00'}),
            'p_venta': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 100.00'}),
        }
