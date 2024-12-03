from django.db import models

# Create your models here.
class Orden(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    id_empleado=models.IntegerField(null=True)
    id_cliente=models.IntegerField(null=True)
    id_producto=models.IntegerField(null=True)
    id_mesa=models.IntegerField(null=True)
    productos=models.CharField(max_length=255)
    mesa=models.CharField(max_length=100)
    nom_cliente=models.CharField(max_length=100)
    tipo=models.CharField(max_length=100)
    costo=models.CharField(max_length=100)
    hora=models.CharField(max_length=12)

    def __str__(self):
        return self.productos
