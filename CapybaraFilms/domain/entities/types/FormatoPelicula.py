# Importación del módulo Enum para crear enumeraciones
from enum import Enum

# Excepción personalizada para manejar errores específicos de reservas
class ReservaException(Exception):
    """Excepción personalizada para errores en reservas."""
    pass

# Enumeración que representa los formatos disponibles para las películas
class FormatoPelicula(Enum):
    # Miembros de la enumeración con sus respectivos atributos:
    DOS_D = ("2D", 0)          # Formato 2D sin costo adicional (precio extra = 0)
    TRES_D = ("3D", 1000)      # Formato 3D con costo adicional de 1000

    # Constructor de la enumeración que recibe y asigna los atributos
    def __init__(self, tipo, precio_extra):
        self._tipo = tipo       # Almacena el tipo de formato ("2D" o "3D")
        self._precio_extra = precio_extra  # Almacena el precio adicional

    # Propiedad para acceder al tipo de formato de manera segura
    @property
    def tipo(self):
        try:
            return self._tipo
        except AttributeError:
            # Lanza excepción si el atributo no está definido correctamente
            raise ReservaException("El tipo del formato de película no está definido correctamente.")

    # Propiedad para acceder al precio extra de manera segura
    @property
    def precio_extra(self):
        try:
            return self._precio_extra
        except AttributeError:
            # Lanza excepción si el atributo no está definido correctamente
            raise ReservaException("El precio extra del formato de película no está definido correctamente.")

    # Método alternativo para obtener el precio extra
    def get_precio_extra(self):
        try:
            return self._precio_extra
        except AttributeError:
            # Lanza excepción si hay problemas al obtener el precio
            raise ReservaException("No se pudo obtener el precio extra del formato de película.")

    # Método alternativo para obtener el tipo de formato
    def get_tipo(self):
        """Devuelve la representación como '2D' o '3D'."""
        try:
            return self._tipo
        except AttributeError:
            # Lanza excepción si hay problemas al obtener el tipo
            raise ReservaException("No se pudo obtener el tipo del formato de película.")