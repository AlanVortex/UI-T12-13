from django.urls import path
from .views import *

urlpatterns = [
    path('api/get/', lista_categoria, name='lista'),
    path('verCategoria/', ver_categorias, name='ver'),
    path('agregarCategoria/', agregar_categoria, name='agregar'),
    path('api/registrar/', registrar_categoria, name='registrar'),
    path('api/actualizar/<str:id_categoria>/', actualizar_categoria, name='actualizar'),
    path('api/eliminar/<str:id_categoria>/', borrar_categoria, name='eliminar'),
    path('api/consultar/<str:id_categoria>/', obtener_categoria, name='ver_categoria'),
]