from django.contrib import admin

from api.models import Artista, Album, Genero, UserProfile, UserType

# Register your models here.
admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(Genero)
admin.site.register(UserProfile)
admin.site.register(UserType)