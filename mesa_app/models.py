from django.db import models

# Create your models here.
class Mesa(models.Model):
    id_mesa=models.CharField(primary_key=True, max_length=6)
    ubicacion=models.CharField(max_length=255)
    tamaño=models.CharField(max_length=100)
    sillas=models.CharField(max_length=100)
    id_gato=models.IntegerField(null=True)

    def __str__(self):
        return self.ubicacion
