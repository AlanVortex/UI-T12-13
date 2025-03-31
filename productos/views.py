from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
from django.shortcuts import render
from .forms import productoForm

class ProductoViewSet(viewsets.ModelViewSet):
    #esta variable me dice de donde saco el modelo y la informacion de base de datos
    queryset = Producto.objects.all()
    #como serializo la informacion
    serializer_class = ProductoSerializer
    #como renderizar mi informacion   
    renderer_classes = [JSONRenderer]

    #permitir filtar los metodos HTTP que se pueden usar
    #GET, POST, PUT, DELETE
    #Si no lo pongo, por defecto se permiten todos
    #http_method_names = ['GET', 'POST']

def agregar_view(request):
    form = productoForm()
    return render(request, 'agregar.html', {'form': form})