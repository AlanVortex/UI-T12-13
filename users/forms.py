from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
import re

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Contraseña',
                'title': 'La contraseña debe contener al menos 8 caracteres, una letra mayúscula, un número y un caracter especial (!#$%&?)',
            }
        )
    )

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        # Validar la longitud mínima de la contraseña
        if len(password1) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
        
        # Validar el formato de la contraseña (1 número, 1 mayúscula y 1 especial)
        regex = r'^(?=.*\d)(?=.*[A-Z])(?=.*[!#$%&?])'
        if not re.match(regex, password1):
            raise ValidationError("La contraseña debe incluir al menos un número, una letra mayúscula y un carácter especial.")
        
        return password1
    
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Confirmar Contraseña',
            }
        )
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")
        return password2

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel','password1', 'password2']
        
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo electrónico',
                    'required': True,
                    'pattern': '^[a-zA-Z0-9]+@utez\.edu\.mx$',
                    'title': 'Debes ingresar un correo electrónico valido de la UTEZ',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Nombre',
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Apellido',
                }
            ),
            'control_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Número de control',
                    'pattern': '^[0-9]{5}[a-zA-Z]{2}[0-9]{3}$',
                    'title': 'Debes ingresar un número de control válido (ej. 20223tn018)',
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Edad',
                    'min': 18,
                    'max': 100,
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Teléfono',
                    'pattern': '^[0-9]{10}$',
                    'title': 'Debes ingresar un número de teléfono de 10 dígitos',
                }
            )
        }

#Segundo formulario (Inicio de sesión)
class CustomUserLoginForm(AuthenticationForm):
    pass
    #pass es una palabra reservada que se utiliza para indicar que no se va a hacer nada