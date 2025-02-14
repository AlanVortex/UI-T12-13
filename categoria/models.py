from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.URLField()

    def __str__(self):
        return self.nombre
    #Necesito una funcion que devuela el objeto en forma de diccionario
    def to_dict(self):
        return{
            # 'claveValor': 'valor'
            'nombre': self.nombre,
            'imagen': self.imagen
        }