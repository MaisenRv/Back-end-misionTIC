from rest_framework import serializers
from HVApp.models.usuarios import User
from HVApp.models.hojaDeVida import HojaDeVida
from HVApp.serializers.hojaDeVidaSerializer import HojaDeVidaSerializer

from drf_writable_nested import WritableNestedModelSerializer

from django.http import HttpResponse

class UserSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    HojaDeVida = HojaDeVidaSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'HojaDeVida'] 

        def create(self, validated_data):
            hojaDeVidaData = validated_data.pop('HojaDeVida')
            userInstance = User.objects.create(**validated_data)
            HojaDeVida.objects.create(user=userInstance, **hojaDeVidaData)
            return userInstance
        def to_representation(self, obj):
            user = User.objects.get(id=obj.id)
            hojaDeVida = HojaDeVida.objects.get(user=obj.id)
            return HttpResponse( {
                'id': user.id,
                'username': user.username,
                'password': user.password,
                'name': user.name,
                'email': user.email,
                'HojaDeVida': {
                    'id' : hojaDeVida.id,
                    'cedula': hojaDeVida.cedula,
                    'Agnos_experiencia': hojaDeVida.Agnos_experiencia,
                    'profesion': hojaDeVida.profesion,
                    'descripcion': hojaDeVida.descripcion
                }
            })