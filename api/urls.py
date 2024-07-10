from django.urls import path, include
from rest_framework.routers import DefaultRouter # Importamos DefaultRouter
from .views import ArtistaViewSet, AlbumViewSet, GeneroViewSet, CustomTokenObtainPairView, RegisterView, UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter() # Creamos una instancia de DefaultRouter

router.register('artistas', ArtistaViewSet) # Registramos la vista de Artista
router.register('albums', AlbumViewSet) # Registramos la vista de Album
router.register('generos', GeneroViewSet) # Registramos la vista de Genero

urlpatterns = [
    path('', include(router.urls)), # Incluimos las URLs de la API
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
]




