from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=100)
    no_telefono=models.CharField(max_length=100)
    email=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
