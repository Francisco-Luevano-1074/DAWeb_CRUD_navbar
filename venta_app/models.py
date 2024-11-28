from django.db import models

# Create your views here.

class Venta(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    empaque=models.CharField(max_length=100)
    contenido=models.CharField(max_length=100)
    dir_cliente=models.CharField(max_length=100)
    tel_cliente=models.CharField(max_length=100)
    nom_cliente=models.CharField(max_length=100)
    total=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nom_cliente