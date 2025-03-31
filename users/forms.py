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
    
    def clean_control_number(self):
        control_number = self.cleaned_data.get('control_number')
        regex = r'^[0-9]{5}[a-zA-Z]{2}[0-9]{3}$'
        if not re.match(regex, control_number):
            raise ValidationError("Debes ingresar un número de control válido (ej. 20223tn018).")
        return control_number

    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        regex = r'^[0-9]{10}$'
        if not re.match(regex, tel):
            raise ValidationError("Debes ingresar un número de teléfono de 10 dígitos.")
        return tel

    def clean_email(self):
        email = self.cleaned_data.get('email')
        regex = r'^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$'
        if not re.match(regex, email):
            raise ValidationError("Debes ingresar un correo electrónico válido de la UTEZ.")
        return email

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
                    'minLength': 10,
                    'maxLength': 10,
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

#Segundo formulario (inicio de sesión)
class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Correo electrónico", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    
def clean(self):
    cleaned_data = super().clean()
    username = cleaned_data.get("username")
    password = cleaned_data.get("password")
    if username and password:
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Usuario o contraseña incorrectos.")
    return cleaned_data