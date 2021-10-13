from HVApp.models.hojaDeVida import HojaDeVida
from rest_framework import serializers

class HojaDeVidaSerializer(serializers.ModelSerializer):   
    class Meta:
        model = HojaDeVida
        fields = ['cedula','Agnos_experiencia','profesion','descripcion']

