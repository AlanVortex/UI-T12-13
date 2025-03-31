from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AlumnosViewSet
from .views import *

router = SimpleRouter()
router.register(r'api', AlumnosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('agregarAlumnos/', agregar_alumnos, name='agregar'),
    # path('api/registrar/', registrar_alumnos, name='registrar'),
    # path('api/actualizar/<str:id_alumnos>/', actualizar_alumnos, name='actualizar'),
    # path('api/eliminar/<str:id_alumnos>/', borrar_alumnos, name='eliminar'),
    # path('api/consultar/<str:id_alumnos>/', obtener_alumnos, name='ver_alumnos'),
]