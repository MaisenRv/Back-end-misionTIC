from HVApp.models.hojaDeVida import HojaDeVida
from rest_framework import serializers

class HojaDeVidaSerializer(serializers.ModelSerializer):   
    class Meta:
        model = HojaDeVida
        fields = ['nombre', 'apellido', 'cedula','correo','Agnos_experiencia','profesion','descripcion']

