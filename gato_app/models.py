from django.db import models

# Create your models here.
class Gato(models.Model):
    id_gato=models.IntegerField(primary_key=True)
    id_venta=models.IntegerField(null=True)
    id_orden=models.IntegerField(null=True)
    nombre=models.CharField(max_length=255)
    edad=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    raza=models.CharField(max_length=100)
    precio=models.CharField(max_length=100)
    caracteristica=models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

