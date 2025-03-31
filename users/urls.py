
from django.urls import path , include
from .views import *
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

#Configurar el router 
router = SimpleRouter()
router.register(r'api',UserViewsSets)

urlpatterns = [
        path('',include(router.urls)),
        path('token/',CustomTokenObtainPairView.as_view() , name = 'token'),
        path('token/refresh/',TokenRefreshView.as_view() , name = 'refresh'),
        path('form/',CustomUserFormAPI.as_view() , name = 'form'),
]