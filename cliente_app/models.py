from django.db import models

# Create your models here.
class Cliente(models.Model):
    codigo=models.IntegerField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=100)
    no_telefono=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    orden=models.CharField(max_length=100)
    mesa=models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

