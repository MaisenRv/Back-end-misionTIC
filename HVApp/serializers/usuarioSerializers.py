from rest_framework import serializers
from HVApp.models.usuarios import User
from HVApp.models.hojaDeVida import HojaDeVida
from HVApp.serializers.hojaDeVidaSerializer import HojaDeVidaSerializer

class UserSerializer(serializers.ModelSerializer):
    HojaDeVida = HojaDeVidaSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'hojaDeVida']
        def create(self, validated_data):
            hojaDeVidaData = validated_data.pop('hojaDeVida')
            userInstance = User.objects.create(**validated_data)
            HojaDeVida.objects.create(user=userInstance, **hojaDeVidaData)
            return userInstance
        def to_representation(self, obj):
            user = User.objects.get(id=obj.id)
            hojaDeVida = HojaDeVida.objects.get(user=obj.id)
            return {
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'email': user.email,
                'hojaDeVida': {
                    'id' : hojaDeVida.id,
                    'nombre' : hojaDeVida.nombre,
                    'apellido': hojaDeVida.apellido, 
                    'cedula': hojaDeVida.cedula,
                    'correo': hojaDeVida.correo,
                    'Agnos_experiencia': hojaDeVida.Agnos_experiencia,
                    'profesion': hojaDeVida.profesion,
                    'descripcion': hojaDeVida.descripcion
                }
            }