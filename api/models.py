from django.db import models 
from django.contrib.auth.models import User # Importamos el modelo User de Django para utilizarlo en el modelo UserProfile

# Create your models here.
class Genero(models.Model): # Definimos la clase Genero que hereda de models.Model
    nombre = models.CharField(max_length=100) # Definimos el campo nombre como un CharField con una longitud máxima de 100 caracteres

    def __str__(self): # Definimos el método __str__ para retornar el nombre del género
        return self.nombre

class Artista(models.Model): # Definimos la clase Artista que hereda de models.Model
    nombre = models.CharField(max_length=100) # Definimos el campo nombre como un CharField con una longitud máxima de 100 caracteres

    def __str__(self): # Definimos el método __str__ para retornar el nombre del artista
        return self.nombre

class Album(models.Model): # Definimos la clase Album que hereda de models.Model
    titulo = models.CharField(max_length=100) # Definimos el campo titulo como un CharField con una longitud máxima de 100 caracteres
    precio = models.FloatField() # Definimos el campo precio como un FloatField
    stock = models.IntegerField() # Definimos el campo stock como un IntegerField
    publicacion = models.DateField() # Definimos el campo publicacion como un DateField
    genero = models.ManyToManyField(Genero) # Definimos el campo genero como una relación ManyToMany con el modelo Genero
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE) # Definimos el campo artista como una relación ForeignKey con el modelo Artista
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True) # Definimos el campo portada como un ImageField con la ruta de subida 'portadas/'

    def __str__(self): # Definimos el método __str__ para retornar el título del álbum
        return self.titulo
    
class UserType(models.Model):
    user_type = models.CharField(max_length=10, unique=True) # Definimos el campo user_type como un CharField con una longitud máxima de 10 caracteres y único

    def __str__(self): # Definimos el método __str__ para retornar el tipo de usuario
        return self.user_type

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Dejamos null=True y blank=True para permitir que el campo sea opcional y poder crear 
    # superusuario sin tipo de usuario
    user_type = models.ForeignKey(UserType, on_delete=models.RESTRICT, null=True, blank=True) # Definimos el campo user_type como una relación ForeignKey con el modelo UserType  

    def __str__(self): # Definimos el método __str__ para retornar el nombre de usuario
        return self.user.username

    