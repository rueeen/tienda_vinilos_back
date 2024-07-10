from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Señal para manejar la actualización de un UserProfile cuando se guarda un User.

    Args:
        sender (Model): La clase del modelo que envía la señal (en este caso, User).
        instance (User): La instancia del modelo User que se está guardando.
        **kwargs: Argumentos adicionales.
    """
    # Si el usuario tiene un perfil asociado, lo guardamos
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()