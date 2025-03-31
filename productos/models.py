from django.db import models
from categoria.models import Categoria

class DetallesProducto(models.Model):
    descripcion = models.CharField(max_length=300)
    fecha_caducidad = models.DateField()

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)


# Clase de productos
class Producto(models.Model):
    #atributos de clase
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()
    detalles_producto = models.OneToOneField(DetallesProducto, null=True, blank=True, on_delete=models.CASCADE)
    #cuando se requiera usar una relación se usa un campo:
    # OneToOneField (1 a 1)
    # ForeignKey (1 a muchos)
    # ManyToManyField (muchos a muchos)
    categoria = models.ForeignKey(Categoria, null=True, blank=True , on_delete=models.SET_NULL)
    proveedor = models.ManyToManyField(Proveedor)


    def __str__(self):
        return self.nombre
    
    #Necesito una función que devuelva el objeto en formato de Diccionario
    def to_dict(self):
        return{
            #'ClaveValor': 'Valor'
            'nombre': self.nombre,
            'precio': self.precio,
            'imagen': self.imagen
        }
    


