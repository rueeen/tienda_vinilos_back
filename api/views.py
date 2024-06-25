from rest_framework import viewsets
from .models import Artista, Album, Genero
from .serializers import ArtistaSerializer, AlbumSerializer, GeneroSerializer, AlbumCreateUpdateSerializer

# Create your views here.
class ArtistaViewSet(viewsets.ModelViewSet): # Creamos una clase que hereda de viewsets.ModelViewSet
    queryset = Artista.objects.all() # Indicamos el queryset
    serializer_class = ArtistaSerializer # Indicamos el serializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return AlbumCreateUpdateSerializer
        return AlbumSerializer
    
class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer



