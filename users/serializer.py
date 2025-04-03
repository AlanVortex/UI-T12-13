from rest_framework.renderers import JSONRenderer
from .models import CustomUser
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'surname', 'control_number', 'age', 'tel', 'is_active', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True},
            # No marcamos 'email' como read_only para permitir su edición
        }
    
    def update(self, instance, validated_data):
        # Actualizar el email junto a los demás campos
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.control_number = validated_data.get('control_number', instance.control_number)
        instance.age = validated_data.get('age', instance.age)
        instance.tel = validated_data.get('tel', instance.tel)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

# Serializador para los tokens
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token =  super().get_token(user)
        token['email'] = user.email
        return token

