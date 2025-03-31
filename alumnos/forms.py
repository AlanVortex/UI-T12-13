#Aqui se generan todos los formularios HTML que se utilizarán en la aplicación.

from django import forms
from .models import Alumnos


#Crear una clase para cada formulario que necesitemos
class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['nombre', 'apellido', 'edad', 'matricula', 'correo']
        labels = {
            'nombre': 'Nombre del alumnos',
            'apellido': 'Apellido del alumno',
            'edad': 'Edad del alumno',
            'matricula': 'Matricula del alumno',
            'correo': 'Correo del alumno'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Nombre del alumno'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Apellido del alumno'
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Edad del alumno'
                }
            ),
            'matricula': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Matricula del alumno'
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Correo del alumno'
                }
            )
        }
        #Etiquetas
        labels = {
            'nombre': 'Nombre del alumno',
            'apellido': 'Apellido del alumno',
            'edad': 'Edad del alumno',
            'matricula': 'Matricula del alumno',
            'correo': 'Correo del alumno'
        }
        #Personalizar los mensajes de error
        error_messages = {
            'nombre': {
                'required': 'Ingresa un nombre de alumno válido'
            },
            'apellido': {
                'required': 'Ingresa un apellido de alumno válido'
            },
            'edad': {
                'required': 'Ingresa una edad de alumno válida'
            },
            'matricula': {
                'required': 'Ingresa una matricula de alumno válida'
            },
            'correo': {
                'required': 'Ingresa un correo de alumno válido'
            }
        }