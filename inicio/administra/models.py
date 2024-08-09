from django.db import models
from django.contrib.auth.models import User

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='administra')
    edad = models.IntegerField()
    genero = models.CharField(max_length=12)
    raza = models.CharField(max_length=100)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'mascota'
        verbose_name_plural = 'mascotas'


    def __str__(self):
        return self.nombre
    
    

