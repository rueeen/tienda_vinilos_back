from rest_framework import viewsets, generics

from api.permissions import IsClient, IsEmployee # Importamos viewsets y generics de la librería rest_framework
from .models import Artista, Album, Genero # Importamos los modelos que vamos a serializar
from django.contrib.auth.models import User
from .serializers import ArtistaSerializer, AlbumSerializer, GeneroSerializer, AlbumCreateUpdateSerializer, RegisterSerializer
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Para inicio de sesion
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsClient | IsEmployee]
        else:
            permission_classes = [IsAuthenticated, IsEmployee]
        return [permission() for permission in permission_classes]

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return AlbumCreateUpdateSerializer
        return AlbumSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsClient | IsEmployee]
        else:
            permission_classes = [IsAuthenticated, IsEmployee]
        return [permission() for permission in permission_classes]

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsClient | IsEmployee]
        else:
            permission_classes = [IsAuthenticated, IsEmployee]
        return [permission() for permission in permission_classes]

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)