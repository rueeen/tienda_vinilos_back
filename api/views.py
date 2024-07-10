from rest_framework import viewsets, generics
from api.permissions import IsClient, IsEmployee
from .models import Artista, Album, Genero
from django.contrib.auth.models import User
from .serializers import (
    ArtistaSerializer, AlbumSerializer, GeneroSerializer, 
    AlbumCreateUpdateSerializer, RegisterSerializer,
    UserSerializer, CustomTokenObtainPairSerializer
)
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# ViewSet para el modelo Artista
class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

    def get_permissions(self):
        """
        Define los permisos para las acciones del ViewSet de Artista.
        Permite acceso a usuarios autenticados con permisos de cliente o empleado para las acciones de listar y recuperar.
        Permite acceso solo a empleados autenticados para las demás acciones.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsClient | IsEmployee]
        else:
            permission_classes = [IsAuthenticated, IsEmployee]
        return [permission() for permission in permission_classes]

# ViewSet para el modelo Album
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()

    def get_serializer_class(self):
        """
        Retorna el serializador adecuado según la acción.
        Utiliza AlbumCreateUpdateSerializer para las acciones de creación y actualización.
        Utiliza AlbumSerializer para las demás acciones.
        """
        if self.action in ['create', 'update', 'partial_update']:
            return AlbumCreateUpdateSerializer
        return AlbumSerializer

    def get_permissions(self):
        """
        Define los permisos para las acciones del ViewSet de Album.
        Permite acceso a usuarios autenticados con permisos de cliente o empleado para las acciones de listar y recuperar.
        Permite acceso solo a empleados autenticados para las demás acciones.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsClient | IsEmployee]
        else:
            permission_classes = [IsAuthenticated, IsEmployee]
        return [permission() for permission in permission_classes]

# ViewSet para el modelo Genero
class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

    def get_permissions(self):
        """
        Define los permisos para las acciones del ViewSet de Genero.
        Permite acceso a usuarios autenticados con permisos de cliente o empleado para las acciones de listar y recuperar.
        Permite acceso solo a empleados autenticados para las demás acciones.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsClient | IsEmployee]
        else:
            permission_classes = [IsAuthenticated, IsEmployee]
        return [permission() for permission in permission_classes]

# Vista personalizada para obtener tokens JWT
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# Vista para registrar nuevos usuarios
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Vista para obtener los detalles del usuario autenticado
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Retorna los detalles del usuario autenticado.
        
        Args:
            request: El objeto de la solicitud.

        Returns:
            Response: La respuesta con los datos del usuario serializados.
        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
