from django.contrib import admin # Importamos el módulo admin de Django para registrar los modelos en el panel de administración
from api.models import Artista, Album, Genero, UserProfile, UserType # Importamos los modelos Artista, Album, Genero, UserProfile y UserType

# Register your models here.
admin.site.register(Artista) # Registramos el modelo Artista en el panel de administración
admin.site.register(Album) # Registramos el modelo Album en el panel de administración
admin.site.register(Genero) # Registramos el modelo Genero en el panel de administración
admin.site.register(UserProfile) # Registramos el modelo UserProfile en el panel de administración
admin.site.register(UserType) # Registramos el modelo UserType en el panel de administración