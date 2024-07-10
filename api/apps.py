from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Clase de configuración para la aplicación 'api'.

    Esta clase hereda de AppConfig y se utiliza para configurar la aplicación 'api' en Django.

    Atributos:
        default_auto_field (str): El tipo de campo automático utilizado por los modelos de la aplicación.
        name (str): El nombre de la aplicación.

    Métodos:
        ready(): Método llamado cuando la aplicación está lista para ser utilizada.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    
    def ready(self):
        """
        Método llamado cuando la aplicación está lista para ser utilizada.

        Este método importa las señales de la aplicación.
        """
        import api.signals



