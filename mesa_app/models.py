from django.db import models

# Create your models here.
class Mesa(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    ubicacion=models.CharField(max_length=255)
    tamaño=models.CharField(max_length=100)
    sillas=models.CharField(max_length=100)

    def __str__(self):
        return self.ubicacion
