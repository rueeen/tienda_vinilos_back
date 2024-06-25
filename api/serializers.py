from rest_framework import serializers # Importamos el módulo serializers de la librería rest_framework
from .models import Artista, Album, Genero # Importamos los modelos que vamos a serializar

class GeneroSerializer(serializers.ModelSerializer): # Creamos una clase que hereda de serializers.ModelSerializer
    class Meta: # Definimos la clase Meta
        model = Genero # Indicamos el modelo que vamos a serializar
        fields = '__all__' # Indicamos que vamos a serializar todos los campos del modelo

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    artista = ArtistaSerializer() # Indicamos que vamos a serializar el artista
    genero = GeneroSerializer(many=True) # Indicamos que vamos a serializar los géneros
    class Meta:
        model = Album
        fields = '__all__'

class AlbumCreateUpdateSerializer(serializers.ModelSerializer):
    artista = serializers.PrimaryKeyRelatedField(queryset=Artista.objects.all())
    genero = serializers.PrimaryKeyRelatedField(many=True, queryset=Genero.objects.all())
    
    class Meta:
        model = Album
        fields = '__all__'

