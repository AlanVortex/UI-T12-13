from django.db import models

class Alumnos(models.Model):
    #atributos de clase
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    matricula = models.CharField(max_length=100, unique=True)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
    
    #Necesito una función que devuelva el objeto en formato de Diccionario
    def to_dict(self):
        return{
            #'ClaveValor': 'Valor'
            'nombre': self.nombre,
            'apellido': self.apellido,
            'edad': self.edad,
            'matricula': self.matricula,
            'correo': self.correo
        }

