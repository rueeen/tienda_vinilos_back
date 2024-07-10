from rest_framework import serializers
from .models import Artista, Album, Genero, UserProfile, UserType
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    artista = ArtistaSerializer()
    genero = GeneroSerializer(many=True)
    class Meta:
        model = Album
        fields = '__all__'

class AlbumCreateUpdateSerializer(serializers.ModelSerializer):
    artista = serializers.PrimaryKeyRelatedField(queryset=Artista.objects.all())
    genero = serializers.PrimaryKeyRelatedField(many=True, queryset=Genero.objects.all())
    
    class Meta:
        model = Album
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user_type']

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'userprofile')

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializer(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    user_type = serializers.ChoiceField(choices=[('Client', 'Client'), ('Employee', 'Employee')], required=True, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'user_type')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
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
            raise serializers.ValidationError(f"UserType '{user_type_str}' does not exist")

        UserProfile.objects.create(user=user, user_type=user_type)

        return user
