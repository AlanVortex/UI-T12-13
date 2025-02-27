from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Alumnos
from .serializers import AlumnosSerializer

class AlumnosViewSet(viewsets.ModelViewSet):
    #esta variable me dice de donde saco el modelo y la informacion de base de datos
    queryset = Alumnos.objects.all()
    #como serializo la informacion
    serializer_class = AlumnosSerializer
    #como renderizar mi informacion   
    renderer_classes = [JSONRenderer]

    #permitir filtar los metodos HTTP que se pueden usar
    #GET, POST, PUT, DELETE
    #Si no lo pongo, por defecto se permiten todos
    #http_method_names = ['GET', 'POST']