from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=255)
    proveedor=models.CharField(max_length=100)
    cantidad=models.CharField(max_length=100)
    peso=models.CharField(max_length=100)
    tamaño_empaque=models.CharField(max_length=100)
    costo=models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

