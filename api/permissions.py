from rest_framework.permissions import BasePermission

class IsEmployee(BasePermission):
    """
    Permiso personalizado para permitir el acceso solo a usuarios empleados.
    """

    def has_permission(self, request, view):
        """
        Verifica si el usuario está autenticado y si es un empleado.

        Args:
            request: El objeto de la solicitud.
            view: La vista que está siendo accedida.

        Returns:
            bool: True si el usuario está autenticado, tiene un perfil de usuario y es un empleado, False en caso contrario.
        """
        return (
            request.user.is_authenticated and  # Verifica si el usuario está autenticado
            hasattr(request.user, 'userprofile') and  # Verifica si el usuario tiene un perfil asociado
            request.user.userprofile.user_type.user_type == 'Employee'  # Verifica si el tipo de usuario es 'Employee'
        )

class IsClient(BasePermission):
    """
    Permiso personalizado para permitir el acceso solo a usuarios clientes.
    """

    def has_permission(self, request, view):
        """
        Verifica si el usuario está autenticado y si es un cliente.

        Args:
            request: El objeto de la solicitud.
            view: La vista que está siendo accedida.

        Returns:
            bool: True si el usuario está autenticado, tiene un perfil de usuario y es un cliente, False en caso contrario.
        """
        return (
            request.user.is_authenticated and  # Verifica si el usuario está autenticado
            hasattr(request.user, 'userprofile') and  # Verifica si el usuario tiene un perfil asociado
            request.user.userprofile.user_type.user_type == 'Client'  # Verifica si el tipo de usuario es 'Client'
        )


