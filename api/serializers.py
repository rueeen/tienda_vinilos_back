from rest_framework import serializers
from .models import Artista, Album, Genero, UserProfile, UserType
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password

class GeneroSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Genero.
    """
    class Meta:
        model = Genero
        fields = '__all__'

class ArtistaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Artista.
    """
    class Meta:
        model = Artista
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Album, incluyendo relaciones anidadas con Artista y Genero.
    """
    artista = ArtistaSerializer()
    genero = GeneroSerializer(many=True)

    class Meta:
        model = Album
        fields = '__all__'

class AlbumCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializador para la creación y actualización del modelo Album.
    Utiliza PrimaryKeyRelatedField para las relaciones con Artista y Genero.
    """
    artista = serializers.PrimaryKeyRelatedField(queryset=Artista.objects.all())
    genero = serializers.PrimaryKeyRelatedField(many=True, queryset=Genero.objects.all())
    
    class Meta:
        model = Album
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo UserProfile.
    """
    class Meta:
        model = UserProfile
        fields = ['user_type']

class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo User, incluyendo el perfil de usuario.
    """
    userprofile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'userprofile')

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializador personalizado para obtener tokens JWT, incluyendo información adicional del usuario.
    """
    def validate(self, attrs):
        """
        Agrega datos adicionales del usuario al token.
        
        Args:
            attrs: Atributos proporcionados para la validación.

        Returns:
            dict: Datos del token con información adicional del usuario.
        """
        data = super().validate(attrs)
        serializer = UserSerializer(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializador para el registro de nuevos usuarios.
    Incluye validación de contraseñas y creación del perfil de usuario.
    """
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    user_type = serializers.ChoiceField(choices=[('Client', 'Client'), ('Employee', 'Employee')], required=True, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'user_type')

    def validate(self, attrs):
        """
        Valida que las contraseñas coincidan.

        Args:
            attrs: Atributos proporcionados para la validación.

        Returns:
            dict: Atributos validados.

        Raises:
            serializers.ValidationError: Si las contraseñas no coinciden.
        """
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        return attrs

    def create(self, validated_data):
        """
        Crea un nuevo usuario y su perfil asociado.

        Args:
            validated_data: Datos validados para crear el usuario.

        Returns:
            User: El usuario creado.

        Raises:
            serializers.ValidationError: Si el tipo de usuario no existe.
        """
        user_type_str = validated_data.pop('user_type')
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        # Buscar el tipo de usuario en la base de datos
        try:
            user_type = UserType.objects.get(user_type=user_type_str)
        except UserType.DoesNotExist:
            raise serializers.ValidationError(f"UserType '{user_type_str}' no existe")

        UserProfile.objects.create(user=user, user_type=user_type)

        return user
