from django.db import models
from .usuarios import User

class HojaDeVida (models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,related_name="HojaDeVida",on_delete=models.CASCADE)
    cedula = models.CharField(max_length= 12)
    Agnos_experiencia = models.CharField(max_length=3)
    profesion = models.CharField(max_length= 20) 
    descripcion = models.TextField()  