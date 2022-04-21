from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.

class estadomascota(models.Model):
    situacion=models.CharField(max_length=20)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='estadomascota'
        verbose_name_plural='estadosmascota'
    
    def __str__(self):
        return self.situacion

class mascota(models.Model):
    correlativo=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    fotografia=models.ImageField(upload_to='mascota')
    edad=models.CharField(max_length=30)
    genero=models.CharField(max_length=12)
    fecha_de_rescate=models.DateField()
    estado=models.ForeignKey(estadomascota, on_delete=models.CASCADE)
    raza=models.CharField(max_length=25)
    enfermedad=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=300)
    adoptante=models.TextField(blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='mascota'
        verbose_name_plural='mascotas'
    def _str_(self):
        return self.titulo



