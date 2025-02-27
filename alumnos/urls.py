from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AlumnosViewSet

router = SimpleRouter()
router.register(r'api', AlumnosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]