from django.urls import path, include
from rest_framework.routers import DefaultRouter # Importamos DefaultRouter
from .views import ArtistaViewSet, AlbumViewSet, GeneroViewSet

router = DefaultRouter() # Creamos una instancia de DefaultRouter

router.register('artistas', ArtistaViewSet) # Registramos la vista de Artista
router.register('albums', AlbumViewSet) # Registramos la vista de Album
router.register('generos', GeneroViewSet) # Registramos la vista de Genero

urlpatterns = [
    path('', include(router.urls)), # Incluimos las URLs de la API
]




