from django.urls import path
from .views import *

urlpatterns = [
    path('api/get/', lista_productos, name='lista'),
    path('ver/', ver_productos, name='ver'),
    path('agregar/', agregar_producto, name='agregar'),
    path('api/registrar/', registrar_producto, name='registrar'),
    path('api/actualizar/<str:id_producto>/', actualizar_producto, name='actualizar'),
    path('api/eliminar/<str:id_producto>/', borrar_producto, name='eliminar'),
    path('api/consultar/<str:id_producto>/', obtener_producto, name='ver_producto'),
]