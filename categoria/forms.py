#Aqui se generan todos los formularios HTML que se utilizarán en la aplicación.

from django import forms
from .models import Categoria


#Crear una clase para cada formulario que necesitemos
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'imagen']
        labels = {
            'nombre': 'Nombre de la categoria',
            'imagen': 'URL de la imagen'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Nombre de la categoria'
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'URL de la imagen'
                }
            )
        }
        #Etiquetas
        labels = {
            'nombre': 'Nombre de la categoria',
            'imagen': 'URL de la imagen'
        }
        #Personalizar los mensajes de error
        error_messages = {
            'nombre': {
                'required': 'Ingresa un nombre de categoria válido'
            },
            'imagen': {
                'required': 'Ingresa una URL de imagen válida'
            }
        }