from django.db import models

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Artista(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.IntegerField()
    publicacion = models.DateField()
    genero = models.ManyToManyField(Genero)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)

    def __str__(self):
        return self.titulo
    


    