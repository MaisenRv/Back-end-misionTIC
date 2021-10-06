from django.db import models

class HojaDeVida (models.Model):

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length= 20, unique = True)
    apellido = models.CharField(max_length= 20)
    cedula = models.CharField(max_length= 12)
    correo = models.EmailField(max_length= 100)
    Agnos_experiencia = models.CharField(max_length=3)
    profesion = models.CharField(max_length= 20) 
    descripcion = models.TextField()  