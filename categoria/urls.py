from django.urls import path
from .views import *

urlpatterns = [
    path('api/get/', lista_categoria, name='lista'),
    path('verCategoria/', ver_categorias, name='ver'),
    path('agregarCategoria/', agregar_categoria, name='agregar'),
]