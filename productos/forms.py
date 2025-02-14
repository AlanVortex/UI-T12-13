#Generar aquí los formularios necesarios para la aplicación de productos
from django import forms
from .models import Producto

class productoForm(forms.ModelForm):
    class Meta:
        model = Producto
        
        #Campos que se van a mostrar en el formulario
        fields = ['nombre', 'precio', 'imagen']
        
        #Personalizar los campos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-input placeholder="Nombre del producto"'}),
            'precio': forms.NumberInput(attrs={'class': 'form-input placeholder="Precio del producto"'}),
            'imagen': forms.URLInput(attrs={'class': 'form-input placeholder="URL de la imagen"'}),
        }

        #Personalizar las etiquetas
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio (MXN)',
            'imagen': 'URL de la imagen'
        }

        #Personalizar los mensajes de error
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio',
                'unique': 'Este producto ya existe',
                'invalid': 'El nombre no es válido',
                'max_length': 'El nombre es muy largo'
            },
            'precio': {
                'required': 'Este campo es obligatorio',
            },
            'imagen': {
                'required': 'Este campo es obligatorio'
            }
        }